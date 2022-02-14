from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.hgoc9.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students

student_list + students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find{} QUERY --")

for doc in student_list:
    print("STUDENT ID:" + doc["student_id"] + "\n First Name:" + doc["first_name"] + "\n Last Name:" + doc["last_name"])

benny = students.find_one({"student_id": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID:" + benny["student_id"] + "\n First Name:" + benny["first_name"] + "\n Last Name:" + benny["last_name"])

input("\n\n END of program, press any key to continue")
