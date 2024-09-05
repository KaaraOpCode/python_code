import hashlib

i = 0
while(True):

    plaintext = '0e%d' % i
    m = hashlib.md5()
    m.update(plaintext.encode('utf-8'))
    h = m.hexdigest()

    if h.startswith('0e'):
        if h[2:].isdigig():
            print(plaintext,h)
            break
       
        i += 1