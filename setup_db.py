import pyodbc

# Connect to master database to create SAMS
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-LK3TR\\SQLEXPRESS;'
    'DATABASE=master;'
    'Trusted_Connection=yes;',
    autocommit=True
)

cursor = conn.cursor()
cursor.execute("IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'SAMS') CREATE DATABASE SAMS")
print("SAMS database created/verified!")
cursor.close()
conn.close()

# Now connect to SAMS and create required tables
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-LK3TR\\SQLEXPRESS;'
    'DATABASE=SAMS;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

# Create subjects table
cursor.execute('''
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'subjects')
BEGIN
    CREATE TABLE subjects(
        Id_number VARCHAR(50),
        subjects VARCHAR(100)
    );
END
''')

# Create images table
cursor.execute('''
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'images')
BEGIN
    CREATE TABLE images(
        Id_number VARCHAR(50) PRIMARY KEY,
        image VARCHAR(255)
    );
END
''')

# Create faculty_subjects table
cursor.execute('''
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'faculty_subjects')
BEGIN
    CREATE TABLE faculty_subjects(
        Id_number VARCHAR(50),
        subjects VARCHAR(100)
    );
END
''')

conn.commit()
print("All tables created successfully!")
cursor.close()
conn.close()
