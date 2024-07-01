import streamlit as st

def dalle_completion(user_prompt):
    url = "https://i.etsystatic.com/53119727/r/il/654f9a/6079073194/il_1588xN.6079073194_l09a.jpg"
    return url

st.title("DALL·E: Creating Images from Text")

message = st.text_area("Enter a description of the image that you want to create...")
print("User prompt:", message)
gen_button = st.button("Generate Image")

if gen_button and message:
    response_url = dalle_completion(message)
    print(response_url)
    st.image(response_url, caption="Dalle generated Image", use_column_width=True)
