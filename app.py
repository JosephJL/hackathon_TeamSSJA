import streamlit as st
from PIL import Image
import pandas as pd

#-------------------------------------------------#
st.set_page_config(page_title='Spend and Save!',
                   layout='wide')
st.write('# **Spend and Save - Your financial safeguarder!**')

page_directory = st.sidebar.radio('Page Navigation' ,('Getting started', 'Main Page - Financial overview', 'Payment options', 'Invest and grow your funds', 'Peer to Peer loans' , 'Donate and help a person.'))

if 'donation_amount' not in st.session_state:
    st.session_state.donation_amount = '300' #Used for donation
if 'donate_total' not in st.session_state:
    st.session_state.donate_total = '30' #Used for donation leaderboard

if 'donate' not in st.session_state: 
    st.session_state.donate = '0'

if 'loan_amount' not in st.session_state: 
    st.session_state.loan_amount = '400'


if page_directory == 'Getting started':
    st.write('Welcome to Spend and Save, your financial safeguarder! Spend and Save is your one stop service for payment, investing, donations and loans.')
    st.write('Lets get to know each other! Answer the following questions to give us a better gauge of your financial situation.')

    name = st.text_input("What is your name?",  key='name')

    current_balance = st.text_input("Enter your current balance", key="current_balance")

    current_savings = st.text_input("Enter your current savings", key = "current_savings", value = 0)

    savings_goal = st.text_input("Enter your savings goal", key= 'savings_goal', value = 0)
    
    st.write('**Head on over to the side bar to navigate to the payment, investing and donation options!**')

elif page_directory == 'Main Page - Financial overview':
    st.header('Spend and Save: Financial overview')

    try:
        st.write(f'**Welcome Back {st.session_state.name}!**' )
        st.write(f'Your current balance is ${st.session_state.current_balance}')

        st.write(f'You have saved ${st.session_state.current_savings} out of ${st.session_state.savings_goal}')

        percentage_savings_goal = (float(st.session_state.current_savings)/float(st.session_state.savings_goal))

        st.progress(percentage_savings_goal)
        st.write(f'You have achieved {round(percentage_savings_goal*100,2)}% of your savings goal. ')

        st.button('Withdraw savings', help = 'non-functional')

        st.write('**Head on over to the side bar to navigate to the payment, investing and donation options!**')
    except:
        st.error('ERROR: Head on over to the getting started page to input all the required information on your current financial situation!') 
        st.stop() 


elif page_directory == 'Payment options':
    st.write('### Scan to Pay')
    try: 
        payment_amount = st.text_input("Enter the payment amount ($).", key = 'payment_amount')

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

elif page_directory == 'Peer to Peer loans':
    st.write("# Peer to peer loaning")
    trust = 0.1
    st.write(f'Your current trust meter is {trust*100}%!')
    st.write('Increase your trust meter through successfully repaying your loans.')

    st.progress(trust)

    def loan_remainder():
        st.session_state.loan_amount = str(float(st.session_state.loan_amount) - float(st.session_state.loan_repayment))

        st.session_state.current_balance = str(float(st.session_state.current_balance) - float(st.session_state.loan_repayment))

    st.write(f'**Outstanding Loans: ${st.session_state.loan_amount}**')
    st.write(f'**Your current balance: ${st.session_state.current_balance}**')

    st.button('Pay off your loans', help = 'Non-functional')


    if st.checkbox(label = 'Apply for a new loan.'):
        st.write('To take on a new loan, create a new post about your situation, and user of the Spend And Save app might decide to give you a loan. \n A higher trustmeter gives you a higher chance of securing a loan \n \n')
        text_info = st.text_input('Tell us about why you need a loan, what you would use it for, and some details about yout repayment plan!')

        

        file = st.file_uploader("Upload an image illustrating your need for the loan. The image should be uploaded in jpg format.", type=['jpg'])

        if file is None:
            st.write('Waiting for image to be uploaded...') 
            st.stop() 

        else: 
            st.write(file)

    if st.checkbox(label = 'Become a lender: View lending options.'):
        st.write('**1. Loan needed to improve the productivity of my farming business...**')
        st.write('Sarah wants to expand her farming business and wants to take on a loan to fund the purchase of her tractor. With the tractor, Sarah will be able to increase her crop yield, and support her family and community.')
        st.write('**Loan amount needed: $50,000**')
        st.write('Annual interest rate: 10%.\n Repayment schedule: Monthly.')
        image = Image.open("tractor.jpg")
        st.image(image)
        st.button('Fund Now!!',help = 'Funding page will be developed later on')

        st.write("**2. Loan required to fund my childrens education...**")
        st.write('Sean wants to give his children a secondary school education. A secondary school education will drastically improve his childrens chances of a brighter future.')
        st.write('**Loan amount needed: $4000**')
        st.write('Annual interest rate: 10%.\n Repayment schedule: Monthly.')
        st.image(Image.open("education.jpg"))
        st.button('Fund Now!!!', help = 'Funding page will be developed later on' )            

elif page_directory == 'Invest and grow your funds':
    st.title("Welcome to Our Investment Page")
    st.write("\n")
    st.image(Image.open("stocks.jpg"))

    st.subheader("Please Choose your Preferred Risk Tolerance, and click on the links to learn more about the different type of investments.")
    st.write("\n")

    if st.button(label = "Low Risk",  help=" Click to find out more about Bonds, Treasurey Yields!"):
        link = '[More about Low Risk Invesments](https://www.bankrate.com/investing/low-risk-investments/)'
        st.markdown(link, unsafe_allow_html=True)

    if st.button(label = "Medium Risk", help="Click to find out more about Exchange Trade Funds!"): 
        link = '[More about Exchange Traded Funds](https://www.investopedia.com/articles/exchangetradedfunds/11/building-an-etf-portfolio.asp)'
        st.markdown(link, unsafe_allow_html=True)

    if st.button(label = "High Risk",  help="Click to find out more about Individual Stocks!"):
        link = '[More about Individual Stocks Picking](https://www.investopedia.com/articles/basics/11/how-to-pick-a-stock.asp)'
        st.markdown(link, unsafe_allow_html=True)
    st.write("\n")

    st.subheader("Try out our very own Investment Calculator below!")
    st.write("Please fill in all the blanks with numbers greater than 0s!")

    starting_amt = st.text_input("Enter your desired starting amount ($): ", value = 0)
    duration = st.text_input("Enter the duration you wish to invest for (years): ", value = 0)
    monthly_amt = st.text_input("Enter the amount you will be contributing every month ($): ", value = 0)

    compound_interest = float(starting_amt)*(((1+0.10)**float(duration))-1)
    total_return = compound_interest + float(starting_amt) + float(monthly_amt) * float(duration) * 12
    normal_return = float(starting_amt) + float(duration) * float(monthly_amt) * 12
    difference = abs(float(total_return)-float(normal_return))
    st.write(f"Your total return will be ***${round(total_return,2)}*** after investing for ***{duration} years*** with a ***starting amount of ${starting_amt}*** along with a ***${monthly_amt} monthly contribution***. \n This was calculated following the average annual 10% return of the index fund S&P 500 since its inception in 1926 till 2018.")
    st.write(f"With the same starting amount and monthly contribution, you would only receive ***${round(normal_return,2)}*** if you had left all your money in an ordinary savings account. You are losing out on a total difference of ***${round(difference,2)}!***")

    st.subheader("What are you waiting for? Click the button below to find out more!")
    st.button(label = "Invest with Us Now!", help ='Page will be developed later')

elif page_directory == 'Donate and help a person.':
    st.write('A donation during a critical time of need can make all the difference. Donate now, and change a persons life.')

    if st.checkbox(label = 'Request for donations.'):
        st.write('To request for a donation, create a new post about your situation, and a user of the Spend And Save app might decide to donate to help your cause. \n It is important to help others understand your situation, and how the donation will help.')
        text_info = st.text_input('Tell us about why you need a donation and what you would use it for.')

        file = st.file_uploader("Upload an image illustrating your need for the donation. The image should be uploaded in jpg format.", type=['jpg'])

        if file is None:
            st.write('Waiting for image to be uploaded...') 
            st.stop() 

        else: 
            st.write(file)
        
        st.button('Submit donation request', help = 'non-functional')

    if st.checkbox(label = 'Donate now: View donation options.'):
        st.write('**1. Donation needed to save my daughters life...**')
        st.write('Aarons child has been diagonsed with liver cancer, and requires intensive chemotherapy to survive. Donations are required to fund medical treatment to give his child a chance to live.')
        st.write('**Donation amount needed: $8,000**')

        
        image = Image.open("sick-child.jpg")
        st.image(image)
 
        try: 
            st.progress(float(st.session_state.donation_amount)/8000)
        except: 
            st.write('The donation goal has been reached! Thank you for your contribution.')

        st.write(f'**Current donation amount is ${st.session_state.donation_amount}**')

        
        def total_donation():
            st.session_state.donation_amount = float(st.session_state.donate) + float(st.session_state.donation_amount)
            st.session_state.donate_total += float(st.session_state.donate)
            st.session_state.current_balance = str(float(st.session_state.current_balance) - float(st.session_state.donate))

        if st.button('Donate Now!!') :

            donate = st.text_input('Input your donation amount', key = 'donate')

            if st.button('Confirm Donation',on_click = total_donation): 
            
                if float(st.session_state.current_balance) < float(st.session_state.donate) :
                    st.write(f'Your Current balance is ${st.session_state.current_balance}')
                    st.write('There are insufficient funds to complete the payment.')
                else: 
                    st.write('Thank you for your contribution! You have provided aid in a time of great need.')


        st.write('**2. Donation needed to build a home...**')
        st.write('Joseph is currently living in a shelter and requires a donation to buy the materials to build himself a home. The new home will give much needed shelter to his family. ')
        st.write('**Donation amount needed: $2,000**')

        
        image = Image.open("home.jpg")
        st.image(image)
        st.progress(0.999)
        st.write(f'**Current donation amount is 21000**')
        st.write('The donation goal has been reached! Thank you for your contribution.')
    
    st.write('**Donation leaderboard**')

    st.session_state.donate_total = float(st.session_state.donate_total) + float(st.session_state.donate)

    df = pd.DataFrame({
    'User': ["You", 'Aaron', 'Joseph', 'Sarah', 'Sean'],
    'Donated Amount': [st.session_state.donate_total, 10, 20, 30, 40]})

    st.write(df)







         





    
   


 





    
        
        



