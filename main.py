#! /usr/bin/env python
# -*- coding:utf-8 -*-
import harvard
import apa
import mla
print("Remember to input in the right form\nRemember to use \"None\" when you don't need that part in your reference")
a=input("harvard/apa/mla:")
n=int(input("number of references:"))
final_reference=[]
if a=="harvard":
    for i in range(0,n):
        final_reference.append(harvard.main())
    final_reference.sort()
if a=="apa":
    for i in range(0,n):
        final_reference.append(apa.main())
    final_reference.sort()
if a=="mla":
    for i in range(0,n):
        final_reference.append(mla.main())
    final_reference.sort()
print(final_reference)
with open("reference.txt","w",encoding="utf-8") as f:
    f.write("Reference List\n")
    for i in final_reference:
        f.write(i)
        f.write("\n\n")
print("done")
print("Thank for using")
input()