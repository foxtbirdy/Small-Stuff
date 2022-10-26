# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-08-30 17:38:50
# @Last Modified by:   Climax
# @Last Modified time: 2022-08-30 18:28:25



# work with me on the run~


from rich.console import Console, OverflowMethod
import time 

console = Console()

console.print([1,2,3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")

## JSON Printing

console.print_json('[false, true, null, "foo"]')

# divider

console.rule("[bold red]Chapter 2") 


# print status based timer

# for i in range(10):
# 	with console.status(f"Working script...{i}"):
# 		time.sleep(1)
# 		print(f"Completed Script {i}")



## Justify / Alignment

console2 = Console(width=30) # set 

style = "bold white on blue"
console2.print("Rich", style=style)
console2.print("Will you be my lover?", style=style, justify="left")
console2.print(':heart:', style=style, justify="center")
console2.print("then make me last forever", style=style, justify="right")



# fold, crop, ellipis large words
# import OverflowMethod

console3 = Console(width=16)
console3.print("Fold = " , "File_2032-31w3-ADE2-2123-AFJFSOFJSDFS", overflow="fold", style="bold blue")
console3.print()
console3.print("Crop = ", "File_2032-31w3-ADE2-2123-AFJFSOFJSDFS", overflow="crop", style="bold blue")
console3.print()
console3.print("Ellipsis = ", "File_2032-31w3-ADE2-2123-AFJFSOFJSDFS", overflow="ellipsis", style="bold blue")

