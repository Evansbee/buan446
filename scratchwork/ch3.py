# STUDENT GRADE ANALYZER PROJECT
#
# Document your AI collaboration below:
# - Prompts used:
# - Key insights from AI:
# - Modifications you made:
#
# Your code below:

# Sample data
students = [
    {"name": "Alice", "college": "Business", "gpa": 3.8, "credits": 45},
    {"name": "Bob", "college": "Engineering", "gpa": 3.2, "credits": 52},
    {"name": "Charlie", "college": "Arts", "gpa": 2.9, "credits": 38},
    {"name": "Diana", "college": "Business", "gpa": 3.95, "credits": 60},
    {"name": "Eve", "college": "Engineering", "gpa": 3.5, "credits": 48},
    {"name": "Frank", "college": "Health", "gpa": 3.1, "credits": 55},
    {"name": "Grace", "college": "Arts", "gpa": 3.7, "credits": 42},
    {"name": "Henry", "college": "Health", "gpa": 2.5, "credits": 30},
]

# Start building your functions here...

def get_letter_grade(gpa):
    """Convert GPA to letter grade."""
    #Convert GPA to letter grade (A: 3.7+, B: 3.0-3.69, C: 2.0-2.99, D: 1.0-1.99, F: below 1.0)
    if gpa >= 3.7:
        return 'A'
    elif gpa >= 3.0:
        return 'B'
    elif gpa >= 2.0:
        return 'C'
    elif gpa >= 1.0:
        return 'D'
    else:
        return 'F'


def calculate_class_standing(credits):
    """Convert Class Year Standing."""
    # - Return "First Year" (<30), "Sophomore" (30-59), "Junior" (60-89), "Senior" (90+)
    if credits >= 90:
        return 'Senior'
    elif credits >= 60:
        return 'Junior'
    elif credits >= 30:
        return 'Sophomore'
    else:
        return 'First Year'
    

def is_deans_list(gpa, credits):
    """Returns whether the gpa/credit combo is deans list worthy."""
    # - Return True if GPA >= 3.5 AND credits >= 12
    return gpa >= 3.5 and credits >= 12
    

def filter_by_college(students, college):
    """Returns only return studens in a specific college."""
    # - Return list of students in a specific college
    return [s for s in students if s['college'] == college ]


def calculate_college_stats(students, college):
    """Caclulate college stats."""
    # - Return a dictionary with:

#"college": college name
#"count": number of students
#"avg_gpa": average GPA
#"deans_list_count": number on dean's list
    pass

def generate_report(students):
    # - Print a formatted report showing:

    # Each student's name, college, GPA, letter grade, and standing
    # Summary statistics by college
    # List of dean's list students


# Continue with other functions...