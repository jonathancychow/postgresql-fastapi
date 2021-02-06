import psycopg2
import yaml
from pathlib import Path

def get_credentials():
    current_file_dir = Path(__file__).resolve()
    repo_dir = current_file_dir.parent
    cred_path = Path(repo_dir, 'cred.yaml')
    with open(cred_path) as f:
        configurations = yaml.safe_load(f.read())
        credentials = configurations['CREDENTIALS']
        user = credentials['USER']
        db = credentials['DB']
        password = credentials['PASSWORD']
        host = credentials['HOST']
        port = credentials['PORT']

    return user, db, password, host, port


user, db, password, host, port = get_credentials()
con = psycopg2.connect(database="postgres", user="postgres", password=password, host="127.0.0.1", port="5432")

print("Database opened successfully")

cur = con.cursor()
# cur.execute('''CREATE TABLE STUDENT
#       (ADMISSION INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       COURSE        CHAR(50),
#       DEPARTMENT        CHAR(50));''')
# print("Table created successfully")

# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");
# print("Added student")

cur.execute("SELECT admission, name, age, course, department from STUDENT")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3419")
con.commit()

cur.execute("DELETE from STUDENT where ADMISSION=3420;")
con.commit()

cur.execute("SELECT admission, name, age, course, department from STUDENT")
rows = cur.fetchall()

for row in rows:
    print("ADMISSION =", row[0])
    print("NAME =", row[1])
    print("AGE =", row[2])
    print("COURSE =", row[3])
    print("DEPARTMENT =", row[4], "\n")

con.commit()
con.close()