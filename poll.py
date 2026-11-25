import streamlit as st 
st.title("Poll for best programming language")
col1,col2,col3=st.columns(3)
with col1:
    st.header("Python")
    st.image("https://www.python.org/static/community_logos/python-logo.png",width=100)
    st.write("Python is a high-level, interpreted programming language known for its simplicity and readability. It is widely used in web development, data analysis, artificial intelligence, and scientific computing.")
    vote1 =st.button("Vote for Python")
with col2:
    st.header("JavaScript")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",width=100)
    st.write("JavaScript is a versatile, high-level programming language primarily used for web development. It enables interactive web pages and is an essential part of web applications, alongside HTML and CSS.")
    vote2 =st.button("Vote for JavaScript")
with col3:
    st.header("Java")
    st.image("https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg",width=100)
    st.write("Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible. It is widely used for building enterprise-scale applications, Android apps, and web applications.")
    vote3 =st.button("Vote for Java")

if vote1:
    st.success("You voted for Python!")
elif vote2:
    st.success("You voted for JavaScript!")
elif vote3:
    st.success("You voted for Java!")