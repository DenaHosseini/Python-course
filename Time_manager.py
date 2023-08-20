print("Welcome to time manager!")

def get_time(text):
    while True:
        time_str = input(text + " (HH:MM:SS): ")
        parts = time_str.split(":")
        if len(parts) != 3:
            print("Invalid format. Please enter the time in format HH:MM:SS (e.g. 08:30:00).")
            continue
        if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
            print("Invalid characters. Please enter the time in format HH:MM:SS (e.g. 08:30:00).")
            continue
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        if h < 0 or h > 23 or m < 0 or m > 59 or s < 0 or s > 59:
            print("Invalid time. Please enter a valid time.")
            continue
        return {"h": h, "m": m, "s": s}

    
def sum(t1, t2):
    result = {}
    result ["h"] = t1["h"] + t2["h"]
    result ["m"] = t1["m"] + t2["m"]
    result ["s"] = t1["s"] + t2["s"]
    if result['s']>= 60 :
        result['s'] -= 60
        result["m"] += 1

    if result['m'] >= 60:
        result['m'] -= 60
        result["h"] += 1

    return result

def is_later(time1, time2):
    if time1["h"] > time2["h"]:
        return True
    elif time1["h"] == time2["h"]:
        if time1["m"] > time2["m"]:
            return True
        elif time1["m"] == time2["m"]:
            if time1["s"] > time2["s"]:
                return True
    return False

def subtract(time1, time2):
    if is_later(time1, time2):
        result = {}
        result["h"] = time1["h"] - time2["h"]
        result["m"] = time1["m"] - time2["m"]
        result["s"] = time1["s"] - time2["s"]
    else:
        result = {}
        result["h"] = time2["h"] - time1["h"]
        result["m"] = time2["m"] - time1["m"]
        result["s"] = time2["s"] - time1["s"]
    if result['s'] < 0:
        result['s'] += 60
        result['m'] -= 1
    if result['m'] < 0:
        result['m'] += 60
        result['h'] -= 1
    return result

def show(result):
    print(f"{result['h']}:{result['m']:02}:{result['s']:02}")

def get_input():
    while True:
        choice = input("Do you want to 1.add or 2.subtract the times? (1/2): ")
        if choice == "1" or choice == "2":
            return int(choice)
        else:
            print("Invalid choice. Please enter either '1' or '2'.")

def main():
    while True:
        c_e = input("Enter e to exit the program or any other key to continue: ")
        if c_e == "e":
            print("Bye! Have a good time.")
            break
        else:
            entry_time, exit_time = get_times()
            choice = get_input()
            if choice == 1:
                result_a = sum(entry_time, exit_time)
                print("Sum of two times:")
                show(result_a)
            elif choice == 2:
                result_s = subtract(entry_time, exit_time)
                print("subtraction of two times:")
                show(result_s)
            else:
                print("Invalid choice! Please enter 1 or 2")

def get_times():
    entry_time = get_time("Enter the entry time")
    exit_time = get_time("Enter the exit time")
    return entry_time, exit_time

if __name__ == "__main__":
    main()