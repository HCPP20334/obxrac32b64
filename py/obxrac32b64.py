import base64

def xor32(s_text: bytes, s_secret_key: bytes) -> bytes:
    if not s_secret_key:
        return s_text
    result = bytearray()
    key_len = len(s_secret_key)
    for i, byte in enumerate(s_text):
        c = byte ^ s_secret_key[i % key_len]
        result.append(c)
    return bytes(result)
def addc(s: int, i: str) -> str:
    result = []
    d = 0
    for c in i:
        result.append(c)
        d += 1
        if d == s:
            result.append("$$")
            d = 0
            
    return "".join(result)
def addce(s: str) -> str:
    return s.replace("$$", "")
def rvbstr(_key: str) -> str:
    hash_str = ""
    n = len(_key)
    for i in range(n):
        hash_str += _key[n - 1 - i]
    return hash_str
a = ""
b = ""
c = ""
def obxrac32b64(isDecode: bool, m0: str, m1:str)-> str:
    if (isDecode):
        a = base64.decode((m0))
        b = xor32(a, m1)
        b = addce(b)
        b = rvbstr(b)
    
    else:
        a = rvbstr(m0)
        a = addc(5, a)
        b = xor32(a, m1)
        b = base64.encode(b)
    
    return b


a = ""
b = ""
c = ""

def obxrac32b64(is_decode: bool, m0: str, m1: str) -> str:
    global a, b
    key_bytes = m1.encode('utf-8')
    
    if is_decode:
        a = base64.b64decode(m0) 
        b = xor32(a, key_bytes) 
        b = addce(b.decode('utf-8')) 
        b = rvbstr(b)
    else:
        a = rvbstr(m0)
        a = addc(5, a)
        b = xor32(a.encode('utf-8'), key_bytes)
        b = base64.b64encode(b).decode('utf-8')
    return b

def main():
    print("obxrac32b64 python build\n")
    print("e - encode\nd - decode\n")  
    cmd = input()
    dec = False if cmd == 'e' else True
    print("text:")
    text = input() 
    print("secret key:")
    key = input()
    result = obxrac32b64(dec, text, key)
    print("Result:", result)

if __name__ == "__main__":
    main()