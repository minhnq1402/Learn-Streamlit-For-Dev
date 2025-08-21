import streamlit as st
from huggingface_hub import InferenceClient 

st.title('Simple Chat Bot')

with st.sidebar:
    st.title('Hugging Face Setup')
    hf_api_token = st.text_input('Hugging Face API Token:', type='password')
    
    st.markdown("Take API [this](https://huggingface.co/settings/tokens).")
    
    selected_model = st.selectbox(
        'pick model:',
        ['mistralai/Mixtral-8x7B-Instruct-v0.1', 'mistralai/Mistral-7B-Instruct-v0.2', 'google/gemma-7b-it']
    )


if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Tôi có thể giúp gì cho bạn?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def generate_response(prompt_input, token, model):
    try:
        client = InferenceClient(model=model, token=token)
        response = client.chat_completion(
            messages=st.session_state.messages,
            max_tokens=256,
            stream=False,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
    
if prompt := st.chat_input(disabled=not hf_api_token):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    with st.chat_message("assistant"):
        with st.spinner("Suy Nghi..."):
            response = generate_response(prompt, hf_api_token, selected_model) 
            st.write(response)
    
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)