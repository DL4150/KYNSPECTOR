
import streamlit as st
from streamlit_option_menu import option_menu
from components.content import content
import random
st.image("kyn/components/logo.png",)
st.markdown("""
    <style>
        .flex { display: flex; }
        .items-center { align-items: center; }
        .justify-between { justify-content: space-between; }
        .rounded-full { border-radius: 9999px; }
        .bg-secondary-grey-2 { background-color: #f3f4f6; }
        .text-primary-black { color: #000; }
        .hover\\:text-primary:hover { color: #007aff; }
        .text-micro { font-size: 0.875rem; }
        .text-red { color: red; font-weight: bold; font-size: 1.25rem; }
        button { border: none; background: none; cursor: pointer; }
        input { border: none; outline: none; }
        .navbar { margin: 0; padding: 0; width: 100%; }
        .navbar > div { margin: 0; padding: 0; }
    </style>
""", unsafe_allow_html=True)

# Navbar HTML
st.markdown("""
    <div class="navbar flex items-center justify-between h-full" style="padding-bottom: 30px;">
        <div class="flex items-center">
            <span class="text-red">KŸN</span>
        </div>
        <div class="flex-shrink-0 rounded-full bg-secondary-grey-2">
            <div class="relative rounded-full overflow-hidden">
                <input placeholder="Search location" class="h-full w-[280px] rounded-full text-primary-black placeholder-gray-500 focus:outline-none bg-secondary-grey-2" type="text">
            </div>
        </div>
        <nav class="flex space-x-8">
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">🏠</span>
                <span class="text-micro text-primary">Home</span>
            </button>
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">🎥</span>
                <span class="text-micro text-primary-black">Live</span>
            </button>
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">📹</span>
                <span class="text-micro text-primary-black">Videos</span>
            </button>
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">🎞️</span>
                <span class="text-micro text-primary-black">Klips</span>
            </button>
        </nav>
        <div class="flex create-container">
            <button onclick="window.location.reload()" class="rounded-full border border-primary-black flex items-center justify-center">
                <span style="font-size: 1.5rem; margin-right: 5px;">➕</span>
                <span class="text-primary-black text-body">Create</span>
            </button>
        </div>
        <nav class="flex space-x-8">
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">🔔</span>
                <span class="text-micro text-primary">Home</span>
            </button>
            <button class="flex flex-col items-center text-center text-primary-black hover:text-primary">
                <span style="font-size: 1.5rem;">🙎</span>
                <span class="text-micro text-primary-black">Account</span>
            </button>
        </nav>
    </div>
""", unsafe_allow_html=True)
slt = option_menu(
    menu_title="",
    options=["Content","Post"],
    icons=["book","envelope"],
    default_index=0,
    orientation= "horizontal"
)
if slt == "Content":
    content(user="user1",age=12)
elif slt == "Post":
    @st.dialog("POST")
    def vote():
        uploaded_file = st.file_uploader("Upload a video or image", type=["mp4", "png", "jpg", "jpeg"],accept_multiple_files=False)
        if uploaded_file is not None:
            st.write("File uploaded successfully!")
            media_op = "unflagged"
            media_tp = "media"
            if uploaded_file.type.startswith("video"):
                media_tp = "video"
                st.video(uploaded_file)
                with st.spinner("evaluating video"):
                    media_op = st.session_state.resources.video_check(uploaded_file)["category"]
            else:
                media_tp = "image"
                st.image(uploaded_file)
                media_op= st.session_state.resources.image_check(uploaded_file)["category"]
        cap = st.text_input("Caption")
        if st.button("Submit") and uploaded_file:
            cap_op = st.session_state.resources.text_check(cap)["category"]
            if cap_op == "inappropriate" or media_op == "inappropriate":
                st.error("cannnot submit due to community guidelines")
            else:
                st.session_state.cnt[f"user1_{random.randint(100000,999999)}"] = {
                    "username": "user1",
                    "content": uploaded_file,
                    "type": media_tp,
                    "comment": [],
                    "reported": 0,
                    "flag": media_op,
                    "caption": cap,
                }
                st.success("uploaded successfully")

    vote()
    