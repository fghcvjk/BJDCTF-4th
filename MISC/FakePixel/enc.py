from PIL import Image
import math

def encode(text):
  length = len(text)
  width = math.ceil(length**0.5)
  picture = Image.new("RGB",(width, width), 0x0)
  
  x,y = 0,0
  for i in text:
    index = ord(i)
    rgb = (0, (index & 0xFF00)>> 8, index & 0xFF)
    picture.putpixel((x, y),rgb)
    if x == width - 1:
       x = 0
       y += 1
    else:
       x += 1
  return picture

if __name__ == '__main__':
  with open("secret.txt",encoding = "utf-8") as f:
    all_text = f.read()
    
    picture = encode (all_text)
    picture.save("FakePicture.bmp")