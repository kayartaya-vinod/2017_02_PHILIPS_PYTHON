def num_to_words(num=12345):
    list1 = ["", "one", "two", "three", "four",
             "five", "six", "seven", "eight", "nine", "ten", "eleven",
             "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen", "twenty"]
    list2 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
             "seventy", "eighty", "ninety"]
    list3 = ["", "hundred", "thousand", "lakh", "crore"]

    list4 = []
    i = 0
    while num > 0:
        if i == 1:
            rem = num % 10
            num //= 10
        else:
            rem = num % 100
            num //= 100
        i += 1
        list4.append(rem)

    i -= 1
    out = ""
    while i >= 0:
        if list4[i] == 0:
            i -= 1
            continue

        if list4[i] <= 20:
            out += "{0} {1} ".format(list1[list4[i]], list3[i])
        else:
            n1 = list4[i] % 10
            n2 = list4[i]//10
            out += "{0} {1} {2} ".format(list2[n2], list1[n1], list3[i])
        i -= 1

    return out


if __name__ == "__main__":
    in_words = num_to_words()
    print(in_words)
    in_words = num_to_words(num=1001)
    print(in_words)
    in_words = num_to_words(1000002)
    print(in_words)
    in_words = num_to_words(999999999)
    print(in_words)


