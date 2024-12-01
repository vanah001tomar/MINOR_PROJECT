import streamlit as st
from streamlit_option_menu import option_menu
import login
import joblib

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
            ['Welcome', 'Disease & Breed Detection', 'Petcare ChatBot', 'Prescription-Analyzer',
             'Check Severity', 'Team Details', 'Feedback', 'Add Animal', 'Logout'],
            icons=['house-door-fill', 'search', 'chat-right-fill', 'file-earmark-break-fill',
                   'thermometer-half', 'info', 'star', 'plus-circle', 'box-arrow-right'],
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

    elif selected == 'Check Severity':
        st.title("Check Disease Severity")
        st.write("Enter the symptoms for the animal:")

        # Hybrid approach: Dropdown + Custom Input
        symptom_1 = st.selectbox("Symptom 1", options=["Choose an option", "Fever", "Coughing", "Vomiting", "Other"])
        if symptom_1 == "Other":
            symptom_1 = st.text_input("Specify Symptom 1", placeholder="Type your symptom here...")

        symptom_2 = st.selectbox("Symptom 2", options=["Choose an option", "Diarrhea", "Fatigue", "Loss of Appetite", "Other"])
        if symptom_2 == "Other":
            symptom_2 = st.text_input("Specify Symptom 2", placeholder="Type your symptom here...")

        symptom_3 = st.selectbox("Symptom 3", options=["Choose an option", "Weight Loss", "Sneezing", "Seizures", "Other"])
        if symptom_3 == "Other":
            symptom_3 = st.text_input("Specify Symptom 3", placeholder="Type your symptom here...")

        symptom_4 = st.selectbox("Symptom 4", options=["Choose an option", "Dehydration", "Lethargy", "Pain", "Other"])
        if symptom_4 == "Other":
            symptom_4 = st.text_input("Specify Symptom 4", placeholder="Type your symptom here...")

        symptom_5 = st.selectbox("Symptom 5", options=["Choose an option", "Anemia", "Joint Pain", "Coughing", "Other"])
        if symptom_5 == "Other":
            symptom_5 = st.text_input("Specify Symptom 5", placeholder="Type your symptom here...")

        # Load the trained model and vectorizer
        if st.button("Check Severity"):
            try:
                # Load model and vectorizer once to avoid reloading on every click
                model = joblib.load("severity_model.pkl")
                vectorizer = joblib.load("symptom_vectorizer.pkl")  # Ensure the vectorizer is loaded
                
                symptoms = [symptom_1, symptom_2, symptom_3, symptom_4, symptom_5]
                symptoms_str = ' '.join(symptoms)  # Combine symptoms into one string

                # Vectorize the input symptoms using the same vectorizer
                symptoms_encoded = vectorizer.transform([symptoms_str])  # Vectorize input text

                # Ensure that only 5 features are passed to the model
                if symptoms_encoded.shape[1] == 5:  # Expecting 5 features, not 1111
                    prediction = model.predict(symptoms_encoded)[0]
                    
                    st.write(f"The disease is predicted to be **{'Dangerous' if prediction == 'Yes' else 'Not Dangerous'}**.")
                else:
                    st.error(f"The input symptoms do not match the expected number of features. Expected 5, but got {symptoms_encoded.shape[1]}")
            except Exception as e:
                st.error("Error loading the model or processing the input. Please check the implementation.")
                st.exception(e)

    elif selected == 'Team Details':
        import team
        team.team_details()

    elif selected == 'Add Animal':
        import add_animal
        add_animal.add_animal()

    elif selected == 'Feedback':
        import feedback
        feedback.feedback()

    elif selected == 'Logout':
        login.logout()
        st.session_state['logged_in'] = False  # Reset login state
        st.session_state['signup_selected'] = False  # Reset signup state
        login.login()  # Refresh the app after logging out
