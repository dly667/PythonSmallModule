from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11559967'
API_KEY = 'ehhaRYCnGpRyY27n83VrPRlw'
SECRET_KEY = 'IlZqr30Fxy98FmFVEMbjG4ODFhFLuRt8'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('demo.jpg')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
aa = client.basicAccurate(image, options)
