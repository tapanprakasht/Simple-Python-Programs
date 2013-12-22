#!/usr/bin/python3
import base64
def main():
   encode=base64.b64encode(b'tapanprakasht')
   print(encode)
   print(str(base64.b64decode(encode)))
if __name__=="__main__":main()