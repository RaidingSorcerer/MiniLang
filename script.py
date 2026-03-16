import Mini

file_path = "C:\\Users\\USER\\Desktop\\MiniLang\\examples\\example1.txt"
lines = []
try:
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                lines.append(line)
except FileNotFoundError:
    print("That file not found")
except PermissionError:
    print("You do not have permission")

interpreter = Mini.MiniLang()
for line in lines:
    tokens = line.split()
    if tokens:
        interpreter.execute(tokens)