alias play_r1='omxplayer --timeout 60s -o local https://nhkradiobkr1-i.akamaihd.net/hls/live/512291/1-r1/1-r1-01.m3u8'
alias play_r2='omxplayer --timeout 60s -o local https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8'
alias record_r1='ffmpeg -i https://nhkradiobkr1-i.akamaihd.net/hls/live/512291/1-r1/1-r1-01.m3u8 -t 900 -movflags faststart -c copy -bsf:a aac_adtstoasc radio_english_r1.m4a'
alias record_r2='ffmpeg -i https://nhkradioakr2-i.akamaihd.net/hls/live/511929/1-r2/1-r2-01.m3u8 -t 900 -movflags faststart -c copy -bsf:a aac_adtstoasc radio_english_r2.m4a'
