import streamlit as st

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

st.title("Basic Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
  result = add(num1, num2)
elif operation == "Subtract":
  result = subtract(num1, num2)
elif operation == "Multiply":
  result = multiply(num1, num2)
elif operation == "Divide":
  result = divide(num1, num2)

st.write("The result is", result)

