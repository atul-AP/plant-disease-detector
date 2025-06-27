import os
import sys
import streamlit as st
import pandas as pd
from PIL import Image

# Setup import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.predict import predict_image

# 🌐 Language dictionary
LANGUAGES = {
    "English": {
        "title": "🌿 Plant Disease Detector",
        "caption": "Upload images of plant leaves to detect diseases using AI",
        "upload": "📤 Upload one or more leaf images",
        "image": "🖼️ Image",
        "analyzing": "🔍 Analyzing...",
        "prediction": "✅ Prediction",
        "healthy": "Healthy",
        "failed": "❌ Prediction failed",
        "summary": "📋 Summary",
        "download": "📥 Download Results (CSV)",
        "upload_prompt": "📂 Please upload images from the sidebar."
    },
    "Hindi": {
        "title": "🌿 पौधों के रोग पहचानने वाला",
        "caption": "AI की मदद से पत्तियों की तस्वीरें अपलोड करें और रोग पहचानें",
        "upload": "📤 एक या अधिक पत्तियों की छवियां अपलोड करें",
        "image": "🖼️ छवि",
        "analyzing": "🔍 विश्लेषण कर रहे हैं...",
        "prediction": "✅ भविष्यवाणी",
        "healthy": "स्वस्थ",
        "failed": "❌ भविष्यवाणी विफल रही",
        "summary": "📋 सारांश",
        "download": "📥 परिणाम CSV के रूप में डाउनलोड करें",
        "upload_prompt": "📂 कृपया साइडबार से छवियां अपलोड करें।"
    }
}

# Page config
st.set_page_config(page_title="Plant Disease Detector", layout="wide", page_icon="🌿")

# 🌿 Stylish CSS for a polished UI
st.markdown("""
    <style>
        .stApp {
            background-color: #0e1a17;
            background-image: url('https://images.unsplash.com/photo-1524594227084-5d7d70865a02?auto=format&fit=crop&w=1400&q=80');
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
            color: #e8f5e9;
        }
        .stSidebar {
            background-color: #0b2821;
        }
        h1, h2, h3, h4 {
            color: #b2dfdb;
        }
        .css-1v0mbdj, .css-1n76uvr {
            color: #d0f0c0;
        }
        .stDownloadButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .stButton>button {
            background-color: #388e3c;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 📂 Sidebar configuration
st.sidebar.title("⚙️ Options")
language = st.sidebar.selectbox("🌍 Language / भाषा", list(LANGUAGES.keys()))
T = LANGUAGES[language]

uploaded_files = st.sidebar.file_uploader(
    T["upload"],
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# 🧾 Header with logo
logo_path = "your_logo.png"  # Optional local logo
col1, col2 = st.columns([1, 6])
with col1:
    if os.path.exists(logo_path):
        st.image(logo_path, width=100)
    else:
        st.markdown("🌱")

with col2:
    st.markdown(f"## {T['title']}")
    st.caption(f"_{T['caption']}_")

st.markdown("---")

# 🔍 Prediction process
summary_results = []

if uploaded_files:
    cols = st.columns(3)

    for i, uploaded_file in enumerate(uploaded_files):
        with cols[i % 3]:
            try:
                with st.spinner(T["analyzing"]):
                    img = Image.open(uploaded_file).convert("RGB")
                    temp_path = f"temp_{i}.jpg"
                    img.save(temp_path)

                    label, confidence, _, _ = predict_image(temp_path)
                    color = "lightgreen" if "healthy" in label.lower() else "salmon"

                    st.image(img, use_column_width=True, caption=f"{T['image']} {i+1}")
                    st.markdown(
                        f"<div style='padding: 5px 10px; background-color: {color}; border-radius: 6px;'>"
                        f"<b>{T['prediction']}:</b> {label} ({confidence * 100:.2f}%)</div>",
                        unsafe_allow_html=True
                    )

                    summary_results.append({
                        "Image Name": uploaded_file.name,
                        "Prediction": label,
                        "Confidence (%)": round(confidence * 100, 2)
                    })

            except Exception as e:
                st.image(uploaded_file, use_column_width=True)
                st.error(f"{T['failed']}: {e}")

    # 📋 Summary Table
    if summary_results:
        st.markdown("## " + T["summary"])
        df = pd.DataFrame(summary_results)

        healthy_count = df["Prediction"].str.lower().str.contains("healthy").sum()
        diseased_count = len(df) - healthy_count

        st.success(f"✅ {T['healthy']}: {healthy_count}")
        st.warning(f"🦠 Diseased: {diseased_count}")

        st.dataframe(df, use_container_width=True)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label=T["download"],
            data=csv,
            file_name="plant_disease_results.csv",
            mime="text/csv"
        )

else:
    st.info(T["upload_prompt"])







# import os
# import sys
# import streamlit as st
# import pandas as pd
# from io import BytesIO
# from PIL import Image

# # Add src directory to the path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from src.predict import predict_image

# # --------------🌐 Language Dictionary --------------
# LANGUAGES = {
#     "English": {
#         "title": "🌿 Plant Disease Detector",
#         "caption": "Upload images of plant leaves to detect diseases using AI",
#         "upload": "📤 Upload one or more leaf images",
#         "image": "🖼️ Image",
#         "analyzing": "🔍 Analyzing...",
#         "prediction": "✅ Prediction",
#         "healthy": "Healthy",
#         "failed": "❌ Prediction failed",
#         "summary": "📋 Summary",
#         "download": "📥 Download Results (CSV)"
#     },
#     "Hindi": {
#         "title": "🌿 पौधों के रोग पहचानने वाला",
#         "caption": "AI की मदद से पत्तियों की तस्वीरें अपलोड करें और रोग पहचानें",
#         "upload": "📤 एक या अधिक पत्तियों की छवियां अपलोड करें",
#         "image": "🖼️ छवि",
#         "analyzing": "🔍 विश्लेषण कर रहे हैं...",
#         "prediction": "✅ भविष्यवाणी",
#         "healthy": "स्वस्थ",
#         "failed": "❌ भविष्यवाणी विफल रही",
#         "summary": "📋 सारांश",
#         "download": "📥 परिणाम CSV के रूप में डाउनलोड करें"
#     }
# }

# # -------------------- 🎨 PAGE CONFIG --------------------
# st.set_page_config(page_title="Plant Disease Detector", layout="wide")

# # -------------------- 📂 SIDEBAR --------------------
# st.sidebar.title("⚙️ Options")
# language = st.sidebar.selectbox("🌍 Language / भाषा", list(LANGUAGES.keys()))
# T = LANGUAGES[language]

# st.sidebar.markdown("---")
# uploaded_files = st.sidebar.file_uploader(
#     T["upload"], type=["jpg", "jpeg", "png"], accept_multiple_files=True
# )

# # -------------------- 🖼️ HEADER --------------------
# # st.markdown(f"## {T['title']}")
# # st.caption(T["caption"])
# # st.divider()

# # -------------------- 🖼️ HEADER --------------------
# logo_path = "your_logo.png"  # Replace with your actual logo image
# col1, col2 = st.columns([1, 5])
# with col1:
#     if os.path.exists(logo_path):
#         st.image(logo_path, width=80)
#     else:
#         st.markdown("🌿")

# with col2:
#     st.markdown(f"## {T['title']}")
#     st.caption(T["caption"])
# st.divider()


# # -------------------- 📊 RESULTS --------------------
# summary_results = []

# if uploaded_files:
#     cols = st.columns(3)  # display images in a grid

#     for i, uploaded_file in enumerate(uploaded_files):
#         with cols[i % 3]:
#             try:
#                 img = Image.open(uploaded_file).convert("RGB")
#                 img.save("temp.jpg")
#                 label, confidence, _, _ = predict_image("temp.jpg")
#                 color = "green" if "healthy" in label.lower() else "red"

#                 st.image(img, use_column_width=True)
#                 st.markdown(f"**{T['prediction']}:** <span style='color:{color}'>{label}</span> ({confidence*100:.2f}%)", unsafe_allow_html=True)

#                 summary_results.append({
#                     "Image Name": uploaded_file.name,
#                     "Prediction": label,
#                     "Confidence (%)": round(confidence * 100, 2)
#                 })

#             except Exception as e:
#                 st.image(uploaded_file, use_column_width=True)
#                 st.error(f"{T['failed']}: {e}")




#     # -------------------- 📋 SUMMARY PANEL --------------------
#     if summary_results:
#         st.divider()
#         st.subheader(T["summary"])

#         df = pd.DataFrame(summary_results)
#         healthy_count = df['Prediction'].str.lower().str.contains("healthy").sum()
#         diseased_count = len(df) - healthy_count

#         st.markdown(f"- ✅ **Healthy:** {healthy_count}")
#         st.markdown(f"- 🦠 **Diseased:** {diseased_count}")

#         st.dataframe(df, use_container_width=True)

#         csv = df.to_csv(index=False).encode("utf-8")
#         st.download_button(label=T["download"], data=csv, file_name="plant_disease_results.csv", mime="text/csv")

# else:
#     st.info("📂 Please upload images from the sidebar.")