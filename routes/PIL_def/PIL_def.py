from PIL import Image, ImageDraw, ImageFont

def create_card(직군, 이름, 영어이름, 전화번호):
    W = 1250
    H = 600
    bg_color = 'rgb(255, 255, 255)'

    image =Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)

    font1 = ImageFont.truetype('BareunBatangB.ttf', size=25)
    font2 = ImageFont.truetype('BareunBatangB.ttf', size=35)
    draw.text((50, 300), 직군, font=font1, fill='#0000')
    draw.text((50, 340), f'{이름}│{영어이름}', font=font2, fill='#0000')

    draw.text((50, 450), f'TEL│{전화번호}', font=font1, fill='#0000')
    draw.text((50, 480), 'GitHub│@HP657', font=font1, fill='#0000')
    draw.text((50, 510), 'E-mail│junlee5070@gmail.com', font=font1, fill='#0000')

    image.save(f"cards/{이름}님의 명함.png")


