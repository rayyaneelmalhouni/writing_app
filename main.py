
from tkinter import *

# # Variable
min_timer_id = None
typing = False


# # Functions
def on_start():
    global typing
    start_button.config(state="disabled")
    text_area.delete("1.0", "end")
    text_area.focus_set()
    start_timer(300)
    typing = True


def key_press(event):
    if typing:
        key = event.keysym
        if key not in ["space", "Return", "BackSpace"]:
            min_timer(5)


def min_timer(count):
    global min_timer_id
    if typing:
        if count == 5 and min_timer_id:
            window.after_cancel(min_timer_id)
        if count > 0:
            min_timer_id = text_area.after(1000, min_timer, count - 1)
        else:
            text_area.delete("1.0", "end")


def start_timer(count):
    minutes = int(count / 60)
    seconds = count - (minutes * 60)
    formatted_minutes = str(minutes)
    formatted_seconds = str(seconds).zfill(2)
    timer.config(text=f"{formatted_minutes}:{formatted_seconds}")
    if count > 0:
        timer.after(1000, start_timer, count - 1)
    else:
        stop_timer()


def stop_timer():
    global typing
    timer.config(text=f"5:00")
    typing = False
    start_button.config(state="normal")



# # Display
window = Tk()
window.title("Writing App")

title = Label(text="Writing App", font=("Arial", 36, "normal"))
title.grid(column=0, row=0, pady=20)

timer = Label(text="5:00", font=("Arial", 18, "bold"))
timer.grid(column=1, row=0, padx=20)

text_area = Text(height=10, width=50)
text_area.grid(column=0, row=1, pady=20, padx=20)
text_area.bind("<Key>", key_press)

start_button = Button(text="Start", padx=20, pady=5, command=on_start)
start_button.grid(column=0, row=2, pady=15)

window.mainloop()
