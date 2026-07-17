import csv
from collections import Counter
import sys
from datetime import datetime
import pprint


class DuplicateEntryError(Exception):
    """For niceness, i want to have a clear duplicate entry error to throw"""

    pass


class BusinessLogicError(Exception):
    """credit errors, or something else that violates a higher level construct, could be ValueError"""

    pass


def load_student_data(filename, validate=True, skip_invalid=True):
    """
    Load student data from a CSV file.

    Parameters:
        filename: Path to the CSV file
        validate: Whether to validate each record
        skip_invalid: If True, skip invalid records; if False, raise exception

    Returns:
        Tuple of (valid_records, stats)
    """
    valid_records = []

    results = {
        "total_rows": 0,
        "valid_rows": 0,
        "invalid_rows": 0,
        "errors_by_type": {},
        "errors_by_field": {
            "id": 0,
            "college": 0,
            "major": 0,
            "class_year": 0,
            "gpa": 0,
            "credits_attempted": 0,
            "credits_earned": 0,
            "enrollment_date": 0,
            "record": 0,
        },
        "error_log": [],
    }

    def make_error_log_entry(row, field, e, input_value):
        return {
            "row": row,
            "field": field,
            "error_type": type(e).__name__,
            "message": str(e),
            "input_value": f"{input_value!r}",
        }

    def clean_text(value):
        # A missing/short column comes back as None; guard against .strip() on None
        return value.strip() if value else ""

    def normalize_id(id, record):
        return clean_text(id).upper()

    def normalize_college(college, record):
        valid_colleges = [
            "College of Business",
            "College of Engineering",
            "College of Arts and Sciences",
            "College of Health",
            "College of Education",
        ]

        college = clean_text(college)

        college_map = {
            "arts and sciences": "College of Arts and Sciences",
            "cob": "College of Business",
            "business": "College of Business",
            "engineering": "College of Engineering",
            "a&s": "College of Arts and Sciences",
            "health": "College of Health",
            "ed": "College of Education",
            "cas": "College of Arts and Sciences",
            "coh": "College of Health",
            "health college": "College of Health",
            "education": "College of Education",
            "buisness": "College of Business",
            "school of engineering": "College of Engineering",
            "arts & sciences": "College of Arts and Sciences",
        }

        if college.casefold() in college_map:
            college = college_map[college.casefold()]

        for vc in valid_colleges:
            if vc.casefold() == college.casefold():
                return vc

        if college == "COE":
            if record["major"] in [
                "Elementary Education",
                "Secondary Education",
                "Special Education",
            ]:
                return "College of Education"
            else:
                return "College of Engineering"

        raise ValueError(f"Invalid College Name {college!r}")

    def normalize_major(major, record):
        major = clean_text(major)
        valid_majors = [
            "Accounting",
            "Finance",
            "Marketing",
            "Supply Chain Management",
            "Business Analytics",
            "Management",
            "Economics",
            "Computer Science",
            "Mechanical Engineering",
            "Civil Engineering",
            "Electrical Engineering",
            "Chemical Engineering",
            "Industrial Engineering",
            "Computer Engineering",
            "Bioengineering",
            "Biology",
            "Chemistry",
            "Psychology",
            "English",
            "Mathematics",
            "Physics",
            "Political Science",
            "Sociology",
            "History",
            "Philosophy",
            "Health Science",
            "Public Health",
            "Nursing",
            "Community Health",
            "Elementary Education",
            "Secondary Education",
            "Special Education",
        ]

        major_map = {
            "computer sceince": "Computer Science",
            "business analystics": "Business Analytics",
            "marketting": "Marketing",
        }
        if major.casefold() in major_map:
            major = major_map[major.casefold()]

        for vm in valid_majors:
            if vm.casefold() == major.casefold():
                return vm
        raise ValueError(f"Invalid Major Name {major!r}")

    def normalize_class_year(class_year, record):
        class_year = clean_text(class_year)
        valid_class_years = ["First Year", "Sophomore", "Junior", "Senior", "Graduate"]

        class_year_map = {
            "freshman": "First Year",
            "sr": "Senior",
            "phd": "Graduate",
            "jr": "Junior",
            "fr": "First Year",
            "2nd year": "Sophomore",
            "grad": "Graduate",
            "3rd year": "Junior",
            "soph": "Sophomore",
            "1st year": "First Year",
            "master's": "Graduate",
            "4th year": "Senior",
            "masters": "Graduate",
        }
        if class_year.casefold() in class_year_map:
            class_year = class_year_map[class_year.casefold()]

        for vcy in valid_class_years:
            if vcy.casefold() == class_year.casefold():
                return vcy

        raise ValueError(f"Invalid Class Year {class_year!r}")

    def normalize_gpa(gpa, record):
        gpa = clean_text(gpa)
        gpa = float(gpa) if gpa else None
        if gpa is not None:
            if not (0 <= gpa <= 4.0):
                return None
                raise ValueError(f"Invalid GPA: {gpa}")
            return gpa
        return None
        raise ValueError(f"GPA Missing")

    def normalize_credits_attempted(credits_attempted, record):
        credits_attempted = credits_attempted.casefold()
        try:
            if "credits" in credits_attempted:
                credits_attempted = credits_attempted.replace("credits", "")
            credits_attempted = clean_text(credits_attempted)
            credits_attempted = int(clean_text(credits_attempted)) if credits_attempted else None
            if credits_attempted is None:
                return None
                raise ValueError("Credits attempted can not be null")
        except ValueError as e:
            raise e
        if credits_attempted < 0:
            return None
            raise ValueError("Credits attempted can not be negative")
        return credits_attempted

    def normalize_credits_earned(credits_earned, record):
        credits_earned = credits_earned.casefold()
        try:
            if "credits" in credits_earned:
                credits_earned = credits_earned.replace("credits", "")
            credits_earned = clean_text(credits_earned)

            credits_earned = int(clean_text(credits_earned)) if credits_earned else None
            if credits_earned is None:
                return None
                raise ValueError("Credits earned can not be null")
        except ValueError as e:
            raise e
        if credits_earned < 0:
            return None
            raise ValueError("Credits earned can not be negative")
        return credits_earned

    def normalize_enrollment_date(enrollment_date, record):
        enrollment_date = clean_text(enrollment_date)

        # we should thinka bout this ordering since it can be unclear which is month vs. day in non iso formats
        valid_date_formats = [
            "%Y-%m-%d",
            "%m/%d/%y",
            "%m/%d/%Y",
            "%d/%m/%y",
            "%d/%m/%Y",
            "%m-%d-%Y",
            "%B %d, %Y",
        ]
        for vdf in valid_date_formats:
            try:
                typed_date = datetime.strptime(enrollment_date, vdf)
            except ValueError as e:
                pass
            else:
                return typed_date
        raise ValueError(f"Invalid Date Format {enrollment_date}")

    def normalize_record(record):
        if (
            record["credits_attempted"] is None
            or record["credits_earned"] is None
            or record["credits_attempted"] < record["credits_earned"]
        ):
            record["credits_attempted"] = None
            record["credits_earned"] = None

        return record

    seen_students = set()
    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for row_num, row in enumerate(reader, start=2):  # Start at 2 (row 1 is the header)
                record = {}
                try:

                    record_lookup = {
                        "id": {"csv_name": "Student_ID", "normalizer": normalize_id},
                        "major": {"csv_name": "Major", "normalizer": normalize_major},
                        "college": {
                            "csv_name": "College",
                            "normalizer": normalize_college,
                        },
                        "class_year": {
                            "csv_name": "Class_Year",
                            "normalizer": normalize_class_year,
                        },
                        "gpa": {"csv_name": "GPA", "normalizer": normalize_gpa},
                        "credits_attempted": {
                            "csv_name": "Credits_Attempted",
                            "normalizer": normalize_credits_attempted,
                        },
                        "credits_earned": {
                            "csv_name": "Credits_Earned",
                            "normalizer": normalize_credits_earned,
                        },
                        "enrollment_date": {
                            "csv_name": "Enrollment_Date",
                            "normalizer": normalize_enrollment_date,
                        },
                    }

                    for field, data in record_lookup.items():
                        try:
                            record[field] = data["normalizer"](row.get(data["csv_name"]), record)
                        except (
                            KeyError,
                            ValueError,
                            DuplicateEntryError,
                            BusinessLogicError,
                        ) as e:
                            results["errors_by_field"][field] += 1
                            results["error_log"].append(
                                make_error_log_entry(row_num, field, e, row.get(data["csv_name"]))
                            )
                            raise

                    if record["id"] in seen_students:
                        raise DuplicateEntryError(f"Valid entry for student {record['id']} already exists")

                    try:
                        record = normalize_record(record)
                    except BusinessLogicError as e:
                        results["errors_by_field"]["record"] += 1
                        results["error_log"].append(make_error_log_entry(row_num, "record", e, record))
                        raise

                    seen_students.add(record["id"])
                    valid_records.append(record)

                except (
                    KeyError,
                    ValueError,
                    DuplicateEntryError,
                    BusinessLogicError,
                ) as e:
                    if type(e).__name__ not in results["errors_by_type"]:
                        results["errors_by_type"][type(e).__name__] = 0
                    results["errors_by_type"][type(e).__name__] += 1
                    results["invalid_rows"] += 1
                    if type(e).__name__ == "KeyError":
                        print(row)
                    if not skip_invalid:
                        raise
                else:
                    results["valid_rows"] += 1
                finally:
                    results["total_rows"] += 1

    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file: {filename}")

    return valid_records, results


# Test with the clean dataset (datasets live one level up, in ../data/)
students, stats = load_student_data("../data/crestview_students_messy.csv")
pprint.pprint(stats)
