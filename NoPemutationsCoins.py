def Toss(n, ans):
  if n == 0:
    print(ans)
    return

  Toss(n - 1, ans + "H")
  Toss(n - 1, ans + "T")


ans = ""
noCoins = 3

Toss(noCoins, ans)
