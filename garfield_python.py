import webbrowser
import random
import datetime
import garfield

print("""
Garfield on the TERMINAL!

|\\---/|
| o_o |
 \\_^_/


[1] View today's comic.
[2] View yesterday's comic.
[3] View a random comic.
[4] View the first strip.
[5] View a comic by date.
[6] Exit
""")

while True:
	input_option = raw_input("What would you like to do? ")

	if input_option == "1":
		garfield.today()

	elif input_option == "2":
		garfield.yesterday()

	elif input_option == "3":
		garfield.random()

	elif input_option == "4":
		garfield.first()

	elif input_option == "5":
		day = raw_input("What is the day of the comic you want to read? ")
		month = raw_input("What is the month of the comic you want to read? ")
		year = raw_input("What is the year of the comic you want to read? ")
		garfield.fetch()

	elif input_option == "6":
		break

	else:
		print("Please choose another option.")
