import streamlit as st
from joblib import load
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# Set the page configuration
st.set_page_config(
    page_title="credit card defaulter prediction app",
    page_icon=":guardsman:",  # You can use an emoji or a custom icon
    layout="wide",  # Options: 'centered', 'wide'
    initial_sidebar_state="auto",  # Options: 'auto', 'expanded', 'collapsed'
    
)


# Set the title of the app
st.title("Welcome to CREDIT CARD DEFAULTERS :rocket:")
# Load the model
model = load("gnb_credit_card_model.joblib")
st.sidebar.header("Model Prediction :-")
st.sidebar.image("https://chargebacks911.com/wp-content/uploads/2023/04/Detecting-Credit-Card-Fraud-fb.jpg")
st.sidebar.warning("""* Application is for educational purposes only. Please do not use it for real transactions.\n * The model is trained on a dataset and may not reflect real-world scenarios.\n* Always verify predictions with domain experts before making decisions.""")
st.sidebar.markdown("### About the Model :-") 
st.sidebar.markdown("This app uses a Gaussian Naive Bayes model to predict credit card fraud.")      




   
# Input features
st.markdown("### Please enter the following details to predict credit card defaulter:")
ltbal = st.number_input("LIMIT_BAL", min_value=10000.0, max_value=1000000.0, value=10000.0, step=10000.0, key="feature1")

user_gender = st.selectbox("SEX",[1,2], index=0, key="feature2")
if user_gender == 1:
    st.write("You selected : Male")
else:
    st.write("You selected : Female")

educ = st.selectbox("EDUCATION", [1,2,3,4,5,6], key="feature3")
marriage = st.selectbox("MARRIAGE", [1,2,3], key="feature4")
age = st.number_input("AGE", min_value=21.0, max_value=79.0, value=25.0, step=1., key="feature5")
pay1 =st.number_input("PAY_1", min_value=-2.0, max_value=8.0, value=0., step=1.0, key="feature6")
pay2 =st.number_input("PAY_2", min_value=-2.0, max_value=8.0, value=0.0, step=1.0, key="feature7")
pay3 =st.number_input("PAY_3", min_value=-2.0, max_value=8.0, value=0.0, step=1.0, key="feature8" )
pay4 =st.number_input("PAY_4", min_value=-2.0, max_value=8.0, value=0.0, step=1.0, key="feature9")
pay5 =st.number_input("PAY_5", min_value=-2.0, max_value=8.0, value=0.0, step=1.0, key="feature10")
pay6 =st.number_input("PAY_6", min_value=-2.0, max_value=8.0, value=0.0, step=1.0, key="feature11")
bilamt1 = st.number_input("BILL_AMT1", min_value=-165580.0, max_value=964511.0, value=800000.0, step=100000.0, key="feature12")
bilamt2 =st.number_input("BILL_AMT2", min_value=-69777.0, max_value=983931.0, value=800000.0, step=100000.0, key="feature13")
bilamt3 =st.number_input("BILL_AMT3", min_value=-157264.0, max_value=1664089.0, value=800000.0, step=100000.0, key="feature14")
bilamt4 =st.number_input("BILL_AMT4", min_value=-170000.0, max_value=891586.0, value=800000.0, step=100000.0, key="feature15")
bilamt5 =st.number_input("BILL_AMT5", min_value=-81334.0, max_value=927171.0, value=800000.0, step=100000.0, key="feature16")
bilamt6 =st.number_input("BILL_AMT6", min_value=-339603.0, max_value=961664.0, value=800000.0, step=100000.0, key="feature17")
pyamt1 = st.number_input("PAY_AMT1", min_value=0.0, max_value=873552.0, value=1000.0, step=1000.0, key="feature18")
pyamt2 =st.number_input("PAY_AMT2", min_value=0.0, max_value=1684259.0, value=1000.0, step=1000.0, key="feature19")
pyamt3 =st.number_input("PAY_AMT3", min_value=0.0, max_value=896040.0, value=1000.0, step=1000.0, key="feature20")
pyamt4 =st.number_input("PAY_AMT4", min_value=0.0, max_value=621000.0, value=1000.0, step=1000.0, key="feature21")
pyamt5 =st.number_input("PAY_AMT5", min_value=0.0, max_value=426529.0, value=1000.0, step=1000.0, key="feature22")
pyamt6 =st.number_input("PAY_AMT6", min_value=0.0, max_value=528666.0, value=1000.0, step=1000.0, key="feature23")

input = [ltbal,user_gender,educ,marriage,age,pay1,pay2,pay3,pay4,pay5,pay6,
         bilamt1,bilamt2,bilamt3,bilamt4,bilamt5,bilamt6,
         
         pyamt1,pyamt2,pyamt3,pyamt4,pyamt5,pyamt6
]


# Define a function to predict the class of the input data

def predict(input):
    """Predict the class of the input data using the pre-trained model."""
        
    if input:
        st.write(f"my input values to predict : {input}")
        # Scale the input using the scaler
        scaled_input = scaler.fit_transform([input])
        prediction = model.predict(scaled_input)
        return prediction[0]
    else:
        st.error("Please provide all input values before making a prediction.")
        return None

st.markdown("""
    <style> 
     .center-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    

    div.stButton > button:first-child {
        background-color: blue;  /* Green */
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        align-items: center;
        justify-content: center;
        cursor: pointer;
    }

    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

#
if __name__ == '__main__':
    if st.button("Predict"):
        predicts = predict(input)
        if predicts > 0.80        st.success("The transaction is not fraudulent. ✅")
            st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEoepJUqvJlc2vpBLQckFpVDfDCoclISv3Tg&s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True)
        else:
            st.error("The transaction is fraudulent. ⚠️")
            st.warning("Please check the transaction details and take necessary actions.⏩")
            # st.image("https://www.onlygfx.com/wp-content/uploads/2020/05/alert-stamp-1.png", use_column_width=True)
            st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.onlygfx.com/wp-content/uploads/2020/05/alert-stamp-1.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: semired; /* Semi-transparent red background */
    }
    </style>
    """,
    unsafe_allow_html=True)


