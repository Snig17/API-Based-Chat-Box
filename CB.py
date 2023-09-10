import streamlit as st
import openai

st.title("ChAT BOX !!!")
st.sidebar.header("Hey!!! Welcome to chatbox")
st.sidebar.info(
    '''Chatbox refers to the interface that allows users to interact with a chat application. It typically appears as a small window or pop-up on a website and includes a text input field for the user to type in their message and a button to initiate the chat with an AI chatbot or a live agent. Chatboxes are often used for customer service, technical support, or sales inquiries. They can also include features such as quick selection options, file sharing, and the ability for the representative to initiate the chat.
       '''
    )




# Set the model engine and your OpenAI API key
model_engine = "text-davinci-003"
openai.api_key = "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" #follow step 4 to get a secret_key


def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter query here, to exit enter :q", "")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")

def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine =model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    response = completion.choices[0].text
    return response


 # call the main function
main()            