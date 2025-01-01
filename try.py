import streamlit as st
import opennsfw2 as n2
import tempfile

def main():
    st.title("NSFW Video Prediction with OpenNSFW2")
    
    # File uploader for video file
    video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    
    if video_file is not None:
        st.write("File uploaded successfully!")
        
        # Create a temporary file to store the uploaded video
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(video_file.read())
            temp_file_path = temp_file.name
        
        st.write("Analyzing the video...")
        
        try:
            # Use the temp_file_path with n2.predict_video_frames
            results = n2.predict_video_frames(temp_file_path)
            
            # Display results
            st.write("Prediction Results:")
            st.write(results)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Cleanup: Optionally delete the temporary file after processing
        # import os
        # os.remove(temp_file_path)

if __name__ == "__main__":
    main()
