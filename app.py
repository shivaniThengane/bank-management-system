import streamlit as st
from hello import Bank


st.set_page_config(
    page_title="SecureBank",
    page_icon="🏦",
    layout="wide"
)



def home():

    st.markdown(
    """
    <style>

    .hero{
        background:#0F4C81;
        padding:40px;
        border-radius:15px;
        color:white;
        text-align:center;
    }


    </style>
    """,
    unsafe_allow_html=True
    )


    st.markdown(
    """
    <div class="hero">

    <h1>🏦 SecureBank</h1>

    <h3>
    Digital Banking Management System
    </h3>

    </div>
    """,
    unsafe_allow_html=True
    )


    st.write("")

    col1,col2,col3 = st.columns(3)


    with col1:
        st.info("👤 Create Account")


    with col2:
        st.success("💰 Easy Transactions")


    with col3:
        st.warning("🔐 Secure Data")



    st.divider()


    st.subheader("Features")

    st.write(
    """
    ✅ Account Creation

    ✅ Deposit Money

    ✅ Withdraw Money

    ✅ Account Details

    ✅ Update Profile

    ✅ Delete Account
    """
    )




def create_account():

    st.header("Create New Account")


    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=18
    )

    email = st.text_input("Email")

    pin = st.text_input(
        "4 Digit PIN",
        type="password"
    )


    if st.button("Create"):

        if len(pin)==4:

            user,msg = Bank.create_account(
                name,
                age,
                email,
                int(pin)
            )

            st.success(msg)

            st.info(
                f"Account Number: {user['accountNo.']}"
            )

        else:

            st.error("PIN must be 4 digits")





def deposit():

    st.header("Deposit Money")


    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )


    if st.button("Deposit"):

        success,msg = Bank.deposit(
            acc,
            int(pin),
            amount
        )


        if success:
            st.success(msg)

        else:
            st.error(msg)





def withdraw():

    st.header("Withdraw Money")


    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )


    if st.button("Withdraw"):

        success,msg = Bank.withdraw(
            acc,
            int(pin),
            amount
        )


        if success:
            st.success(msg)

        else:
            st.error(msg)





def details():

    st.header("Account Details")


    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )


    if st.button("Show"):

        user = Bank.find_user(
            acc,
            int(pin)
        )


        if user:
            st.json(user)

        else:
            st.error("Account not found")





def update():

    st.header("Update Information")


    acc = st.text_input("Account Number")

    pin = st.text_input(
        "Current PIN",
        type="password"
    )


    name = st.text_input("New Name")

    email = st.text_input("New Email")

    new_pin = st.text_input("New PIN")


    if st.button("Update"):


        success,msg = Bank.update_user(
            acc,
            int(pin),
            name,
            email,
            new_pin
        )


        if success:
            st.success(msg)

        else:
            st.error(msg)





def delete():

    st.header("Delete Account")


    acc = st.text_input("Account Number")

    pin = st.text_input(
        "PIN",
        type="password"
    )


    if st.button("Delete"):


        success,msg = Bank.delete_user(
            acc,
            int(pin)
        )


        if success:
            st.success(msg)

        else:
            st.error(msg)





# Sidebar

st.sidebar.title("SecureBank")


choice = st.sidebar.selectbox(
    "Menu",
    [
        "Home",
        "Create Account",
        "Deposit",
        "Withdraw",
        "Account Details",
        "Update Info",
        "Delete Account"
    ]
)



st.title("🏦 Bank Management System")


if choice=="Home":
    home()

elif choice=="Create Account":
    create_account()

elif choice=="Deposit":
    deposit()

elif choice=="Withdraw":
    withdraw()

elif choice=="Account Details":
    details()

elif choice=="Update Info":
    update()

elif choice=="Delete Account":
    delete()