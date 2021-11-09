from Crypto.Cipher import DES
def decrypt(msg, modo):
    des = DES.new(b'01020304', modo)
    
    return des.decrypt(msg)

