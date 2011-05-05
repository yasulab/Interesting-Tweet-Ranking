printf "Generating the interesting tweet ranking for @%s... \n\n" "BarackObama"
sleep 5	
python tweet-scorer/tweet-scorer.py log/tweets-by-BarackObama_en.txt log/yasulab-watch-list_en.txt
printf "Generating the interesting tweet ranking for @%s... \n\n" "BillGates"
sleep 5	
python tweet-scorer/tweet-scorer.py log/tweets-by-billgates_en.txt log/yasulab-watch-list_en.txt
printf "Generating the interesting tweet ranking for @%s... \n\n" "yasulab (Yohei)"
sleep 5	
python tweet-scorer/tweet-scorer.py log/tweets-by-yasulab_en.txt log/yasulab-watch-list_en.txt
