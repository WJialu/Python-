# BMI = 体重（kg）/(身高(m) **2 )

while(1):
    tizhong = float(input("输入体重(单位：KG)： "))
    shenggao = float(input("输入身高(单位：M)： "))
    bmi = tizhong / (shenggao ** 2)
    if bmi >= 30:
        print("你太胖了")
        print("BIM = "+str(bmi))
    else:
        print("还可以")
        print("BIM = "+str(bmi))