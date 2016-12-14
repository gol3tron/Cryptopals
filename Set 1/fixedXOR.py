def fixedXOR(stringx,stringy):
    # decode stringx
    hex_decode_x = bytes.fromhex(stringx).decode()

def hex2base64(hexstr):
    
    import base64
    
    # converts a hex string to base64
    raw = bytes.fromhex(hexstr)
    base64string = base64.b64encode(raw).decode()

    return base64string

def xorb(a,b):
    
    #xors two strings of raw bytes
    
    return bytes(x^y for x,y in zip(a,b))

