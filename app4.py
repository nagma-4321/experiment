
print("hello")

import streamlit as st

# Initialize session state for tracking conversation
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Define chatbot questions
questions = [
    "What's your name?",
    "How are you feeling today?",
    "Let's talk about this year 2024.",
    "How was your year?",
    "What is the most amazing memory of this year of yours?",
    "What is the one learning you got from this year?",
    "What is the one thing you liked the most about yourself this year?",
    "Have you captured the best memories of your life with you? If yes, I can give a suggestion to you.",
    "If you get a chance to write a book regarding the philosophy of living life, what would be the title?",
    "Do you pay gratitude to the higher for all the opportunities in your life?",
    "What one advice do you want to give yourself to be happier in life?"
]

suggestion = "Please convert them to physical copies; otherwise, you might lose them due to storage issues."

# Streamlit layout
st.set_page_config(page_title="DATE TO MEMORIES (2024 Edition)", layout="centered")

# Chat header
st.markdown(
    """
    <div style="background-color:orange; padding:20px; border-radius:10px;">
        <h1 style="color:white; text-align:center;">DATE TO MEMORIES (2024 Edition)</h1>
        <h3 style="color:white; text-align:center;">Reliving Moments, Creating Memories</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Display conversation
st.write("### Chat")
chat_area = st.container()

with chat_area:
    for message in st.session_state.conversation:
        if message["sender"] == "bot":
            st.markdown(
                f"""
                <div style="text-align:left; background-color:#F0F8FF; padding:10px; margin:10px; border-radius:10px; width:60%; border:1px solid #FF4500;">
                    <b>Bot:</b> {message['message']}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div style="text-align:right; background-color:#E6FFED; padding:10px; margin:10px; border-radius:10px; width:60%; border:1px solid #32CD32;">
                    <b>You:</b> {message['message']}
                </div>
                """,
                unsafe_allow_html=True,
            )

# Input box for user response
user_input = st.text_input("Your response:", "")

# Send button to submit the response
if st.button("Send"):
    if user_input.strip():
        # Add user's response to the conversation
        st.session_state.conversation.append({"sender": "user", "message": user_input})

        # Add bot's next question or thank-you message
        if st.session_state.current_question_index < len(questions):
            question = questions[st.session_state.current_question_index]
            st.session_state.conversation.append({"sender": "bot", "message": question})

            # Handle suggestion for Question 7
            if st.session_state.current_question_index == 7:
                st.session_state.conversation.append(
                    {"sender": "bot", "message": suggestion}
                )

            # Update the question index
            st.session_state.current_question_index += 1
        else:
            user_name = st.session_state.conversation[0]["message"]
            st.session_state.conversation.append(
                {
                    "sender": "bot",
                    "message": f"Thank you for your responses, {user_name}! I appreciate your thoughtful answers and wish you the best for the future.",
                }
            )
    else:
        st.warning("Please type your response before sending!")

# Auto-scroll to the latest chat
st.markdown(
    """
    <script>
    var chat_area = document.querySelector('.element-container');
    chat_area.scrollTop = chat_area.scrollHeight;
    </script>
    """,
    unsafe_allow_html=True,
)




        