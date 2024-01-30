import os


if(not os.path.exists("Course")):
    os.mkdir("Course")

for folder in range(0,101):
    os.mkdir(f"Course/Day {folder}")
    