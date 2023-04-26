# this is part of the TraceScan project.
#
# Release: v1.0-dev3
#
# Copyright (c) 2023  Juan Bindez  <juanbindez780@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#  
# repo: https://github.com/juanBindez

import time
from datetime import datetime
import subprocess

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from scapy.all import *


def traceroute(target):
    ttl = 1
    while True:
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=False, timeout=2)
        if reply is None:
            result_text.insert(END, f"* * * * no reply * * * *\n")
            pass
        elif reply.type == 11:
            result_text.insert(END, f"{reply.src} - {round(reply.time*1000, 2)} ms (TTL={reply.ttl})\n")
        elif reply.type == 0:
            result_text.insert(END, f"{reply.src} - {round(reply.time*1000, 2)} ms (TTL={reply.ttl})\n")
            break
        else:
            result_text.insert(END, f"{reply.src} - ?? (TTL={reply.ttl})\n")
            break
        ttl += 1
   

def run_traceroute():
    try:
        target = target_entry.get()
        if target:
            traceroute(target)
        else:
            messagebox.showerror("Error", "Target field is empty")
    except PermissionError:
        messagebox.showerror("Error", "you need to run this program as superuser")


def ping_google_ipv4():
    result_text.delete('1.0', END)
    target = "8.8.8.8"
    cmd = ["ping", "-c", "23", "-n", target]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        now = datetime.now()
        time_now = now.strftime("%H:%M:%S")
        output = process.stdout.readline().decode()
        if not output:
            break
        #result_text.delete('1.0', END)
        result_text.insert(END, f"{time_now} {output}")
        result_text.update()


def ping_google_ipv6():
    result_text.delete('1.0', END)
    target = "google.com"
    cmd = ["ping", "-c", "23", "-n", target]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        now = datetime.now()
        time_now = now.strftime("%H:%M:%S")
        output = process.stdout.readline().decode()
        if not output:
            break
        #result_text.delete('1.0', END)
        result_text.insert(END, f"{time_now} {output}")
        result_text.update()


window = Tk()
window.title("TraceScan")
window.geometry("685x650")
window.resizable(False, False)


def make_menu(w):
    global the_menu_1
    the_menu_1 = Menu(w, tearoff=0)
    the_menu_1.add_command(label="Colar")
    
    
def show_menu(e):
    w = e.widget
    the_menu_1.entryconfigure("Colar",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu_1.tk.call("tk_popup", the_menu_1, e.x_root, e.y_root)


target_label = Label(window, text="Target IP:")
target_label.place(x=20, y=10)

make_menu(window)
target_entry = Entry(window)
target_entry.place(x=80, y=10)
target_entry.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
lbl = Label(window, text = "")


run_button = Button(window, text="Run Traceroute", command=run_traceroute)
run_button.place(x=100, y=40)

result_text = Text(window, height=30)
result_text.place(x=20, y=100)

ping_button = Button(window, text="Ping Google IPv4", command=ping_google_ipv4)
ping_button.place(x=400, y=5)

ping_button = Button(window, text="Ping Google IPv6", command=ping_google_ipv6)
ping_button.place(x=545, y=5)

result_text = Text(window, height=30)
result_text.place(x=20, y=100)

license_label = Label(window, text="License GPLv2")
license_label.place(x=500, y=620)

aboult_label = Label(window, text="TraceScan  v1.0-dev3")
aboult_label.place(x=300, y=620)

copy_label = Label(window, text="Copyright (c) 2023  Juan Bindez")
copy_label.place(x=40, y=620)


if __name__ == "__main__":
    window.mainloop()
