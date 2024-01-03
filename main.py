import PySimpleGUI as sg

sg.theme("LightGray6")

first_layout = [
    [sg.Text("Welcome to Gates Tutorial Application (GTA)", font="Calibre 30", text_color="red", expand_x=True,
             justification="center")],
    [sg.Text("Click tabs to start", font="Caliber 25", text_color="blue", expand_x=True, justification="center")],
    [sg.Image("gates/start.png", expand_x=True)],
    [sg.Text("By AliLaser", font="Calibre 15", text_color="black", expand_x=True, justification="center")]
]

and_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-ANDBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-ANDBTN2-", size=(4, 30), pad=(0, 5))]
])

and_layout = [
    [
        sg.Column([
            [
                and_btn,
                sg.Image("gates/and.png", expand_x=True, expand_y=True, key="-ANDGATE-", pad=0),
                sg.Image("gates/off.png", expand_x=True, expand_y=True, key="-OFF-", pad=0)
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/and_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="Center", pad=(100, 0))
    ]
]

window = sg.Window("GTA", and_layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
