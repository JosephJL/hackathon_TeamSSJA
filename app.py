from typing_extensions import Annotated
import streamlit as st

#-------------------------------------------------#
st.set_page_config(page_title='Spend and Save!',
                   layout='wide')
st.write('# **Spend and Save - Your financial safeguarder!**')

page_directory = st.sidebar.radio('Page Navigation' ,('Getting started', 'Main Page', 'Payment options', 'Invest', 'Loan' , 'Donate'))

if 'count' not in st.session_state:
	st.session_state.count = 0

if page_directory == 'Getting started':
    st.write('Welcome to Spend and Save, your financial safeguarder! Spend and Save is your one stop service for payment, investing, donations and loans.')
    st.write('Lets get to know each other! Answer the following questions to give us a better gauge of your financial situation.')

    name = st.text_input("What is your name?", value = "Your name.", key='name')

    current_balance = st.text_input("Enter your current balance", value = "Your current balance ($)", key="current_balance")

    current_savings = st.text_input("Enter your current savings", value = "Your current savings ($)", key = "current_savings")

    savings_goal = st.text_input("Enter your savings goal", value = "Your savings goal ($)", key= 'savings_goal')
    
elif page_directory == 'Main Page':
    st.header('Spend and Save: Financial overview')

    try:
        st.write(f'**Welcome Back {st.session_state.name}!**' )
        st.write(f'Your current balance is ${st.session_state.current_balance}')

        st.write(f'You have saved ${st.session_state.current_savings} out of ${st.session_state.savings_goal}')

        percentage_savings_goal = (float(st.session_state.current_savings)/float(st.session_state.savings_goal))

        st.progress(percentage_savings_goal)
        st.write(f'You have achieved {round(percentage_savings_goal*100,2)}% of your savings goal. ')

        st.write('**Head on over to the side bar to navigate to the payment, investing and donation options!**')
    except:
        st.error('ERROR: Head on over to the getting started page to input all the required information on your current financial situation!') 
        st.stop() 


elif page_directory == 'Payment options':
    st.write('### Scan to Pay')
    try: 

        payment_amount = st.text_input("Enter the payment amount ($).", value = "Your payment amount ($)", key = 'payment_amount')

        payment_amount2 = float(payment_amount)

        saving_amount = st.text_input("Enter the savings amount ($). We automatically configure the savings amount to be 10% of your expenditure. You may edit it if you wish!", value = 0.1*
        payment_amount2, key = 'saving_amount')    

    except:
        st.error('Enter the desired payment amount to get started with payment.') 
        st.stop() 

    if st.button('pay'):
        if float(st.session_state.current_balance) < float(st.session_state.payment_amount) :

            st.write(f'Your Current balance is ${st.session_state.current_balance}')
            st.write('There are insufficient funds to complete the payment.')

        else: 
            st.session_state.current_balance = str( float(st.session_state.current_balance) - float(st.session_state.payment_amount) )

            st.session_state.current_savings = str( float(st.session_state.current_savings) + float(st.session_state.saving_amount) )

            st.write('**Successful payment!**')
            st.write(f'Your remaining balance is ${ st.session_state.current_balance}.')
            st.write(f'Your new savings balance is ${ st.session_state.current_savings}')

#elif page_directory == 'Loan':

            
