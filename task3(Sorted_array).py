def is_sorted():
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True

print ("Hello!Enter an array of numbers and I'll tell if it's sorted in ascending order or not.'")
arr = input("Please enter an array of numbers (separate them with commas):")
arr = [int(x) for x in arr.split(",")]

if is_sorted():
    print("The array is sorted.")
else:
    print("The array is not sorted.")

