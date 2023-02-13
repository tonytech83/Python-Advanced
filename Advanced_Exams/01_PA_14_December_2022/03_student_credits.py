def students_credits(*args, total_credits=240):
    """
    This func calculates student point and returns if he pass or not based on total_points.
    """
    courses = {}
    final_output = []

    for line in args:
        # separate the info in variables
        course_name, *courses_info = line.split('-')
        course_credits, max_test_points, student_points = [int(x) for x in courses_info]

        # calculates credits for each course
        test_percentage = student_points / max_test_points
        student_credits = course_credits * test_percentage

        # add the course result to total points of student and keep the course and points for course.
        courses[course_name] = student_credits

    final_credits = sum(courses.values())

    if final_credits >= total_credits:
        final_output.append(f'Diyan gets a diploma with {final_credits:.1f} credits.')
    else:
        final_output.append(f'Diyan needs {(total_credits - final_credits):.1f} credits more for a diploma.')

    for course, points in sorted(courses.items(), key=lambda kvp: -kvp[1]):
        final_output.append(f'{course} - {points:.1f}')

    return '\n'.join(final_output)


# Test input 1
print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

# Test input 2
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

# Test input 3
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
