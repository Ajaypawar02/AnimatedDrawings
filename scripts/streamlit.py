import streamlit as st

# Sidebar
st.sidebar.title("Parameters")
num_eval_questions = st.sidebar.slider("Number of Evaluation Questions", min_value=1, max_value=15, value=5)

# Main content
st.title("Get Started")
input_style = "text-align: center; width: 100%;"

# Input field for the evaluation question
# question = st.text_input("Evaluation Question", "", key="input", value="", style=input_style)

question = st.text_input("Evaluation Question", "")# Display the selected number of evaluation questions
prompt = st.text_area("Prompt", "")

# Rest of the content goes here...