import PySimpleGUI as gui

# format = [[gui.Text("Hello from PySimpleGUI")], [gui.Button("OK")]]
window = gui.Window(
    background_color="light pink",
    title="Plant Watering Calendar",
    layout=[[gui.Text("Hello from PySimpleGUI")]],
    margins=(100, 50),
    icon="icon.png",
).read()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == gui.WIN_CLOSED:
        break

window.close()
