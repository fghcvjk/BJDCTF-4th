#encoding:utf-8
from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
import gmpy2, os
from Crypto.Cipher import AES
from flag import flag

assert flag.startswith("DASCTF{") and flag.endswith("}")

def padding(s,blocklen):
    length = (blocklen-len(s)) % blocklen
    return s + chr(length) * length

key = os.urandom(16)
iv = os.urandom(16)
m = padding(flag,16)
c = AES.new(key, AES.MODE_CBC, iv).encrypt(m)
print c.encode("hex")

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537
m = bytes_to_long(key)
c = pow(m,e,n)
print hex(n).strip("L")
print hex(c).strip("L")
q = getPrime(512)
n = p*q
m = bytes_to_long(iv)
c = pow(m,e,n)
print hex(n).strip("L")
print hex(c).strip("L")

'''
f8559d671b720cd336f2d8518ad6eac8c405585158dfde74ced376ba42d9fe984d519dc185030ddec7b4dc240fd90fa8
0x661d752110bcc6ee5ca33edaf244716cccce6400dfdbfd84ce6ae2d8fbbeb2f61584da7668768403b6135e7810eae9d4d8e044935f8680de5324c3fc0f9bffb01812f9d2ac9055ee8dbd17b90c5a60cb7595a82f24a075d951db3b7f913b8543ecd52b8c8464ce348c3970d511ae911e814f9ca33b8412db2730e61820f5de47
0xd7931796fa39cfa37c0b621c01175904206dff1d74a28369dcd6517957ed76c5eb7d4934cbeb902119f9215f9ae7926debe3abe856244b45dbb4caaa2b93dbb79a3ca1a9813e1466c49fe3c03e5462811afbf3f40ff79927f9fe3681b7f3cef34466b9a736512f4931b5026eefacbae9be6e408085a7a636c514574c3b22ffe
0x9f159326c907441326c88d17eae1c6e8aaea23922c5e628a585294e379e9245644f9c249c57f54a2b83921b4adc988fecc90c00feb6936d9be1f3a5ffae951b74ffbc6fc7aa11743e4ca179a937392dacf931e820d1d83016562ff608e8c59ef7310654a09bbba4a0129f71dcb61bd9bef073bbb93bfcac4a7a2e81156dbb32d
0x6240740d41a539a88634726cf0a791a87e02419c3c3e00dff62eba59e81a93fd04a59109e57f64fc375b9a321583b6fa133317eb5c4e6eb1e6f6d9a0b4ae6ff0c54423718811f7956cd63b7bf9c7f8e29f48dad8f05b63b71d6c5112d91864adba0d6bb342c67aee39ccd5e2a6928a8e4ab2248d29a0c990bae821b31b39b1f3
'''