def removeAGivenWord(word, list):
    list.remove(word.strip())
    return list, word


def removeWord(word, list):
    n = []
    for item in list:
        if not (item == word):
            n.append(item.strip(word))
    return n


list = "remove extra whitespaces and specified characters from the start and from the end of the strip irrespective of how the parameter is passed".split(
    " "
)
# print(list.remove("  start ".strip()))
# print("  start ".strip())

# lst has list and word has word
# lst, word = removeAGivenWord(" start ", list)
# print(lst, word)

lst = removeWord("start", list)
print(
    lst,
)

# returns tuple with list and word
# (lst,) = removeAGivenWord(" start ", list)
# print(lst)
