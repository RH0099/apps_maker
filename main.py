import os
import time
import pyfiglet

def banner():
    os.system("clear")
    print("\033[1;32m" + pyfiglet.figlet_format("APP BUILDER"))
    print("\033[1;34m" + "="*40)
    print("\033[1;33m  ⚡ Android App Builder for Termux ⚡")
    print("\033[1;34m" + "="*40 + "\n")

def create_app():
    banner()
    code = input("\033[1;36m[+] Enter Your Apps Code: \033[1;32m")
    
    if not code.strip():
        print("\033[1;31m[!] ⚠️ Enter Your Code")
        time.sleep(2)
        create_app()
    
    banner()
    app_name = input("\033[1;36m[+] Enter Your Apps Name: \033[1;32m")

    if not app_name.strip():
        print("\033[1;31m[!] ⚠️ Please Enter Your Apps Name!")
        time.sleep(2)
        create_app()

    banner()
    save_path = input("\033[1;36m[+] Enter Your Drectory (Example: /sdcard/MyApp): \033[1;32m")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    apk_file = f"{save_path}/{app_name}.apk"

    # অ্যাপ ফাইল তৈরি
    with open(apk_file, "w") as f:
        f.write(code)

    print(f"\033[1;32m[✓] ✅ apps successfully created!\n")
    print(f"\033[1;33m[💾]  your apps saving Directory: {apk_file}\n")
    print("\033[1;34m[✔] Use your apps enjoy your life ")

create_app()
        
