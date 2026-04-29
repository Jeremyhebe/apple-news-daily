from PIL import Image, ImageDraw, ImageFont

# 创建 1200x630 的图片
img = Image.new('RGB', (1200, 630), '#1d1d1f')
draw = ImageDraw.Draw(img)

# 加载 Apple favicon 作为 logo
logo_path = '/Users/jeremy.yang/WorkBuddy/20260319004420/apple-favicon.ico'
logo = Image.open(logo_path)
logo = logo.convert('RGBA')

# 放大 logo 到 280x280
logo = logo.resize((280, 280), Image.Resampling.LANCZOS)

# 居中粘贴
img.paste(logo, (460, 145), logo)

# 底部添加文字
try:
    font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
    font_light = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except:
    font = ImageFont.load_default()
    font_light = ImageFont.load_default()

# 标题
draw.text((600, 480), "Apple 每日热点资讯", fill='white', font=font, anchor='mm')
# 副标题
draw.text((600, 530), "每日 09:15 自动更新", fill='#888888', font=font_light, anchor='mm')

# 保存
img.save('/Users/jeremy.yang/WorkBuddy/20260319004420/og-image.png', 'PNG')
print('Created og-image.png with text at bottom')
