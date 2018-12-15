#! /usr/bin/env python3
import argparse
import requests


def hello(r_hello):
    hello_url = 'http://localhost:8081'
    r_hello = requests.get(hello_url)
    return r_hello.text


def world(r_world):
    world_url = 'http://localhost:8082'
    r_world = requests.get(world_url)
    return r_world.text

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--hello', type=str,
                        dest='hello', help='print hello container text')
parser.add_argument('-w', '--world', type=str,
                        dest='world', help='print world container text')
parser.add_argument('-a', '--all', type=str,
                        dest='all', help='print both container text')

args = parser.parse_args()

if args.hello:
    print(hello(hello))
elif args.world:
    print(world(world))
elif args.all:
    print(f"Output from : {hello(hello)}Output from: {world(world)}")
