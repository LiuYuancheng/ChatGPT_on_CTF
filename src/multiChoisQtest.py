
#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        mutlitchoiceQtester
#
# Purpose:     This module is used to test the OpenAI's question answer correct 
#              rate to answer the noraml mutliple-cyber-sercurity-qesution which
#              may appear in the CTF event  
#              
# Author:      Yuancheng Liu
#
# Created:     2023/07/2
# Version:     v_0.1
# Copyright:   n.a
# License:     n.a
#-----------------------------------------------------------------------------
import os
import ConfigLoader

import openai

# load the config file.
dirpath = os.path.dirname(__file__)
CONFIG_FILE_NAME = 'config.txt'
gGonfigPath = os.path.join(dirpath, CONFIG_FILE_NAME)
iConfigLoader = ConfigLoader.ConfigLoader(gGonfigPath, mode='r')
if iConfigLoader is None:
    print("Error: The config file %s is not exist.Program exit!" %str(gGonfigPath))
    exit()
CONFIG_DICT = iConfigLoader.getJson()

# set OpenAI's config
openai.api_key = CONFIG_DICT['API_KEY']
AI_MODEL = CONFIG_DICT['AI_MODEL']

# question bank file
questionsFile = CONFIG_DICT['QUES_BANK']

FILTER_CHAR = ('#', '', '\n', '\r', '\t')

questionsList = []
answerList = []
count = 0

answerCount = 0 
questionStr = ""

# load the question bank
with open(questionsFile) as fp:
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
            answerList.append(answerStr)
        elif questionStr:
            questionStr += line +' , '

# get AI's answer        
def get_completion(prompt, model=AI_MODEL):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create( model=model,
                                            messages=messages,
                                            temperature=0,)
    return response.choices[0].message["content"]

# 
correctCount = 0
for i in range(count):
    question = questionsList[i]
    answer = get_completion(question)
    print(answer)
    if answer[0].lower() ==  answerList[i]:
        correctCount+=1

result = 100.0*correctCount/count

print(str(correctCount) + '/' +str(count))
print(str(result)+'%')