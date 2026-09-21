from sqlalchemy import text
from app.db.database import engine


with engine.begin() as connection:
    connection.execute(text("""INSERT into users (email) VALUES (:email)"""),{"email":"annukumari202478@gmail.com"})
   
    print("User inserted sucessfully")
    