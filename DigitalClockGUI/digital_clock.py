from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date
from tkinter import messagebox

class DigitalClock:
    def __init__(self):
        self.root = Tk()
        self.root.title('Digital Clock')

        # Digital Clock
        self.lbl = Label(self.root, font=('calibri', 40, 'bold'),
                         background='purple',
                         foreground='white')
        self.lbl.pack(anchor='center')

        # Date Display
        self.date_lbl = Label(self.root, font=('calibri', 20, 'bold'),
                              background='purple',
                              foreground='white')
        self.date_lbl.pack(anchor='center')

        # Alarm Settings
        self.alarm_frame = Frame(self.root)
        self.alarm_frame.pack(anchor='center')
        self.alarm_lbl = Label(self.alarm_frame, text='Alarm Time (HH:MM:SS):')
        self.alarm_lbl.pack(side=LEFT)
        self.alarm_entry = Entry(self.alarm_frame, width=10)
        self.alarm_entry.pack(side=LEFT)
        self.alarm_button = Button(self.alarm_frame, text='Set Alarm', command=self.set_alarm)
        self.alarm_button.pack(side=LEFT)

        # Update Time and Date
        self.update_time()

    def update_time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.date_lbl.config(text=str(date.today()))
        self.lbl.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time = self.alarm_entry.get()
        if alarm_time:
            self.alarm_button.config(text='Alarm Set')
            self.check_alarm(alarm_time)
        else:
            messagebox.showerror('Error', 'Please enter alarm time')

    def check_alarm(self, alarm_time):
        current_time = strftime('%H:%M:%S')
        if current_time == alarm_time:
            messagebox.showinfo('Alarm', 'Wake Up!')
            self.alarm_button.config(text='Set Alarm')
        else:
            self.alarm_frame.after(1000, lambda: self.check_alarm(alarm_time))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock = DigitalClock()
    clock.run()