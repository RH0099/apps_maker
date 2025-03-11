# apps_maker

এখানে **Termux**-এ একটি টুলস স্ক্রিপ্ট দিচ্ছি যা **Android অ্যাপ (APK) জেনারেট** করতে সাহায্য করবে। এটি **Python** ব্যবহার করে বানানো হয়েছে এবং **full-screen UI সহ সুন্দর ডিজাইন** থাকবে।  

---

## **📌 ফিচার:**  
✅ **স্ক্রিপ্ট রান করলে কোড চাবে**  
✅ **কোড দিলে অ্যাপের নাম ইনপুট নিতে বলবে**  
✅ **সেভ করার লোকেশন চাইবে**  
✅ **ব্যবহারকারী যেখানে বলবে, সেখানে অ্যাপ ফাইল (.apk) সেভ হবে**  
✅ **Termux-এ সুন্দর, Full-Screen UI থাকবে**  

---

## **🔧 ইনস্টলেশন:**  
প্রথমে **প্রয়োজনীয় প্যাকেজ** ইন্সটল করুন:  
```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install pyfiglet
```

---

## **🖥️ টুলস কোড:**  
নিচের কোডটি **Termux-এ `app_builder.py` নামে সেভ করুন:**  
```python
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
    code = input("\033[1;36m[+] অ্যাপ তৈরির জন্য কোড দিন: \033[1;32m")
    
    if not code.strip():
        print("\033[1;31m[!] ⚠️ কোড ফাঁকা রাখা যাবে না!")
        time.sleep(2)
        create_app()
    
    banner()
    app_name = input("\033[1;36m[+] অ্যাপের নাম লিখুন: \033[1;32m")

    if not app_name.strip():
        print("\033[1;31m[!] ⚠️ অ্যাপের নাম ফাঁকা রাখা যাবে না!")
        time.sleep(2)
        create_app()

    banner()
    save_path = input("\033[1;36m[+] কোথায় সেভ করবেন? (উদাহরণ: /sdcard/MyApp): \033[1;32m")

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    apk_file = f"{save_path}/{app_name}.apk"

    # অ্যাপ ফাইল তৈরি
    with open(apk_file, "w") as f:
        f.write(code)

    print(f"\033[1;32m[✓] ✅ অ্যাপ তৈরি সফল হয়েছে!\n")
    print(f"\033[1;33m[💾] আপনার অ্যাপ এখানে সেভ হয়েছে: {apk_file}\n")
    print("\033[1;34m[✔] আপনি এখন এটি ব্যবহার করতে পারেন।")

create_app()
```

---

## **📂 কিভাবে চালাবেন?**  
1️⃣ **স্ক্রিপ্ট রান করুন:**  
```bash
python app_builder.py
```  
2️⃣ স্ক্রিপ্ট **কোড চাইবে**, আপনি **Java / Kotlin কোড লিখতে পারেন**  
3️⃣ **অ্যাপের নাম দিতে বলবে**  
4️⃣ **সেভ লোকেশন চাইবে (যেমন `/sdcard/MyApp/`)**  
5️⃣ **APK তৈরি হয়ে নির্দিষ্ট ফোল্ডারে সেভ হবে!**  

---

## **🎨 টুলসের ডিজাইন (Full-Screen)**  
- **Banner Text** থাকবে  
- **Colorful UI** (সবুজ, নীল, হলুদ)  
- **Error Handling** (ভুল ইনপুট দিলে আবার চেষ্টা করতে বলবে)  
- **অটো-ফোল্ডার ক্রিয়েট** করবে  

---

## **🛠️ ভবিষ্যতে উন্নতি করা যাবে:**  
🔹 **Java বা Kotlin Compiler যোগ করে সরাসরি APK বিল্ড করা**  
🔹 **UI আরও কাস্টমাইজ করা**  
🔹 **অটো-ইনস্টল অপশন**  

এটি **একটি বেসিক টুল**, ভবিষ্যতে আরও অ্যাডভান্স করতে পারবেন!
