import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")

# # Create a plotly figure for use by st.plotly_chart()
# fig = px.line(
#     data,
#     title="Gold Prices",
#     x="DateTime",
#     y=["Gold"],
#     color_discrete_map={"Gold": "gold"}
# )

# # Streamlit part
# st.title("Precious Metal Prices")

# # Header area
# # st.header("Gold Prices")
# st.write("The cost of precious metals between 2018 and 2021")

# # Menu area
# metal_filter = st.selectbox("Select Metal", data.columns[1:], index=0)

# # Graph container
# st.plotly_chart(fig)

# # Update the chart based on the selected metal
# selected_data = data[["DateTime", metal_filter]]
# selected_fig = px.line(selected_data, x="DateTime", y=metal_filter, title=f"{metal_filter} Prices 2018-2021")
# st.plotly_chart(selected_fig)



# Create a plotly figure for use by st.plotly_chart()
fig = px.line(
    data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=["Gold"],
    color_discrete_map={"Gold": "gold"}
)

# Streamlit part
st.title("Precious Metal Prices")

# Header area
#st.header("Gold Prices")
st.write("The cost of precious metals between 2018 and 2021")

# Menu area
metal_filter = st.selectbox("Select Metal", data.columns[1:], index=0)

# Filter data for the selected metal
selected_data = data[["DateTime", metal_filter]]

# Create a plotly figure for the selected metal
selected_fig = px.line(selected_data, x="DateTime", y=metal_filter, title=f"{metal_filter} Prices 2018-2021")

# Display the updated chart
st.plotly_chart(selected_fig)
