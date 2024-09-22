import streamlit as st

# Define the About page function
def about():
   
    # Section 1: Text on the left, Image on the right
    st.markdown("<h1 style='font-size: 48px;'>How the heart works</h1>", unsafe_allow_html=True)  # Increased text size for the title
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <p style='font-size: 22px; line-height: 1.6;'>
        The human heart pumps blood to every part of your body.Your heart is the pump which powers your body. It supplies blood carrying oxygen and nutrients to every cell, nerve, muscle and vital organ in your body. It sits in your chest between your lungs, slightly to the left of centre, and is protected by your rib cage. Your heart is about the size of your clenched fist and weighs about 300 grams (that's just over half a packet of butter).
        </p>
        """, unsafe_allow_html=True)  # Increased font size and line spacing for better readability
        
    with col2:
        st.image("11.jpg", caption="Heart Chambers (Rooms)", width=600)  # Increased image width

    # Section 2: Image on the left, Text on the right
    st.markdown("<h2 style='font-size: 36px;'>Heart valves (the doors between the rooms)</h2>", unsafe_allow_html=True)  # Increased subtitle size
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("22.jpg", caption="Heart Valves", width=600)  # Increased image width
        
    with col2:
        st.markdown("""
        <p style='font-size: 22px; line-height: 1.6;'>
        There are four valves that act like doors to keep blood flowing in the right direction. They open and close as your heart pumps. The valves only open one way. This stops blood flowing in the wrong direction between the chambers of your heart.
        
        The two valves that sit between the upper and lower chambers of the heart are called the atrioventricular (AV) valves.
        
        - The tricuspid valve is the door between the right atrium and ventricle.
        - The mitral valve is the door between the left atrium and ventricle.
        
        The other two valves are the doors out of the ventricles:
        
        - The aortic valve is the door out of the left ventricle into the aorta.
        - The pulmonary valve is the door out of the right ventricle into the pulmonary artery.
        </p>
        """, unsafe_allow_html=True)

    # Section 3: Text on the left, Image on the right
    st.markdown("<h2 style='font-size: 36px;'>The blood vessels (the plumbing)</h2>", unsafe_allow_html=True)  # Increased subtitle size
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <p style='font-size: 22px; line-height: 1.6;'>
        Blood travels between the heart, lungs, and the rest of the body via a network of blood vessels. There are three main types of blood vessels:

        - **Arteries**: Carry oxygenated blood from your heart to the rest of your body.
        - **Veins**: Carry deoxygenated blood back to your heart and lungs.
        - **Capillaries**: Small vessels where oxygenated and deoxygenated blood are exchanged.
        </p>
        """, unsafe_allow_html=True)  # Increased text size and line height for readability
        
    with col2:
        st.image("55.jpg", caption="Blood Vessels", width=600)  # Increased image width

    # Section 4: Image on the left, Text on the right
    st.markdown("<h2 style='font-size: 36px;'>How the heart pumps</h2>", unsafe_allow_html=True)  # Increased subtitle size
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("33.jpg", caption="Heart Pumping Mechanism", width=600)  # Increased image width
        
    with col2:
        st.markdown("""
        <p style='font-size: 22px; line-height: 1.6;'>
        Your heart's conduction system sends electrical signals that trigger the heart to pump blood around the body, and to and from the lungs.

        - Deoxygenated blood is returned to the right side of the heart via large veins called the **inferior** and **superior vena cava**.
        - The right side pumps blood to the lungs via the **pulmonary artery** to receive oxygen.
        - Oxygenated blood travels through the **pulmonary veins** to the left side of the heart.
        - The left side pumps blood to the rest of the body via the **aorta**.
        </p>
        """, unsafe_allow_html=True)

