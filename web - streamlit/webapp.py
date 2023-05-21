from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


# Emojis - https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# -----LOAD ASSETS-----
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_3rwasyjy.json")
img_contact_form = Image.open("images/nobg.png")
img_lottie_animation = Image.open("images/file.png")


# ----HEADER SECTION-----

with st.container():
    st.subheader("Hi, I am Munyi Victor :wave:")
    st.title("A Junior Software Developer From Kenya")
    st.write("I want to learn Python by all means and beacome a professional to be more productive in my development")
    st.write("[Learn More >](https://python.org)")


# ----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
            The Python Package Index, abbreviated as PyPI (/ˌpaɪpiˈaɪ/) and 
            also known as the Cheese Shop (a reference to the Monty Python's 
            Flying Circus sketch "Cheese Shop"),[2][3] is the official third-party 
            software repository for Python.[4] It is analogous to the CPAN repository 
            for Perl[5] and to the CRAN repository for R. PyPI is run by the Python Software 
            Foundation, a charity. Some package managers, including pip, use PyPI as the default 
            source for packages and their dependencies.
        """)
        st.write("[Youtube channel](https://youtube.com)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")


# -----PROJECTS-----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
            st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streanlit App")
        st.write("""
            Flying Circus sketch "Cheese Shop"),[2][3] is the official third-party 
            software repository for Python.[4] It is analogous to the CPAN repository 
            for Perl[5] and to the CRAN repository for R. PyPI is run by the Python Software 
            Foundation, a charity. Some package managers, including pip, use PyPI as the default 
            source for packages and their dependencies.
        """)
        st.markdown("[Watch Video...](https://youtube.com)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How to Add a Cotact Form to Your Streamlit App")
        st.write("""
            The Python Package Index, abbreviated as PyPI (/ˌpaɪpiˈaɪ/) and 
            also known as the Cheese Shop (a reference to the Monty Python's 
            Flying Circus sketch "Cheese Shop"),[2][3] is the official third-party 
            software repository for Python.
        """)
        st.markdown("[Watch Video...](https://youtube.com)")


#-----CONTACT-----
with st.container():
    st.write("---")
    st.write("Get in Touch With Me!")
    st.write("##")

    #Use - https://formsubmit.co
    contact_form = """
    <form action="https://formsubmit.co/munyivictor6@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
