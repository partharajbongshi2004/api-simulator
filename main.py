import streamlit as st
import time

st.set_page_config(page_title="API Simulator", layout="centered")

st.title("API Request and Response Simulator")
st.write("Welcome to your first backend project. Practice how APIs handle requests and responses.")

st.sidebar.header("API Configuration")
request_type = st.sidebar.selectbox("Select Request Type", ["GET", "POST"])
endpoint = st.sidebar.text_input("API Endpoint", value="/api/v1/products")

st.subheader(f"Sending {request_type} Request")
st.code(f"{request_type} {endpoint}")

payload = ""
if request_type == "POST":
    st.markdown("### Enter JSON Payload")
    default_json = '{\n  "product_name": "T-Shirt",\n  "price": 450,\n  "stock": 25\n}'
    payload = st.text_area("JSON Body", value=default_json, height=120)

if st.button("Send API Request"):
    with st.spinner("Processing request..."):
        time.sleep(1)
    
    st.success("Response Received")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Status Code", value="200 OK" if request_type == "GET" else "201 Created")
    with col2:
        st.metric(label="Response Time", value="120 ms")
        
    st.markdown("### Response Body")
    if request_type == "GET":
        st.json({
            "status": "success",
            "message": "Data fetched successfully",
            "data": [
                {"id": 1, "product_name": "Premium Polo Shirt", "price": 850, "stock": 15},
                {"id": 2, "product_name": "Casual Denim Jeans", "price": 1200, "stock": 8}
            ]
        })
    else:
        st.json({
            "status": "success",
            "message": "New product added successfully",
            "created_item": {
                "id": 105,
                "product_name": "T-Shirt",
                "price": 450,
                "stock": 25
            }
        })
