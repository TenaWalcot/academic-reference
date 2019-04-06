#! /usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
def get_journal(authors,journal,title,year,volume,page):
    reference = []
    if authors != "None":
        for author in authors:
            author = str(author).title()
            author = author.replace(" ", ",")
            reference += author + "."
    if title != "None":
        title="\""+title+"\""
        reference += title + ","
    if journal != "None":
        journal=str(journal).title()
        reference += journal + " "
    if volume != "None":
        reference +=volume+" "
    if year != "None":
        reference += "(" + str(year) + "):"
    if page != "None":
        reference +=page+"."
    return ''.join(reference)
def getbook(authors,title,place,publisher,year,edition):
    reference=[]
    if authors != "None":
        for author in authors:
            author = str(author).title()
            author = author.replace(" ", ",")
            reference += author + "."
    if title!= "None":
        reference += title+ "."
    if edition!="None":
        reference+=edition+" ed."
    if place!= "None":
        reference += place+":"
    if publisher!= "None":
        reference += publisher+","
    if year!= "None":
        reference +=str(year)+"."
    return ''.join(reference)
def geturl(authors,title,name,year,url):
    reference=[]
    if authors!="None":
        for author in authors:
            k=author.replace(" ",",")
            reference+=k+"."
    if title!= "None":
        reference+="\""+title+"\""
    if name!= "None":
        reference+=name+"."
    if year!= "None":
        reference+=str(year)+". "
    reference+=str(datetime.datetime.now())[0:11]
    if url!="None":
        reference+="<"+url+">"
    return ''.join(reference)
def main():
    a=input("do you wnat to referce website/journal/book:")
    if a=="website":
        authors=[]
        author_num=int(input("how many authors:"))
        i=1
        for i in range(author_num):
            i+=1
            print("Remember to enter the full name")
            print("eg: Stewart Donald C")
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
            print("Remember to enter the full name")
            print("eg: Stewart Donald C")
            authors.append(input("enter the author {}:".format(i)))
        title_article=input("please enter the title of the article:")
        title_journal=input("please enter the title of the journal:")
        year=input("please enter the publish year:")
        volume=input("please enter the volume:")
        page=input("please enter the page(eg:10-11):")
        print(get_journal(authors, title_journal, title_article,year, volume, page))
        return get_journal(authors, title_journal, title_article,year, volume, page)
    if a=="book":
        authors = []
        author_num = int(input("how many authors:"))
        i = 1
        for i in range(author_num):
            i+=1
            print("Remember to enter the full name")
            print("eg: Stewart Donald C")
            authors.append(input("enter the author {}:".format(i)))
        title = input("please enter the title:")
        edition = input("please enter the edition(eg:1st/2nd):")
        publisher = input("please enter the name of the publisher:")
        place = input("please enter the location of the publisher:")
        year = input("please enter the publish year:")
        print(getbook(authors,title,place,publisher,year,edition))
        return getbook(authors,title,place,publisher,year,edition)
if __name__=="__main__":
    main()