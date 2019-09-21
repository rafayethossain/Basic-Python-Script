import pprint
message = '''
    
Rafayet Hossain


    
(Software Quality Analyst &
    Programmer)


    
14/3
    Baparipara, Khilkhet, Dhaka


    
https://rafayethossain.github.io


    
rafayet13@gmail.com


    
(+88)
    01710 49 36 13


    
 




Career
Objectives:



Aiming to work in the field of Software
Quality Assurance to enhance my knowledge and skills
through individual and group based work to become a professional contributor to
the development
of the organization. 



 



Area
of Expertise:



☑
Software Quality Assurance ☑ Functional & Non-
Functional Testing ☑ Software Process
Improvement ☑
Technical Documentation ☑ System Analysis &
Design ☑
Microsoft Office ☑
Python Programming ☑ Data Visualization ☑ Data Analysis ☑ Analytical Research ☑ Selenium Automation
Testing ☑
JIRA Bug Tracking ☑
SQL ☑
Root Cause Analysis ☑ Object Oriented
Programming ☑
Web Design & Development ☑ Laravel Framework ☑ Big Data ☑  Digital Marketing ☑ Lean Six Sigma ☑ CMMI Framework ☑ SDLC ☑ STLC ☑ Data Mining



 



Professional
Courses:




  
Title


  	
  
Subject


  	
  
Institute


  	
  
Duration


  

  
Certified Lean Six Sigma Black Belt 


  	
  
Lean Six Sigma


  	
  
RTIAC
  (India), Hi-Tech Park Project Bangladesh


  	
  
130
  Hrs


  

  
Top
  Up Training (LICT)


  	
  
Big
  Data Analytics


  	
  
NASSCOM
  (India) , ICT BD


  	
  
300
  Hrs


  

  
English
  & Business Communication


  	
  
English
  Communication 


  	
  
BITM,
  SEIP, BASIS Bangladesh


  	
  
32
  Hrs


  

  
Become
  a Full Stack Web Developer


  	
  
PHP,
  Laravel Framework


  	
  
Udemy
  


  	
  
20
  Hrs


  

  
Basic
  QA & Selenium Automation   


  	
  
Selenium
  Webdriver


  	
  
Udemy


  	
  
20
  Hrs


  


Projects Link & Portfolio:



☑ https://rafayet13.github.io/Resume



Work
Experience:



Jr. Software Quality
Assurance Engineer (August 2018 –
Present)  



TechnoVista Limited (Nikunja-1, Khilkhet,
Dhaka)



Responsibilities:



·        
Performing
Functional & Non Functional Testing



·        
Performing
Regression Testing



·        
Reporting
& Tracking Bug Life Cycle in JIRA



·        
Preparing User Manual in Both Bengali & English



·        
Writing & Performing Test Case Using Selenium Framework. 



·        
Prepare Technical Documentation.



·        
Perform IQA and Facilitate to Quality Implement.



 Projects done for: SESIP, DGDA, ILO, SDF, BBS, Tottho Apa 


Jr. Software Engineer (January
2018 – July 2018)  



Wardan Tech Limited (Uttara, Dhaka)



Responsibilities:



·        
Software Requirement Analysis & Specification.



·        
Software Designing & Development.



·        
System Development, Testing & Documentation.



Projects done: Fully Functional
E-Commerce, Inventory Management System, Blog Posting 



 



Educational
Profile:




  
Exam Title


  	
  
Major (Group)


  	
  
Institute


  	
  
Passing Year


  	
  
Result


  

  
B.Sc. (Hons)


  	
  
Computer Science & Engineering


  	
  
Shanto-Mariam
  University of Creative Technology (SMUCT)


  	
  
2018


  	
  
3.74
  (Out of 4)


  

  
HSC


  	
  
Science


  	
  
Poyalgacha
  Degree College


  	
  
2013


  	
  
3.70
  (Out of 5)

  
SSC


Science


  	
  
Poyalgacha
  High School


  	
  
2009


  	
  
4.44
  (Out of 5)

Computer
Skills:

❖
MS Office: MS-Word,
MS-Excel, MS-PowerPoint.

❖ OS Setup:
Windows OS, Linux.

❖ Programming Language:
C, Python, PHP, JavaScript.

❖ Computer/IT:
Troubleshooting & Setup



❖
Testing Tool:
JIRA Bug Tracker, Selenium, Katalon Studio 

Personal Profile:

Father’s name: Md. Amir
Hossain Bhuiyain

Mother’s name: Bilkis Akter



Permanent Address: Vill: Perul, P.O: Poyalgacha,
P.S: Barura, Dist: Comilla.

Date of Birth: October 10, 1993

Religion: Islam


Nationality: Bangladeshi (by birth). 



Social
Network: https://linkedin.com/in/rafayet13

Language Skills:



     ☑ Bengali (1ST
Language) ☑
English (Good command in both verbal and written
communication)



Interests:



☑ Reading Blogs ☑ Contributing Open Source Platform
☑  Artificial Intelligence ☑ Big Data
Technology


Achievements & Other Activities:

☑
Recognized and awarded for contributing CMMI-L3
certification process of TechnoVista Limited.



☑ IBM Certification
Badge on Data
Science Foundation Level 1 & 2.



☑ Key instructor for 40
Hours Freelancing Hands on at Comilla University Organized
by World Bank.



☑ Predictive Data Analysis & Forecasting
with open Govt. data set (Oracle Data
Visualizer)

☑ Easy Way to Learn Data Mining (Video Tutorial)
in Bangla Collaborating with Bookbd@
YouTube.

  Rafayet Hossain




'''
message = message.upper()
wordlist = message.split()



count = {}

for word in wordlist:
    count.setdefault(word, 0)
    count[word] = count[word] + 1

maximum = max(count, key=count.get)
minimum = min(count, key=count.get)


print("Number of word found:", len(wordlist))
print("Maximum times:",  maximum, "And minimum times", minimum)

pprint.pprint(count)