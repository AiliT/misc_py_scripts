# search pattern in string using quicksearch algorithm, print lps values,
# valid offsets, and number of comparisons in total + before each match

def QS(text, pattern):
    shift = {c: len(pattern) + 1 for c in set(text)}

    for i in range(len(pattern), 0, -1):
        shift[pattern[len(pattern) - i]] = i

    print("Shift:")
    for k, v in shift.items():
        print(f"  {k}: {v}")

    ctr = 0
    s = 0
    matches = []
    
    while s + len(pattern) <= len(text):
        cmpret = cmp(text[s : s + len(pattern)], pattern)

        if cmpret == len(pattern):
            matches.append(s)
            ctr += cmpret
            print(f"- {ctr} comparisons until match {len(matches)}")
        else:
            ctr += cmpret + 1

        if s + len(pattern) + 1 >= len(text):
            break

        s += shift[text[s + len(pattern)]]

    print(f"{len(matches)} matches found, these are: {matches}")
    return ctr


def cmp(s1, s2):
    j = 0
    while j < len(s1) and s1[j] == s2[j]:
        j += 1

    return j



t = input("Text: ").replace(" ", "")
p = input("Pattern: ").replace(" ", "")

print(f"Text is: {t}")
print(f"Pattern is: {p}")

print(QS(t, p), "comparisons happened.")
