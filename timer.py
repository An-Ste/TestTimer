import streamlit as st
import time

# コード本文
st.title("タイマー")

with st.sidebar: # サイドバー
    st.subheader("タイマー 管理メニュー")
    minutes = st.slider("### **時間を選択してください  (分)**", min_value=0, max_value=10, value=0)
    seconds = st.slider("### **時間を選択してください  (秒)**", min_value=1, max_value=59, value=1)

min_time = minutes
sec_time = seconds

min_count = 0
sec_count = 0

OverWrite = st.empty()
# タイマー
col1, col2 = st.columns((1, 1))
with col1: # スタートボタン
    if st.button("Start", type="primary"):
        if minutes == 0: # 0分の場合
            for secs in range(seconds): # 秒タイマー
                with st.empty():
                    with OverWrite.container():
                            sec_count += 1
                            st.subheader(f"{min_count:02}：{sec_count:02}")
                            time.sleep(1)
            with st.empty():
                with OverWrite.container():
                    st.subheader(f"⌛ Timer Succeeded !!")

        elif minutes != 0: # 1分以上の場合
            for mins in range(minutes):
                if sec_count >= 59: #分タイマー
                    min_count += 1
                    for secs in range(seconds): # 秒タイマー
                        with st.empty():
                            with OverWrite.container():
                                    sec_count += 1
                                    st.subheader(f"{min_count:02}：{sec_count:02}")
                                    time.sleep(1)
            with st.empty():
                with OverWrite.container():
                    st.subheader(f"⌛ Timer Succeeded !!")
                    
with col2: # ストップボタン
    if st.button("Stop", type="secondary"):
        st.write("STOP !!")
