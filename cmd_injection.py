# cmd_injection.py

import os

def dangerous_command(user_input):
    # ⚠️ Vulnerable to command injection
    os.system("ping " + user_input)
