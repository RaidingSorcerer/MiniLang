# MiniLang Phase 1 Starter Template
import os
import json
class MiniLang:
    path="C:\\Users\\USER\\Desktop\\variables.json"

    def __init__(self):
        # Store all variables here
        if os.path.exists(MiniLang.path):
            try:
                with open(MiniLang.path, "r") as file:
                    self.variables = json.load(file)
            except json.JSONDecodeError:
                self.variables = {}
        else:
            self.variables = {}
    
    def run(self):
        print("Welcome to MiniLang! Type EXIT to quit.")
        while True:
            command = input(">> ").strip()
            if not command:
                continue

            # Split input into tokens
            tokens = command.split()
            self.execute(tokens)

    def execute(self, tokens):
        """
        Dispatch commands to the appropriate method.
        Implement logic for:
        - SET
        - ADD
        - PRINT
        - SHOW
        - EXIT
        """
        cmd = tokens[0].upper()

        if cmd == "SET" and( ("INT" in tokens) or ("STR" in tokens)):
            self.set_var(tokens)
        elif cmd == "ADD":
            self.add_var(tokens)
        elif cmd == "PRINT":
            self.print_var(tokens)
        elif cmd == "SHOW":
            self.show_vars()
        elif cmd == "EXIT":
            print("Exiting MiniLang...")
            exit()
        else:
            print(f"Unknown command: {tokens[0]}")

    # ================================
    # Methods to implement yourself
    # ================================
    
    def set_var(self, tokens):
        if len(tokens)>4:
            print("SyntaxError: SET command requires 4 tokens: SET TYPE VAR VALUE")
        if("INT" in tokens and len(tokens)==4):
            try:
                self.variables[tokens[2]]=[int(tokens[3]),"INT"]
                with open(MiniLang.path, "w") as file:
                    json.dump(self.variables, file, indent=4)
            except ValueError:
                print("INT must be integers")
        if("STR" in tokens and len(tokens)==4):
            self.variables[tokens[2]]=[tokens[3],"STR"]
            with open(MiniLang.path, "w") as file:
                json.dump(self.variables, file, indent=4)
        """
        Syntax: SET variable value
        Assigns a value to a variable.
        """
        
    def add_var(self, tokens):
        if len(tokens) != 3:
            print("Invalid ADD command. Syntax: ADD variable value")
            return

        var_name = tokens[1]
        value = tokens[2]

        if var_name not in self.variables:
            print("Variable not created")
            return

        var_value, var_type = self.variables[var_name]

        if var_type == "INT":
            # Try converting input to int
            try:
                if value.lstrip("-").isdigit():  # allow negative numbers
                    self.variables[var_name][0] += int(value)
                    with open(MiniLang.path, "w") as file:
                        json.dump(self.variables, file, indent=4)

            except Exception as e:
                print(f"Cannot add non-integer to integer {e}")
        elif var_type == "STR":
            # Always treat input as string
            self.variables[var_name][0] += value
            with open(MiniLang.path, "w") as file:
                json.dump(self.variables, file, indent=4)
        else:
            print(f"Unsupported variable type: {var_type}")
    
       
        """
        Syntax: ADD variable value
        Adds a number to a variable.
        """
        pass

    def print_var(self, tokens):
        if len(tokens)>2:
           print("SyntaxError: PRINT command takes exactly one argument")
        if len(tokens)==2:

            if tokens[1] in self.variables.keys():
                print(f"{self.variables[tokens[1]][0]} ({self.variables[tokens[1]][1]})")
            else:
                print("Variable not created yet")
        else:
            print("Too Much to Unpack")
        """
        Syntax: PRINT variable
        Prints the value of a variable.
        """
        pass

    def show_vars(self):
        for k,v in self.variables.items():
            print(f"{k}={v[0]} ({v[1]})")
        """
        Syntax: SHOW
        Prints all current variables and values.
        """
        pass


if __name__ == "__main__":
    interpreter = MiniLang()
    interpreter.run()