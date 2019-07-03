import sys
import re
from collections import defaultdict
from itertools import product


# spilt symbol,like , . !
def exemptSymbol(word):
    if word.isalpha():
        return word
    else:
        return word[0:len(word) - 1]


def findSir(contents):
    line_split = contents.split()
    index_and = 0
    index_sirs = 0
    index_sir = 0
    Sir = []
    # if we have mutiplied  Sirs , Sir
    flag_sirs = False
    flag_and = False
    flag_sir = False
    for i in range(len(line_split)):
        # append sir
        if (line_split[i] == "Sir" or line_split[i] == "\"Sir"):
            index_sir = i
            flag_sir = True
            if (flag_sir):
                sir = line_split[index_sir + 1: index_sir + 2]
                for j in range(len(sir)):
                    if (sir[j].istitle()):
                        if (sir[j].isalpha()):
                            Sir.append(sir[j])
                        else:
                            for k in range(len(sir[j])):
                                if not sir[j][k].isalpha():
                                    sir[j] = sir[j][:k]
                                    Sir.append(sir[j])
                                    break
                flag_sir = False
            continue
        # appden sirs
        if (line_split[i] == "Sirs" or line_split[i] == "\"Sirs"):
            temp = i
            index_sirs = temp
            flag_sirs = True
            continue
        if (line_split[i] == "and" or line_split[i] == "or"):
            index_and = i
            flag_and = True
            continue
        # append sirs
        if (flag_sirs and flag_and):
            if (index_sirs < index_and):
                sirs = line_split[index_sirs + 1: index_and + 2]
                for j in range(len(sirs)):
                    if (sirs[j].istitle()):
                        if (sirs[j].isalpha()):
                            Sir.append(sirs[j])
                        else:
                            for k in range(len(sirs[j])):
                                if not sirs[j][k].isalpha():
                                    sirs[j] = sirs[j][:k]
                                    Sir.append(sirs[j])
                                    break
                flag_sirs = False
                flag_and = False
    Sir = sorted(set(Sir))
    return Sir


def all_Sirdic(Sir):
    # possible number of each Sir
    dic_name_tf = {}
    for name in Sir:
        dic_name_tf[name] = 2
    return dic_name_tf


name_indentity = []


def all_situations(Sir):
    # possible identity,1 means knight
    all_list = list(product((0, 1), repeat=len(Sir)))

    for i in all_list:
        all_possible = []
        k = 0
        for name in Sir:
            all_possible.append((name, i[k]))
            k += 1

        name_indentity.append(all_possible)
    return name_indentity


def all_times(dic):
    # all number
    sum = 1
    for i in dic:
        sum *= dic[i]
    return sum


def find_their_identity(contents):
    # return all quote senteces
    pattern = re.compile(r"\"(.*?)\"")
    res = pattern.findall(contents)
    return res


# 1-8 consider possible result and return true
def checkonesentence(sentence, participate, onesituation):
    print(participate)
    print(sentence)
    sentence_list = sentence.split(" ")
    print(sentence_list)
    # 1 at least ,knight
    if sentence_list[1] == "least" and "Knight" in sentence:
        print("1")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if num >= 1:
            return True
        return False
    # 1 at least ,knave
    if sentence_list[1] == "least" and "Knave" in sentence:
        print("2")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if num >= 1:
            return True
        return False

    # 2 ,at most Knight
    if sentence_list[1] == "most" and "Knight" in sentence:
        print("3")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if (num <= 1):
            return True
        return False
    # 2 ,at most Knave
    if sentence_list[1] == "most" and "Knave" in sentence:
        print("4")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if (num <= 1):
            return True
        return False
    # 3 ,exactly Knight
    if ("Exactly" in sentence_list[0] or "exactly" in sentence_list[0]) and "Knight" in sentence:
        print("5")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if (num == 1):
            return True
        return False

    if ("Exactly" in sentence_list[0] or "exactly" in sentence_list[0]) and "Knave" in sentence:
        print("6")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if (num == 1):
            return True
        return False
    # 4 ,All Knight
    if ("All" in sentence_list[0] or "all" in sentence_list[0]) and "Knight" in sentence:
        print("7")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if (num == len(participate)):
            return True
        return False
    # 4 ,All Knave
    if ("All" in sentence_list[0] or "all" in sentence_list[0]) and "Knave" in sentence:
        print("8")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if (num == len(participate)):
            return True
        return False
    # 5, I am
    if sentence_list[1] == "am" and "Knight" in sentence:
        print("9")
        for i in onesituation:
            for j in participate:
                # name in the situation equals to the name in participate.
                if i[0] == j and i[1] == 1:
                    return True
        return False
    if sentence_list[1] == "am" and "Knave" in sentence:
        return "exit"
    # 6,one person ,Knight
    if "Sir" in sentence_list[0] and sentence_list[2] == "is" and "Knight" in sentence:
        print("11")
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    return True
        return False
    # 6,one person ,Knave
    if "Sir" in sentence_list[0] and sentence_list[2] == "is" and "Knave" in sentence:
        print("12")
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    return True
        return False

    # 7 ,Knight
    if not sentence_list[1] == "least" and not sentence_list[1] == "most" \
            and (sentence_list[-5] == "or" or sentence_list[-6] == "or") \
            and "Knight" in sentence and sentence_list[-3] == "is" and len(participate) >= 2:
        print("13")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if num >= 1:
            return True
        return False
    if not sentence_list[1] == "least" and not sentence_list[1] == "most" \
            and (sentence_list[-5] == "or" or sentence_list[-6] == "or") \
            and "Knave" in sentence and sentence_list[-3] == "is" and len(participate) >= 2:
        print("14")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if num >= 1:
            return True
        return False
    # 8
    if sentence_list[-2] == "are" and "Knight" in sentence and "and" in sentence \
            and not sentence_list[1] == "All" and not sentence_list[1] == "all":
        print("15")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 1:
                    num = num + 1
        if (num == len(participate)):
            return True
        return False

    if sentence_list[-2] == "are" and "Knave" in sentence and "and" in sentence \
            and not sentence_list[1] == "All" and not sentence_list[1] == "all":
        print("16")
        num = 0
        for i in onesituation:
            for j in participate:
                if i[0] == j and i[1] == 0:
                    num = num + 1
        if (num == len(participate)):
            return True
        return False
    return False


try:
    input_puzzle_file = input("Which text file do you want to use for the puzzle?")
    f = open(input_puzzle_file)
    contents = f.read()
    contents = contents.replace('\n', ' ')
    # file_sir is a list
    file_sir = findSir(contents)

    # first question
    print("The Sirs are:", end=' ')
    for num in range(len(file_sir)):
        if (num == len(file_sir) - 1):
            print(file_sir[num])
        else:
            print(file_sir[num], end=' ')

    # next qustion
    copycontents = contents

#  dic = find_numof_Iam(deal_Iam(contents), file_sir)
#  solution_num = all_times(dic)

except FileNotFoundError:

    print("No such file, please input correct file name")
    sys.exit()
finally:
    f.close()

contents = contents.replace("!", "")
contents = contents.replace("?", "")
contents = contents.replace(".", "")
quotesentences = find_their_identity(contents)
sentenceAndname = defaultdict(list)
copycontents = re.split(r'[?.!]', copycontents)

# split txt into sentences
for line in copycontents:
    for i in quotesentences:
        if line.__contains__(i):
            line_split = line.split()
            print(line_split)
            if not line_split[0] == "\"Sir" and not line_split[1] == "\"Sir":
                for index in range(0, len(line_split)):

                    if line_split[index] == "Sir":
                        if (sentenceAndname[exemptSymbol(line_split[index + 1])].__contains__((i))):
                            continue
                        sentenceAndname[exemptSymbol(line_split[index + 1])].append(i)
                        break
            else:
                for index in range(len(line_split) - 1, -1, -1):
                    if line_split[index] == "Sir":
                        if (sentenceAndname[exemptSymbol(line_split[index + 1])].__contains__((i))):
                            continue
                        sentenceAndname[exemptSymbol(line_split[index + 1])].append(i)
                        break


for z in sentenceAndname:
    print(z, sentenceAndname[z])

def find_paticipate(onesentence, key_name):
    # the first element is who said it,but not include them if they
    # are not participating
    participate = []
    file_sir_deletekey = list(file_sir)
    if "us" in onesentence:
        participate.append((key_name))
        file_sir_deletekey.remove(key_name)
        participate = participate + file_sir_deletekey
        return participate
    elif "I" in onesentence:
        thissentenceSir = findSir(onesentence)
        #print(thissentenceSir)
        participate.append(key_name)
        participate = participate + thissentenceSir
        return participate
    else:
        return findSir(onesentence)


situations = all_situations(file_sir)
result = []


def calculate_sentence(sentenceAndname):
    num = 0
    for key in sentenceAndname:
        num = num + len(sentenceAndname[key])
    return num


sentence_num = calculate_sentence(sentenceAndname)

print(sentenceAndname)


# print(sentence_num)

def final(situations, sentenceAndname):
    for onesituation in situations:
        tempresult = []
        for key in sentenceAndname:
            for sentence in sentenceAndname[key]:
                participate = find_paticipate(sentence, key)
                for keyname in onesituation:
                    if checkonesentence(sentence, participate, onesituation) == "exit":
                        return 0
                    if (keyname[0] == key and keyname[1] == 1 and checkonesentence(sentence, participate,
                                                                                   onesituation) == True):
                        tempresult.append(onesituation)
                    elif (keyname[0] == key and keyname[1] == 0 and checkonesentence(sentence, participate,
                                                                                     onesituation) == False):
                        tempresult.append(onesituation)
                    else:
                        continue
                if len(tempresult) == sentence_num:
                    result.append(onesituation)
    # print(result)
    return len(result)


solution_num = final(situations, sentenceAndname)

if (solution_num == 0):
    print("There is no solution.")
elif (solution_num == 1):
    print("There is a unique solution:")
    for solution in result:
        for i in solution:
            if (i[1] == 1):
                print(f'Sir {i[0]} is a Knight.')
            elif (i[1] == 0):
                print(f'Sir {i[0]} is a Knave.')
else:
    print(f'There are {solution_num} solutions.')
