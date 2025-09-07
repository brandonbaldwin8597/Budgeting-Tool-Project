import streamlit as st
import pandas as pd

## TITLE
st.title("BUDGETING TOOL")


## SIDEBAR
st.sidebar.title("Your Finances:")

st.sidebar.subheader("Income")
income_type = st.sidebar.radio("Are you payed Hourly or Salary?", ('Hourly', 'Salary'))

if income_type == 'Hourly':
    income_M = st.sidebar.number_input("What is your HOURLY income?", step=0.25)
    income = f"{(income_M * 40 * 4):.2f}"
else:  
    income_A = st.sidebar.number_input("What is your ANNUAL income?", step=500.00)
    income = f"{(income_A / 12):.2f}"
    
st.sidebar.write("Rough Monthly Income: " + str(income))
    

## BODY
st.header("Bills Breakdown by MONTH")

st.subheader("First Bill -")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        bill1 = st.text_input("Enter 1st bill NAME:", placeholder="bill 1")
    with col2:
        bill1_amount = st.number_input("Enter 1st bill AMOUNT:")
        
st.subheader("Second Bill -")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        bill2 = st.text_input("Enter 2nd bill NAME:", placeholder="bill 2")
    with col2:
        bill2_amount = st.number_input("Enter 2nd bill AMOUNT:")
        
st.subheader("Third Bill -")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        bill3 = st.text_input("Enter 3rd bill NAME:", placeholder="bill 3")
    with col2:
        bill3_amount = st.number_input("Enter 3rd bill AMOUNT:")

df = pd.DataFrame(
    [
        {"Bill Name": bill1, "Bill Amount": bill1_amount},
        {"Bill Name": bill2, "Bill Amount": bill2_amount},
        {"Bill Name": bill3, "Bill Amount": bill3_amount}
    ]
    ,index=[1, 2, 3]
)
st.dataframe(df)


## SUMMARY
st.subheader("How much can you save with current salary and bills?")
st.write("Find out now")


total_bills = bill1_amount + bill2_amount + bill3_amount
savings = round((float(income) - total_bills), 2)

if st.button("Calculate"):
    st.write("total monthly income: $" + str(income))
    st.write("total bills amount: $" + str(total_bills))
    if savings < 500:
        st.error(f"Total Savings: ${savings}")
    elif savings < 1500 and savings >= 500:
        st.warning(f"Total Savings: ${savings}")
    elif savings >= 1500:
        st.success(f"Total Savings: ${savings}")