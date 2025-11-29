import pyodbc

# Connect to SAMS database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-LK3TR\\SQLEXPRESS;'
    'DATABASE=SAMS;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

print("=" * 60)
print("SAMS DATABASE - DATA VIEWER")
print("=" * 60)

# List all tables in the database
print("\n📋 TABLES IN DATABASE:")
print("-" * 40)
cursor.execute("""
    SELECT TABLE_NAME 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_TYPE = 'BASE TABLE'
""")
tables = cursor.fetchall()
for table in tables:
    print(f"  • {table[0]}")

# Show data from registration table (students)
print("\n👨‍🎓 REGISTERED STUDENTS (registration table):")
print("-" * 40)
try:
    cursor.execute("SELECT Id_number, Name, email, phone_number, Gender, semister, batch, branch FROM registration")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"  ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
            print(f"     Phone: {row[3]}, Gender: {row[4]}")
            print(f"     Semester: {row[5]}, Batch: {row[6]}, Branch: {row[7]}")
            print()
    else:
        print("  No students registered yet.")
except Exception as e:
    print(f"  Table not found or error: {e}")

# Show data from faculty_data table
print("\n👨‍🏫 REGISTERED FACULTY (faculty_data table):")
print("-" * 40)
try:
    cursor.execute("SELECT Id_number, email, branch FROM faculty_data")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"  ID: {row[0]}, Email: {row[1]}, Branch: {row[2]}")
    else:
        print("  No faculty registered yet.")
except Exception as e:
    print(f"  Table not found or error: {e}")

# Show subjects
print("\n📚 STUDENT SUBJECTS (subjects table):")
print("-" * 40)
try:
    cursor.execute("SELECT Id_number, subjects FROM subjects")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"  Student ID: {row[0]}, Subject: {row[1]}")
    else:
        print("  No subjects assigned yet.")
except Exception as e:
    print(f"  Table not found or error: {e}")

# Show faculty subjects
print("\n📖 FACULTY SUBJECTS (faculty_subjects table):")
print("-" * 40)
try:
    cursor.execute("SELECT Id_number, subjects FROM faculty_subjects")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"  Faculty ID: {row[0]}, Subject: {row[1]}")
    else:
        print("  No faculty subjects assigned yet.")
except Exception as e:
    print(f"  Table not found or error: {e}")

print("\n" + "=" * 60)
cursor.close()
conn.close()
