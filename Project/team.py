import streamlit as st

# Define the Team Page function
def team_page():
    
    # Team header
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>Meet Our Team</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>We are a team of passionate individuals working together to make a difference.</p>", unsafe_allow_html=True)

    # Team Members
    team_members = [
        {
            "name": "Ambika Ajai Singh",
            "bio": "Ambika is a software engineer with a passion for AI and machine learning. ",
            "image": "ambikaa.jpg"  # Make sure the image exists or give the full path
        },
        {
            "name": "Ashish Gupta",
            "bio": "Ashish is a data scientist who loves transforming raw data into meaningful insights. She is the brain behind our data strategies.",
            "image": "ashish.jpg"
        },
        {
            "name": "Atul Srivastav",
            "bio": "Atul is a full-stack developer with user experiences and efficient back-end systems.",
            "image": "atul.jpg"
        },
        {
            "name": "Sakshi Chaurasia",
            "bio": "Sakshi is a project manager ensuring our projects stay on track and our clients remain satisfied with the outcomes.",
            "image": "profile.jpg"
        }
    ]

    # Create the layout with 4 columns
    col1, col2, col3, col4 = st.columns(4)

    # Assign a team member to each column
    with col1:
        member = team_members[0]
        st.image(member["image"], caption=member["name"], width=150)  # Use st.image
        st.markdown(f"**{member['name']}**")
        st.write(member['bio'])

    with col2:
        member = team_members[1]
        st.image(member["image"], caption=member["name"], width=150)  # Use st.image
        st.markdown(f"**{member['name']}**")
        st.write(member['bio'])

    with col3:
        member = team_members[2]
        st.image(member["image"], caption=member["name"], width=150)  # Use st.image
        st.markdown(f"**{member['name']}**")
        st.write(member['bio'])

    with col4:
        member = team_members[3]
        st.image(member["image"], caption=member["name"], width=150)  # Use st.image
        st.markdown(f"**{member['name']}**")
        st.write(member['bio'])

