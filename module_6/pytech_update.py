from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.hgoc9.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list = students.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY--")

for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"])

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bones II"}})

# find the update
benny = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + benny["student_id"] + "\n  First Name: " + benny["first_name"] + "\n  Last Name: " + benny["last_name"])

# exit message
input("\n\n  End of program, press any key to continue...")