#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/7/27 17:09
@annotation = '' 
"""
import click


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo('Initialized the database')


@cli.command()
def dropdb():
    click.echo('Dropped the database')


@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    """Hello many time"""
    for x in range(count):
        click.echo('Hello %s!' % name)


cli()
