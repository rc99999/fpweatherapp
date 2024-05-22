import flet as ft
import configparser
import requests


config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['DEFAULT']['API_KEY']
url = "http://api.openweathermap.org/data/2.5/weather"
headers = {}
params = {
    "appid":api_key,
    "q":"Tokyo",
    "units":"metric",
    "lang":"ja",
}


# データ取得
_data = requests.get(url, headers=headers, params=params)


def main(page: ft.Page):
    page.window_width = 620
    page.window_height = 360
    page.title = "天気"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.PURPLE


    # データ取り出し
    def _info():
        # 場所
        _location = _data.json()["name"]
        # 天気
        _weather = _data.json()["weather"][0]["description"]
        # 気温
        _temp = str(int(_data.json()["main"]["temp"]))

        return[
            _location,
            _weather,
            _temp,
        ]


    #
    _today = _info()


    #
    _v = ft.Container(
        width=600,
        height=300,
        bgcolor=ft.colors.PURPLE,
        padding=30,
        content=ft.Column(
            alignment="start",
            spacing=30,
            controls=[
                ft.Row(
                    alignment="center",
                    controls=[
                        ft.Text(_today[0], size=36, weight='w500'),
                    ],
                ),
                ft.Container(padding=ft.padding.only(bottom=5)),
                ft.Row(
                    alignment="center",
                    spacing=50,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(_today[1], size=56, weight='w500'),
                            ]
                        ),
                        ft.Column(
                            spacing=5,
                            horizontal_alignment="center",
                            controls=[
                                ft.Text("気温", size=16, text_align="center"),
                                ft.Row(
                                    vertical_alignment="start",
                                    spacing=0,
                                    controls=[
                                        ft.Container(
                                            content=ft.Text(_today[2] + " ℃", size=40),
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
            ],
        )
    )


    page.add(_v)


ft.app(target=main)

