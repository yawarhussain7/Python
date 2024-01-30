import os as o

folders  = o.listdir("Course")

for i in folders:
    print(i)
    print(o.listdir(f"Course/{i}"))