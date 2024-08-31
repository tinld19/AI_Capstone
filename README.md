# AI_Capstone

# run build elasticSearch Docker

step 1: pip install -r requirements.txt \n
step 2: docker compose up —build -d

# run web server

step 1: python main.py

# nếu lần đầu start project trên máy mới

di chuyển vào folder /AI_Capstone/src/chatbot/database để load data vào database
chạy lệnh: python handle_data.py

sau khi đã build docker, load data, run web server thì call API như bình thường
