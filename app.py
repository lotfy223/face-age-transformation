import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Face Age Transformation",
    page_icon="🎭",
    layout="wide",
)

st.title("🎭 Face Age Transformation")
st.write(
    "مشروع تجريبي لاستكشاف شكل الوجه في مراحل عمرية مختلفة "
    "باستخدام نماذج التعلم العميق."
)

st.info(
    "الصفحة تعرض نتيجة محفوظة من التجربة. "
    "رفع الصور وتشغيل النموذج مباشرة غير متاحين بعد."
)

st.subheader("📸 نتائج التجربة")

image_path = Path(__file__).parent / "results.png"

if image_path.exists():
    st.image(
        str(image_path),
        caption="مقارنة تجريبية لتغيير العمر قبل وبعد التدريب",
    )
else:
    st.warning(
        "الصورة غير موجودة. ارفع ملف results.png "
        "في المجلد الرئيسي للمستودع."
    )

st.subheader("🧠 عن المشروع")
st.write(
    "استخدمنا StyleGAN لتوليد وجه صناعي، ثم جرّبنا "
    "Style-based Age Manipulation (SAM) لتغيير العمر. "
    "وأجرينا تجربة تدريب إضافي قصيرة لمدة 100 خطوة."
)

st.warning(
    "الصور تصورات احتمالية، وليست توقعًا مؤكدًا لشكل "
    "الشخص الحقيقي في المستقبل."
)

st.caption("Python · PyTorch · StyleGAN · SAM · Streamlit")
