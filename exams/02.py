# CIS 3680 - Assessment #2
import statistics

def main():
    filename = input("Enter file name: ")
    file = open(filename, 'r')
    bolts = []
    low_limit = 4.00 - 0.125
    high_limit = 4.00 + 0.125

    for line in file:
        word = line.split()
        bolts.append(float(word[0]))

    mean = statistics.mean(bolts)
    mean_pass = low_limit <= mean <= high_limit
    mean_result = "Pass" 
    if mean_pass != True: mean_result ="Fail"

    bad_bolts = []
    for bolt in bolts:
        if bolt < low_limit or bolt > high_limit:
            bad_bolts.append(bolt)

    tolerance = "Pass" 
    if len(bad_bolts) >= 2: tolerance ="Fail"

    print(f"\tMean: {mean:.3f} {mean_result}")
    print(f"Bad Bolts: {len(bad_bolts)} {tolerance}")


if __name__ == "__main__":
    main()
