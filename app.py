import streamlit as st

st.set_page_config(
    page_title="Face Age Transformation",
    page_icon="🎭",
    layout="centered",
)

st.title("🎭 Face Age Transformation")

st.write(
    "ارفع صورة وجه عشان تعرضها في الموقع. "
    "المشروع بيستكشف تغيير شكل الوجه عبر مراحل عمرية مختلفة."
)

uploaded = st.file_uploader(
    "اختار صورة من جهازك",
    type=["jpg", "jpeg", "png"],
)

if uploaded is not None:
    st.image(
        uploaded.getvalue(),
        caption="الصورة اللي رفعتها",
    )

    st.info(
        "تم عرض صورتك. تغيير العمر تلقائيًا غير متاح بعد؛ "
        "هنحتاج نوصّل الموقع بالموديل."
    )
else:
    st.write("اختار صورة واضحة للوجه للبدء.")

st.warning(
    "أي صور عمرية هي تصورات احتمالية، "
    "وليست توقعًا مؤكدًا لشكل الشخص الحقيقي."
)

st.caption("Python · PyTorch · StyleGAN · SAM · Streamlit")
