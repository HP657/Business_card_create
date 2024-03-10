from PIL import Image, ImageDraw, ImageFont
import base64
import io

def encoding(image):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)

    encoded_data = base64.b64encode(img_byte_array.getvalue()).decode('utf-8')
    return encoded_data

def decoing(image):
    decoded_data = base64.b64decode(image)
    return decoded_data

from PIL import Image, ImageDraw, ImageFont

def mak_card(job, ko_name, en_name, tel, email):
    W = 1050
    H = 600
    bg_color = 'rgb(255, 255, 255)'

    image =Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)

    # Load fonts
    font1 = ImageFont.truetype('BareunBatangB.ttf', size=25)
    font2 = ImageFont.truetype('BareunBatangB.ttf', size=35)

    # Draw text on the image
    draw.text((50, 300), job, font=font1, fill='#000000')
    draw.text((50, 340), f'{ko_name}│{en_name}', font=font2, fill='#000000')
    draw.text((50, 450), f'TEL│{tel}', font=font1, fill='#000000')
    draw.text((50, 510), f'E-mail│{email}', font=font1, fill='#000000')
    
    encoded_data = encoding(image)
    return encoded_data





