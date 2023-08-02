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
APP_NAME = ('OpenAI', 'ctf_category')
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
count = 0

with open(questionsFile, encoding="utf8") as fp:
    for line in fp.readlines():
        if line[0] in FILTER_CHAR: 
            questionStr = None
            continue
        line = line.strip('\n')
        if 'Question' in line:
            questionStr = line.split(':', 1)[1]
            questionStr = questionStr.replace('?', '')
            questionsList.append(questionStr)
            count +=1

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
for i in range(count):
    print('Start to test question %s' %str(i+1))
    question = questionsList[i]
    print(question)
    catQuestion = "Categorize this question string '%s' to below type : A. Forensics, B. Cryptography,  C. Web Exploitation, D. Reverse Engineering, E.Binary Exploitation, F.None of above" %str(question)
    answer = str(get_completion(catQuestion)).strip()
    Log.info('Question %s category: %s' %(str(i+1), str(answer)))
    time.sleep(1)

print ("finished")