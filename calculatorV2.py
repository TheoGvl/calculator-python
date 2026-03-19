import flet as ft

def main(page: ft.Page):
    page.title = "My Calculator"
    page.window.width = 380
    page.window.height = 550
    page.bgcolor = ft.Colors.BLACK
    
    # Using a list to hold variables so we can edit them inside the button function
    # mem = [flag for new number, saved number, math operator]
    mem = ["", 0, ""] 
    
    # The main text on screen
    screen = ft.Text("0", size=50, color=ft.Colors.WHITE)
    
    def btn_click(e):
        val = e.control.data
        # print("clicked button:", val) # left this here for debugging
        
        # If the user clicks a number
        if val in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if screen.value == "0" or mem[0] == "new":
                screen.value = val # replace the zero
                mem[0] = "" # clear the 'new' flag
            else:
                screen.value += val # attach it to the end
                
        # Clear everything
        elif val == "C":
            screen.value = "0"
            mem[1] = 0
            mem[2] = ""
            
        # If the user clicks math stuff
        elif val in ["+", "-", "*", "/"]:
            mem[1] = float(screen.value) # save the first number
            mem[2] = val                 # save the operator
            mem[0] = "new"               # tell the app we are starting a new number
            
        # Do the math
        elif val == "=":
            num2 = float(screen.value)
            res = 0
            
            if mem[2] == "+": res = mem[1] + num2
            elif mem[2] == "-": res = mem[1] - num2
            elif mem[2] == "*": res = mem[1] * num2
            elif mem[2] == "/": 
                if num2 == 0:
                    res = "Error"
                else:
                    res = mem[1] / num2
            
            screen.value = str(res)
            mem[0] = "new"
            
        page.update()

    # Quick function so I don't have to write the button code 16 times
    def make_btn(text, color=ft.Colors.BLUE_GREY_900):
        return ft.ElevatedButton(
            content=ft.Text(text, size=24, color=ft.Colors.WHITE),
            bgcolor=color,
            data=text,
            on_click=btn_click,
            width=75,
            height=75
        )

    # UI Layout (just shoving the buttons into rows)
    page.add(
        ft.Container(content=screen, padding=20, alignment=ft.Alignment(1, 0)),
        ft.Row([make_btn("7"), make_btn("8"), make_btn("9"), make_btn("/", ft.Colors.ORANGE_800)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([make_btn("4"), make_btn("5"), make_btn("6"), make_btn("*", ft.Colors.ORANGE_800)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([make_btn("1"), make_btn("2"), make_btn("3"), make_btn("-", ft.Colors.ORANGE_800)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([make_btn("C", ft.Colors.RED_800), make_btn("0"), make_btn("="), make_btn("+", ft.Colors.ORANGE_800)], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.run(main)