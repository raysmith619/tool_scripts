#loop_lvalue.py
ls = [1,2,3,4]
print(f"ls:{ls}")
for l in ls:
    l = 10
print(f"ls:{ls}")
print("Changing loop variable doesn't change the list")

