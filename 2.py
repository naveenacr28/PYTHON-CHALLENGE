"""Given a string s, find the length of the longest substring with all unique characters.
Example
s = "abcabcbb" → longest unique substring = "abc" → length = 3"""

s = "aabcbb"

def funn(s):
        lenght = 0
        i=0
        seen=[]
        for i in range(0, len(s)-1):
                if s[i] not in seen:
                        seen.append(s[i])
                else:
                        print(seen)
                        print(f"lenght is {len(seen)}")
                        exit()

result = funn(s)