# import streamlit as st
# from streamlit_option_menu import option_menu

# import login

# st.set_page_config(
#     page_title="PawSome-AI",
#     page_icon="🐾",
#     layout="centered",
#     initial_sidebar_state="auto"
# )

# # Initialize session state for login and signup page selection
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False
# if 'signup_selected' not in st.session_state:
#     st.session_state['signup_selected'] = False

# # Display login or signup form based on selection and login status
# if not st.session_state['logged_in']:
#     if st.session_state['signup_selected']:
#         login.signup()
#         if st.button("Already have an account? Login here"):
#             st.session_state['signup_selected'] = False
#     else:
#         login.login()
#         if st.button("Don't have an account? Sign up here"):
#             st.session_state['signup_selected'] = True
# else:
#     # Display sidebar with options when logged in
#     with st.sidebar:
#         selected = option_menu(
#             'PawSome AI',
#             ['Welcome', 'Disease & Breed Detection', 'Petcare ChatBot', 'Prescription-Analyzer','find_veternary', 'Team Details', 'Feedback', 'Logout',],
#             icons=['house-door-fill', 'search', 'chat-right-fill', 'file-earmark-break-fill', 'info', 'star', 'box-arrow-right'],
#             menu_icon="🐶",
#             default_index=0
#         )

#     # Render the appropriate page based on selection
#     if selected == 'Welcome':
#         import welcome
#         welcome.welcome()

#     elif selected == 'Disease & Breed Detection':
#         import model
#         model.model()

#     elif selected == 'Petcare ChatBot':
#         import chatbot
#         chatbot.chatbot()

#     elif selected == 'Prescription-Analyzer':
#         import prescription
#         prescription.presc_analyze()

#     elif selected == 'Feedback':
#         import feedback
#         feedback.feedback()

#     elif selected == 'Team Details':
#         import team
#         team.team_details()

#     elif selected == 'Logout':
#         login.logout()
#         login.login()  # Refresh the app after logging out
    
#     elif selected =='find_veternary':
#         import fl1
#         fl1.fn1()





#-------------------------------


import streamlit as st
from streamlit_option_menu import option_menu
import login

st.set_page_config(
    page_title="Medi-Chain",
    page_icon="🐾",
    layout="centered",
    initial_sidebar_state="auto"
)

# Initialize session state for login and signup page selection
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'signup_selected' not in st.session_state:
    st.session_state['signup_selected'] = False

# Display login or signup form based on selection and login status
if not st.session_state['logged_in']:
    if st.session_state['signup_selected']:
        login.signup()
        if st.button("Already have an account? Login here"):
            st.session_state['signup_selected'] = False
    else:
        login.login()
        if st.button("Don't have an account? Sign up here"):
            st.session_state['signup_selected'] = True
else:
    # Display sidebar with options when logged in
    with st.sidebar:
        selected = option_menu(
            'Medi-Chain',
            ['Welcome', 'Disease & Breed Detection', 'Petcare ChatBot', 'Prescription-Analyzer', 'Team Details',
             'Feedback','find_veternary', 'Add Animal', 'Logout'],
            icons=['house-door-fill', 'search', 'chat-right-fill', 'file-earmark-break-fill', 'info', 'star',
                   'plus-circle', 'box-arrow-right'],
            menu_icon="🐶",
            default_index=0
        )

    # Render the appropriate page based on selection
    if selected == 'Welcome':
        import welcome
        welcome.welcome()

    elif selected == 'Disease & Breed Detection':
        import model
        model.model()

    elif selected == 'Petcare ChatBot':
        import chatbot
        chatbot.chatbot()

    elif selected == 'Prescription-Analyzer':
        import prescription
        prescription.presc_analyze()

    elif selected == 'Feedback':
        import feedback
        feedback.feedback()

    elif selected == 'Team Details':
        import team
        team.team_details()

    elif selected == 'Add Animal':
        import add_animal
        add_animal.add_animal()

    elif selected == 'Logout':
        login.logout()
        st.session_state['logged_in'] = False  # Reset login state
        st.session_state['signup_selected'] = False  # Reset signup state
        login.login() # Refresh the app after logging out
    
    elif selected =='find_veternary':
        import fl1
        fl1.fn1()