from array import *

print("--- Step 1. ---")
arr = array("i", [0, 1, 2, 3, 4, 5])
print()

print("--- Step 2. ---")
for i in arr:
    print(i)
print()


print("--- Step 3. ---")
print(arr[2])
print()

print("--- Step 4. ---")
arr.append(999)
print(arr)
print()

print("--- Step 5. ---")
arr.extend([-1, -2, -3])
print(arr)
print()


print("--- Step 6. ---")
arr.fromlist([10, 10, 10])
print(arr)
print()

print("--- Step 7. ---")
arr.remove(0)
print()

print("--- Step 8. ---")
arr.pop()
print()

print("--- Step 9. ---")
print(arr.index(5))
print()

print("--- Step 10. ---")
arr.reverse()
print(arr)
print()

print("--- Step 11. ---")
print(arr.buffer_info())
print()

print("--- Step 12. ---")
print(arr.count(10))
print()

print("--- Step 13. ---")
print(".toString()")
print()

print("--- Step 14. ---")
print(arr.tolist())
print()

print("--- Step 15. ---")
print(".fromString()")
print()

print("--- Step 16. ---")
print(arr[1:4])
print()
