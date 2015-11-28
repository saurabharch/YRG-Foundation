from django.shortcuts import render

from django.http import HttpResponse
from twilio.rest import TwilioRestClient
import json
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

def index(request):
    if request.method == 'POST':
        body = request.read().decode("utf-8")
        req = json.loads(body)
        to = req['recepient']
        account_sid = "AC9a9ddc10ea7ebbcee4551116b30453ba"
        auth_token = "b880c3636c7291b54c6edc1421001315"
        client = TwilioRestClient(account_sid, auth_token)

        msg = "Hello there!"    ## Put your message here

        message = client.messages.create(to="+918008529177", from_="+12017318779",
                                     body=msg)
        return HttpResponse("SMS Sent successfully.")
    else:
        return HttpResponse("Please send a POST request!")

def email(request):

    if request.method == 'POST':
        body = request.read().decode("utf-8")
        req = json.loads(body)
        msg = MIMEText("Dear Sir/Madam,\n\nWe thank you for your agreeing to make a donation to “KATHIR DHAN” on the " + req['date'] + ". \n\nIn response to your request we confirm that we are making arrangements to provide Lunch on " + req['date'] + " to " + req['number_of_people'] + " Elderly Destitute at " + req['address'] + " at " + req['time'] + ".\n\nPlease send your donation amount of Rs. " + req['amount'] + " by cheque/Demand draft drawn in the name of Y.R.Gaitonde Medical Educational and Research Foundation to our office at VHS Campus, Chennai-600113. If you decide to send the remittance by RTGS/NEFT please find the details of our bank account below:\n\nBeneficiary Name: YR Gaitonde Medical, Educational and Research Foundation\nName of Bank: HDFC Bank Ltd.\nBank Address: No: 30, Cenotaph Road, Teynampet, Chennai – 600 018.\nAccount Number: No. 12162020000248\nRTGS/NEFT IFSC: HDFC0001216\nAccount Short Name: YR Gaitonde Medical\n\nWe once again thank you for your kind gesture and look forward to hearing from you.\n\n\nYours sincerely,\nFor Y.R.GAITONDE MEDICAL EDUCATIONAL AND RESEARCH FOUNDATION")

        sender = 'senderEmail@gamil.com'
        receiver = req['email']
        msg['Subject'] = 'Email From Python Script'
        msg['From'] = sender
        msg['To'] = receiver
        password = ''   #   Enter sender email's password here.
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, [receiver], msg.as_string())
        s.quit()

        return HttpResponse("Email Sent Successfully.")
    else:
        return HttpResponse("Please send a POST request!")