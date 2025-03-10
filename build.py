import os

def build_apk(project_name):
    print(f"📱 {project_name} থেকে APK বানানো হচ্ছে...")
    os.system(f"termux-create-package {project_name}")

def build_web(project_name):
    print(f"💻 {project_name} থেকে Web App বানানো হচ্ছে...")
    os.system(f"zip -r {project_name}.zip {project_name}")

if __name__ == "__main__":
    name = input("👉 আপনার প্রোজেক্টের নাম দিন: ")
    print("1️⃣ APK বানান")
    print("2️⃣ Web App বানান")
    
    choice = input("👉 অপশন দিন: ")
    
    if choice == "1":
        build_apk(name)
    elif choice == "2":
        build_web(name)
    else:
        print("❌ ভুল অপশন!")
