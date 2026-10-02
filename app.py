"""순천공장 최대수요전력 관리 — Streamlit 배포용 진입점.

화면과 계산 로직은 검증이 끝난 demand-monitor.html(DemandModel selfTest 32건)을
그대로 사용한다. Streamlit은 이 파일을 st.iframe으로 띄워 주는 역할만 한다.
iframe은 같은 출처 + 스크립트 실행이 허용되므로 localStorage 저장,
탭 간 리더/팔로워 동기화, 경보음(autoplay 허용)이 브라우저에서 그대로 동작한다.
"""
from pathlib import Path

import streamlit as st

HTML_FILE = Path(__file__).parent / "demand-monitor.html"

st.set_page_config(
    page_title="순천공장 수요전력 관리",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit 기본 여백을 줄여 앱 화면을 넓게 쓴다.
st.markdown(
    """
    <style>
      .block-container { padding-top: 1rem; padding-bottom: 0; max-width: 100%; }
      header[data-testid="stHeader"] { height: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


if not HTML_FILE.exists():
    st.error(f"{HTML_FILE.name} 파일을 찾을 수 없습니다. app.py와 같은 폴더에 두세요.")
    st.stop()

with st.sidebar:
    st.header("화면 설정")
    height = st.slider(
        "앱 표시 높이(px)", min_value=800, max_value=4000, value=2000, step=100,
        help="화면 아래가 잘리면 높이를 늘리세요. 변경하면 앱이 다시 열리며 저장된 상태가 복원됩니다.",
    )
    st.caption(
        "데이터는 이 브라우저의 저장소에 보관됩니다. "
        "다른 PC·브라우저와는 공유되지 않습니다."
    )

# Path 객체를 넘기면 st.iframe이 HTML 파일을 읽어 같은 출처(same-origin) iframe으로 띄운다.
st.iframe(HTML_FILE, height=height)
