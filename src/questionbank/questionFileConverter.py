# a small converter to convert the html CTF-D multiple choice question to 
# the question bank formate
import os 


FILTER_CHAR = ('#', '', '\n', '\r', '\t')
dirpath = os.path.dirname(__file__)

srcFile = os.path.join(dirpath, 'src.txt')
destFile = os.path.join(dirpath, 'converted.txt')

questionDataList = []

with open(srcFile, encoding="utf8") as fp:
    for line in fp.readlines():
        if line[0] in FILTER_CHAR: continue
        if 'QUESTION' in line: continue
        if 'A.' in line or 'B.' in line or 'C.' in line or 'D.' in line:
            questionDataList.append(line)
        elif 'Correct Answer:' in line:
            answer = line.split(':')[1]
            questionDataList.append('Answer:'+answer.strip()+'\n\n')
        else:
            questionDataList.append('Question:'+line)


fh = open(destFile, "a")
for line in questionDataList:
    fh.write(line)
fh.close()