import base64
import streamlit as st

image_file = st.file_uploader(
    "Upload an image with company names or logos...",
    type=["jpg", "jpeg", "png", "webp"],
)

if image_file:
    st.image(image_file, caption="Uploaded Image")

    image_bytes = image_file.getvalue()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    # payload = {
    #     "model": "gpt-4o",
    #     "messages": [
    #         {
    #         "role": "user",
    #         "content": [
    #             {
    #             "type": "text",
    #             "text": "What’s in this image?"
    #             },
    #             {
    #             "type": "image_url",
    #             "image_url": {
    #                 "url": f"data:image/jpeg;base64,{base64_image}"
    #             }
    #             }
    #         ]
    #         }
    #     ],
    #     "max_tokens": 300
    #     }

    # response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response = "Fake response from OpenAI API"
    st.write(response)


    
