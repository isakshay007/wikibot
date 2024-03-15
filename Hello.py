import openai
import os
from PIL import Image
import streamlit as st
from lyzr import ChatBot
#import nest_asyncio

openai.api_key= st.secrets["apikey"]
#os.environ['OPENAI_API_KEY'] = st.secrets["apikey"]

# Apply nest_asyncio
#nest_asyncio.apply()

# Create a temporary directory if it doesn't exist
#if not os.path.exists('tempDir'):
    #os.makedirs('tempDir')

# Setup your config
st.set_page_config(
    page_title="WikiBot",
    layout="centered",  # or "wide" 
    initial_sidebar_state="auto",
    page_icon="lyzr-logo-cut.png"
)

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    .button-group { display: flex; justify-content: space-between; }
    .button { flex: 1; margin: 0 0.5rem; }
    </style>
    """, unsafe_allow_html=True)

# Call the function to apply the styles
style_app()

# Load and display the logo
image = Image.open("lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("WikiBot")
st.markdown("### Welcome to WikiBot! 🤖")
st.markdown("Interact with Wikipedia Through Chatbots (built using LYZR SDK)")

# Define function to initialize chatbot
def initialize_chatbot(url):
    # Replace these parameters with your actual Weaviate Vector Store parameters
    vector_store_params = {
        "vector_store_type": "WeaviateVectorStore",
        "url": "https://wikibot-zn4f2emj.weaviate.network",
        "api_key": "JKkfz6V0kxYa3WX40FdyiFf2DDTM3GlAIyTT",
        "index_name": "Akshay"
    }
    # Initialize the Webpage Chatbot with the provided URL
    return ChatBot.webpage_chat(
        url=url,
        vector_store_params=vector_store_params
    )

# Main function to run the Streamlit app
def main():
    # User input for URL
    url = st.text_input("Enter the URL of the webpage:")
    
    # Check if URL is provided
    if url:
        # Initialize the chatbot with the provided URL
        chatbot = initialize_chatbot(url)
        
        # Pre-prompt section with buttons
        st.markdown("### Choose Your Option")
        option = st.radio("Select an option:", ["Pre-defined Prompts", "Enter Your Own Question"])
        
        # Handle pre-defined prompts
        if option == "Pre-defined Prompts":
            st.markdown("### Pre-defined Prompts")
            prompts = [
                "What is the summary of this page?",
                "Can you explain the history of this topic?",
                "Who are the notable figures related to this topic?",
                "What are the controversies surrounding this topic?"
            ]
            
            # Create buttons for each prompt
            col1, col2 = st.columns(2)
            for i, prompt in enumerate(prompts):
                if i % 2 == 0:
                    button = col1.button(prompt, key=f"button_{i}")
                else:
                    button = col2.button(prompt, key=f"button_{i}")
                
                # Check if button is clicked
                if button:
                    # Chat with the chatbot
                    response = chatbot.chat(prompt)
                    
                    # Display chatbot's response
                    st.write("Chatbot's Response:")
                    st.write(response.response)
                    
                    # Display source nodes for additional information
                    #st.write("Source Nodes:")
                    #for n, source in enumerate(response.source_nodes):
                        #st.write(f"Source {n+1}: {source.text}")
        
        # Handle user's own question
        elif option == "Enter Your Own Question":
            user_question = st.text_input("Enter your question:")
            
            # Chat with the chatbot
            if user_question:
                response = chatbot.chat(user_question)
                
                # Display chatbot's response
                st.write("Chatbot's Response:")
                st.write(response.response)
                
                # Display source nodes for additional information
                #st.write("Source Nodes:")
                #for n, source in enumerate(response.source_nodes):
                    #st.write(f"Source {n+1}: {source.text}")

# Run the Streamlit app
if __name__ == "__main__":
    main()

# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown("""
    This app uses Lyzr Core to generate notes from transcribed audio. The audio transcription is powered by OpenAI's Whisper model. For any inquiries or issues, please contact Lyzr.
    
    """)
    st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
    st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
    st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
    st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)
