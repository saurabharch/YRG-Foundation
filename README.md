# YRG-Foundation
Save a HIV patient by creating a system that will enable donors to donate funds towards the betterment and treatment of HIVpositive patients.

##Team members

[Krish Munot] (https://github.com/KrishMunot) <br/>
[Dilip Kumar] <br/>
[Naresh Kumar]<br/>
[Ipsita Prakash] (https://github.com/ipsi16) <br/>
[Aravind Srivatsan] (https://github.com/aravindsrivats) <br/>
[Anubhav Chaturvedi] (https://github.com/AnubhavChaturvedi) <br/>
[Nageswara Rao Bommena] (https://github.com/bnagesh) <br/>
[Abhishek Chauhan] <br/>

# Notification Server ReadMe
Check the dependencies.sh file for related dependencies and install them.
To run the server, execute python manage.py runserver from inside postFacebookAPI folder.
Example send email query:

POST request to http://localhost:8000/send/email/ with request body:
{"address":"Vishranthi Charitable Trust, A.V.M Rajeswari Gardens, #4/227, M.G.R.Salai, Palavakkam, ECR, Chennai – 600 041", "time":"12.30pm", "date":"29-11-2015", "amount":"10000", "number_of_people":"200", "email":"abhishek.chauhan792@gmail.com"}

Example of send sms query:

POST request to http://localhost:8000/send/SMS/ with request body:
{"recepient":"+918008529177"}
