import subprocess
import os

# Start a detached session named 'calculator' if it doesn't exist
subprocess.run(["tmux", "new-session", "-d", "-s", "calc-builder"], stderr=subprocess.DEVNULL)
    
# Send the echo command to the 'hi' session
subprocess.run(["tmux", "send-keys", "-t", "calc-builder", "cd ~/x/My-Calculator && clear && echo build calculator", "C-m"])

os.system("tmux attach -t calc-builder")
