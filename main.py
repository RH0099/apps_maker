import os

def create_project():
    name = input("📂 choose your project name: ")
    os.makedirs(name, exist_ok=True)
    with open(f"{name}/main.py", "w") as f:
        f.write("# New project\nprint('Hello, World!')")
    print(f"✅ {name} project successful!")

def edit_project():
    name = input("✍️ Enter the project name to edit: ")
    os.system(f"nano {name}/main.py")

def run_project():
    name = input("🚀 Name the project to: ")
    os.system(f"python {name}/main.py")

def main():
    while True:
        print("\n🔹 Termux App Maker 🔹")
        print("1️⃣ Create new project")
        print("2️⃣ Code Edit")
        print("3️⃣ Project start")
        print("4️⃣ Exit")
        
        choice = input("👉 your option 🔢: ")

        if choice == "1":
            create_project()
        elif choice == "2":
            edit_project()
        elif choice == "3":
            run_project()
        elif choice == "4":
            print("👋 out!")
            break
        else:
            print("❌ Wrong option!")

if __name__ == "__main__":
    main()
