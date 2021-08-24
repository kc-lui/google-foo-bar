import base64

MESSAGE = '''
EERdGRYKCQYaTEMUTFIOHhAIH0QCTFIKAxkFDgJJGRBOTE9JTAZdGBAMARANTE8OSxAPChobHxAJ TE9JSxwHCBFLCBwLABBOR0MJDRYBBRAfDg5LAgFOTE9JTBZAABoKBxANTE8OSwcIDhcAHxAJTE9J SwYIDQYJQFVOChoGTEMUTFIeBRtITB4=
'''

KEY = 'kc.luilui'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
