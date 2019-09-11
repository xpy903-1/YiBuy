#!/usr/bin/python3
# coding: utf-8
from redis import Redis

config = {
    'host': '114.116.231.3',
    'port': 6378,
    'db': 9,
    'decode_responses': True
}


rd_client = Redis(**config)

if __name__ == '__main__':
    rd_client.keys('*')