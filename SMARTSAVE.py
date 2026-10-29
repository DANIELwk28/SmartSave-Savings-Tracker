users = {}
savings_data = {}


def register_user():
    username = input("Create username: ")

    if username in users:
        print("Username already exists!")
        return

    users[username] = input("Create password: ")
    savings_data[username] = []
    print("Account created successfully!")


def login_user():
    username = input("Username: ")
    password = input("Password: ")

    # Admin account
    if username == "admin" and password == "AKOPABA123":
        print("Welcome, Admin!")
        return username

    if username in users and users[username] == password:
        print(f"Welcome to SmartSave, {username}!")
        return username

    print("Invalid login!")
    return None


def create_goal(username):
    name = input("Goal name: ")

    try:
        target = float(input("Target amount: ₱"))
        if target <= 0:
            print("Amount must be positive!")
            return

        savings_data[username].append({
            "name": name, "target": target,
            "savings": 0, "history": []
        })
        print("Goal created successfully!")

    except ValueError:
        print("Invalid amount!")


def select_goal(username):
    goals = savings_data[username]

    if not goals:
        print("No savings goals found!")
        return None

    for i, goal in enumerate(goals, 1):
        print(f"{i}. {goal['name']} - ₱{goal['savings']:.2f}/₱{goal['target']:.2f}")

    try:
        choice = int(input("Select goal: "))
        return goals[choice - 1] if 1 <= choice <= len(goals) else None
    except ValueError:
        print("Invalid choice!")
        return None


def manage_savings(username, action):
    goal = select_goal(username)
    if not goal:
        return

    try:
        amount = float(input("Enter amount: ₱"))
        if amount <= 0 or (action == "Withdraw" and amount > goal["savings"]):
            print("Invalid amount or insufficient savings!")
            return

        goal["savings"] += amount if action == "Add" else -amount
        goal["history"].append(f"{action}: ₱{amount:.2f}")
        print(f"Current savings: ₱{goal['savings']:.2f}")

    except ValueError:
        print("Invalid amount!")


def view_progress(username):
    goal = select_goal(username)
    if goal:
        target = goal["target"]
        savings = goal["savings"]
        progress = min(savings / target * 100, 100)

        print(f"\nGoal: {goal['name']}")
        print(f"Target: ₱{target:.2f}")
        print(f"Savings: ₱{savings:.2f}")
        print(f"Remaining: ₱{max(target - savings, 0):.2f}")
        print(f"Progress: {progress:.2f}%")
        print("[" + "#" * int(progress / 5) + "-" * (20 - int(progress / 5)) + "]")
        print("Goal Completed!" if savings >= target else "Still Saving")


def view_history(username):
    goal = select_goal(username)
    if goal:
        print("\n".join(goal["history"]) if goal["history"] else "No transactions yet.")


def delete_goal(username):
    goal = select_goal(username)
    if goal:
        savings_data[username].remove(goal)
        print("Goal deleted successfully!")


def display_main_menu(username):
    while True:
        print("\n===== SMARTSAVE =====")
        print("1. Create Goal\n2. Add Savings\n3. Withdraw Savings")
        print("4. View Progress\n5. Transaction History")
        print("6. View Goals\n7. Delete Goal\n8. Logout")

        choice = input("Choose: ")

        if choice == "1":
            create_goal(username)
        elif choice == "2":
            manage_savings(username, "Add")
        elif choice == "3":
            manage_savings(username, "Withdraw")
        elif choice == "4":
            view_progress(username)
        elif choice == "5":
            view_history(username)
        elif choice == "6":
            for goal in savings_data[username]:
                print(f"{goal['name']} - ₱{goal['savings']:.2f}/₱{goal['target']:.2f}")
        elif choice == "7":
            delete_goal(username)
        elif choice == "8":
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n===== SMARTSAVE =====")
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                display_main_menu(username)
        elif choice == "3":
            print("Thank you for using SmartSave!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()