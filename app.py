from flask import Flask, render_template
from random import choice
DailyExcuse = Flask(__name__)

excuses = []
with open('undskyldninger.txt') as f:
	excuses = f.readlines()

def getRandomExcuse():
	exc = choice(excuses)
	if len(exc) != 0:
		exc = exc[0].lower() + exc[1:len(exc)-1]
		return exc.strip()
	return None

@DailyExcuse.route("/")
def hello():
	return render_template('index.html', excuse=getRandomExcuse())

if __name__ == "__main__":
	DailyExcuse.run()
