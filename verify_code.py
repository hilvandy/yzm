from aip import AipOcr
import cv2
import base64

# 百度OCR API参数
APP_ID = '115977876'
API_KEY = 'OTCi6vMH3dHtsJw1avsKvDl6'
SECRET_KEY = '3RmRAD5IEk4LASVq0d0QpyVUgZWrwc3d'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def recognize_captcha(image_path):
    # 读取图片
    with open(image_path, 'rb') as f:
        image = f.read()
    
    # 调用通用文字识别（高精度版）
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }
    result = client.basicAccurate(image, options)
    
    # 提取识别结果
    if 'words_result' in result:
        words = [w['words'] for w in result['words_result']]
        return ''.join(words)
    else:
        return ''

# 使用示例
captcha_path = 'C:/Users/AA226/Desktop/小工具/yzm/vertifyCode.jfif'
recognized_text = recognize_captcha(captcha_path)
print(f'识别结果: {recognized_text}')
