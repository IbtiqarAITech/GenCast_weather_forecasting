import streamlit as st
from datetime import datetime, timedelta
from gencast_model import GenCastModel

model = GenCastModel()

st.title("GenCast Weather Forecast")
st.markdown("Real-time predictions using the GenCast AI model.")

hour = st.slider("Hour of day", 0, 23, datetime.now().hour)
base_time = datetime.now().replace(hour=hour, minute=0, second=0, microsecond=0)

prediction = model.predict(base_time)

st.subheader("Current Prediction")
st.metric("Temperature (\u00b0C)", prediction["temperature"])
st.metric("Humidity (%)", prediction["humidity"])

# Forecast for the next 24 hours at 3-hour intervals
future_times = [base_time + timedelta(hours=i) for i in range(0, 24, 3)]
forecast = {"Time": future_times,
            "Temperature (\u00b0C)": [model.predict(t)["temperature"] for t in future_times],
            "Humidity (%)": [model.predict(t)["humidity"] for t in future_times]}

st.subheader("24h Forecast")
st.line_chart({"Temperature (\u00b0C)": forecast["Temperature (\u00b0C)"]})
st.line_chart({"Humidity (%)": forecast["Humidity (%)"]})
