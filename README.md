# coolpc-checker

Periodically check 原價屋 for updated Radeon RX6800XT availability status.

## Info
- url: http://coolpc.com.tw/eachview.php?IGrp=12
- css-selector: `.main > span:nth-child(2) > div:nth-child(2)`
- xpath: `/html/body/div[2]/span[2]/div[1]`

- title includes: rx6800xt

- notify when:
    - 沒貨 not in title
    - 售完 not in title

    - show updated title
    - send notification email (include old+new title, time)
    - break loop

- check once every 30 minutes
