# ACTIVITY 4: DYNAMIC ASCII ART

# Old Design
print("OLD DESIGN: ")
print("")
print("##::::'##::::'###::::'########:::'######::")
print("###::'###:::'## ##::: ##.... ##:'##... ##:")
print("####'####::'##:. ##:: ##:::: ##: ##:::..::")
print("## ### ##:'##:::. ##: ########:: ##:::::::")
print("##. #: ##: #########: ##.. ##::: ##:::::::")
print("##:.:: ##: ##.... ##: ##::. ##:: ##::: ##:")
print("##:::: ##: ##:::: ##: ##:::. ##:. ######::")

# Asks the user to input a new character/symbol to replace '#'
print("")
x = input("Enter a new character/symbol to replace '#' : ")

# Function to replace '#' with the new character/symbol in the ASCII art design
print("")
print("NEW DESIGN: ")                            
print("")
print(f"{x}{x}::::'{x}{x}::::'{x}{x}{x}::::'{x}{x}{x}{x}{x}{x}{x}{x}:::'{x}{x}{x}{x}{x}{x}::")
print(f"{x}{x}{x}::'{x}{x}{x}:::'{x}{x} {x}{x}::: {x}{x}.... {x}{x}:'{x}{x}... {x}{x}:")
print(f"{x}{x}{x}{x}'{x}{x}{x}{x}::'{x}{x}:. {x}{x}:: {x}{x}:::: {x}{x}: {x}{x}:::..::")
print(f"{x}{x} {x}{x}{x} {x}{x}:'{x}{x}:::. {x}{x}: {x}{x}{x}{x}{x}{x}{x}{x}:: {x}{x}:::::::")
print(f"{x}{x}. {x}: {x}{x}: {x}{x}{x}{x}{x}{x}{x}{x}{x}: {x}{x}.. {x}{x}::: {x}{x}:::::::")
print(f"{x}{x}:.:: {x}{x}: {x}{x}.... {x}{x}: {x}{x}::. {x}{x}:: {x}{x}::: {x}{x}:")
print(f"{x}{x}:::: {x}{x}: {x}{x}:::: {x}{x}: {x}{x}:::. {x}{x}:. {x}{x}{x}{x}{x}{x}::")

# Para maging dynamic ASCII Art, papalitan yung main character (in this case, '#'), to the variable name using f-string kung saan naka-assign yung user input (in this case, x)
# In essence print("#") -> f"{x}"      x being the variable name nung user input
