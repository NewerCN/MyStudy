list1 = ['1.Just do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is Noting']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [name + ':' + slogan[2:] for slogan in list1 for name in list2  if name[0] == slogan[0]] 
for each in list3:
    print(each)
