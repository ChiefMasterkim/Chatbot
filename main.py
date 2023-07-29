import streamlit as st
import numpy as np
import random
import time

st.title("Whatsapp marketing bot")


#initialize the chat history

if "messages" not in st.session_state:
    st.session_state.messages = []


# displaying chat messagwes from history

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


#accept user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({'role':'user', 'content':prompt})
    with st.chat_message("User"):
        st.markdown(prompt)


#assistant message 
    with st.chat_message('assistant'):
        message_placeholder = st.empty()
        full_response = " "
        assistant_response = random.choice(
            [
               "שלום לך היום!, אני עדיין בבנייה והתפקיד שלי הוא לעבוד כעוזרת שלך ולספק לך הודעה על הזדמנויות הנסיעה הטובות ביותר בעיר שצוינה, אני יכול לעבוד בוואטסאפ ובטלגרם",
                "How are you? I'm still under construction , resend another message so i can respond in hebrew",
            ]
        )
        #simulate the time
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + " ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant", "content": full_response})
