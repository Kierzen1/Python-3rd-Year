def find_average(marks)->None:
    sum_marks = sum(marks)
    length_marks = len(marks)
    average_marks = sum_marks / length_marks
    return average_marks
    
def compute_grade(average_marks)->None:
    if average_marks <= 80:
        print("A")
    elif 60 >= average_marks > 80:
        print("B")
    
def main()->None:
    marks = [54, 64, 46]
    average_marks = find_average(marks)
    print("Average is", average_marks)
    compute_grade(average_marks)
   
if _name__== "__main_":
    main()