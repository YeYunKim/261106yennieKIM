import streamlit as st

st.set_page_config(page_title="나의 소개", page_icon="👋", layout="centered")

st.title("👋 안녕하세요! 저는 [김예연]입니다")

st.markdown("### 스무살, 청주교대 26학번입니다" \
"")
st.write(
    "여기는 나를 소개하는 공간입니다. 아래 내용을 참고해서 나중에 자유롭게 수정해보세요."
)

st.header("✨ About Me")
st.write(
    "저는 [교사가 되기 위해 초등교육학을 배우고 있는 학생]이며, [근래 독서에 다시금 취미를 가지고 텍스트를 읽는것에]에 관심이 많습니다. "
    "이 앱은 간단한 자기소개 페이지 예시로 만들어졌습니다."
)

st.header("🛠️ Skills")
st.write(
    "- [기술 1]\n"
    "- [기술 2]\n"
    "- [기술 3]"
)

st.header("📌 나의 목표")
st.write(
    "저의 주요 목표는 [목표를 여기에 입력하세요]. "
    "새로운 도전과 배움을 통해 성장하는 것을 좋아합니다."
)

st.header("📫 Contact")
st.write(
    "- 이메일: [your.email@example.com]"
    "\n- GitHub: [https://github.com/yourname](https://github.com/yourname)"
)

st.info("이제 이 내용을 바꿔서 나만의 프로필 페이지로 완성해보세요!")
