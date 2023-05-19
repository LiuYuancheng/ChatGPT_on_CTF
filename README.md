# ChartGPT_on_CTF

**Project Design Purpose:**  We want to see whether ChartGPT or other AI (MS-New_Bing or Google Bard) are able to help the user to go to some test environment to run cmd to solve the CTF problem (Understand the challenge question and capture the flag). And we will also show how to use the Jailbreak Prompt such as Always Intelligent and Machiavellian chatbot prompt (AIM) to simplify the process. Then based on the result,  the further work we want to do is to find how to help the CTF-D organizer to improve their question / environment which is not easily broken by AI. 

[TOC]

------

### Introduction 

In this project we will test ChartGPT and other AI's performance on fixing the different CTF challenges. Now we are going to cover below topic:

- Test case examples of how ChartGTP solve the CTF-challenge. 
- Use case about how to use Jailbreak Prompt  bypass most of OpenAI’s policy guidelines when to solve different CTF-challenges.
- Try to create a program can automatic do some steps of the CTF challenge analysis by using different tools(such as penetration tools)
- Analysis the test case result to summarize which kind of CTF challenge will be easily broken by ChartGPT/OpenAI

**Final Goal** : we want to try to use OpenAI to create automatic tools/interface which can auto login the CTF web and the hands-on environment to finish the CTF-D competition. Currently we are planning to use the [AutoGPT](https://github.com/Significant-Gravitas/Auto-GPT) as the interface between our current CTF-GPT's module to the CTF-D web and test cloud environment.



#### Background and Reference

There are some background information if you want to know such as the categories of CTF challenges. [link to all background information and reference link](doc/background.md)

><details>
><summary> Backgound Information List</summary>
>
>What is CTF-D event. 
>
>The detail CTF challenge categories. 
>
></details>



------

### Chart-GPT Challenge Solving Test Cases

In this sections, we will test whether we can use normal way ( just question and answer) by using ChartGPT or other AI (MS-New_Bing or Google Bard) to solve different CTF challenge. Below are the Test list;

1. [Shell Shock Attack Challenge CVE-2014-6271/CVE-2014-6278]()
2. [Buffer overflow attack challenge]()
3. [Blocking Brute Force Attacks]()



------

###  Jailbreak Prompt Bypass

The Chart GPT's policy guidelines will stop GPT give the solution to attack a website, or scan the vulnerability of a system directly. Such as if you paste the scan result in GPT and ask how to attack the web direct, GPT will not give you the answer :

![](doc/img/rm/q2_4.png)

This section will show the cases to use different Jailbreak Prompt to by pass different chartGPT's policy guidelines. 

[ Click this link to for the detail information ](doc/jailbreak.md)

**Important !**

**We don't encourage you do this, but for CTF-D instructor, they may need to know there is one direct way to break their questions.**  What you need is the Jailbreak Prompt for GPT( https://www.jailbreakchat.com/ ) , the The Always Intelligent and Machiavellian chatbot prompt (AIS) can be applied to bypass most of OpenAI’s policy guidelines that it’s placed on ChatGPT for cyber security questions.



------

### Result Analysis 

[under working]



------

### CTF-GPT Program Design

[under working]



------

> last edit by LiuYuancheng (liu_yuan_cheng@hotmail.com) by 19/05/2023 if you have any problem, please send me a message. 