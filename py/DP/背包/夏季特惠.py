# 夏季特惠
# 某公司游戏平台的夏季特惠开始了，你决定入手一些游戏
# 现在你一共有X元的预算，平台上所有的 n 个游戏均有折扣
# 标号为 i 的游戏的原价a_i元，现价只要b_i元
# 也就是说该游戏可以优惠 a_i - b_i，并且你购买该游戏能获得快乐值为w_i
# 由于优惠的存在，你可能做出一些冲动消费导致最终买游戏的总费用超过预算
# 只要满足 : 获得的总优惠金额不低于超过预算的总金额
# 那在心理上就不会觉得吃亏。
# 现在你希望在心理上不觉得吃亏的前提下，获得尽可能多的快乐值。
# 测试链接 : https://leetcode.cn/problems/tJau2o/



def compute():
    dp = [0] * (x + 1)
    for i in range(1, n + 1):
        for j in range(x, cost[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - cost[i]] + val[i])
    return dp[x]

n, x = list(map(int, input().split()))
val = [0] * (n + 1)
cost = [0] * (n + 1)
ans, m = 0, 0

for i in range(1, n + 1):
    a, b, w = list(map(int, input().split()))
    # 如下是一件"一定要买的商品"
    # 预算 = 100，商品原价 = 10，打折后 = 3
    # 那么好处(well) = (10 - 3) - 3 = 4
    # 所以，可以认为这件商品把预算增加到了104！一定要买！
    # 如下是一件"需要考虑的商品"
    # 预算 = 104，商品原价 = 10，打折后 = 8
    # 那么好处(well) = (10 - 8) - 8 = -6
    # 所以，可以认为这件商品就花掉6元！
    # 也就是说以后花的不是打折后的值，是"坏处"
    well = (a - b) - b
    if well >= 0:
        x += well
        ans += w
    else:
        val[m] = w
        cost[m] = -well
        m += 1
    ans += compute()
print(ans)
