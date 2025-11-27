import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Streamlit app of VGU")
st.text("Welcome to our dashboard")
st.header("I am a header")
st.write("you can Write ", 10+5)

name = st.text_input("Enter your name")
age = st.text_input("Enter your age")
st.write("your name is :", name , "your age is :", age)
st.selectbox("Enter your course :", ["BCA", "MCA" , "B.TECH"])
if st.button ("Click Me"):
    st.success("Clicked Button")
file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File Uploaded Successfully !!!!")


data = {"Name": ["Tom", "Jack", "Pop", "Harry"], "Marks": [10,20,20,10]}
df = pd.DataFrame(data)


st.dataframe(df)

data = pd.DataFrame({
    "Marks" : [10,20,20,10]
})

st.line_chart(data)
st.bar_chart(data)

subject = ["Python", "C", "Java"]
marks = [20, 10, 5]

fig , ax = plt.subplots()
ax.pie(marks, labels=subject,autopct='%1.1f%%')
st.pyplot(fig)

st.toast("Welcome Sir")
st.balloons()
st.snow()

