import tkinter as tk


root = tk.Tk()
root.title("Interface")


start_button = tk.Button(root, text="Start")
start_button.pack(pady=5)


frame = tk.Frame(root)  
frame.pack(pady=5)  


tk.Label(frame, text="inhale1:").pack(side=tk.LEFT)
einatmen1_entry = tk.Entry(frame)
einatmen1_entry.pack(side=tk.LEFT)

tk.Label(frame, text="pause_in1:").pack(side=tk.LEFT)
pause_ein1_entry = tk.Entry(frame)
pause_ein1_entry.pack(side=tk.LEFT)

tk.Label(frame, text="exhale1:").pack(side=tk.LEFT)
ausatmen1_entry = tk.Entry(frame)
ausatmen1_entry.pack(side=tk.LEFT)

tk.Label(frame, text="pause_ex1:").pack(side=tk.LEFT)
pause_aus1_entry = tk.Entry(frame)
pause_aus1_entry.pack(side=tk.LEFT)

row2_frame = tk.Frame(root)  
row2_frame.pack(pady=5) 

tk.Label(row2_frame, text="inhale2:").pack(side=tk.LEFT)
einatmen2_entry = tk.Entry(row2_frame)
einatmen2_entry.pack(side=tk.LEFT)

tk.Label(row2_frame, text="pause_in2:").pack(side=tk.LEFT)
pause_ein2_entry = tk.Entry(row2_frame)
pause_ein2_entry.pack(side=tk.LEFT)

tk.Label(row2_frame, text="exhale2:").pack(side=tk.LEFT)
ausatmen2_entry = tk.Entry(row2_frame)
ausatmen2_entry.pack(side=tk.LEFT)

tk.Label(row2_frame, text="pause_ex2:").pack(side=tk.LEFT)
pause_aus2_entry = tk.Entry(row2_frame)
pause_aus2_entry.pack(side=tk.LEFT)


row3_frame = tk.Frame(root) 
row3_frame.pack(pady=5) 

tk.Label(row3_frame, text="inhale3:").pack(side=tk.LEFT)
einatmen3_entry = tk.Entry(row3_frame)
einatmen3_entry.pack(side=tk.LEFT)

tk.Label(row3_frame, text="pause_in3:").pack(side=tk.LEFT)
pause_ein3_entry = tk.Entry(row3_frame)
pause_ein3_entry.pack(side=tk.LEFT)

tk.Label(row3_frame, text="exhale3:").pack(side=tk.LEFT)
ausatmen3_entry = tk.Entry(row3_frame)
ausatmen3_entry.pack(side=tk.LEFT)

tk.Label(row3_frame, text="pause_ex3:").pack(side=tk.LEFT)
pause_aus3_entry = tk.Entry(row3_frame)
pause_aus3_entry.pack(side=tk.LEFT)


def fade_to_black(window, duration):
    steps = 100  
    delay = duration / steps  
    for i in range(steps + 1):
        
        color_value = int(255 - (255 * (i / steps)))  
        color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'  
        window.after(int(i * delay), lambda c=color: window.configure(bg=c))
       
def fade_to_white(window,duration):
    steps = 100
    delay = duration / steps
    for i in range(steps + 1):
        color_value = int(0 + (255 * (i / steps)))
        color = f'#{color_value:02x}{color_value:02x}{color_value:02x}'
        window.after(int(i * delay), lambda c=color: window.configure(bg=c))

def open_window():
    
    try:
        einatmen1_duration = int(einatmen1_entry.get())  
    except ValueError:
        einatmen1_duration = 2000  

    try:
        pause_ein_duration1 = int(pause_ein1_entry.get())
    except ValueError:
        pause_ein_duration1 = 2000
    
    try:
        ausatmen1_duration1 = int(ausatmen1_entry.get())
    except ValueError:
        ausatmen1_duration1 = 2000

    try:
        pause_aus_duration1 = int(pause_aus1_entry.get())
    except ValueError:
        pause_aus_duration1 = 2000

    try:
        einatmen2_duration = int(einatmen2_entry.get())
    except ValueError:
        einatmen2_duration = 2000

    try:
        pause_ein_duration2 = int(pause_ein2_entry.get())
    except ValueError:
        pause_ein_duration2 = 2000

    try:
        ausatmen2_duration2 = int(ausatmen2_entry.get())
    except ValueError:
        ausatmen2_duration2 = 2000

    try:
        pause_aus_duration2 = int(pause_aus2_entry.get())
    except ValueError:
        pause_aus_duration2 = 2000

    try:
        einatmen3_duration = int(einatmen3_entry.get())
    except ValueError:
        einatmen3_duration = 2000

    try:
        pause_ein_duration3 = int(pause_ein3_entry.get())
    except ValueError:
        pause_ein_duration3 = 2000

    try:
        ausatmen3_duration2 = int(ausatmen3_entry.get())
    except ValueError:
        ausatmen3_duration2 = 2000

    try:
        pause_aus_duration3 = int(pause_aus3_entry.get())
    except ValueError:
        pause_aus_duration3 = 2000
        

    


    open_window1 = tk.Toplevel(root)  
    open_window1.title("start_window")
    open_window1.geometry("1000x1000")  
    fade_to_black(open_window1, einatmen1_duration)  

    all = einatmen1_duration + pause_ein_duration1
    open_window1.after(all, lambda: fade_to_white(open_window1, ausatmen1_duration1))
    all = all + pause_aus_duration1 + ausatmen1_duration1
    open_window1.after(all, lambda: fade_to_black(open_window1, einatmen2_duration))
    all = all + einatmen2_duration + pause_ein_duration2
    open_window1.after(all, lambda: fade_to_white(open_window1, ausatmen2_duration2))
    all = all + ausatmen2_duration2 + pause_aus_duration2
    open_window1.after(all, lambda: fade_to_black(open_window1, einatmen3_duration))
    all = all + einatmen3_duration + pause_ein_duration3
    open_window1.after(all, lambda: fade_to_white(open_window1, ausatmen3_duration2))
    all = all + ausatmen3_duration2 + pause_aus_duration3

    open_window1.after(all, open_window1.destroy)

start_button.config(command=open_window)


root.mainloop()
