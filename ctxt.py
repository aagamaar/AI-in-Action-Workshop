import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the numbers
num1 = st.number_input("Enter the first number:", format="%.2f")
num2 = st.number_input("Enter the second number:", format="%.2f")

# Dropdown to select the operation
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Result placeholder
result = None

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero")

    if result is not None:
        st.success(f"The result is: {result}")
