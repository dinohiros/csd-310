from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.hgoc9.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

# display message
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# test document
test_doc = {
    "student_id": "1010",
    "first_name": "Dino",
    "last_name": "Hiros"
}


test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

student_test_doc = students.find_one({"student_id": "1010"})

# display the results
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"])

# call delete_one
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students
new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop and output
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"])

input("\n\n  End of program, press any key to continue...")
