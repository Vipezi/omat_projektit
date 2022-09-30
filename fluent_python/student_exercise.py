#! /usr/bin/python3

def assignment_score(score):
    totalsum = sum(score)
    assignments = len(score)
    result = (totalsum / assignments) * 0.35
    return result

def test_score(score):
    totalsum = sum(score)
    assignments= len(score)
    result = (totalsum/assignments) * 0.65
    return result

def get_grade(total_score):
    if total_score <= 60:
        F = "FAIL"
        return F
    elif total_score >= 60 and total_score < 70:
        D = "D"
        return D
    elif total_score >= 70 and total_score < 80:
        C = "C"
        return C
    elif total_score >= 80 and total_score < 90:
        B = "B"
        return B
    elif total_score <= 90:
        A = "A"
        return A

def class_average(scores):
    amount_of_grades = len(scores)
    sum_of_grades = sum(scores)
    average = sum_of_grades / amount_of_grades
    return average

def print_grades(student, letter):
    answer = f"{student} got the grade {letter}"
    print(answer)


    
def main():

    Jarkko = { "name":"Jarkko Mydks",
         "assignment" : [70, 80, 90, 100],
         "test" : [70, 98]
       }

    Myndy = { "name" : "Mindy Koskinen",
            "assignment" : [85, 86, 43, 100],
            "test" : [89, 71]
            }  

    Harry = { "name":"Harry Potter",
            "assignment" : [88, 56, 88 ,80],
            "test" : [80, 80],
            }
    

    Ida = { "name" : "Ida Makkilen",
            "assignment" : [67, 12, 45, 100],
            "test" : [69, 77]
            }
            

    Kari = { "name" : "Kari Potter",
            "assignment" : [77, 10, 45, 12],
            "test" : [40, 50]
        }
    student_list = [Jarkko, Myndy, Harry, Ida, Kari]
    scores = []

    for s in student_list:
        assignment = assignment_score(s["assignment"])
        test = test_score(s["test"])
        points = assignment + test
        s["points"] = points
        grade = get_grade(points)
        s["final_grades"] = grade
        result = print_grades(s['name'],grade)
        print(result)
        scores.append(s['points'])
        average = class_average(scores)


    print(student_list)   
    print(f"{average} Is the average for the whole.")
        
if __name__ == "__main__":
    main()