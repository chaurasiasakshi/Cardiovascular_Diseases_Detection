import streamlit as st

# Define the Team Page function
def team_page():
    # Custom CSS for uniform image size and center alignment
    st.markdown("""
        <style>
        .team-member {
            text-align: center;
        }
        .team-member img {
            border-radius: 50%;  /* Makes the images circular */
            width: 150px;
            height: 150px;
            object-fit: cover;
            margin-bottom: 10px;
        }
        .team-member h3 {
            font-size: 18px;
            margin-top: 0;
            margin-bottom: 5px;
        }
        .team-member p {
            font-size: 14px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Team header
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>Meet Our Team</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>We are a team of passionate individuals working together to make a difference.</p>", unsafe_allow_html=True)

    # Team Members
    team_members = [
        {
            "name": "Ambika Ajai Singh",
            "bio": "Ambika is a software engineer with a passion for AI and machine learning.",
            "image": "ambikaa.jpg"  # Make sure the image exists or give the full path
        },
        {
            "name": "Ashish Gupta",
            "bio": "Ashish is a data scientist who loves transforming raw data into meaningful insights.",
            "image": "ashish.jpg"
        },
        {
            "name": "Atul Srivastav",
            "bio": "Atul is a full-stack developer with a focus on user experiences and efficient back-end systems.",
            "image": "atul.jpg"
        },
        {
            "name": "Sakshi Chaurasia",
            "bio": "Sakshi is a project manager ensuring our projects stay on track and our clients remain satisfied.",
            "image": "profile.jpg"
        }
    ]

    # Create the layout with 4 columns
    col1, col2, col3, col4 = st.columns(4)

    # Assign a team member to each column and apply custom styling
    with col1:
        member = team_members[0]
        st.markdown(f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['bio']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        member = team_members[1]
        st.markdown(f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['bio']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        member = team_members[2]
        st.markdown(f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['bio']}</p>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        member = team_members[3]
        st.markdown(f"""
            <div class="team-member">
                <img src="{member['image']}" alt="{member['name']}">
                <h3>{member['name']}</h3>
                <p>{member['bio']}</p>
            </div>
        """, unsafe_allow_html=True)

