# Import the necessary modules and functions
from Search_From_CSV import Search_For_Matches  # Assuming Search_From_CSV contains a function to search for matches
import streamlit as st  # Streamlit library for creating a web application
import streamlit_authenticator as stauth
import pandas as pd  # Pandas library for data manipulation
import pickle
from pathlib import Path
def main():
    #USER Authintication 
    names = ['Akmal','Menna']
    usernames = ['Akmal','Menna']

    file_path = Path(__file__).parent / "hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    credentials = {
            "usernames":{
                usernames[0]:{
                    "name":names[0],
                    "password":hashed_passwords[0]
                    },
                usernames[1]:{
                    "name":names[1],
                    "password":hashed_passwords[1]
                    }            
                }
            }

    authenticator = stauth.Authenticate(credentials,"Loan_CSV", "xyz", cookie_expiry_days=0)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status:
        desired_value = st.text_input('Enter the Loan ID:')

        # Set the title of the web application
        st.title('LOAN Details Searcher')
        # Check if the 'Search' button is clicked
        if st.button('Search'):
            if desired_value:
                # Call the Search_For_Matches function to find matches
                result = Search_For_Matches(desired_value)

                # Check if the result is a Pandas DataFrame
                if isinstance(result, pd.DataFrame):
                            # Display matching codes if found
                    st.write('Matching Loan:')
                    st.write(result)
                else:
                            # Display an error message if there was an issue with the search
                    st.write(result)
            else:
                    # Display a warning if the user didn't provide any input
                st.warning('Please Fill all required entries')
    elif authentication_status == False:
        st.error('Username/password is incorrect')
    elif authentication_status == None:
        st.warning('Please enter your username and password')
    authenticator.logout('Logout','main')
    
main()