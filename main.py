import streamlit as st

from few_shot import FewShotPosts

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("Linkedin Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

if __name__ == "__main__":
    main()