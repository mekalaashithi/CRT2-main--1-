#1248,1763
'''1763. Longest Nice Substring'''

def longestNiceSubstring(s: str) -> str:
    if len(s)<2:
        return ""
    uni=set(s)
    for i,ch in enumerate(s):
        if ch.lower() in uni and ch.upper() in uni:
            continue
        left=longestNiceSubstring(s[:i]) 
        right=longestNiceSubstring(s[i+1:])
        if len(left)>=len(right):
            return left
        else:
            return right
    return s
s1="YazaAay"
s2="Bb"
s3="c"
print(longestNiceSubstring(s1))
print(longestNiceSubstring(s2))
print(longestNiceSubstring(s3))
