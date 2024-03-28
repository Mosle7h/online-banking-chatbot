# Predefined questions and answers
banking_qa = {
    "balance": "Your current account balance is $5000.",
    "transfer": "Sure, please provide the recipient's account number and the amount you'd like to transfer.",
    "transaction history": "You can view your transaction history by logging into your online banking account.",
    "open account": "To open an account, please visit our nearest branch with your identification documents.",
    "close account": "Account closure requests are usually processed at our branch offices. Please visit one for assistance.",
    "interest rates": "Our current interest rates are as follows: Savings Account - 1.5%, Fixed Deposit - 2.0%, Loan - 6.5%.",
    "loan application": "To apply for a loan, you can fill out an online application form on our website or visit our branch office.",
    "credit card application": "You can apply for a credit card by visiting our branch office and filling out an application form.",
    "lost card": "If your card is lost or stolen, please contact our customer service immediately to block the card and request a replacement.",
    "change pin": "You can change your PIN at any of our ATMs or by visiting our branch office.",
    "help": "How can I assist you today?",
    "exit": "Thank you for using our banking services. Have a great day!"
}

# Function to interact with the user
def banking_chatbot():
    print("Welcome to our banking chatbot!")
    print("Our chat bot can help you with queries such as\n1)Balance\n2)Transfer\n3)Transaction history\n4)Open account\n5)Close account\n6)Interest rates\n7)Loan application\n8)Credit card application\n9)lost card\n10)change pin\n11)Help\n12)Exit")
    print("How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("Banking Chatbot: " + banking_qa["exit"])
            break
        elif user_input in banking_qa:
            print("Banking Chatbot: " + banking_qa[user_input])
        else:
            print("Banking Chatbot: I'm sorry, I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    banking_chatbot()
