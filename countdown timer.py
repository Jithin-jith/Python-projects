import streamlit as st
import time

def countdown_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        st.write(f"## ⏳ {time_format}")
        time.sleep(1)
        duration -= 1
    st.write("## 🎉 Time's up!")

def main():
    st.title("Countdown Timer ⏲️")
    
    duration = st.number_input("Enter countdown time in seconds:", min_value=1, value=10, step=1)
    if st.button("Start Countdown"):
        countdown_timer(int(duration))

if __name__ == "__main__":
    main()
