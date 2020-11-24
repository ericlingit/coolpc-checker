# coolpc-checker

Periodically check 原價屋 for updated Radeon RX6800XT availability status.


## emailer setup

https://developers.google.com/gmail/api/quickstart/python

https://developers.google.com/gmail/api/guides/sending


## Info
- url: http://coolpc.com.tw/eachview.php?IGrp=12
- css-selector: `.main > span:nth-child(2) > div:nth-child(2)`
- xpath: `/html/body/div[2]/span[2]/div[1]`

```html
<div class="t">華碩 Radeon RX6800XT-16G(2250MHz/26.7cm/註四年/三風扇) 『沒貨！炒作別來找』</div>

<div class="t">技嘉 Radeon RX6800XT 16G(2250MHz/26.7cm/註四年/三風扇) 『沒貨！睡醒了再說』</div>
```

- title includes: rx6800xt

- notify when:
    - '沒貨', '售完', '缺貨' not in title
    - show updated title
    - send notification email (include old+new title, time)
    - break loop

- check once every 30 minutes
