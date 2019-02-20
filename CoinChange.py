#-------------------------------------------
#function getCoinChange
def getCoinChange(money):
    strSumCoin = ''
    coinArray = [10, 7, 5, 3, 1]
    totalCoin = 0
    for i in coinArray:
        if money > 0:
            if int(money / i) > 0:
                numCoin = int(money / i)
                strSumCoin += '[' + str(i) + '] = ' + str(numCoin) + ' coins '
                money = money - (i * numCoin)
                totalCoin += numCoin
    strSumCoin = 'total coins = ' + str(totalCoin) + ' coins\nSolution is ' + strSumCoin
    return strSumCoin
#---------------------------------------------
#main()
inputVal = input ("Enter number : ")
answer = getCoinChange(int(inputVal))
print(answer)
#---------------------------------------------