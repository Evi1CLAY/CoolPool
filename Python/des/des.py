#coding:utf-8
import base64
from pyDes import *
# DES 加密解密工具
# 使用前需要配置 Des_key
# 无论加密解密输入文件从文本中读取
# 输出文件可以保存在文本中
# anka9080


Des_Key = "********" # Key need 8 letters

def read_file(filename):
  with open(filename) as input:
      text = input.read()
  return text

def write_file(secret,filename):
  with open(filename,'w') as output:
      output.write(secret)

def des_encrypt(text):
    k = des(Des_Key, pad=None, padmode=PAD_PKCS5)
    secret = k.encrypt(text)
    secret = base64.b64encode(secret)
    print secret
    return secret

def des_decrypt(secret):
    k = des(Des_Key, pad=None, padmode=PAD_PKCS5)
    secret = base64.b64decode(secret)
    text = k.decrypt(secret)
    print text
    return text

def main():

    ### ENCRYPT AREA
    text = read_file("123.txt")
    secret = des_encrypt(text)
    write_file(secret,"321.txt")

    ### DECRYPT AREA
    # secret = read_file("abc.txt")
    # plain = des_decrypt(secret)
    # write_file(plain,"cba.txt")
    

if __name__ == '__main__':
  main()

