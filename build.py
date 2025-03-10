import os

def build_apk(project_name):
    print(f"📱 {project_name} Making APK from....")
    os.system(f"termux-create-package {project_name}")

def build_web(project_name):
    print(f"💻 {project_name} Making APK from......")
    os.system(f"zip -r {project_name}.zip {project_name}")

if name == "main":
    name = input("👉 Enter your project name: ")
    print("1️⃣ Make APK ")
    print("2️⃣ Make Web App ")
    
    choice = input("👉 Enter options: ")
    
    if choice == "1":
        build_apk(name)
    elif choice == "2":
        build_web(name)
    else:
        print("❌ Wrong option!")
