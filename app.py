from database import *
#from flask_bootstrap import Bootstrap
from flask import Flask, request, redirect, render_template
from flask import session as login_session
from model import *
from textblob import TextBlob
import smtplib

app = Flask(__name__)
#Bootstrap(app)


app.config['SECRET_KEY'] = 'you-will-never-guess'



@app.route('/About.html')
def fullList1():
    items=query_all()
    return render_template('About.html',items=items)




@app.route('/' , methods=['GET','POST'])
def upload():
	if request.method == 'GET' :
		return render_template('Home.html')

	else:
		

		print("creating object")
		name = request.form['name']
		email = request.form['email']
		comment = request.form['comment']
		link = request.form['link']
		date = request.form['date']
		add_item(name , email , comment, date , link)

		feedback = TextBlob(comment).polarity
		if feedback > 0:
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				smtp.login('facial.recognition.feedback@gmail.com','faceface123')
				subject = 'Thank you for reviewing our website!!'
				subject1 = 'cheer up, godd review'
				body = 'Hey, thank you very much for you positivity, we are very happy that you liked the website, and would like to hear more from you about what do you think will make it even better!!. KEEP THAT GOOD ATTITUDE:)'
				msg = f'subject: {subject}\n\n{body}'
				msg1 = f'subject: {subject1}\n\n{comment}'
				smtp.sendmail('','facial.recognition.feedback@gmail.com',msg1)
				smtp.sendmail('',email,msg)
				return render_template("About.html")
		else:
			with smtplib.SMTP('smtp.gmail.com',587) as smtp:
				smtp.ehlo()
				smtp.starttls()
				smtp.ehlo()
				smtp.login('facial.recognition.feedback@gmail.com','faceface123')
				subject = 'Thank you for reviewing our website!!'
				subject1 = 'mmm, some one was in a bad mood'
				body = 'Hey, we noticed that you did not like the website that much, but, we are here for you... just tell us what do you think will make this website amazing and suitable for you. Your opinion is our top priority;)!!!'
				msg = f'subject: {subject}\n\n{body}'
				msg1 = f'subject: {subject1}\n\n{comment}'
				smtp.sendmail('','facial.recognition.feedback@gmail.com',msg1)
				smtp.sendmail('',email,msg)
				return render_template("About.html")


if __name__ == '__main__':
	app.run(debug=True)
