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