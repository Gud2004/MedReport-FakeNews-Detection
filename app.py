# # app.py
# import streamlit as st
# from summarization import summarize_text
# from fake_news_detection import detect_fake_news
# from translation import translate_text
#
# st.title("AI-Powered Medical Report Summarization & Fake Health News Detection")
#
# # Create two tabs for different functionalities
# tab1, tab2 = st.tabs(["Medical Report Summarization", "Fake Health News Detection"])
#
# with tab1:
#     st.header("Summarize Medical Report")
#     report_text = st.text_area("Enter the medical report text", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option = st.checkbox("Translate to English before summarizing")
#     if translate_option and report_text.strip():
#         report_text = translate_text(report_text, dest='en')
#         st.info("Translated text:")
#         st.write(report_text)
#
#     if st.button("Summarize Report"):
#         if report_text.strip():
#             with st.spinner("Summarizing..."):
#                 summary = summarize_text(report_text)
#             st.success("Summary:")
#             st.write(summary)
#         else:
#             st.error("Please provide the medical report text.")
#
# with tab2:
#     st.header("Fake Health News Detection")
#     news_text = st.text_area("Enter the health news article", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option_news = st.checkbox("Translate to English before detection")
#     if translate_option_news and news_text.strip():
#         news_text = translate_text(news_text, dest='en')
#         st.info("Translated text:")
#         st.write(news_text)
#
#     if st.button("Detect Fake News"):
#         if news_text.strip():
#             with st.spinner("Analyzing..."):
#                 label, confidence = detect_fake_news(news_text)
#             st.success("Detection Result:")
#             st.write(f"Predicted: **{label.upper()}** with a confidence of {confidence:.2f}")
#         else:
#             st.error("Please provide the news article text.")







#
#
# import streamlit as st
# from summarization import summarize_text
# from fake_news_detection import detect_fake_news
# from translation import translate_text
#
# # Set global page configuration
# st.set_page_config(
#     page_title="Medical Report Summarization & Fake News Detection",
#     page_icon=":microscope:",
#     layout="wide"
# )
#
# # Inject custom CSS for enhanced styling
# st.markdown(
#     """
#     <style>
#     /* Overall background style */
#     .reportview-container {
#         background: linear-gradient(135deg, #f6f9fc, #e9eff5);
#     }
#     /* Main title styling */
#     h1 {
#         color: #264653;
#         font-family: 'Helvetica Neue', sans-serif;
#         font-weight: bold;
#     }
#     /* Header styling */
#     h2, h3 {
#         color: #264653;
#         font-family: 'Helvetica Neue', sans-serif;
#     }
#     /* Button styling */
#     .stButton>button {
#         background-color: #264653;
#         color: white;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-size: 16px;
#         transition: background-color 0.3s ease;
#     }
#     .stButton>button:hover {
#         background-color: #2a9d8f;
#     }
#     /* Text area styling */
#     .stTextArea>div>textarea {
#         font-size: 16px;
#         padding: 10px;
#         border: 1px solid #ccc;
#         border-radius: 5px;
#     }
#     /* Sidebar customization (optional) */
#     .sidebar .sidebar-content {
#         background: #264653;
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # App Title
# st.title("AI-Powered Medical Report Summarization & Fake Health News Detection")
#
# # Create two tabs for different functionalities
# tab1, tab2 = st.tabs(["Medical Report Summarization", "Fake Health News Detection"])
#
# with tab1:
#     st.header("Summarize Medical Report")
#     report_text = st.text_area("Enter the medical report text", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option = st.checkbox("Translate to English before summarizing")
#     if translate_option and report_text.strip():
#         report_text = translate_text(report_text, dest='en')
#         st.info("Translated text:")
#         st.write(report_text)
#
#     if st.button("Summarize Report"):
#         if report_text.strip():
#             with st.spinner("Summarizing..."):
#                 summary = summarize_text(report_text)
#             st.success("Summary:")
#             st.write(summary)
#         else:
#             st.error("Please provide the medical report text.")
#
# with tab2:
#     st.header("Fake Health News Detection")
#     news_text = st.text_area("Enter the health news article", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option_news = st.checkbox("Translate to English before detection")
#     if translate_option_news and news_text.strip():
#         news_text = translate_text(news_text, dest='en')
#         st.info("Translated text:")
#         st.write(news_text)
#
#     if st.button("Detect Fake News"):
#         if news_text.strip():
#             with st.spinner("Analyzing..."):
#                 label, confidence = detect_fake_news(news_text)
#             st.success("Detection Result:")
#             st.write(f"Predicted: **{label.upper()}** with a confidence of {confidence:.2f}")
#         else:
#             st.error("Please provide the news article text.")

#
# import streamlit as st
# from summarization import summarize_text
# from fake_news_detection import detect_fake_news
# from translation import translate_text
#
# # Set global page configuration
# st.set_page_config(
#     page_title="Medical Report Summarization & Fake News Detection",
#     page_icon=":microscope:",
#     layout="wide"
# )
#
# # Inject custom CSS to add a background image and enhance UI styling
# st.markdown(
#     """
#     <style>
#     /* Set a background image for the entire app */
#     .reportview-container {
#         background: url("https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80") no-repeat center center fixed;
#         background-size: cover;
#     }
#
#     /* Optional: add a semi-transparent overlay to improve readability */
#     .reportview-container::before {
#         content: "";
#         position: absolute;
#         top: 0;
#         left: 0;
#         right: 0;
#         bottom: 0;
#         background: rgba(0, 0, 0, 0.3);
#         z-index: -1;
#     }
#
#     /* Customize headers */
#     h1, h2, h3 {
#         color: #ffffff;
#         text-shadow: 2px 2px 4px #000;
#         font-family: 'Helvetica Neue', sans-serif;
#     }
#
#     /* Style buttons */
#     .stButton>button {
#         background-color: #264653;
#         color: white;
#         border-radius: 8px;
#         padding: 10px 20px;
#         font-size: 16px;
#         transition: background-color 0.3s ease;
#     }
#     .stButton>button:hover {
#         background-color: #2a9d8f;
#     }
#
#     /* Style text areas */
#     .stTextArea>div>textarea {
#         font-size: 16px;
#         padding: 10px;
#         border: 1px solid #ccc;
#         border-radius: 5px;
#     }
#
#     /* Optional: Customize sidebar */
#     .sidebar .sidebar-content {
#         background: rgba(38, 70, 83, 0.9);
#         color: white;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Now continue with your app content...
# st.title("AI-Powered Medical Report Summarization & Fake Health News Detection")
#
# # Create two tabs for different functionalities
# tab1, tab2 = st.tabs(["Medical Report Summarization", "Fake Health News Detection"])
#
# with tab1:
#     st.header("Summarize Medical Report")
#     report_text = st.text_area("Enter the medical report text", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option = st.checkbox("Translate to English before summarizing")
#     if translate_option and report_text.strip():
#         report_text = translate_text(report_text, dest='en')
#         st.info("Translated text:")
#         st.write(report_text)
#
#     if st.button("Summarize Report"):
#         if report_text.strip():
#             with st.spinner("Summarizing..."):
#                 summary = summarize_text(report_text)
#             st.success("Summary:")
#             st.write(summary)
#         else:
#             st.error("Please provide the medical report text.")
#
# with tab2:
#     st.header("Fake Health News Detection")
#     news_text = st.text_area("Enter the health news article", height=300)
#
#     # Checkbox to optionally translate the input to English
#     translate_option_news = st.checkbox("Translate to English before detection")
#     if translate_option_news and news_text.strip():
#         news_text = translate_text(news_text, dest='en')
#         st.info("Translated text:")
#         st.write(news_text)
#
#     if st.button("Detect Fake News"):
#         if news_text.strip():
#             with st.spinner("Analyzing..."):
#                 label, confidence = detect_fake_news(news_text)
#             st.success("Detection Result:")
#             st.write(f"Predicted: **{label.upper()}** with a confidence of {confidence:.2f}")
#         else:
#             st.error("Please provide the news article text.")
#
# import streamlit as st
#
# # Set page config
# st.set_page_config(page_title="AI-Powered Medical App", page_icon="🧑‍⚕️", layout="wide")
#
#
# # Apply background image with overlay
# def set_bg_image():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
#                         url("https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#
#
# set_bg_image()
#
# # Apply custom styles
# st.markdown(
#     """
#     <style>
#     h1, h2, h3 {
#         color: #ffffff !important;
#         text-shadow: 2px 2px 4px #000;
#         font-family: 'Arial', sans-serif;
#     }
#
#     .stButton>button {
#         background-color: #2a9d8f;
#         color: white;
#         border-radius: 10px;
#         font-size: 16px;
#         padding: 10px 20px;
#     }
#
#     .stButton>button:hover {
#         background-color: #e76f51;
#     }
#
#     .stTextInput>div>div>input {
#         border-radius: 10px;
#         padding: 8px;
#         background-color: #ffffff;
#         color: #000000;
#     }
#
#     .stTextArea>div>textarea {
#         background-color: rgba(255, 255, 255, 0.9);
#         color: #000;
#         border-radius: 10px;
#         padding: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )





# import streamlit as st
# from summarization import summarize_text  # Importing actual summarization function
#
# # Set page config
# st.set_page_config(page_title="AI-Powered Medical App", page_icon="🧑‍⚕️", layout="wide")
#
# # Apply background image with overlay
# def set_bg_image():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
#                         url("https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#
# set_bg_image()
#
# # Apply custom styles
# st.markdown(
#     """
#     <style>
#     h1, h2, h3 {
#         color: #ffffff !important;
#         text-shadow: 2px 2px 4px #000;
#         font-family: 'Arial', sans-serif;
#     }
#
#     .stButton>button {
#         background-color: #2a9d8f;
#         color: white;
#         border-radius: 10px;
#         font-size: 16px;
#         padding: 10px 20px;
#     }
#
#     .stButton>button:hover {
#         background-color: #e76f51;
#     }
#
#     .stTextInput>div>div>input {
#         border-radius: 10px;
#         padding: 8px;
#         background-color: #ffffff;
#         color: #000000;
#     }
#
#     .stTextArea>div>textarea {
#         background-color: rgba(255, 255, 255, 0.9);
#         color: #000;
#         border-radius: 10px;
#         padding: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# import streamlit as st
# from summarization import summarize_text  # Import summarization function
# from fake_news_detection import detect_fake_news  # Import fake news detection function
#
# # Set page config
# st.set_page_config(page_title="AI-Powered Medical App", page_icon="🧑‍⚕️", layout="wide")
#
# # Apply background image with overlay
# def set_bg_image():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
#                         url("https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
#             background-size: cover;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#
# set_bg_image()
#
# # Apply custom styles
# st.markdown(
#     """
#     <style>
#     h1, h2, h3 {
#         color: #ffffff !important;
#         text-shadow: 2px 2px 4px #000;
#         font-family: 'Arial', sans-serif;
#     }
#     .stButton>button {
#         background-color: #2a9d8f;
#         color: white;
#         border-radius: 10px;
#         font-size: 16px;
#         padding: 10px 20px;
#     }
#     .stButton>button:hover {
#         background-color: #e76f51;
#     }
#     .stTextArea>div>textarea {
#         background-color: rgba(255, 255, 255, 0.9);
#         color: #000;
#         border-radius: 10px;
#         padding: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
#
# # Main Title
# st.title("🌟 AI-Powered Medical Report Summarization & Fake News Detection")
#
# # Tabs for different functionalities
# tab1, tab2 = st.tabs(["📜 Medical Report Summarization", "📰 Fake News Detection"])
#
# # 📜 Medical Report Summarization Tab
# with tab1:
#     st.header("📑 Medical Report Summarization")
#     text = st.text_area("Enter medical report", height=200)
#
#     if st.button("Summarize"):
#         if text.strip() == "":
#             st.error("⚠ Please enter a medical report before summarizing.")
#         else:
#             summary = summarize_text(text)  # Call summarization function
#             st.subheader("📝 Summarized Report")
#             st.text_area("Summary", summary, height=150)
#
# # 📰 Fake News Detection Tab
# with tab2:
#     st.header("📰 Fake Health News Detection")
#     news_text = st.text_area("Enter health news article", height=200)
#
#     if st.button("Detect Fake News"):
#         if news_text.strip() == "":
#             st.error("⚠ Please enter a news article before detecting.")
#         else:
#             predicted_label, confidence = detect_fake_news(news_text)  # Call fake news function
#             st.subheader("🔎 Fake News Detection Result")
#
#             # Display result with color coding
#             if predicted_label == "FAKE":
#                 color = "#f8d7da"  # Red for fake
#                 text_color = "#721c24"
#             elif predicted_label == "REAL":
#                 color = "#d4edda"  # Green for real
#                 text_color = "#155724"
#             else:
#                 color = "#fff3cd"  # Yellow for uncertain
#                 text_color = "#856404"
#
#             st.markdown(
#                 f'<div style="padding:10px; background:{color}; border-radius:10px; color:{text_color};">'
#                 f'Prediction: **{predicted_label}** <br> Confidence: **{confidence:.2f}**'
#                 f'</div>',
#                 unsafe_allow_html=True
#             )







import streamlit as st
from summarization import summarize_text  # Import summarization function
from fake_news_detection import detect_fake_news  # Import fake news detection function

# Set page config
st.set_page_config(page_title="AI-Powered Medical App", page_icon="🧑‍⚕️", layout="wide")

# Apply background image with overlay
def set_bg_image():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                        url("https://images.unsplash.com/photo-1593642634367-d91a135587b5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_image()

# Apply custom styles
st.markdown(
    """
    <style>
    h1, h2, h3 {
        color: #ffffff !important;
        text-shadow: 2px 2px 4px #000;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #2a9d8f;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #e76f51;
    }
    .stTextArea>div>textarea {
        background-color: rgba(255, 255, 255, 0.9);
        color: #000;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title
st.title("🌟 AI-Powered Medical Report Summarization & Fake News Detection")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["📜 Medical Report Summarization", "📰 Fake News Detection"])

# 📜 Medical Report Summarization Tab
with tab1:
    st.header("📑 Medical Report Summarization")
    text = st.text_area("Enter medical report", height=200)

    if st.button("Summarize"):
        if text.strip() == "":
            st.error("⚠ Please enter a medical report before summarizing.")
        else:
            summary = summarize_text(text)  # Call summarization function
            st.subheader("📝 Summarized Report")
            st.text_area("Summary", summary, height=150)

# 📰 Fake News Detection Tab
with tab2:
    st.header("📰 Fake Health News Detection")
    news_text = st.text_area("Enter health news article", height=200)

    if st.button("Detect Fake News"):
        if news_text.strip() == "":
            st.error("⚠ Please enter a news article before detecting.")
        else:
            predicted_label, confidence = detect_fake_news(news_text)  # Call fake news function
            st.subheader("🔎 Fake News Detection Result")

            # Display result with color coding
            if predicted_label == "FAKE":
                color = "#f8d7da"  # Red for fake
                text_color = "#721c24"
            elif predicted_label == "REAL":
                color = "#d4edda"  # Green for real
                text_color = "#155724"
            else:
                color = "#fff3cd"  # Yellow for uncertain
                text_color = "#856404"

            st.markdown(
                f'<div style="padding:10px; background:{color}; border-radius:10px; color:{text_color};">'
                f'Prediction: **{predicted_label}** <br> Confidence: **{confidence:.2f}**'
                f'</div>',
                unsafe_allow_html=True
            )




