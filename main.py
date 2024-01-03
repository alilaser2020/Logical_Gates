import PySimpleGUI as sg

sg.theme("LightGray6")

first_layout = [
    [sg.Text("Welcome to Gates Tutorial Application (GTA)", font="Calibre 30", text_color="red", expand_x=True,
             justification="center")],
    [sg.Text("Click tabs to start", font="Caliber 25", text_color="blue", expand_x=True, justification="center")],
    [sg.Image("gates/start.png", expand_x=True)],
    [sg.Text("By AliLaser", font="Calibre 15", text_color="black", expand_x=True, justification="center")]
]

window = sg.Window("GTA", first_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
