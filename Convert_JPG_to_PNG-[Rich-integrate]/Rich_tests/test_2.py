# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-08-30 18:29:03
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-31 20:26:22


import sys
from rich.console import Console
from datetime import datetime

error_console = Console(stderr=False, style="bold red")
error_console.print("error found")


# with open("report.txt" , "wt") as report_file:
# 	console = Console(file=report_file, width=34)
# 	console.rule(f"Report Generated {datetime.now().ctime()}")


## record or capture the output of the terminal to present it later on

console = Console()

with console.capture() as capture:
	console.print("[bold red]This output was captured before.")


str_output = capture.get()
print(str_output)


# output using paging

# from rich.__main__ import make_test_card

# with console.pager():
# 	console.print(make_test_card())

# alternate screen

from time import sleep

from rich.align import Align
from rich.text import Text 
from rich.panel import Panel

# with console.screen(style="bold white on red") as screen:
# 	for count in range(5):
# 		renderable = Text.from_markup(f"[blink]Do not Panic boi[/blink]\n{count}", justify="center")
# 		text = Align.left(renderable, vertical="top")
# 		screen.update(Panel(text))
# 		sleep(1)


with console.screen(style="bold blue on red") as screen:
	while True:
		renderable = Text.from_markup(f"[blink]YOU ARE GOD DAMN LATE TAMIM SIR[/blink]", justify="center")
		text = Align.center(renderable, vertical="middle")
		screen.update(Panel(text))
		sleep(50)
