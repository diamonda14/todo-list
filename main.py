tasks = []

def show_menu():
    print("\n📋 قائمة المهام:")
    print("1. إضافة مهمة")
    print("2. عرض المهام")
    print("3. حذف مهمة")
    print("4. خروج")

def add_task():
    task = input("🔹 اكتب المهمة: ")
    tasks.append(task)
    print("✅ تمت إضافة المهمة.")

def view_tasks():
    if not tasks:
        print("🚫 لا توجد مهام بعد.")
    else:
        print("\n📌 المهام:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    try:
        index = int(input("❌ اكتب رقم المهمة لحذفها: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ تم حذف المهمة: {removed}")
        else:
            print("⚠️ رقم غير صحيح.")
    except ValueError:
        print("⚠️ المرجو إدخال رقم صحيح.")

while True:
    show_menu()
    choice = input("اختر خيار (1-4): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("👋 إلى اللقاء!")
        break
    else:
        print("⚠️ خيار غير صالح.")
