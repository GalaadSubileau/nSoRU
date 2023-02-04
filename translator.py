#!/usr/bin/env python3

"""
nSoRU language to Brainfuck translator. The main function 
reads from a file and writes to a new file the translated code.

Their are 3 possible arguments:
    -h, --help: shows the help message
    -f, --file: the file to translate
    -o, --output: the file to write the translated code

If the syntax is not correct, the program will show the help message.

The language is a simple one, with only 8 commands: 

"roses"     -> ">"
"are"       -> "<"
"red"       -> "+"
"violets"   -> "-"
"blue"      -> "."
"sugar"     -> ","
"is"        -> "["
"sweet"     -> "]"

Each command must be separated by a space, and you can use comments with #.
"""

import sys

### GLOBAL VARIABLES ###
NO_ARGS = "No arguments given. Use -h or --help for help."
INCORRECT_ARGS = "Incorrect arguments. Use -h or --help for help."

### FUNCTIONS ###

def argument_parser():
    """
    Parses the arguments.
    """
    if len(sys.argv) == 1:
        print(NO_ARGS)
        return
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            print(__doc__)
            return
        else:
            print(INCORRECT_ARGS)
            return
    elif len(sys.argv) == 5:
        if ("-f" in sys.argv or "--file" in sys.argv) and ("-o" in sys.argv or "--output" in sys.argv):
            try:
                if "-f" in sys.argv:
                    file = sys.argv[sys.argv.index("-f") + 1]
                else:
                    file = sys.argv[sys.argv.index("--file") + 1]
                if "-o" in sys.argv:
                    output = sys.argv[sys.argv.index("-o") + 1]
                else:
                    output = sys.argv[sys.argv.index("--output") + 1]
            except IndexError:
                print(INCORRECT_ARGS)
                return
        else:
            print(INCORRECT_ARGS)
            return
    else:
        print(INCORRECT_ARGS)
        return

    return file, output

def file_reader(file):
    """
    Reads the file and returns the code.
    If the syntax is not correct, it raises a ValueError.
    """
    with open(file, "r") as f:
        code = []
        for i, line in enumerate(f):
            # Split the line by spaces, remove the comments
            # and the newlines/tabulations.
            splitted = line.split(" ")
            splitted = [command.replace("\t", "").replace("\n", "") for command in splitted]
            for j, command in enumerate(splitted):
                try:
                    if command in ("roses", "are", "red", "violets", "blue", "sugar", "is", "sweet"):
                        code.append(command)
                    elif command in ("","\n","\t"):
                        continue
                    elif "#" in command:
                        command = command[:command.index("#")]
                        if command in ("roses", "are", "red", "violets", "blue", "sugar", "is", "sweet"):
                            code.append(command)
                        elif command in ("","\n","\t"):
                            break
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                except ValueError:
                    error_message = f"Error in line {i+1}, column {j+1}: {command} is not a valid command.\n"
                    error_message += "{0}\n".format(line.replace('\n', ''))
                    error_message += " ".join([" " * len(splitted[k]) for k in range(j)]) + " ^"
                    print(splitted)
                    raise ValueError(error_message)
    return code

def translator(code):
    """
    Translates the code.
    """
    translated = ""
    for command in code:
        if command == "roses":
            translated += ">"
        elif command == "are":
            translated += "<"
        elif command == "red":
            translated += "+"
        elif command == "violets":
            translated += "-"
        elif command == "blue":
            translated += "."
        elif command == "sugar":
            translated += ","
        elif command == "is":
            translated += "["
        elif command == "sweet":
            translated += "]"
        else:
            # The filtering should have removed all the other characters
            raise ValueError("Command not recognized.")
    return translated

def write_output(output, translated):
    """
    Writes the translated code to the output file.
    """
    with open(output, "w") as f:
        f.write(translated)

def main():
    """
    Main function.
    """

    file, output = argument_parser()
    code = file_reader(file)
    translated = translator(code)
    write_output(output, translated)

if __name__ == "__main__":
    main()

