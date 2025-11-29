import pyodbc

# Connect to SAMS database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-LK3TR\\SQLEXPRESS;'
    'DATABASE=SAMS;'
    'Trusted_Connection=yes;'
)
cursor = conn.cursor()

print("Fixing database tables...")

# Drop and recreate registration table with correct structure
print("\n1. Fixing registration table...")
cursor.execute("""
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'registration')
BEGIN
    DROP TABLE registration
END
""")
conn.commit()

cursor.execute("""
CREATE TABLE registration(
    Id_number VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(30) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    DoB VARCHAR(20) NOT NULL,
    semister VARCHAR(20) NOT NULL,
    batch VARCHAR(20) NOT NULL,
    branch VARCHAR(20) NOT NULL,
    reset_token VARCHAR(50)
)
""")
conn.commit()
print("   ✓ registration table fixed")

# Drop and recreate faculty_data table with semister column
print("\n2. Fixing faculty_data table...")
cursor.execute("""
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'faculty_data')
BEGIN
    DROP TABLE faculty_data
END
""")
conn.commit()

cursor.execute("""
CREATE TABLE faculty_data (
    Id_number VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    semister VARCHAR(50),
    branch VARCHAR(255),
    reset_token VARCHAR(255)
)
""")
conn.commit()
print("   ✓ faculty_data table fixed")

# Ensure subjects table exists
print("\n3. Ensuring subjects table exists...")
cursor.execute("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'subjects')
BEGIN
    CREATE TABLE subjects(
        Id_number VARCHAR(50),
        subjects VARCHAR(100)
    )
END
""")
conn.commit()
print("   ✓ subjects table OK")

# Ensure faculty_subjects table exists
print("\n4. Ensuring faculty_subjects table exists...")
cursor.execute("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'faculty_subjects')
BEGIN
    CREATE TABLE faculty_subjects(
        Id_number VARCHAR(50),
        subjects VARCHAR(100)
    )
END
""")
conn.commit()
print("   ✓ faculty_subjects table OK")

# Ensure images table exists
print("\n5. Ensuring images table exists...")
cursor.execute("""
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'images')
BEGIN
    CREATE TABLE images(
        Id_number VARCHAR(50) PRIMARY KEY,
        image VARCHAR(255)
    )
END
""")
conn.commit()
print("   ✓ images table OK")

# List all tables
print("\n" + "=" * 50)
print("📋 ALL TABLES IN DATABASE:")
print("=" * 50)
cursor.execute("""
    SELECT TABLE_NAME 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_TYPE = 'BASE TABLE'
""")
tables = cursor.fetchall()
for table in tables:
    print(f"  • {table[0]}")

# Show table structures
print("\n" + "=" * 50)
print("📊 TABLE STRUCTURES:")
print("=" * 50)

for table in ['registration', 'faculty_data', 'subjects', 'faculty_subjects', 'images']:
    print(f"\n{table}:")
    try:
        cursor.execute(f"""
            SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
            FROM INFORMATION_SCHEMA.COLUMNS 
            WHERE TABLE_NAME = '{table}'
        """)
        columns = cursor.fetchall()
        for col in columns:
            print(f"  - {col[0]} ({col[1]}, nullable: {col[2]})")
    except:
        print(f"  Table not found")

print("\n✅ Database fix completed!")
cursor.close()
conn.close()
