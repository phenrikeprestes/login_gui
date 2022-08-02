import PySimpleGUI as sg

sg.theme('Black')
layout = [
    [sg.Text('User')],
    [sg.Input(key='user')],
    [sg.Text('password')],
    [sg.Input(key='password')],
    [sg.Button('login')],
    [sg.Text(key='message')],
]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'login':
        user = values['user']
        password = values['password']
