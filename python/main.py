from sqlalchemy import create_engine, text

# הגדרת חיבור עם SQLAlchemy
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

# יצירת מנוע SQLAlchemy
engine = create_engine(DATABASE_URL)

# פתיחת חיבור והפעלת השאילתה
with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    version = result.scalar()  # מחזיר את התוצאה הראשונה
    print(f"PostgreSQL Version: {version}")

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM students;"))

    # המרת התוצאה לרשימה של מילונים
    students = [dict(row._mapping) for row in result]

# הדפסת הנתונים
for student in students:
    print(student)
