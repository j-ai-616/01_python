import streamlit as st 

st.title("07. 세션 상태")

# session_state : Streamlit 앱이 rerun 되더라도 사용자 상태(값)을 유지하기 위한 저장 공간
# 로그인 상태, 장바구니, 챗봇 대화 기록 등 사용자 행동을 기억해야 하는 기능 구현에 사용

if "count" not in st.session_state:
    st.session_state.count = 0      # count라는 키값이 없으면 만들어서 0으로 만드세요.
    
col1, col2 = st.columns(2)

with col1:
    if st.button("카운트 +1"):        # click 시 True 됨. 
        st.session_state.count += 1

with col2:
    if st.button("리셋"):            # count 공간 값을 지움.
        st.session_state.count = 0
        
st.write("현재 카운트 :", st.session_state.count)

st.divider()

# session_state 에 저장하는 메모
if "memo_saved" not in st.session_state:
    st.session_state.memo_saved = ""
    
memo_saved = st.text_area("메모(저장됨)", value=st.session_state.memo_saved, key="memo_saved_area")
st.session_state.memo_saved = memo_saved

# session_state 에 저장하지 않는 메모(count 변경 시 초기화)
menu_unsaved = st.text_area("메모(저장안됨)", key="memo_unsaved_{st.session_state.count}")
