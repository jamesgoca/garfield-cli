import webbrowser
import datetime

def yesterday():
	yesterday = datetime.date.today() - datetime.timedelta(1)
	day = yesterday.strftime('%d')
	month = yesterday.strftime('%m')
	year = yesterday.strftime('%Y')
	url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(day, month, year)
	webbrowser.open(url)