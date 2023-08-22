"""
exam: 03. Enrollment
url: https://judge.softuni.org/Contests/Practice/Index/4081#2
"""


def gather_credits(credits: int, *args: tuple):
    courses = set()
    gathered_credits = 0

    for course_name, course_credits in args:
        if gathered_credits >= credits:
            break

        if course_name not in courses:
            courses.add(course_name)
            gathered_credits += course_credits

    if gathered_credits >= credits:
        result = f'Enrollment finished! Maximum credits: {gathered_credits}.\n'
        result += f'Courses: {", ".join(name for name in sorted(courses))}'
        return result

    result = f'You need to enroll in more courses! You have to gather {credits - gathered_credits} credits more.'
    return result


# Test codes
print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27)
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
