# At a job interview, you are challenged to write an algorithm to check if a given string, s,
# can be formed from two other strings, part1 and part2.

# The restriction is that the characters in part1 and part2 should be in the same order as in s.

# The interviewer gives you the following example and tells you to figure out the rest from the
# given test cases.
# 'codewars' is a merge from 'cdw' and 'oears':

#     s:  c o d e w a r s   = codewars
# part1:  c   d   w         = cdw
# part2:    o   e   a r s   = oears


def is_merge(s, part1, part2):
    lst = []
    result = ""
    for i in s:
        for j in part1:
            if i == j:  # and not (i in lst):
                lst.append(j)
                print(lst, "part1")
        for k in part2:
            if i == k:
                lst.append(k)
                print(lst, "part2")
    for char in range(len(lst)):
        result += str(lst[char])
    if result == s:
        return True
    else:
        return False


print(is_merge('codewars', 'cdw', 'oears'))


def is_merge2(s, part1, part2):
    lst = []
    result = ""
    for j in part1:
        lst.append(j)
        print(lst, "part1")
    for k in part2:
        lst.append(k)
        print(lst, "part2")
    for char in range(len(lst)):
        result += str(lst[char])
    if result in s:
        return True
    else:
        return False

print(is_merge2('codewars', 'cdw', 'oears'))


def is_merge3(s, part1, part2):
    result = ""
    for i in part1, part2:
        for j in s: pass
    return result

print(is_merge3('codewars', 'cwdr', 'oeas'))
