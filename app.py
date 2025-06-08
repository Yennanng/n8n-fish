import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Upload Fish Image", page_icon="🐟")
st.title("🐟 Fish Image Uploader")

uploaded_file = st.file_uploader("Upload fish image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Preview", use_column_width=True)

    # Đọc và chuyển ảnh thành base64
    image = Image.open(uploaded_file)
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    if st.button("📤 Nhận diện bệnh ở cá nha"):
        webhook_url = "https://n8n.n2nai.io/webhook/fish-image"

        response = requests.post(webhook_url, json={
            "filename": uploaded_file.name,
            "image_base64": img_base64
        })

        if response.status_code == 200:
            st.success("✅ Ảnh đã được gửi đến n8n!")
        else:
            st.error("❌ Gửi thất bại.")
