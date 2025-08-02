import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page Setup ---
st.set_page_config(page_title="Animal Kingdom Division Dash", page_icon="🐾")

# --- Developer Credit ---
st.markdown("### www.cognitivecloud.ai")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title and Intro ---
st.title("🐾 The Animal Kingdom Division Dash")
st.markdown("""
Welcome to the Animal Kingdom! Here, we learn about **division** by helping animals share their treats.

Division is all about **fair sharing** and figuring out if anything is left over. It's a key math skill used every day, from sharing a pizza to organizing a team.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Understand division as fair sharing among groups.
- Identify the **quotient** (the result of sharing) and the **remainder** (what's left over).
- Apply division to solve real-world problems.
- Relate these concepts to Common Core math standards.
""")

# Common Core Standards Alignment
st.info("📚 **Common Core Alignment:** This lesson aligns with elementary school math standards, specifically focusing on Operations and Algebraic Thinking and Number and Operations in Base Ten (e.g., 3.OA.A.2, 4.NBT.B.6).")

# --- User Info (Moved Up) ---
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your animal guide:", [
    "🐻 Bear", "🐰 Rabbit", "🦊 Fox", "🦔 Hedgehog"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's start our division adventure.")

st.markdown("---")

# --- Interactive Explorer Section ---
st.header("🔍 Sharing is Caring: An Interactive Division Story")
st.markdown("Use the sliders below to change the number of tasty treats and the number of hungry animals. The program will show you how to divide them fairly!")

# Create columns for sliders
col1, col2 = st.columns(2)

with col1:
    treats = st.slider("Total Tasty Treats (e.g., Berries)", 10, 50, 25, 1)
    treats_emoji = "🍓"

with col2:
    animals = st.slider("Number of Hungry Animals", 2, 10, 5, 1)
    animals_emoji = "🐻"

# Perform the division
quotient = treats // animals
remainder = treats % animals

st.subheader(f"Story Time: There are {treats} {treats_emoji} for {animals} {animals_emoji}s.")
st.write("")

# Display the results
col3, col4, col5 = st.columns(3)
with col3:
    st.metric("Each Animal Gets", f"{quotient} {treats_emoji}")
with col4:
    st.metric("Treats Left Over", f"{remainder} {treats_emoji}")
with col5:
    st.metric("Total Treats Shared", treats)

# Visualization
st.header("📈 Visualizing the Division")
st.markdown("This chart shows the fair share for each animal and any treats that were left over.")

labels = [f'Each Animal\'s Share ({animals} animals)', 'Leftovers']
sizes = [quotient * animals, remainder]
colors = ['#6495ED', '#FFA500']
explode = (0, 0.1)  # explode the leftovers slice

if treats > 0:
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

st.markdown("---")

# Quick Quiz Section
st.header("🎲 Quick Understanding Check")

quiz_questions = [
    {
        "question": f"If 20 {treats_emoji} are divided among 5 {animals_emoji}s, how many does each animal get?",
        "options": ["3", "4", "5", "25"],
        "correct": 1,
        "explanation": "20 divided by 5 is 4. Each animal gets 4 treats."
    },
    {
        "question": "What is the remainder if you divide 17 by 3?",
        "options": ["1", "2", "3", "0"],
        "correct": 1,
        "explanation": "17 divided by 3 is 5 with a remainder of 2."
    },
    {
        "question": "If each of 8 animals gets 3 treats, how many total treats were there?",
        "options": ["11", "24", "8", "3"],
        "correct": 1,
        "explanation": "This is multiplication! 8 animals times 3 treats each equals 24 treats total."
    }
]

for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"q{i}")
    
    if st.button(f"Check Answer {i+1}", key=f"check{i}"):
        if q['options'].index(answer) == q['correct']:
            st.success(f"✅ Correct! {q['explanation']}")
        else:
            st.error(f"❌ Try again! {q['explanation']}")

# Exit Reflection
st.header("🧾 Reflection")
reflection = st.text_area("What is one thing you learned about division today? Describe a real-life situation where you would use division with a remainder.")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent! You're thinking like a mathematician.")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# Final Summary
st.header("🎓 What You've Learned")
st.markdown("""
**Congratulations!** You've explored:
- ✅ **Division as fair sharing** using a fun animal theme.
- ✅ The difference between the **quotient** and the **remainder**.
- ✅ How to visualize division and apply it to **real-world problems**.
""")

st.markdown("---")

# Related Lessons
st.header("📚 Additional Resources")
resources = {
    "🌐 Websites & Interactive Tools": [
        {
            "name": "Khan Academy: Division",
            "url": "https://www.khanacademy.org/math/arithmetic/arith-review-multiply-divide/arith-division-intro/v/the-concept-of-division",
            "description": "Video tutorials and practice problems for all levels of division."
        },
        {
            "name": "Coolmath Games: Division",
            "url": "https://www.coolmathgames.com/division",
            "description": "Fun, interactive games to practice your division skills."
        }
    ],
    "📖 Articles & Fun Facts": [
        {
            "name": "Fun Facts About Animals and Sharing",
            "url": "https://www.nationalgeographic.com/animals/mammals/facts",
            "description": "Explore how different animal species share food and resources in the wild."
        }
    ]
}

# Display resources in organized tabs
resource_tabs = st.tabs(list(resources.keys()))

for i, (category, items) in enumerate(resources.items()):
    with resource_tabs[i]:
        for item in items:
            st.markdown(f"**[{item['name']}]({item['url']})**")
            st.write(f"📝 {item['description']}")
            st.write("---")
