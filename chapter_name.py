#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/29 下午6:24
# @Author  : luoxing
# @Email   : 635541878@qq.com
# @File    : chapter_name.py
# @Software: PyCharm

number_dict={'一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10,'零':0,
             '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'0':0}
chinese_dict={1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九',10:'十',0:'零'}

def chapter_name_trans(str_chapter):
    str_rev=str_chapter[::-1]#将字符串翻转
    res=0#转成数字的章节号
    addcount=0
    allcount=0
    lost_add=0
    num_end=0
    num_begin=0
    count=0
    flag=0
    res_str=""
    for single_word in str_rev:
        if single_word in number_dict:
            if number_dict[single_word]!=10:
                res=res+number_dict[single_word]*pow(10,addcount)-lost_add
                addcount=addcount+1
                lost_add=0
            else:
                res=res+number_dict[single_word]
                if allcount==0:
                    addcount=addcount+1
                lost_add=10
            allcount=allcount+1
    res=res+1 #锁定下一章节
    for single_word in str_chapter:
        if single_word in number_dict and flag==0:
            num_begin=count
            num_end=count+allcount
            flag=1
            break
        count=count+1
    count=0
    for single_word in str_chapter:
        if count<num_begin:
            res_str=res_str+single_word
            break
        count=count+1
    if res<=10:
        res_str=res_str+chinese_dict[res]
    else:
        #假定res值不超过两位数
        tmp=int(res/10)
        if tmp==1:
            res_str=res_str+chinese_dict[10]
        else:
            res_str = res_str + chinese_dict[tmp] + chinese_dict[10]
        tmp=(res%10)
        if tmp!=0:
            res_str = res_str + chinese_dict[tmp]
    res_str=res_str+str_chapter[num_end]

    #print(res_str)
    return res_str

if __name__ == '__main__':
    print(chapter_name_trans('第十四章')) #passed
    print(chapter_name_trans('第一章'))  # passed
    print(chapter_name_trans('第二十四章'))  # passed
    print(chapter_name_trans('第二十2章'))  # passed
    print(chapter_name_trans('第12章'))  # passed
    print(chapter_name_trans('第十2章'))  # passed
    print(chapter_name_trans('第10章'))  # passed
    print(chapter_name_trans('第十章'))  # passed
    print(chapter_name_trans('第十九章'))  # passed
    print(chapter_name_trans('第一十章'))  # passed
    print(chapter_name_trans('第一十一章'))  # passed
    print(chapter_name_trans('第二十章'))  # passed
    print(chapter_name_trans('第零四章'))  # passed
    print(chapter_name_trans('第二零章'))  # passed
    print(chapter_name_trans('九、基金的'))  # passed
    print(chapter_name_trans('十、基金的'))  # passed
    print(chapter_name_trans('十五、基金的'))  # passed
    print(chapter_name_trans('二十、基金的'))  # passed
    print(chapter_name_trans('二十五、基金的'))  # passed
    print(chapter_name_trans('第二十五、基金的'))  # passed