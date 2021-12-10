# search pattern in string using KMP algorithm, print lps values, valid offsets,
# and number of comparisons in total + before each match

def init_next(pattern):
    cur_ind = 1
    cur_lps_ind = 0

    n = [0]

    while cur_ind < len(pattern):
        if pattern[cur_ind] == pattern[cur_lps_ind]:
            cur_lps_ind += 1
            cur_ind += 1
            n.append(cur_lps_ind)

        elif cur_lps_ind == 0:
            n.append(0)
            cur_ind += 1

        else:
            # try with second longest prefix-suffix
            cur_lps_ind = n[cur_lps_ind]

    return n


def KMP(text, pattern):
    n = init_next(pattern)
    print(f"Next: {n}")

    ctr = 0
    t_ind = 0
    p_ind = 0
    matches = []
    
    while t_ind < len(text):
        ctr += 1
        if text[t_ind] == pattern[p_ind]:
            t_ind += 1
            p_ind += 1

            if p_ind == len(pattern):
                matches.append(t_ind - len(pattern))
                p_ind = n[p_ind - 1]
                print(f"- {ctr} comparisons until match {len(matches)}")

        else:
            if p_ind == 0:
                t_ind += 1
            else:
                # set pattern index to next one, that has same prefix as
                # previous suffix
                p_ind = n[p_ind - 1]

    print(f"{len(matches)} matches found, these are: {matches}")
    return ctr



t = input("Text: ").replace(" ", "")
p = input("Pattern: ").replace(" ", "")

print(f"Text is: {t}")
print(f"Pattern is: {p}")

print(KMP(t, p), "comparisons happened.")
