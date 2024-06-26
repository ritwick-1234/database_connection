import streamlit as st
import mysql.connector
import re

# MySQL connection configuration
db_config = {
    "host": "bo0ph9vwiuipeiftw587-mysql.services.clever-cloud.com",
    "user": "utvwj7co7dtikh5c",
    "password": "o9o0Ar42kur7ndfnWy0A",
    "database": "bo0ph9vwiuipeiftw587"
}

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Function to validate password
def validate_password(password):
    if len(password) >= 8 and password[0].islower():
        return True
    return False

# Function to validate integer input
def validate_integer(value):
    try:
        return int(value)
    except ValueError:
        return None

st.markdown("<h4 style='text-align: center;'>Register Yourself</h4>", unsafe_allow_html=True)
with st.form('registration_form', clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name *")
    l_name = col2.text_input("Last Name *")
    email = st.text_input("Email Address *")
    password = st.text_input("Password *", type='password')
    confirm_password = st.text_input("Confirm Password *", type='password')
    col_day, col_month, col_year = st.columns(3)
    day = col_day.text_input("Day *")
    month = col_month.text_input("Month *")
    year = col_year.text_input("Year *")

    state = st.form_submit_button("Submit")

    if state:
        if f_name == '' or l_name == '' or email == '' or password == '' or confirm_password == '' or day == '' or month == '' or year == '':
            st.warning("Please fill all the mandatory fields")
        elif not validate_email(email):
            st.warning("Please enter a valid email address")
        elif not validate_password(password):
            st.warning("Password must be at least 8 characters long and start with a lowercase letter")
        elif password != confirm_password:
            st.warning("Passwords do not match")
        else:
            # Validate day, month, and year
            day_int = validate_integer(day)
            month_int = validate_integer(month)
            year_int = validate_integer(year)

            if day_int is None or month_int is None or year_int is None:
                st.warning("Please enter valid numeric values for day, month, and year")
            else:
                mydb = mysql.connector.connect(**db_config)
                mycursor = mydb.cursor()

                # Create the table if it does not exist
                mycursor.execute("DROP TABLE IF EXISTS users_4")
                mycursor.execute("DROP TABLE IF EXISTS users_1")
                mycursor.execute("DROP TABLE IF EXISTS users")
                mycursor.execute("""
                CREATE TABLE IF NOT EXISTS users_10 (
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

                # Insert data into the table
                sql = "INSERT INTO users_10 (first_name, last_name, email, password, birth_day, birth_month, birth_year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (f_name, l_name, email, password, day_int, month_int, year_int)

                mycursor.execute(sql, val)
                mydb.commit()

                st.success("Submitted Successfully")

                mycursor.close()
                mydb.close()
