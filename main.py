import PySimpleGUI as sg


def logical_gates(and1, and2, or1, or2, Not):
    """
    A method for process of input gates and generate appropriate output of gates
    :param and1:
    :param and2:
    :param or1:
    :param or2:
    :param Not:
    :return:
    """
    if bool(and1) and bool(and2):
        window["-OFF1-"].update("gates/on.png")
    else:
        window["-OFF1-"].update("gates/off.png")

    if bool(or1) or bool(or2):
        window["-OFF2-"].update("gates/on.png")
    else:
        window["-OFF2-"].update("gates/off.png")

    if not bool(Not):
        window["-OFF3-"].update("gates/on.png")
    else:
        window["-OFF3-"].update("gates/off.png")


sg.theme("LightBlue7")

first_layout = [
    [sg.Text("Welcome to\nGates Tutorial Application\n(GTA)", font="Calibre 30", text_color="red", expand_x=True,
             justification="center")],
    [sg.Text("Click tabs to start", font="Caliber 25", text_color="blue", expand_x=True, justification="center")],
    [sg.Image("gates/start.png", expand_x=True)],
    [sg.Text("By AliLaser", font="Calibre 15", text_color="black", expand_x=True, justification="center")]
]

and_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-ANDBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-ANDBTN2-", size=(4, 30), pad=(0, 5))]
])

# off_image = sg.Column([
#     [
#         sg.Image("gates/off.png", key="-OFF-", expand_x=True, expand_y=True, pad=0)
#     ]
# ])

and_layout = [
    [
        sg.Column([
            [
                and_btn,
                sg.Image("gates/and.png", expand_x=True, expand_y=True, key="-ANDGATE-", pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF1-", expand_x=True, expand_y=True, pad=(0, 50))
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

or_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-ORBTN1-", size=(4, 30), pad=(0, 5))],
    [sg.Slider(range=(0, 1), key="-ORBTN2-", size=(4, 30), pad=(0, 5))]
])

or_layout = [
    [sg.Column([
        [
            or_btn,
            sg.Image("gates/or.png", key="-OR-", expand_x=True, expand_y=True, pad=(0, 50)),
            sg.Image("gates/off.png", key="-OFF2-", expand_x=True, expand_y=True, pad=(0, 50))
        ]
    ], justification="center")],
    [sg.Column([
        [
            sg.Image("gates/or_table.png", expand_x=True, expand_y=True)
        ]
    ], justification="center", pad=(100, 0))]
]

not_btn = sg.Column([
    [sg.Slider(range=(0, 1), key="-NOTBTN-", size=(4, 30), pad=(0, 50))]
])

not_layout = [
    [
        sg.Column([
            [
                not_btn,
                sg.Image("gates/not.png", expand_x=True, expand_y=True, pad=(0, 50)),
                sg.Image("gates/off.png", key="-OFF3-", expand_y=True, expand_x=True, pad=(0, 50))
            ]
        ], justification="center")
    ],
    [
        sg.Column([
            [
                sg.Image("gates/not_table.png", expand_x=True, expand_y=True)
            ]
        ], justification="center", pad=(100, 0))
    ]
]

tab_group = [[
    sg.TabGroup([
        [
            sg.Tab("start", first_layout),
            sg.Tab("and", and_layout),
            sg.Tab("or", or_layout),
            sg.Tab("not", not_layout)
        ]
    ], font="Calibre 15", tab_location="top", tab_background_color="black", title_color="white",
        selected_background_color="yellow", selected_title_color="red")
]]

window = sg.Window("GTA", tab_group)

while True:
    event, values = window.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    logical_gates(values["-ANDBTN1-"],
                  values["-ANDBTN2-"],
                  values["-ORBTN1-"],
                  values["-ORBTN2-"],
                  values["-NOTBTN-"])

window.close()
