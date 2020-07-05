def extractList(f):
    textList = []

    for line in f.readlines():
        textList.append(line.split('\t'))

    return textList

def appendChild(mN, f, l1, l2):
    found = False

    for line in l1 + l2:
        if len(line) > 0 and line[0] == mN:
            found = True
            f.write('\t'.join(line))
            break

    if not found:
        f.write(mN)


def main():
    fin = open("textureListExprRaw.txt", 'r')
    fout = open("textureListExpr.txt", 'w')
    txt1 = open("../../list.txt", 'r')
    txt2 = open("../../list_jp.txt", 'r')

    list1 = extractList(txt1)
    list2 = extractList(txt2)

    for mN in fin.readlines():
        appendChild(mN.strip(), fout, list1, list2)

    fout.close()


if __name__ == "__main__":
    main()
