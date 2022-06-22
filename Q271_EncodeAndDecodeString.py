class Solution:
    
    def encode(strs):
        rese = (":;").join(strs)
        print(rese)
        return rese

    def decode(str):
        resd = str.split(":;")
        print(resd)
        return resd

    decode(encode(["lint","code","love","you"]))
