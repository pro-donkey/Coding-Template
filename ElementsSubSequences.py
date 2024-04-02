def SubSequences(pos, s, f):
  if pos == len(s):
    print(f + " ")
    return
  SubSequences(pos + 1, s, f + s[pos])
  SubSequences(pos + 1, s, f)


s = "abc"
ans = ""
print("All the Subsequences are : ")
SubSequences(0, s, ans)
