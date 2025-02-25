# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
# w2052891(20230320)
# 11 th of december 2023
from graphics import *
# Part 1
# Initializing variables
paas_credit = 0
defer_credit = 0
fail_credit = 0
credit_range = [0, 20, 40, 60, 80, 100, 120]
continue_quit = 'y'

# Counts for category
progress_count = 0
trailer_count = 0
exclude_count = 0
retriever_count = 0

# List
progress = []
module_trailer = []
exclude = []
module_retriever =[]


user = input("Type here 'student' or 'staff': ")
if user.lower() == 'student' :
    def progression_outcome():
        try:
            total = pass_credit + defer_credit + fail_credit
            if total == 120:
                if pass_credit == 120:
                    print('progressss')
                elif pass_credit == 100:
                    print('progress(module_trailre)')
                elif fail_credit >= 80:
                    print('exclude')
                else:
                    print('do not progress(module_retriever)')
            else:
                print('Total incorrect')

        except ValueError:
            print('Integer required')
    while continue_quit.lower() == "y":
        try:
            pass_credit = int(input("Enter pass credits: "))
            if pass_credit in credit_range:
                defer_credit = int(input("Enter defer credits: "))
                if defer_credit in credit_range:
                    fail_credit = int(input("Enter fail credits: "))
                    if fail_credit in credit_range:
                        progression_outcome()
                    else:
                        print('Out of range')
                else:
                    print('Out of range')
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

        continue_quit = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results ")

elif user.lower() == 'staff':                
    def progression_outcome():
        try:
            global progress_count, trailer_count, retriever_count, exclude_count

            total = pass_credit + defer_credit +fail_credit
            if total == 120:
                if pass_credit == 120:
                    print('progress')
                    progress_count += 1
                    progress.append([pass_credit, defer_credit, fail_credit])
                elif pass_credit == 100:
                    print('progress(module_trailer)')
                    trailer_count += 1
                    module_trailer.append([pass_credit, defer_credit, fail_credit])
                elif fail_credit >= 80:
                    print('exclude')
                    exclude_count += 1
                    exclude.append([pass_credit, defer_credit, fail_credit])
                else:
                    print('do not progress(module_retriever)')
                    retriever_count += 1
                    module_retriever.append([pass_credit, defer_credit, fail_credit])
            else:
                print('Total incorrect')
                
        except ValueError:
            print('Integer required')

    while continue_quit.lower() == "y":
        try:
            pass_credit = int(input("Enter pass credits"))
            if pass_credit in credit_range:
                defer_credit = int(input("Enter defer credits"))
                if defer_credit in credit_range:
                    fail_credit = int(input("Enter fail credits"))
                    if fail_credit in credit_range:
                        progression_outcome()
                    else:
                        print('Out of range')
                else:
                    print('Out of range')
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')

        continue_quit = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results ")
                          
    # Only Histogram is made using Left Peel vidoes in youtube(graphics.py vid 1,2,3)and histogram corrections are done by using chatgpt
    win = GraphWin("Histogram", 600, 600)
    win.setBackground(color_rgb(255, 255, 255))

    # Count Categories
    categories = ['progress', 'trailer', 'exclude', 'retriever']
    Y = 100
    X = 50

    # Making the line at the histogram to draw bars on it
    ln = Line(Point(150, 500), Point(500, 500))
    ln.setOutline(color_rgb(0, 0, 0))
    ln.setWidth(1)
    ln.draw(win)

    # Making the test result to build the topic
    txt = Text(Point(280, 40), "Histogram Results")
    txt.setSize(30)
    txt.setTextColor(color_rgb(81, 82, 87))
    txt.draw(win)

    # Making bars to draw on the line at the same point(500)
    p_bar = Rectangle(Point(X, 500 - progress_count * 30), Point(X + Y, 500))
    p_bar.setOutline(color_rgb(0, 0, 0))
    p_bar.setFill(color_rgb(122, 240, 154))
    p_bar.draw(win)
    p_txt = Text(Point(X + Y / 2, 520), f"progress: {progress_count}")
    p_txt.setTextColor(color_rgb(0, 0, 0))
    p_txt.setSize(12)
    p_txt.draw(win)

    X += Y + 20

    t_bar = Rectangle(Point(X, 500 - trailer_count * 30), Point(X + Y, 500))
    t_bar.setOutline(color_rgb(0, 0, 0))
    t_bar.setFill(color_rgb(128, 189, 131))
    t_bar.draw(win)
    t_txt = Text(Point(X + Y / 2, 520), f"trailer: {trailer_count}")
    t_txt.setTextColor(color_rgb(0, 0, 0))
    t_txt.setSize(12)
    t_txt.draw(win)

    X += Y + 20

    e_bar = Rectangle(Point(X, 500 - exclude_count * 30), Point(X + Y, 500))
    e_bar.setOutline(color_rgb(0, 0, 0))
    e_bar.setFill(color_rgb(147, 179, 96))
    e_bar.draw(win)
    e_txt = Text(Point(X + Y / 2, 520), f"exclude: {exclude_count}")
    e_txt.setTextColor(color_rgb(0, 0, 0))
    e_txt.setSize(12)
    e_txt.draw(win)

    X += Y + 20

    r_bar = Rectangle(Point(X, 500 - retriever_count * 30), Point(X + Y, 500))
    r_bar.setOutline(color_rgb(0, 0, 0))
    r_bar.setFill(color_rgb(235, 171, 220))
    r_bar.draw(win)
    r_txt = Text(Point(X + Y / 2, 520), f"retriever {retriever_count}")
    r_txt.setTextColor(color_rgb(0, 0, 0))
    r_txt.setSize(12)
    r_txt.draw(win)

    X += Y + 20

    # Display the total number of outcomes on the histogram
    total_outcomes = progress_count + trailer_count + exclude_count + retriever_count
    txt_total = Text(Point(X - 400, 550), f"{total_outcomes} outcomes in total")
    txt_total.setTextColor(color_rgb(0, 0, 0))
    txt_total.setSize(15)
    txt_total.draw(win)

    win.getMouse()
    win.close()

    # Part 2
    # List (extension)
    print("\nPart 2:")
    for Y in progress:
        print(f"progress - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in module_trailer:
        print(f"module_trailer - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in exclude:
        print(f"exclude - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in module_retriever:
        print(f"module_retriever - {Y[0]}, {Y[1]}, {Y[2]}")


    # Part 3
    #Text File(extension)
    def file_extension(file, extension, category):# I take these three variable fuctions as my parameters.
    # Process
        for Y in extension:
            file.write(f"{category} - {Y[0]}, {Y[1]}, {Y[2]}\n")
    # Output
    print("\nPart 3:")
    for Y in progress:
        print(f"progress - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in module_trailer:
        print(f"module_trailer - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in exclude:
        print(f"exclude - {Y[0]}, {Y[1]}, {Y[2]}")
    for Y in module_retriever:
        print(f"module_retriever - {Y[0]}, {Y[1]}, {Y[2]}")

    # Output in Text File   
    with open("output.txt", "w") as file:
         file_extension(file, progress, "progress")
         file_extension(file, module_trailer, "progress(module_trailer)")
         file_extension(file, module_retriever, "module_retriever")
         file_extension(file, exclude, "exclude")

           



