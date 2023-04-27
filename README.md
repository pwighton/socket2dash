# socket2dash

Read data from a socket and display it on a real-time dashbord

Geared mostly towards creating a real-time motion dashboard but hopefully useful more generally.

# !!!---!!! WORK IN PROGRESS !!!---!!!

## Setup

```
conda create --name socket2dash python=3.8
conda activate socket2dash
git clone git@github.com:pwighton/socket2dash
cd socket2dash
pip install -r requirements.txt
```

## Run

```
streamlit run app.py
```

## Refs

Forked from https://github.com/amrrs/real-time-live-streamlit-dashboard-python

See Also:
  - https://blog.streamlit.io/how-to-build-a-real-time-live-dashboard-with-streamlit/#2-how-to-do-a-basic-dashboard-setup
  - https://docs.streamlit.io/library/api-reference/charts/st.line_chart
