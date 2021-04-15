import PySimpleGUI as sg
import datetime
layout = [[sg.Text('S\nA\nA\nT', font=("Pure Heart", 30)), sg.Text('', key='time', background_color='black', font=("Helvetica", 70), size=(7, 1))],
         [sg.Quit('ÇIKIŞ')]]

window = sg.Window('CodeCraft Saat Projesi').Layout(layout)
def getTime():
    return datetime.datetime.now().strftime('%H:%M:%S')
def main(interface):
    while True:
        event, values = interface.Read(timeout=10)
        if event in (None, 'ÇIKIŞ'):
            break
        interface.FindElement('time').Update(getTime())
if __name__ == '__main__':
    main(window)
