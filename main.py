# this is part of the TraceScan project.
#
# Release: v1.0-dev1
#
# Copyright (c) 2022-2023  Juan Bindez  <juanbindez780@gmail.com>
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


def ping():
    target = "google.com"  # exemplo de alvo, pode ser substituído
    output = subprocess.run(["ping", "-c", "3", "-n", target], capture_output=True, text=True)
    result_text.delete('1.0', END)
    result_text.insert(END, f"Ping results for {target}:\n{output.stdout}")


window = Tk()
master = window
master.title("TraceScan")
master.geometry("600x700")

ping_button = Button(master, text="Ping", command=ping)
ping_button.pack()

result_text = Text(master, height=30)
result_text.pack()


if __name__ == "__main__":
    window.mainloop()
