import pandas as pd
from sqlalchemy import create_engine, text

# הגדרת חיבור עם SQLAlchemy
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

# יצירת מנוע SQLAlchemy
engine = create_engine(DATABASE_URL)

df_students = pd.read_sql(text("SELECT * FROM students;"), engine)
print(df_students)

df_students.to_csv("studnets.csv")
