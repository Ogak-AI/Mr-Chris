def listToString(s):
    str1 = " "
    return (str1.join(s))

file_ = open("randomfile.txt", "r")

rdf = file_.read()
count = 0
second_count = 9
for i in rdf:
    splitted_lines = rdf.splitlines()[count:second_count]
    new_string = listToString(splitted_lines)
    print(new_string)

    if second_count == 1152:
        exit()
    count += 9
    second_count += 9






