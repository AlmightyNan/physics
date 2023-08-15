import threading
import os
import time
from prettytable import PrettyTable

BLUE = "\033[1;34m"
GREEN = "\033[1;32m"
RESET = "\033[0m"
user = f"{GREEN}{os.environ.get('USER') or os.environ.get('USERNAME')}{RESET}"
directory = f"../{os.path.basename(os.getcwd())}"
prompt = f"{user}@{BLUE}almightynan {directory}{RESET} $ "


while True:
    try:

        def run_command(filename):
            os.system(command)

        def initMessage():
            myTable = PrettyTable(["2D graphs", "3D graphs"])
            myTable.add_row(["1. Sin-wave 2d representation", "7. Sin-wave 3d representation"])
            myTable.add_row(["2. Cos-wave 2d representation", "8. Cos-wave 3d representation"])
            myTable.add_row(["3. Tan-wave 2d representation", "9. Tan-wave 3d representation"])
            myTable.add_row(["4. Csc-wave 2d representation", "10. Csc-wave 3d representation"])
            myTable.add_row(["5. Sec-wave 2d representation", "11. Sec-wave 3d representation"])
            myTable.add_row(["6. Cot-wave 2d representation", "12. Cot-wave 3d representation"])
            print(myTable)

        os.system("cls" if os.name == "nt" else "clear")
        initMessage()
        dirPrompt = int(input(prompt))
        if dirPrompt == 1:
                command = "python 2d/sin_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 2:
                command = "python 2d/cos_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 3:
                command = "python 2d/tan_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 4:
                command = "python 2d/cosec_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 5:
                command = "python 2d/sec_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 6:
                command = "python 2d/cot_wave-2d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 7:
                command = "python 3d/sin_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 8:
                command = "python 3d/cos_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 9:
                command = "python 3d/tan_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 10:
                command = "python 3d/sec_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 11:
                command = "python 3d/cosec_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
        if dirPrompt == 12:
                command = "python 3d/cot_wave-3d.py"
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()

    except Exception as e:
        print(e)
        time.sleep(5)
        os.system("clear")