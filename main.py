import time
from sites import (beebom, digit, gadgetsnow)

# initiate all sites
beebom = beebom.Beebom()
digit = digit.Digit()
gadgetsnow = gadgetsnow.GadgetsNow()

# get all posts from all sites
beebom_post = beebom.latest_post()
digit_post = digit.latest_news()
gadgetsnow_post = gadgetsnow.get_latest_news()


while True:
    # Beebom
    # curr_time = int(time.time())
    new_post_beebom = beebom.latest_post()
    if new_post_beebom['time'] > beebom_post['time']:
        print('Found new post on Beebom!', new_post_beebom)
        beebom_post = new_post_beebom
    else:
        print('No new post found on beebom')

    # Digit
    curr_title = digit_post['title']
    new_post_digit = digit.latest_news()
    if curr_title != new_post_digit['title']:
        print('New Post found on digit!', new_post_digit)
        digit_post = new_post_digit
    else:
        print('No new post found on digit')

    # GadgetsNow
    new_post_gn = gadgetsnow.get_latest_news()
    if new_post_gn['time'] > gadgetsnow_post['time']:
        print('New post found on Gadgets Now', new_post_gn)
        gadgetsnow_post = new_post_gn
    else:
        print('No new post found on GadgetsNow!')
    
    time.sleep(60)
    
