import streamlit as st

st.title('Minh Project')
st.header("this is a Header")
st.subheader('subheader')
st.text('IOT K68')
st.caption('Day la caption')
st.divider()

st.header("this is a Header")
st.subheader('subheader')
st.markdown('# Heading 1')
st.markdown('[Hoc AI](https://)')
st.markdown("""
        1. ML
        2. AL       
            """)
st.markdown(r'$ \sqrt{2x} $')
st.divider()

st.latex('\sqrt{2x}')

st.divider()

st.write('Hoc Ai')
st.write('# heading 1')
st.write('[Google](https://)')
st.write(r'$ \sqrt{2x} $')
st.write('1 + 1 = ', 2)

st.divider()
st.code("""
    import random
        value = random.randin(3,10)
        print(value)
""")

def get_year():
    return '19'
with st.echo():
    st.write('This is a text')
    def get_name():
        return 'Minh'
    
name = get_name()
year = get_year()
st.write(name,year)

st.divider()
st.logo('./anhQM.png')

st.image('./dogs.jpeg',caption='Bư Dog')

st.audio('./audio.mp4')
st.video('./video.mp4')

st.divider()
def get_fullname():
    st.write('Minh')
agree = st.checkbox("I agree!",on_change=get_fullname)
if agree:   
    st.write('Thank!')

status = st.radio('Your favorite colour:', ['Yellow','Blue'],captions=['Vang','Xanh'])
print(status)

staus =st.selectbox('Your Contact',['Email','address'])
print(staus)

st.multiselect('Colour',['Yellow','Green','Blue'])
st.select_slider('Your Colour',['Red','Blue','Yellow'])

st.divider()

if st.button('YEllow'):
    st.write('Say hello')
else:
    st.write('Gud Bye')


value = st.text_input('Your name', value = 'Minh')
st.write('Minh')

st.divider()

upload_file = st.file_uploader('Add File', accept_multiple_files=True)
for upload_file in upload_file:
    read_f = upload_file.read()
    st.write('File Name: ',upload_file.name)
with st.form('My form'):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("Name:")
    f_age = col2.text_input("Age:")
    submit = st.form_submit_button("Submit")
    if submit:
        st.write(f"Name: {f_name}, Age: {f_age}")

st.divider()

import random
value = random.randint(1,10)
if  'key' not in st.session_state:
    st.session_state['email'] = value
    st.session_state['pass'] = value
st.write(st.session_state.key)