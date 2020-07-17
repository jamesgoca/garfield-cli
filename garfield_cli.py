import click
import webbrowser
import datetime

# Define CLI object

@click.group()
def cli():
	pass

# Get today's comic

@cli.command()
def today():
	url = webbrowser.open("https://ermel.org/garfield.php")
	webbrowser.open(url)

@cli.command()
@click.option('-d', '--day', required=True, help="Day of the comic's release.", type=int)
@click.option('-m', '--month', required=True, help="Month of the comic's release.", type=int)
@click.option('-y', '--year', required=True, help="Year of the comic's release.", type=int)
def fetch(day, month, year):
	start_date = datetime.date(1978, 7, 19)
	comic_release_date = datetime.date(year, month, day)
	today = datetime.date.today() + datetime.timedelta(1)

	if start_date < comic_release_date and start_date < today:
		url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(day, month, year)
		webbrowser.open(url)
	else:
		click.echo("This comic does not exist.")

# Get yesterday's comic

@cli.command()
def yesterday():
	yesterday = datetime.date.today() - datetime.timedelta(1)
	day = yesterday.strftime('%d')
	month = yesterday.strftime('%m')
	year = yesterday.strftime('%Y')
	url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(day, month, year)
	webbrowser.open(url)

@cli.command()
def random():
	# Get random date between start of comic and today

	start_date = datetime.date(1978, 7, 19)
	end_date = datetime.date.today()

	# Calculate time between dates

	time_between_dates = end_date - start_date
	days_between_dates = time_between_dates.days
	random_number_of_days = random.randrange(days_between_dates)
	random_date = start_date + datetime.timedelta(days=random_number_of_days)

	url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(random_date.day, random_date.month, random_date.year)
	webbrowser.open(url)

@cli.command()
def first():
	url = "https://ermel.org/garfield.php?day=19&month=06&year=1978"
	webbrowser.open(url)

if __name__ == '__main__':
	cli()
