
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"bhdben92@gmail.com"\"\n\
" > ~/.streamlit/credentials.tom1

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.tom1
