from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.hgoc9.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

# student docs

# benny doc
benny = {
    "student_id": "1007",
    "first_name": "Benny",
    "last_name": "Bones",
    "enrollments": [
        {
            "term": "Session 3",
            "gpa": "4.0",
            "start_date": "January 1, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Lappe",
                    "grade": "A",
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations and Forensics",
                    "instructor": "Fine",
                    "grade": "A",
                }
            ]
        }
    ]
}

# bo doc
bo = {
    "student_id": "1008",
    "first_name": "Bo",
    "last_name": "Bigs",
    "enrollments": [
        {
            "term": "Session 3",
            "gpa": "4.0",
            "start_date": "January 1, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Lappe",
                    "grade": "A",
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations and Forensics",
                    "instructor": "Fine",
                    "grade": "A",
                }
            ]
        }
    ]
}

# buddy doc
buddy = {
    "student_id": "1009",
    "first_name": "Buddy",
    "last_name": "Borks",
    "enrollments": [
        {
            "term": "Session 3",
            "gpa": "4.0",
            "start_date": "January 1, 2022",
            "end_date": "March 6, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security",
                    "instructor": "Lappe",
                    "grade": "A",
                },
                {
                    "course_id": "CYBR420",
                    "description": "Cyber Investigations and Forensics",
                    "instructor": "Fine",
                    "grade": "A",
                }
            ]
        }
    ]
}

students = db.students

print("\n -- INSERT STATEMENTS --")
benny_student_id = students.insert_one(benny).inserted_id
print("Inserted student record Benny Bones into the students collection with document_id" + str(benny_student_id))

bo_student_id = students.insert_one(bo).inserted_id
print("Inserted student record Bo Bigs into the students collection with document_id" + str(bo_student_id))

buddy_student_id = students.insert_one(buddy).inserted_id
print("Inserted student record Buddy Borks into the students collection with document_id" + str(buddy_student_id))

input("\n\n End of program, press any button to exit...")
