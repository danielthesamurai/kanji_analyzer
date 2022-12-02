import collections

n5_kanji = ['日','一','人','国','年','大','十','二','本','中','出','三','見','月','長','生','五','時','上',
            '行','四','後','金','前','九','入','学','間','円','子','東','八','六','下','今','気','小','七',
            '高','山','女','外','百','先','名','川','千','来','水','男','話','校','北','土','午','木','車',
            '書','半','白','天','西','電','火','語','右','左','聞','休','食','何','南','万','毎','雨','母',
            '読','友','父']
n4_kanji = ['会','同','自','事','社','力','立','手','地','田','方','発','目','場','者','業','明','新','正',
            '京','公','通','員','理','体','開','文','問','代','作','用','動','言','強','野','思','家','主',
            '題','町',"意","心","度","教","持","多","口","元","近","考","画","海","早","売","不","世","空",
            "知","院","計","足","界","字","音","朝","以","台","広","道","安","重","赤","青","エ","止","集",
            "物","切","使","品","死","始","楽","運","少","終","花","住","親","真","有","別","夕","急","送",
            "特","答","夜","転","店","帰","研","歌","図","室","究","歩","風","紙","起","着","黒","病","春",
            "待","族","料","銀","建","色","走","秋","医","仕","夏","去","味","犬","古","写","買","週","私",
            "注","試","悪","験","英","館","屋","曜","質","肉","鳥","習","冬","昼","茶","洋","弟","旅","牛",
            "映","兄","服","妹","駅","姉","勉","魚","借","飲","飯","漢","貸","堂"]
n3_kanji = ['政',"内","議","対","部","連","米","合","市","相","定","回","民","当","実","決","全","選","表",
            "調","化","関","首","数","記","戦","最","点","活","石","原","期","交","取","和","約","平","経",
            "法","組","受","要","現","治","成","指","直","機","加","性","制","予","向","都","勝","務","面",
            "続","反","初","進","引","次","王","係","共","番","感","投","打","両","式","支","参","利","談",
            "信","報","形","流","局","側","放","得","求","解","資","昨","球","際","官","権","告","役","変",
            "産","草","由","判","所","済","果","消","神","在","必","件","科","配","争","任","位","育","置",
            "想","増","声","情","示","認","助","追","商","葉","園","落","確","馬","付","頭","容","負","演",
            "夫","論","能","守","美","命","福","格","過","船","害","横","深","常","申","様","席","港","状",
            "残","職","念","構","光","路","労","例"]
n2_kanji = ['党']
n1_kanji = ['氏']

total_dict = {}
n5_dict = {}
n4_dict = {}
n3_dict = {}
n2_dict = {}
n1_dict = {}

n5_counter = 0
n4_counter = 0
n3_counter = 0
n2_counter = 0
n1_counter = 0

def open_file():
    filename = input("enter the name of the file you wish to assess (or press q to quit): ")
    if filename.lower() == "q":
        quit()
    try:
        with open(filename,encoding='UTF-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("file not found, try again!")
        return open_file()
    except UnicodeDecodeError:
        print("please choose a valid file type")
        return open_file()
    else:
        return contents
    
def choose_display():
    choice = input("n1, n2, n3, n4, n5, or overall?: ")
    input_choices = {"n1":n1_dict,"n2":n2_dict,"n3":n3_dict,"n4":n4_dict,"n5":n5_dict,"overall":total_dict}
    try:
        display_list = collections.Counter.most_common(input_choices[choice])
        num1 = int(input("enter a starting place: "))
        num2 = int(input("enter an ending place: "))
        print(display_list[num1:num2:])
    except KeyError:
        print("that's not a valid input. try again.")
        choose_display()

content = open_file()

for kanji in n5_kanji:
    n5_counter += content.count(kanji)
    n5_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n4_kanji:
    n4_counter += content.count(kanji)
    n4_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n3_kanji:
    n3_counter += content.count(kanji)
    n3_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n2_kanji:
    n2_counter += content.count(kanji)
    n2_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
for kanji in n1_kanji:
    n1_counter += content.count(kanji)
    n1_dict[kanji] = content.count(kanji)
    total_dict[kanji] = content.count(kanji)
    
print(f"n1 kanji amount: {n1_counter}, n2 kanji amount: {n2_counter}, n3 kanji amount: {n3_counter}, n4 kanji amount: {n4_counter}, n5 kanji amount: {n5_counter}")

total_sum = n1_counter+n2_counter+n3_counter+n4_counter+n5_counter

print(f"total amount of kanji: {total_sum}")

if total_sum > 0:
    print(f"{int((n5_counter/total_sum)*100)}% N5, {int((n4_counter/total_sum)*100)}% N4, {int((n3_counter/total_sum)*100)}% N3,{int((n2_counter/total_sum)*100)}% N2, {int((n1_counter/total_sum)*100)}% N1")
else:
    print("please choose a file that has japanese in it!")
    open_file()

choose_display()