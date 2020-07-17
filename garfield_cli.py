import click
import webbrowser
import datetime
import garfield

# Define CLI object

@click.group()
def cli():
	pass

# Get today's comic

@cli.command()
def today():
	garfield.today()

@cli.command()
@click.option('-d', '--day', required=True, help="Day of the comic's release.", type=int)
@click.option('-m', '--month', required=True, help="Month of the comic's release.", type=int)
@click.option('-y', '--year', required=True, help="Year of the comic's release.", type=int)
def fetch(day, month, year):
	garfield.fetch(day, month, year)

# Get yesterday's comic

@cli.command()
def yesterday():
	garfield.yesterday()

@cli.command()
def random():
	garfield.random()

@cli.command()
def first():
	garfield.first()

if __name__ == '__main__':
	cli()
