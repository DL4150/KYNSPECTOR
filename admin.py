import streamlit as st
import random
from  components.c import kynspector

if "cnt" not in st.session_state:
    st.session_state.cnt = {
        f"user1_{random.randint(100000,999999)}": {
            "username": "user1",
            "content": "kyn/assets/1_b.mp4",
            "type": "video",
            "comment": [],
            "reported": 0,
            "flag": "unflagged",
            "caption": "A beautiful moment captured!",
        },
        f"user2_{random.randint(100000,999999)}": {
            "username": "user2",
            "content": "kyn/assets/1_a.png",
            "type": "image",
            "comment": [],
            "reported": 0,
            "flag": "appropriate",
            "caption": "This is one for the memories.",
        },
        f"user1_{random.randint(100000,999999)}": {
            "username": "user1",
            "content": "kyn/assets/1_c.mp4",
            "type": "video",
            "comment": [],
            "reported": 0,
            "flag": "inappropriate",
            "caption": "An insightful video to watch.",
        },
        f"user2_{random.randint(100000,999999)}": {
            "username": "user2",
            "content": "kyn/assets/1_d.jpg",
            "type": "image",
            "comment": [],
            "reported": 0,
            "flag": "mildly_appropriate",
            "caption": "Art that speaks volumes.",
        },
    }

st.set_page_config(layout="wide")

if "resources" not in st.session_state:
    with st.spinner("Loading In Resources"):
        st.session_state.resources = kynspector()



st.image("kyn/components/logo.png")
st.markdown(
    '<h1 style="color:red; font-weight: bold; font-size: 5em;">KŸNSPECTOR</h1>',
    unsafe_allow_html=True,
)

st.subheader("Log - Inappropriate Content/Comments")
log_expander = st.expander("Inappropriate Content and Comments")
with log_expander:
    for key, value in st.session_state.cnt.items():
        if value["flag"] == "inappropriate":
            st.write(f"**{value['username']}**: {value['caption']}")
            st.write(f"Content: {value['content']}")
        for i in value["comment"]:
            if i["valid"] == "inappropriate":
                st.write(f"** PostID: **{key} ** User: **{i['username']}")
                st.write(i["comment"])

st.subheader("Ongoing - Mildly Inappropriate Content/Comments")
ongoing_expander = st.expander("Mildly Inappropriate Content and Comments")
with ongoing_expander:
    for key, value in st.session_state.cnt.items():
        if value["flag"] == "mildly_appropriate":
            st.markdown(f"**{value['username']}**: {value['caption']}")
            st.write(f"Content: {value['content']}")
            flag_option = st.selectbox(
                "Update Content Flag",
                options=["appropriate", "inappropriate", "mildly_appropriate"],
                index=["appropriate", "inappropriate", "mildly_appropriate"].index(value["flag"]),
                key = f"{key}"
            )

            if st.button("submit",key=f"button_{key}") and flag_option:
                value["flag"] = flag_option
                st.success(f"Content flag updated to {flag_option}")
                st.rerun()
                
        for ct,comment in enumerate(value["comment"]):
            if comment["valid"] == "mildly_appropriate":
                st.write(f"Comment by {comment['username']}: {comment['comment']}")
                valid_option = st.selectbox(
                    "Update Comment Validity",
                    options=["appropriate", "inappropriate", "mildly_appropriate"],
                    index=["appropriate", "inappropriate", "mildly_appropriate"].index(comment["valid"]),
                    key=f"{key}_{ct}"
                )
                if st.button("submit",key=f"button_{key}_{ct}") and valid_option:
                    comment["valid"] = valid_option
                    st.success(f"Comment validity updated to {valid_option}")
                    st.rerun()