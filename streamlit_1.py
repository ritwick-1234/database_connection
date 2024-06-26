# import streamlit as st
# import streamlit as st

# st.markdown("<h4 style='text-align: center;'>Register Yourself</h4>", unsafe_allow_html=True)

# with st.form('form 2',clear_on_submit=True):
#     col1,col2=st.columns(2)
#     f_name=col1.text_input("First Name")
#     l_name=col2.text_input("Last Name")
#     st.text_input("Email Address")
#     st.text_input("Password")
#     st.text_input("Confirm Password")
#     day,month,year=st.columns(3)
#     day.text_input("Day")
#     month.text_input("Month")
#     year.text_input("Year")


#     state=st.form_submit_button("Submit")
#     if state:
#         if f_name== '' and l_name=='':
#             st.warning("Please fill the above fields")
#         else:
#             st.success("Submitted Successfully")
# import streamlit as st
# import re

# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email)

# def validate_password(password):
#     if len(password) >= 8 and password[0].islower():
#         return True
#     return False

# st.markdown("<h4 style='text-align: center;'>Register Yourself</h4>", unsafe_allow_html=True)

# with st.form('form 2', clear_on_submit=True):
#     col1, col2 = st.columns(2)
#     f_name = col1.text_input("First Name *")
#     l_name = col2.text_input("Last Name *")
#     email = st.text_input("Email Address *")
#     password = st.text_input("Password *", type='password')
#     confirm_password = st.text_input("Confirm Password *", type='password')
#     day, month, year = st.columns(3)
#     day.text_input("Day")
#     month.text_input("Month")
#     year.text_input("Year")

#     state = st.form_submit_button("Submit")

#     if state:
#         if f_name == '' or l_name == '' or email == '' or password == '' or confirm_password == '':
#             st.warning("Please fill all the mandatory fields")
#         elif not validate_email(email):
#             st.warning("Please enter a valid email address")
#         elif not validate_password(password):
#             st.warning("Password must be at least 8 characters long and start with a lowercase letter")
#         elif password != confirm_password:
#             st.warning("Passwords do not match")
#         else:
#             st.success("Submitted Successfully")


import streamlit as st
import mysql.connector
import re

# MySQL connection configuration
# db_config = {
#     "host": "bo0ph9vwiuipeiftw587-mysql.services.clever-cloud.com",    # Replace with your MySQL host
#     "user": "utvwj7co7dtikh5c",    # Replace with your MySQL user
#     "password": "o9o0Ar42kur7ndfnWy0A",  # Replace with your MySQL password
#     "database": "bo0ph9vwiuipeiftw587"  # Replace with your MySQL database name
# }

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate password
def validate_password(password):
    if len(password) >= 8 and password[0].islower():
        return True
    return False

st.markdown("<h4 style='text-align: center;'>Register Yourself</h4>", unsafe_allow_html=True)

with st.form('form 2', clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name *")
    l_name = col2.text_input("Last Name *")
    email = st.text_input("Email Address *")
    password = st.text_input("Password *", type='password')
    confirm_password = st.text_input("Confirm Password *", type='password')
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")

    state = st.form_submit_button("Submit")

    if state:
        if f_name == '' or l_name == '' or email == '' or password == '' or confirm_password == '':
            st.warning("Please fill all the mandatory fields")
        elif not validate_email(email):
            st.warning("Please enter a valid email address")
        elif not validate_password(password):
            st.warning("Password must be at least 8 characters long and start with a lowercase letter")
        elif password != confirm_password:
            st.warning("Passwords do not match")
        # else:
        #     # Insert data into the MySQL database
        #     try:
        #         mydb = mysql.connector.connect(**db_config)
        #         mycursor = mydb.cursor()

        #         # Insert data into the table
        #         sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
        #         val = (f"{f_name} {l_name}", "Some Address")  # Replace "Some Address" with the actual address field if you collect it

        #         mycursor.execute(sql, val)
        #         mydb.commit()

        #         st.success("Submitted Successfully")
        #     except mysql.connector.Error as err:
        #         st.error(f"Error: {err}")
        #     finally:
        #         if mycursor:
        #             mycursor.close()
        #         if mydb:
        #             mydb.close()

mydb = mysql.connector.connect(
    host="bo0ph9vwiuipeiftw587-mysql.services.clever-cloud.com",
    user="utvwj7co7dtikh5c",
    password="o9o0Ar42kur7ndfnWy0A",
    database="bo0ph9vwiuipeiftw587"

   
    

)
# Create a cursor object
mycursor = mydb.cursor()

# Drop the table if it exists
mycursor.execute("DROP TABLE IF EXISTS users")
mycursor.execute("""
CREATE TABLE users (
     id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255),
                birth_day INT,
                birth_month INT,
                birth_year INT
);
""")
sql = "INSERT INTO users_1 (first_name, last_name, email, password, birth_day, birth_month, birth_year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
vals = (f_name, l_name, email, password, int(day), int(month), int(year))
mycursor.executemany(sql, vals)

# Commit the transaction
mydb.commit()

# Close the connection
mycursor.close()
mydb.close()
