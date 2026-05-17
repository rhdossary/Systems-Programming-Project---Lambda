import os
import subprocess

print("\n" + "="*50)
print("   Welcome to Lambda Mini Shell!")
print("   Type 'exit' or 'quit' to leave")
print("="*50 + "\n")

while True:

    current_dir = os.getcwd()

    user_input = input(f"lambda:{current_dir}$ ")
    
    user_input = user_input.strip()
    
    if user_input == "":
        continue

    parts = user_input.split()
    command = parts[0]
    args = parts[1:]

    if command == "exit" or command == "quit":
        print("Goodbye!")
        break    

    elif command == "cd":
        if len(args) == 0:

            os.chdir(os.path.expanduser("~"))
        else:
            try:
                os.chdir(args[0])
            except FileNotFoundError:
                print(f"Error: Directory '{args[0]}' not found")

    elif command == "pwd":
        print(os.getcwd())
    

    elif command == "echo":
        print(" ".join(args))
    

    elif command == "help":
        print("\n--- Available Commands ---")
        print("cd [dir]  - Change directory")
        print("pwd       - Show current directory")
        print("echo text - Print text")
        print("help      - Show this help")
        print("exit/quit - Exit the shell")
        print("--------------------------\n")

    else:
        try:
            subprocess.call(user_input, shell=True)
        except:
            print(f"Error: '{command}' is not recognized")
