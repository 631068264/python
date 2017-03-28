#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author = 'wyx'
@time = 16/8/25 10:49
@annotation = '' 
"""
import click

"""
(.env) ➜  cmd git:(master) ✗ python deploy.py sync
Debug is off
(.env) ➜  cmd git:(master) ✗ python deploy.py --debug sync
Debug is on

"""


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.pass_context
def sync(ctx):
    click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))


if __name__ == '__main__':
    cli(obj={})
