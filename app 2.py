import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="SmartAgri AI", page_icon="🌱")
st.title("🌱 SmartAgri AI - الزراعة الذكية بالذكاء الاصطناعي")
st.write("ارفع صورة النبات لتحليل صحته والحصول على توصية ذكية للمزارع.")

uploaded_file = st.file_uploader("ارفع صورة النبات", type=["jpg", "png", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="صورة النبات", use_column_width=True)

    # نموذج تجريبي: اختيار عشوائي للنتيجة
    diseases = ["سليم", "مصاب بفطر", "نقص عناصر غذائية"]
    result = random.choice(diseases)

    st.subheader("نتيجة التحليل:")
    st.write(f"النبات: **{result}**")

    recommendations = {
        "سليم": "استمر بالري والتسميد المعتاد 🌿",
        "مصاب بفطر": "استخدم مبيد فطري مناسب وقم بتقليم الأجزاء المصابة 🧴",
        "نقص عناصر غذائية": "قم بتسميد النبات بالأسمدة المناسبة ⚡"
    }

    st.subheader("التوصيات:")
    st.write(recommendations[result])
