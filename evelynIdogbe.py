# Student name: Evelyn Idogbe
# Student ID: A00050322


def accept_input():
    student_id = input("Student's ID or Name: ")
    # This section requires students to input their student ID or Name
    
    while True:
        try:
            coursework1 = int(input("Coursework 1 score: "))
            coursework2 = int(input("Coursework 2 score: "))
            coursework3 = int(input("Coursework 3 score: "))
            test_score = int(input("Test score: "))
            break
        # The students are to enter their respective test scores here

        except ValueError:
            print("Invalid input! Please enter a valid integer for the scores.")
            # If a non-numeric value is entered, display an error and prompt again
    
    return student_id, coursework1, coursework2, coursework3, test_score


def calculate_total_score(coursework1, coursework2, coursework3, test_score):
    overall_score = (coursework1 + coursework2 + coursework3 + test_score) // 4
    return overall_score
    # This section determines the overall score of the student by adding the course works and test scores


def student_category(total_score):
    if total_score >= 70:
        return "First"
    elif total_score >= 60:
        return "Second"
    elif total_score >= 50:
        return "Third"
    elif total_score >= 40:
        return "Fourth"
    else:
        return "Fifth"
    # This section categorizes the students based on their obtained averages


def main():
    students = []
    
    while True:
        student_data = accept_input()
        student_id, coursework1, coursework2, coursework3, test_score = student_data
        
        total_score = calculate_total_score(coursework1, coursework2, coursework3, test_score)
        category = student_category(total_score)
        
        students.append((student_id, total_score, category))
        
        continue_input = input("Do you want to enter another student? (yes/no): ").lower()
        if continue_input != 'yes':
            break 
        # This section allows multiple students' data to be entered and processed

    
    print("\nStudent Results:")
    for student in students:
        student_id, score, category = student
        print(f"Student's ID/Name: {student_id}, Score: {score} - {category}")
        # This section displays the results for all entered students 


if __name__ == "__main__":
    main()
    # This section calls the main function to start the program
