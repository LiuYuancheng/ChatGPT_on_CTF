
#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        multi-choice-CTF-question-tester
#
# Purpose:     This module is used to test the OpenAI's question solving correctness
#              rate of the normal multiple choice cyber-security questions which may 
#              appear in the CTF event.
#              
# Author:      Yuancheng Liu
#
# Created:     2023/07/28
# Version:     v_0.1
# Copyright:   n.a
# License:     n.a
#-----------------------------------------------------------------------------

import os
import time
import ConfigLoader

import openai

print("Current working directory is : %s" % os.getcwd())
DIR_PATH = dirpath = os.path.dirname(__file__)
print("Current source code location : %s" % dirpath)
APP_NAME = ('OpenAI', 'ctf_mq')
TOPDIR = 'src'

#-----------------------------------------------------------------------------
# Init the logger:
idx = dirpath.find(TOPDIR)
gTopDir = dirpath[:idx + len(TOPDIR)] if idx != -1 else dirpath   # found it - truncate right after TOPDIR
# Config the lib folder 
import Log
Log.initLogger(gTopDir, 'Logs', APP_NAME[0], APP_NAME[1], historyCnt=100, fPutLogsUnderDate=True)

# load the config file.
CONFIG_FILE_NAME = 'config.txt'
gGonfigPath = os.path.join(dirpath, CONFIG_FILE_NAME)
iConfigLoader = ConfigLoader.ConfigLoader(gGonfigPath, mode='r')
if iConfigLoader is None:
    print("Error: The config file %s is not exist.Program exit!" %str(gGonfigPath))
    exit()
CONFIG_DICT = iConfigLoader.getJson()

# Set OpenAI's config
openai.api_key = CONFIG_DICT['API_KEY']
AI_MODEL = CONFIG_DICT['AI_MODEL']

# question bank file
Q_BANK_DIR = 'questionbank'
questionsFile = os.path.join(Q_BANK_DIR, CONFIG_DICT['QUES_BANK'])
# init the line filter charactor
FILTER_CHAR = ('#', '', '\n', '\r', '\t')

questionsList = []
answerList = []
count = 0

answerCount = 0 
questionStr = ""

# load the question bank
#with open(questionsFile) as fp:
with open(questionsFile, encoding="utf8") as fp:
    for line in fp.readlines():
        if line[0] in FILTER_CHAR: 
            questionStr = None
            continue
        line = line.strip('\n')
        if 'Question' in line:
            questionStr = line.split(':', 1)[1]
            answerCount = 0
            count +=1
        if 'Answer' in line:
            questionsList.append(questionStr)
            answerStr = line.split(':', 1)[1]
            answerList.append(answerStr.strip())
        elif questionStr:
            questionStr += line +' , '

# get AI's answer        
def get_completion(prompt, model=AI_MODEL):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create( model=model,
                                                messages=messages,
                                                temperature=0,)
        return response.choices[0].message["content"]
    except Exception as err:
        print('error: %s'%str(err))
        print('----')
        print('input prompt: %s' %str(prompt))
        return 'error'

print("Start to check the questions.")
correctCount = 0
for i in range(count):
    if i == len(questionsList): break
    print('Start to test question %s' %str(i+1))
    question = questionsList[i]
    if not question:
        Log.info('Question %s got problem: %s.' %(str(i+1), question))
        continue
    answer = str(get_completion(question)).strip()
    if (answer[0].lower() == answerList[i]) or \
        answerList[i]+')' in answer or \
        answerList[i]+'.' in answer:
        correctCount+=1
        Log.info('Question %s: correct.' %str(i+1))
    elif len(answerList[i]) > 1:
        res = True
        # handler multi-choice question wich more than one answer
        for val in answerList[i]:
            if val+')' in answer or val+'.' in answer:
                res = res and True
            else:
                res = res and False
        if res:
            correctCount+=1
            Log.info('Question %s: correct.' %str(i+1))
            #Log.info('Question %s: correct. correct answer: %s, AI answer: %s' %(str(i+1),str(answerList[i]), str(answer) ))
        else:
            Log.info('Question %s: incorrect. correct answer: %s, AI answer: %s' %(str(i+1),str(answerList[i]), str(answer) ))
    else:
        Log.info('Question %s: incorrect. correct answer: %s, AI answer: %s' %(str(i+1),str(answerList[i]), str(answer) ))
    time.sleep(1) # speed to avoid reach the 1 min text limitation.
    
result = 100.0*correctCount/count

print(str(correctCount) + '/' +str(count))
print(str(result)+'%')
Log.info('Ai correct rate: %s ' %str(result))