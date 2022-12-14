from pynput.keyboard import Key, Listener
from datetime import datetime


def on_press(key):
    if key == Key.f8:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("log.txt", "a") as file:
            file.write(f"{dt_string} \n")


if __name__ == '__main__':
    with Listener(on_press=on_press) as listener:
        listener.join()
