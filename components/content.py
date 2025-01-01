
import streamlit as st
import random
import time


def content(user, age):
    posts = st.session_state.cnt
    for post_id, post_data in list(posts.items()):

        if post_data["reported"] >= 5:
            post_data["flag"] = "mildly_appropriate"
            st.session_state.cnt[post_id] = post_data
            continue

        if age <= 18 and post_data["flag"] != "appropriate":
            continue
        if post_data["flag"] != "inappropriate":
            with st.container():
                if post_data["type"] == "image":
                    st.image(post_data["content"])
                elif post_data["type"] == "video":
                    st.video(post_data["content"])
                
                st.subheader("Caption:")
                st.write(post_data["caption"])

                if st.button("Report", key=f"report_{post_id}", icon="📢"):
                    @st.dialog("REPORT")
                    def report():
                        report_reason = st.text_area("Why do you want to report this post?", key=f"report_reason_{post_id}")
                        if st.button("Submit Report", key=f"submit_report_{post_id}"):
                            if report_reason:
                                st.success("Thank you for your report!")
                                post_data["reported"] += 1
                                if post_data["reported"] >= 5:
                                    post_data["flag"] = "mildly_appropriate"
                                st.session_state.cnt[post_id] = post_data
                                time.sleep(1)
                                st.rerun()
                    report()

                st.subheader("Comments")
                new_comment = st.text_input("Add a comment...", key=f"comment_{post_id}")
                if st.button("Post Comment", key=f"post_comment_{post_id}"):
                    if new_comment:
                        flag = {
                            "username": user,
                            "comment": new_comment,
                            "valid": st.session_state.resources.text_check(new_comment)["category"],
                        }
                        post_data["comment"].append(flag)
                        st.session_state.cnt[post_id] = post_data
                        st.rerun()

                with st.expander(f"View all ({len(post_data['comment'])}) comments"):
                    for comment in post_data["comment"]:
                        if comment["valid"] != "inappropriate":
                            st.write(f"**{comment['username']}**")
                            st.write(comment["comment"])
                            if comment["valid"] == "mildly_appropriate":
                                st.warning("Flagged as inappropriate")
                        else:
                            st.error("Remove comment due to community guidelines")

