#! /usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
def geturl(authors,title,name,year,url):
    reference=[]
    if authors!="None":
        for author in authors:
            k=author.replace(" ",",")
            reference+=k+"."
    if year!= "None":
        reference+="("+str(year)+")."
    if title!= "None":
        reference+=title+","
    if name!= "None":
        reference+=name+"[online]."
    if url!="None":
        reference+="Available at:"+url+""
    reference+="[Accessed at "+str(datetime.datetime.now())[0:11]+"]"
    return ''.join(reference)
def getjournal(authors,title_article,title_journal,year,volume,page,part):
    reference=[]
    if authors!="None":
        for author in authors:
            author=str(author).title()
            author=author.replace(" ",",")
            reference+=author+"."
    if year!= "None":
        reference+="("+str(year)+")."
    if title_article!= "None":
        reference+=title_article+","
    if title_journal!= "None":
        reference+=title_journal+"."
    if volume!="None":
        reference+="VOL."+volume
    if part!= "None":
        reference+="("+part+")"
    if page!="None":
        reference+=",pp."+page
    return ''.join(reference)
def getbook(authors,title,place,publisher,year,edition,page):
    reference=[]
    if authors != "None":
        for author in authors:
            author = str(author).title()
            author = author.replace(" ", ",")
            reference += author + "."
    if year!= "None":
        reference += "(" + str(year) + ")."
    if title!= "None":
        reference += title+ "."
    if edition!="None":
        reference+=edition+" ed."
    if place!= "None":
        reference += place+":"
    if publisher!= "None":
        reference += publisher+"."
    if page != "None":
        reference +="pp."+page
    return ''.join(reference)
def main():
    a=input("do you wnat to referce website/journal/book:")
    if a=="website":
        authors=[]
        author_num=int(input("how many authors:"))
        i=1
        for i in range(author_num):
            i+=1
            print("Remember:\nfamily name should be first and the given name should be in one letter")
            print("eg: Smith T")
            authors.append(input("enter the author {}:".format(i)))
        title=input("please enter the title:")
        name=input("please enter the websites name:")
        name=name.title()
        year=input("please enter the year:")
        url=input("please enter the url:")
        print(geturl(authors,title,name,year,url))
        return geturl(authors,title,name,year,url)
    if a=="journal":
        authors = []
        author_num = int(input("how many authors:"))
        i=1
        for i in range(author_num):
            i+=1
            print("Remember:\nfamily name should be first and the given name should be in one letter")
            print("eg: Smith T")
            authors.append(input("enter the author {}:".format(i)))
        title_article=input("please enter the title of the article:")
        title_journal=input("please enter the title of the journal:")
        year=input("please enter the publish year:")
        volume=input("please enter the volume:")
        part=input("please enter the part:")
        page=input("please enter the page(eg:10-11):")
        print(getjournal(authors,title_article,title_journal,year,volume,page,part))
        return getjournal(authors,title_article,title_journal,year,volume,page,part)
    if a=="book":
        authors = []
        author_num = int(input("how many authors:"))
        i = 1
        for i in range(author_num):
            i+=1
            print("Remember:\nfamily name should be first and the given name should be in one letter")
            print("eg: Smith T")
            authors.append(input("enter the author {}:".format(i)))
        title = input("please enter the title:")
        edition = input("please enter the edition(eg:1st/2nd):")
        publisher = input("please enter the name of the publisher:")
        place = input("please enter the location of the publisher:")
        year = input("please enter the publish year:")
        page = input("please enter the page:")
        print(getbook(authors,title,place,publisher,year,edition,page))
        return getbook(authors,title,place,publisher,year,edition,page)
if __name__=="__main__":
    main()