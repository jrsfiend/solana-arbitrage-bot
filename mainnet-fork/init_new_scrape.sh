echo "remove accounts\\n"
# rm accounts/* 
echo "new scrape\\n"
# npx ts-node new_scrape.ts
echo "setup validator\\n"
python setup_validator.py
echo "start fork\\n"
bash start_localnet.sh