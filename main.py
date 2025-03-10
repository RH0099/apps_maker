import os

def create_project():
    name = input("📂 choose your project name: ")
    os.makedirs(name, exist_ok=True)
    with open(f"{name}/main.py", "w") as f:
        f.write("# New project\nprint('Hello, World!')")
    print(f"✅ {name} project successful!")

def edit_project():
    name = input("✍️ এডিট করতে প্রোজেক্টের নাম দিন: ")
    os.system(f"nano {name}/main.py")

def run_project():
    name = input("🚀 চালাতে প্রোজেক্টের নাম দিন: ")
    os.system(f"python {name}/main.py")

def main():
    while True:
        print("\n🔹 Termux App Maker 🔹")
        print("1️⃣ নতুন প্রোজেক্ট তৈরি")
        print("2️⃣ কোড এডিট করুন")
        print("3️⃣ প্রোজেক্ট রান করুন")
        print("4️⃣ প্রস্থান করুন")
        
        choice = input("👉 আপনার অপশন: ")

        if choice == "1":
            create_project()
        elif choice == "2":
            edit_project()
        elif choice == "3":
            run_project()
        elif choice == "4":
            print("👋 বিদায়!")
            break
        else:
            print("❌ ভুল অপশন!")

if __name__ == "__main__":
    main()
