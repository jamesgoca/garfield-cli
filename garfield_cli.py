import click
import webbrowser
import datetime

@click.group()
def cli():
	pass

# Get today's comic

@click.command()
def today():
	url = webbrowser.open("https://ermel.org/garfield.php")
	webbrowser.open(url)

# Get yesterday's comic

@click.command()
def yesterday():
	yesterday = datetime.date.today() - datetime.timedelta(1)
	day = yesterday.strftime('%d')
	month = yesterday.strftime('%m')
	year = yesterday.strftime('%Y')
	url = "https://ermel.org/garfield.php?day={}&month={}&year={}".format(day, month, year)
	webbrowser.open(url)

# Add commands

cli.add_command(today)
cli.add_command(yesterday)

if __name__ == '__main__':
	cli()
