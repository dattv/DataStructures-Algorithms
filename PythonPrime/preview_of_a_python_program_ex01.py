print("welcome to the GPA calculator")
print("please enter all your letter grades, one per line.")
print("enter a blank line to designate the end.")
points = {"A+": 4.0,
          "A": 4.0,
          "A-": 3.67,
          "B+": 3.33,
          "B": 3.0,
          "B-": 2.67,
          "C+": 2.33,
          "C": 1.67,
          "D+": 1.33,
          "D": 1.0,
          "F": 0.}

num_course = 0
total_points = 0
done = False
while not done:
    grad = input()
    if grad == "":
        done = True
    elif grad not in points:
        print("unknown grad {} being ignore".format(grad))
    else:
        num_course += 1
        total_points += points[grad]

    if num_course > 0:
        print("Your GPA is {0:.3}".format(total_points/num_course))


