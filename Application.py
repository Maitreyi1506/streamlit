import streamlit as st
import base64

# Store passwords and their corresponding messages
PASSWORDS_before = {
    "teal12345": "These kinds of messages should be viewed before opening said gift.",
    "password3": "This is the message for password3.",
}

PASSWORDS_after = {
    "teal23456": "These kinds of messages should be viewed after opening said gift.",
}

# Session state to track if guidelines are accepted
if "guidelines_accepted" not in st.session_state:
    st.session_state.guidelines_accepted = False

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "selected_text" not in st.session_state:
    st.session_state.selected_text = None

# Function to display guidelines
def show_guidelines():
    st.title("Welcome to your Gifts Galore Bonanza Shaboinboing")
    st.write("""This website exists to soft launch Birthday week. \n
             Kindly do not fall in nsfec over this website (no matter how difficult it may be). \n
             Go through the following guidelines for your own safety""")
    st.title("Guidelines")
    st.write("""
    Please read and agree to the following guidelines before proceeding:
    1. Always follow the instructions given on this page. (And by a certain medium ugly womanly figure)
    2. Everytime the user receives a parcel labelled "Om Kamal Morendha" the following steps are to be followed:\n
        - Ask the hottest woman on the planet for a password.\n
        - She will return a 5 digit numeric code.
    3. Enter the password in the form of XXXXNNNNN \n
        - where: XXXX -> letters corresponding to a certain woman's favourite colour(in lowercase) and \n
        - NNNNN -> the five numerals provided. 
    4. You will then be directed to a page which shows one of two prompts:\n "AFTER OPENING" or "BEFORE OPENING".
    5. Click on the button corresponding to the prompt you see. \n
        - If you see "BEFORE OPENING", you will be shown a message that should be viewed before opening the gift. [Try "12345" for a test run]\n
        - If you see "AFTER OPENING", you will be shown a message that should be viewed after opening the gift. [Try "23456" for a test run]
    6. If you have any questions or concerns, please contact the administrator.
    7. Do not share your password with anyone else.
    8. This website is for personal use only and should not be shared publicly.
    9. By clicking "I Agree" [you dont have a choice ngl], you acknowledge that you have read and understood these guidelines.
    """)
    if st.button("I Agree"):
        st.session_state.guidelines_accepted = True

# Function to authenticate user
def authenticate():
    st.title("Password Prompt")
    password = st.text_input("Enter your password:", type="password")
    if st.button("Submit"):
        if password in PASSWORDS_before:
            st.session_state.authenticated = True
            st.session_state.message = PASSWORDS_before[password]
            st.session_state.selected_text = "Before Opening"
        elif password in PASSWORDS_after:
            st.session_state.authenticated = True
            st.session_state.message = PASSWORDS_after[password]
            st.session_state.selected_text = "After Opening"
        else:
            st.error("Invalid password. Please try again.")

# Function to display the main page
def main_page():
    # Add "View Guidelines" button to the sidebar
    with st.sidebar:
        st.markdown(
            """
            <style>
            .sidebar-button {
                background-color: #f63366;
                color: white;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                cursor: pointer;
                text-align: center;
                display: inline-block;
                margin: 10px 0;
            }
            .sidebar-button:hover {
                background-color: #ff4b82;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        if st.button("View Guidelines", key="sidebar_button"):
            st.session_state.guidelines_accepted = False
    
    st.title("Your Instruction: ")
    
    # Add custom CSS for the central buttons
    st.markdown(
        """
        <style>
        .central-button {
            display: block;
            margin: 20px auto;
            background-color: #ff69b4;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            padding: 15px 30px;
            cursor: pointer;
            text-align: center;
            width: 200px;
        }
        .central-button:hover {
            background-color: #ff85c1;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    button_text = st.session_state.selected_text
    if button_text == "Before Opening":
        if st.button("Before Opening", key="before_button"):
            st.write(st.session_state.message)
    elif button_text == "After Opening":
        if st.button("After Opening", key="after_button"):
            st.write(st.session_state.message)
    else:
        st.error("Invalid state. Please restart the application.")

# Function to set a background image
def set_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.9), rgba(255, 255, 255, 0.3)), 
                        url("data:image/avif;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
# set_background_image("https://www.google.com/search?q=birthday+themed+image&rlz=1C5GCEM_enIN1125IN1127&oq=birthday+themed+image&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABixAxiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIKCAYQABjJAxiABDIKCAcQABiSAxiABDIHCAgQABiABDIHCAkQABiABNIBCDQ3NzJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#vhid=xQxdzPxEfbYYMM&vssid=_-UkPaI6dOfeF4-EP3MiO8Ao_38:~:text=https%3A//images.app.goo.gl/AgqgpeVseJExVq1A9")
set_background_image("bday_image.avif")

# Main application logic
if not st.session_state.guidelines_accepted:
    show_guidelines()
elif not st.session_state.authenticated:
    authenticate()
else:
    main_page()
