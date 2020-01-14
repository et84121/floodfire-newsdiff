from crawler import Crawler
from configparser import ConfigParser
from datetime import date, timedelta


def test_NTK():
    config = ConfigParser()
    config['NTK'] = {}
    config['NTK']['endDay'] = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')
    config['NTK']['sleepTime'] = '0'
    with open('config.ini', 'a') as configfile:
        config.write(configfile)
    c = Crawler(['none', 'ntk', 'list'])
    c.main()
    c = Crawler(['none', 'ntk', 'page'])
    c.main()


def test_NOW():
    config = ConfigParser()
    config['NOW'] = {}
    config['NOW']['endDay'] = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')
    config['NOW']['sleepTime'] = '0'
    with open('config.ini', 'a') as configfile:
        config.write(configfile)
    c = Crawler(['none', 'now', 'list'])
    c.main()
    c = Crawler(['none', 'now', 'page'])
    c.main()
