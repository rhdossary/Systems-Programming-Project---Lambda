import os
import subprocess
import shlex
import sys

def main():
    print("Welcome to the Python Mini Shell!")
    print("Developed by Group [Lambda] | Type 'exit' to quit.")

    while True:
        try:
            # 1. READ: Create a dynamic prompt
            cwd = os.getcwd()
            user_input = input(f"py-shell:{cwd}$ ").strip()

            if not user_input:
                continue

            # 2. PARSE: Split command from arguments
            tokens = shlex.split(user_input)
            command = tokens[0]
            args = tokens[1:]

            # 3. EVALUATE (Built-ins)
            if command in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            elif command == "cd":
                try:
                    path = args[0] if args else os.path.expanduser("~")
                    os.chdir(path)
                except FileNotFoundError:
                    print(f"cd: No such directory: {args[0]}")
                continue

            # 4. EVALUATE (External Commands)
            else:
                try:
                    # Executes binaries like ls, pwd, echo, etc.
                    subprocess.run(tokens, check=True)
                except FileNotFoundError:
                    print(f"py-shell: command not found: {command}")
                except subprocess.CalledProcessError:
                    pass # Errors from the command itself are handled by the system

        except EOFError: # Handles Ctrl+D
            print("\nExiting...")
            break
        except KeyboardInterrupt: # Handles Ctrl+C
            print("\nType 'exit' to leave the shell.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
