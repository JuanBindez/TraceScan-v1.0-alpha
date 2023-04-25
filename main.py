# this is part of the TraceScan project.
#
# Release: v1.0-dev2
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


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import subprocess
import whois
from scapy.all import *


def traceroute(target):
    result_text.delete('1.0', END)
    ttl = 1
    while True:
        pkt = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(pkt, verbose=False, timeout=2)
        if reply is None:
            result_text.insert(END, f"* * * * \n")
            break
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
    target = target_entry.get()
    if target:
        traceroute(target)
    else:
        messagebox.showerror("Error", "Target field is empty")

def ping_google():
    target = "google.com"  # exemplo de alvo, pode ser substituído
    output = subprocess.run(["ping", "-c", "23", "-n", target], capture_output=True, text=True)
    result_text.delete('1.0', END)
    result_text.insert(END, f"Ping results for {target}:\n{output.stdout}")


window = Tk()
window.title("TraceScan")
window.geometry("700x650")

target_label = Label(window, text="Target:")
target_label.place(x=20, y=20)

target_entry = Entry(window)
target_entry.place(x=80, y=20)

run_button = Button(window, text="Run Traceroute", command=run_traceroute)
run_button.place(x=200, y=20)

result_text = Text(window, height=30)
result_text.place(x=20, y=100)

ping_button = Button(window, text="Ping Google", command=ping_google)
ping_button.pack()

result_text = Text(window, height=30)
result_text.place(x=20, y=100)


if __name__ == "__main__":
    window.mainloop()
