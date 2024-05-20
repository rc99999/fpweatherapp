import flet as ft
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['DEFAULT']['API_KEY']

def main(page):
    page.add(ft.Text('Hello'))

ft.app(target=main)

