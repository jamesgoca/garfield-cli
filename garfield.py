import webbrowser
import random
import datetime

print("""
Garfield on the TERMINAL!

|\\---/|
| o_o |
 \\_^_/


[1] View today's comic.
[2] View yesterday's comic.
[3] View a random comic.
[4] View the first strip.
[5] Exit
""")

while True:
	input_option = raw_input("What would you like to do? ")

	if input_option == "1":
		url = webbrowser.open("https://ermel.org/garfield.php")

	elif input_option == "2":
		yesterday = datetime.date.today() - datetime.timedelta(1)
		day = yesterday.strftime('%d')
		month = yesterday.strftime('%m')
		year = yesterday.strftime('%Y')
		url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(day, month, year)

	elif input_option == "3":
		# Get random date between start of comic and today

		start_date = datetime.date(1978, 7, 19)
		end_date = datetime.date.today()

		# Calculate time between dates

		time_between_dates = end_date - start_date
		days_between_dates = time_between_dates.days
		random_number_of_days = random.randrange(days_between_dates)
		random_date = start_date + datetime.timedelta(days=random_number_of_days)

		url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(random_date.day, random_date.month, random_date.year)
	elif input_option == "4":
		url = "https://ermel.org/garfield.php?day=19&month=06&year=1978"

	elif input_option == "5":
		break

	else:
		print("Please choose another option.")

	webbrowser.open(url)