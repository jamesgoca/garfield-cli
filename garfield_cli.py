import click
import webbrowser
import datetime
import garfield

# Define CLI object

@click.group()
def cli():
	pass

# Comic command

@cli.command()
def today():
	"""Retrieve today's Garfield comic."""
	garfield.today()

@cli.command()
@click.option('-d', '--day', required=True, help="Day of the comic's release.", type=int)
@click.option('-m', '--month', required=True, help="Month of the comic's release.", type=int)
@click.option('-y', '--year', required=True, help="Year of the comic's release.", type=int)
def fetch(day, month, year):
	"""Retrieve a comic from the Garfield archive."""
	garfield.fetch(day, month, year)

@cli.command()
def yesterday():
	"""Retrieve yesterday's Garfield comic."""
	garfield.yesterday()

@cli.command()
def random():
	"""Retrieve a random comic from the Garfield archive."""
	garfield.random()

@cli.command()
def first():
	"""Retrieve the first comic from the Garfield archive."""
	garfield.first()

if __name__ == '__main__':
	cli()
