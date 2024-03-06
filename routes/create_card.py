from PIL import Image, ImageDraw, ImageFont
import base64
import io

def encoding(image):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    encoded_data = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')
    return encoded_data


def set_card():
    W = 1050
    H = 600
    bg_color = 'rgb(255, 255, 255)'

    image =Image.new('RGB', (W, H), color = bg_color)

    encoded_data = encoding(image)
    return encoded_data

from PIL import Image, ImageDraw, ImageFont

def mak_card(직군, 이름, 영어이름, 전화번호):
    # Create a blank image with a white background
    image = Image.new('RGB', (600, 600), 'white')
    draw = ImageDraw.Draw(image)

    # Load fonts
    font1 = ImageFont.truetype('BareunBatangB.ttf', size=25)
    font2 = ImageFont.truetype('BareunBatangB.ttf', size=35)

    # Draw text on the image
    draw.text((50, 300), 직군, font=font1, fill='#000000')
    draw.text((50, 340), f'{이름}│{영어이름}', font=font2, fill='#000000')
    draw.text((50, 450), f'TEL│{전화번호}', font=font1, fill='#000000')
    draw.text((50, 510), 'E-mail│junlee5070@gmail.com', font=font1, fill='#000000')
    
    encoded_data = encoding(image)
    return encoded_data


# draw.text((50, 480), 'GitHub│@HP657', font=font1, fill='#0000')



