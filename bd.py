import streamlit as st
from datetime import date

# Sidebar for user input
st.sidebar.header("Your Special Day 🎈")

# Input fields for name and birthday
name = st.sidebar.text_input("Enter your name:", value="myungbin")
birthday = st.sidebar.date_input("Enter your birthday:", date.today())

# Title of the app
st.title(f"🎉🥳 Happy Birthday, {name}! 💖🎂")

# Calculate age
today = date.today()
age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

def ages():
    if age == 0:
        return 20
    return age

# Fun and loving messages
st.subheader(f"🎉🎂 Happy Birthday, {name}! 🎂🎉")
st.write(f"To the most **amazing**, **gorgeous**, and **awesome** friend in the world, you’re {ages()} years of pure magic! ✨💕")

st.write("Your birthday is the first day of another 365-day journey. Be the shining thread in the beautiful tapestry of the world to make this year the best ever. Enjoy the ride🎁💫")

# Fun fact or joke
st.write("You must have **superpowers**, because every year you grow older, but somehow you’re just getting more and more **beautiful**! 😍✨")

# Optional: Add a romantic birthday song
if st.button("Play Our Song 🎶"):
    st.audio("./01-Monk-Turner-Fascinoma-Its-Your-Birthday(chosic.com).mp3", autoplay=True, start_time=0)

# Final cute message with some humor
st.balloons()

# Custom CSS for better mobile responsiveness
st.markdown(
    """
    <style>
    /* Adjust font sizes for mobile devices */
    @media (max-width: 768px) {
        .css-18e3th9 {
            font-size: 1.5rem; /* Adjust as needed */
        }
        .css-1v0mbdj {
            font-size: 1.2rem; /* Adjust as needed */
        }
        .css-1uv9z2e {
            font-size: 1rem; /* Adjust as needed */
        }
        .css-ffhzg2 {
            margin: 1rem 0; /* Adjust margin for better spacing */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)
