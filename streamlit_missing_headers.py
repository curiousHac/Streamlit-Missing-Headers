import streamlit as st
import requests

def check_response_headers(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            missing_headers = []
            required_headers = [
                "X-Frame-Options", 
                "X-Content-Type-Options", 
                "Strict-Transport-Security", 
                "Content-Security-Policy", 
                "Referrer-Policy"
            ]
            for header in required_headers:
                if header not in response.headers:
                    missing_headers.append(header)
            
            if missing_headers:
                return f"Missing headers: {', '.join(missing_headers)}"
            else:
                return "All required headers are present"
        else:
            return f"Failed to fetch URL. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def main():
    st.title("Response Header Checker")
    url = st.text_input("Enter URL to check:", "https://example.com")
    if st.button("Check Headers"):
        result = check_response_headers(url)
        st.write(result)

if __name__ == "__main__":
    main()
