import itertools
import time

words = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "!", "?"]


passw = ("b", 5, 7,"a","c",3,4,"!")

s = time.time()
pass_cracker = itertools.permutations(words,8)

for i in pass_cracker:
    if i == passw:
        print("Gotcha!")
        time.sleep(1)
        print(i)
        break
e = time.time()
time.sleep(1)
print(f"Found your password in {round(e-s)} seconds!")
