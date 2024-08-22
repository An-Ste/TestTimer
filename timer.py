import streamlit as st
import time

# タイマー部分
class TimeCounts:
    # 分
    def min_time(self, minutes):
        self.minutes = minutes
        with st.empty():
            for m in range(minutes):
                st.write(f"⏳ {m} seconds have passed")
                time.sleep(1)
    # 秒
    def sec_time(self, seconds):
        self.seconds = seconds
        with st.empty():
            for s in range(seconds):
                st.write(f"⏳ {s:02} seconds have passed")
                time.sleep(1)

    def print_time(self, p_hours, p_minutes, p_seconds):
        p_hours = self.hours

        for _ in range(minutes):
            st.write("{hours:02}：{minutes:02}：{seconds:02}")

def start_timer(self, start_num):
    self.start_num = start_num
    st.write(f"{start_num + 1}回目 スタート")

def end_timer(self, end_num):
    self.end_num = end_num
    st.write(f"{end_num + 1}回目 スタート")

# ---------------------------------------------------------------------

Time = TimeCounts()
min_counts = 0
min_limits = 0
hour_counts = 0

st.header("ポモドーロタイマー")
with st.sidebar: # サイドバー
    st.subheader("タイマー 管理メニュー")
    loop_count = st.number_input("タイマーの繰り返し回数", min_value=1, max_value=5, value=1)
    act_mins = st.number_input("作業時間（分）", min_value=1, max_value=60, value=1)
    lest_mins = st.number_input("休憩時間（分）", min_value=1, max_value=10, value=1)

OverWrite = st.empty()
# タイマー
col1, col2 = st.columns((1, 1))
with col1:
    if st.button("Start", type="primary"):
        for j in range(loop_count): # ループ回数
            for i in range(act_mins): # 何分繰り返すか
                # 秒
                with st.empty():
                    for s in range(60):
                        time.sleep(1)
                        min_limits += 1
                        # 分
                        if min_limits == 61:
                            min_counts += 1

                        with OverWrite.container():
                            st.subheader(f"{min_counts:02}：{s:02}")
                            st.subheader(f"{j+1}回目")

                    min_limits = 0

with col2:
    if st.button("Stop", type="secondary"):
        st.write("STOP !!")
