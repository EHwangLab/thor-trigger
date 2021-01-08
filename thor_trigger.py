import os.path
import sys
import tkinter as tk
import tkinter.font as font

from set_com import set_com


def set_com_high():
    set_com(high=True)


def set_com_low():
    set_com(high=False)


pad = 10
geometry = '256x256'
window_title = 'Thor Trigger'
window_icon_file = os.path.join(sys._MEIPASS,'FaceValueDog50.png')

root = tk.Tk()
root.title(window_title)
root.geometry(geometry)

# root.iconbitmap(default=window_icon_file)
root.iconphoto(False, tk.PhotoImage(file=window_icon_file))

frame = tk.Frame(root)
frame.pack(padx=pad, pady=pad, fill='both', expand=True)

button_font = font.Font(family='Sans', size=24, weight='bold')
button = tk.Button(frame, text='START/HIGH', fg='green', command=set_com_high,
                   font=button_font)
button.pack(side=tk.TOP, padx=pad, pady=pad, fill='both', expand=True)
button = tk.Button(frame, text='STOP/LOW', fg='red', command=set_com_low,
                   font=button_font)
button.pack(side=tk.BOTTOM, padx=pad, pady=pad, fill='both', expand=True)

root.mainloop()
