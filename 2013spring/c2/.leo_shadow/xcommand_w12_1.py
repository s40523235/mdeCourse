#@+leo-ver=4-thin
#@+node:amd.20130513215328.2671:@shadow c2/command_w12_1.py
#coding=utf-8
class 求平均(object):
    def 求平均值(self, 幾個輸入):
        self.幾個輸入 = 幾個輸入
        總數 = 0
        # 準備取幾個輸入數值
        for 索引 in range(0,self.幾個輸入,1):
            數值 = input("第"+str(索引+1)+"次請輸入數值:")
            總數 = 總數 + float(數值)
        # 已經取得數值, 確認是否取到數值
            #print("所輸入的數值型別為:", 數值)
        #print(總數)
        # 準備利用幾個輸入數值求取平均值
        平均值 = 總數/self.幾個輸入
        # 準備將所求到的平均值列出給使用者
        print(str(self.幾個輸入)+"個數值平均值為:"+str(平均值))

輸入 = 2
# 利用"求平均"物件建立一個案例, 名稱為"平均"
平均 = 求平均()
# 執行平均案例中的"求平均"方法
平均.求平均值(輸入)
#@nonl
#@-node:amd.20130513215328.2671:@shadow c2/command_w12_1.py
#@-leo
