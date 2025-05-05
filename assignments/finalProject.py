"""
project.py
Court Calendar Processor
Author: Programming Group A
"""

import csv
import re

__author__ = "Programming Group A"
END_HEADER = "*" * 20


def normalize_defendant_name(name):
    # If a comma exists, assume it's formatted correctly
    if "," in name:
        return name

    # If the name contains only spaces, reformat it by inserting a comma
    parts = name.split()
    if len(parts) >= 2:
        return parts[0] + "," + " ".join(parts[1:])

    return name  # Return original if formatting can't be corrected


def is_report_header(line):
    """
    Determines if a line is the header of a court report.

    A header line typically does not start with '1' and contains the keyword 'RUN DATE:'.

    Args:
        line (str): A single line from the report.

    Returns:
        bool: True if the line is a report header, False otherwise.
    """
    return line and line[0] != "1" and "RUN DATE:" in line


def process_report_header(line, infile):
    """
    Parses the header section of the court report to extract metadata.

    Specifically captures the run date, court date, court time, and courtroom number.
    Continues reading lines from the input file until the end of the header is reached or a special header marker is encountered.

    Args:
        line (str): The first line of the report containing the run date.
        infile (file-like object): The input file being read.

    Returns:
        dict: A dictionary containing the extracted metadata, including 'RunDate', 'CourtDate', 'CourtTime', and 'CourtRoom'.
    """
    data = {}
    data["RunDate"] = line[12:20].strip()
    while True:
        line = infile.readline()
        if line == "" or END_HEADER in line:
            break
        elif "COURT DATE:" in line:
            data["CourtDate"] = line[22:30].strip()
            data["CourtTime"] = line[44:52].strip()
            data["CourtRoom"] = line[78:].strip()
    return data


def is_page_header(line):
    """
    Determines if a line is a page header within the court report.

    Page headers typically start with '1' but do not contain the keyword 'RUN DATE:'.

    Args:
        line (str): A single line from the report.

    Returns:
        bool: True if the line is a page header, False otherwise.
    """
    return line and line[0] == "1" and "RUN DATE:" not in line


def process_page_header(line, infile):
    """
    Skips over the page header section of the court report.

    Continues reading lines until the end of the page header is reached or the end of the file is encountered.

    Args:
        line (str): The first line of the page header.
        infile (file-like object): The input file being read.
    """
    while True:
        line = infile.readline()
        if line == "" or END_HEADER in line:
            break
    return


def is_summary_header(line):
    """
    Identifies if a line is the start of the summary section header in the report.

    Summary headers typically start with '1' and contain the keyword 'RUN DATE:'.

    Args:
        line (str): A single line from the report.

    Returns:
        bool: True if the line is a summary header, False otherwise.
    """
    return line and line[0] == "1" and "RUN DATE:" in line


def is_defendant_line(line):
    """
    Determines if a line represents the start of a defendant's record.

    Checks that the line is long enough, contains a numeric ID, and includes a file number
    with a valid case type like 'CR' (Criminal) or 'IF' (Infraction).

    Args:
        line (str): A single line from the report.

    Returns:
        bool: True if the line represents a defendant's record, False otherwise.
    """
    if len(line) < 18:
        return False
    num = line[4:8].strip()
    file_num = line[8:18].strip()
    return num.isdigit() and ("CR" in file_num or "IF" in file_num)


def parse_charge_line(line):
    """
    Parses a single line representing a charge entry on the court docket.

    Handles both fixed-width "CLS:" format lines and free-form lines with labeled fields.
    Extracts details including Charges, Plea, Verdict, CLS, P, L, DOM VL, Judgment, and ADA.

    - If the line starts with "CLS:", fields are assumed to be in fixed positions.
    - Otherwise, uses regex to extract values based on labeled keywords.
    - The ADA field is explicitly included to match expected output columns, even if not present.

    Returns:
        dict: A dictionary with extracted values, using empty strings for missing data.
    """
    line = line.rstrip()

    # Initialize result dictionary with all required fields, including "ADA"
    result = {
        "Charges": "",
        "Plea": "",
        "Verdict": "",
        "CLS": "",
        "P": "",
        "L": "",
        "DOM VL": "",
        "Judgment": "",
        "ADA": "",  # Explicitly adding ADA to align with headers
    }

    # If the line starts with "CLS:" then we expect fixed positions
    if line.lstrip().startswith("CLS:"):
        cls_val = line[8:15].strip() if len(line) >= 15 else ""
        p_val = line[16:20].strip() if len(line) >= 20 else ""
        l_val = line[20:28].strip() if len(line) >= 28 else ""
        domvl_val = line[28:40].strip() if len(line) >= 40 else ""

        # Extract Judgment and ADA separately
        if len(line) >= 84:
            judgment_val = line[41:76].strip()
            ada_val = line[76:84].strip()
        else:
            judgment_val = line[41:].strip() if len(line) > 41 else ""
            ada_val = ""

        # If p_val accidentally contains "P:" at the start, reset it.
        if p_val.upper().startswith("P:"):
            p_val = ""

        # Assign extracted values to the result dictionary
        result.update(
            {
                "CLS": cls_val,
                "P": p_val,
                "L": l_val,
                "DOM VL": domvl_val,
                "Judgment": judgment_val,
                "ADA": ada_val,  # Ensure ADA is stored separately
            }
        )

    else:
        # Regex parsing for non-"CLS:" lines
        charge_match = re.search(
            r"^(.*?)(?=\s+(?:PLEA:|VER:|CLS:|P:|L:|JUDGMENT:))", line, re.IGNORECASE
        )
        if charge_match:
            result["Charges"] = charge_match.group(1).strip()
        else:
            result["Charges"] = line.strip()

        verdict_match = re.search(r"VER:\s*([^\s]+)", line, re.IGNORECASE)
        if verdict_match:
            result["Verdict"] = verdict_match.group(1).strip()

        cls_match = re.search(r"CLS:\s*([^\s]+)(?=\s+[A-Z]+:|$)", line, re.IGNORECASE)
        if cls_match:
            result["CLS"] = cls_match.group(1).strip()

        # Extract DOM VL (assuming it's within positions 28 to 40 in the line)
        domvl_match = re.search(r"DOM VL:\s*(Y|N)", line, re.IGNORECASE)
        if domvl_match:
            result["DOM VL"] = domvl_match.group(1).strip()

        # Extract ADA only if the length permits
        ada_match = re.search(r"ADA:\s*([\w\d]*)", line, re.IGNORECASE)
        if ada_match:
            result["ADA"] = ada_match.group(1).strip()

        # Extract Judgment separately from ADA
        judgment_match = re.search(r"JUDGMENT:\s*([^\s]+)", line, re.IGNORECASE)
        if judgment_match:
            result["Judgment"] = judgment_match.group(1).strip()

    return result


def process_defendant_line(line, infile):
    """
    Processes a defendant's record line and subsequent lines to extract detailed information.

    This function reads through lines of the court report, capturing data about the defendant, including:
    - Number
    - File Number
    - Defendant's Name
    - Complainant
    - Attorney
    - Cont (Continuation/Comments)
    - Bond
    - Charges

    It also checks for special conditions such as "DEFENDANT NEEDS TO BE FINGERPRINTED" and extracts relevant charge details.
    The function processes lines until a new defendant record or the end of the file is encountered.

    Args:
        line (str): The first line containing basic defendant information.
        infile (file-like object): The input file being read, used for reading the following lines.

    Returns:
        tuple: A tuple containing:
            - A dictionary `data` with the extracted defendant data.
            - A string `None` or the next line if the defendant record ends.
    """
    data = {}
    if not line.strip():
        return None, None

    if len(line) >= 56:
        data["Number"] = line[4:8].strip()
        data["File Number"] = line[8:20].strip()
        raw_name = line[20:42].strip()
        data["Defendant"] = normalize_defendant_name(raw_name)
        data["Complainant"] = line[42:61].strip()
        data["Attorney"] = line[61:84].strip()
        data["Cont"] = line[84:].strip()
    else:
        return None, None

    data["Needs Fingerprinted"] = "False"
    data["Bond"] = ""
    data["charge_info"] = []
    current_charge = None

    for next_line in infile:
        if not next_line:
            break
        stripped_line = next_line.strip()
        if not stripped_line:
            continue

        if is_page_header(next_line):
            process_page_header(next_line, infile)
            continue

        if len(next_line) >= 56 and not next_line.lstrip().startswith("("):
            candidate_number = next_line[4:8].strip()
            candidate_file = next_line[8:18].strip()
            if candidate_number and candidate_file:
                if candidate_number != data["Number"]:
                    return data, next_line
                else:
                    if any(
                        charge in next_line for charge in ["(T)", "(I)", "(M)", "(F)"]
                    ):
                        current_charge = parse_charge_line(next_line)
                        current_charge["Verdict"] = (
                            current_charge["Verdict"]
                            .replace("\xa0", "")
                            .replace("\t", "")
                            .strip()
                        )
                        data["charge_info"].append(current_charge)
                        continue

        if "DEFENDANT NEEDS TO" in next_line:
            data["Needs Fingerprinted"] = "True"

        if "BOND:" in next_line:
            data["Bond"] = next_line.split("BOND:")[1].strip()

        if any(charge in next_line for charge in ["(T)", "(I)", "(M)", "(F)"]):
            current_charge = parse_charge_line(next_line)
            data["charge_info"].append(current_charge)
            continue

        if (
            current_charge
        ):  # Check if the current_charge object is available to store data
            # Look for CLS in the line
            if next_line.lstrip().upper().startswith("CLS:"):
                # Use regex to capture the value after "CLS:" (this works for numeric, alphanumeric, or empty)
                cls_match = re.search(
                    r"CLS:\s*(?![A-Z]{1,4}:)([^\s]+)", next_line.lstrip(), re.IGNORECASE
                )
                if cls_match:
                    cls_val = cls_match.group(1).strip()  # Extract value after CLS:
                    # Store the value in the current charge, even if it's empty or any alphanumeric
                    current_charge["CLS"] = cls_val
                else:
                    # If no match is found, you can handle the case (e.g., store empty or None)
                    current_charge["CLS"] = ""

            # Always search for ADA if mentioned
            if "ADA:" in next_line.upper():
                ada_match = re.search(r"ADA:\s*([A-Z0-9]*)", next_line, re.IGNORECASE)
                if ada_match:
                    current_charge["ADA"] = ada_match.group(1).strip()

            # Look for JUDGMENT and clean up text
            if "JUDGMENT:" in next_line.upper():
                judgment_text = next_line.split("JUDGMENT:", 1)[1].strip()
                judgment_text = re.sub(
                    r"ADA:\s*[A-Z0-9]*", "", judgment_text, flags=re.IGNORECASE
                ).strip()
                current_charge["Judgment"] = judgment_text

            # Extract 'DOM VL' value if present; this field is missing in most records
            if "DOM VL:" in next_line.upper():
                domvl_match = re.search(r"DOM VL:\s*(Y|N)", next_line, re.IGNORECASE)
                if domvl_match:
                    current_charge["DOM VL"] = domvl_match.group(1).strip()

    return data, None


def read_file(filename):
    """Reads the input file and processes lines."""
    rows = []
    report_data = {}

    try:
        with open(filename, "r") as infile:
            line = infile.readline()
            while line:
                if is_summary_header(line):
                    break
                if line.strip() == "":
                    line = infile.readline()
                    continue
                elif is_report_header(line):
                    report_data = process_report_header(line, infile)
                    line = infile.readline()
                elif is_page_header(line):
                    process_page_header(line, infile)
                    line = infile.readline()
                elif is_defendant_line(line):
                    defendant_data, next_line = process_defendant_line(line, infile)
                    if defendant_data:
                        defendant_data["CourtDate"] = report_data.get("CourtDate", "")
                        defendant_data["CourtTime"] = report_data.get("CourtTime", "")
                        defendant_data["CourtRoom"] = report_data.get("CourtRoom", "")

                        if not defendant_data["charge_info"]:
                            defendant_data["charge_info"].append(
                                {
                                    "Charges": "",
                                    "Plea": "",
                                    "Verdict": "",
                                    "CLS": "",
                                    "P": "",
                                    "L": "",
                                    "DOM VL": "",
                                    "Judgment": "",
                                    "ADA": "",
                                }
                            )

                        rows.extend(create_rows(defendant_data))

                    if next_line:
                        line = next_line
                    else:
                        line = infile.readline()
                else:
                    line = infile.readline()
    except IOError as e:
        print(f"Could not open file {filename}. Error: {e}")
        return []

    return rows


def create_rows(defendant_data):
    """Creates rows for the CSV from the defendant data."""
    rows = []
    for charge in defendant_data["charge_info"]:
        row = {
            "CourtDate": defendant_data.get("CourtDate", "").strip(),
            "CourtTime": defendant_data.get("CourtTime", "").strip(),
            "CourtRoom": defendant_data.get("CourtRoom", "").strip(),
            "Number": defendant_data.get("Number", "").strip(),
            "File Number": defendant_data.get("File Number", "").strip(),
            "Defendant": defendant_data.get("Defendant", "").strip(),
            "Complainant": defendant_data.get("Complainant", "").strip(),
            "Attorney": defendant_data.get("Attorney", "").strip(),
            "Cont": defendant_data.get("Cont", "").strip(),
            "Needs Fingerprinted": defendant_data.get(
                "Needs Fingerprinted", "False"
            ).strip(),
            "Bond": defendant_data.get("Bond", "").strip(),
            "Charges": charge.get("Charges", "").strip(),
            "Plea": charge.get("Plea", "").strip(),
            "Verdict": charge.get("Verdict", "").strip(),
            "CLS": charge.get("CLS", "").strip(),
            "P": charge.get("P", "").strip(),
            "L": charge.get("L", "").strip(),
            "DOM VL": charge.get("DOM VL", "").strip(),
            "Judgment": charge.get("Judgment", "").strip(),
            "ADA": charge.get("ADA", "").strip(),
        }

    rows.append(row)
    return rows


def write_to_csv(rows):
    """Writes the rows to a CSV file."""
    fieldnames = [
        "CourtDate",
        "CourtTime",
        "CourtRoom",
        "Number",
        "File Number",
        "Defendant",
        "Complainant",
        "Attorney",
        "Cont",
        "Needs Fingerprinted",
        "Bond",
        "Charges",
        "Plea",
        "Verdict",
        "CLS",
        "P",
        "L",
        "DOM VL",
        "Judgment",
        "ADA",
    ]

    rows.sort(key=lambda x: int(x["Number"]) if x["Number"].isdigit() else float("inf"))
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            if "Verdict" in row:
                row["Verdict"] = f'="{row["Verdict"].strip()}"'
            else:
                print(f"Missing Verdict field in row: {row}")
            writer.writerow(row)

    print("CSV file 'output.csv' has been created successfully.")


def main():
    filename = input(
        "Enter the path and name of the txt file (e.g., CourtCalendars/yourfile.txt): "
    ).strip()
    if not filename:
        print("No file name provided. Exiting.")
        return

    rows = read_file(filename)
    print(rows)
    if rows:
        write_to_csv(rows)
    else:
        print("No data found in the file.")


if __name__ == "__main__":
    main()
