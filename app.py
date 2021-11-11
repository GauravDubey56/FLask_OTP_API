import smtplib
import math, random
# from Flask_Cors import CORS
import os 
from flask import Flask,render_template, request, redirect, url_for,jsonify,session
PORT = int(os.environ.get('PORT', 33507))
HOST = 'https://otp--flask-api.herokuapp.com'
#--------------------------------------------------------------------------------------------------------------
sender_email='qliodev@gmail.com'         
password='famousguy'
#--------------------------------------------------------------------------------------------------------------
# function to generate OTP
def generateOTP() : 
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
    
#send mail    
def mail(email,OTP):
	global sender_email,password
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	s.login(sender_email, password)
	s.sendmail(sender_email,email, str(OTP))
	s.quit()

app = Flask(__name__)
# CORS(app)
@app.route('/OTP', methods =["GET", "POST"])
def home():
    email_=request.args.get('id')
    OTP_=generateOTP()
    mail(email_,OTP_)
    return jsonify(OTP=OTP_,email=email_)
    
    
if __name__ == '__main__' :
        app.run(debug=False,host = HOST, port = PORT)
