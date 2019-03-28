def computeMD5hash(string):
    import hashlib
    from hashlib import md5
    m = hashlib.md5()
    m.update((string))
    md5string=m.digest()
    return md5string
#rishi
