# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:12:43 2018
Implementing Stacks with Python
Stack size allocation can be done at runtime
@author: ch@tur
"""

max_stack=0

class my_stack:
    stck=[]
    top=0
    def push_stack(self):
        if self.top >=max_stack:
            print("Stack Overflow")
            return
        else:
            ele=input("Enter element to PUSH: ")
            self.stck.insert(self.top, ele)
            self.top+=1
            print("Element ",ele," PUSHED successfully")
            return
    
    def pop_stack(self):
        if self.top<=0:
            print("Stack Underflow")
            return
        else:
            temp=self.stck[self.top-1]
            del self.stck[self.top-1]
            self.top-=1
            print("Element ",temp," POPED successfully")
            return
    
    def print_stack(self):
        if len(self.stck)==0:
            return "Stack is empty"
        else:
            stckr="|"
            for x in self.stck:
                stckr+=x+"|"
            stckr+="<-TOP"
            return stckr

st=my_stack()
print("Welcome to Stack")
size=int(input("Enter size of stack: "))
max_stack=size
while(True):
    print("0. Exit")
    print("1. PUSH")
    print("2. POP")
    print("3. Print Stack")
    choice=input("Enter your Choice: ")
    if choice=='0':
        print("Exiting program...")
        break
    elif choice=='1':
        print("PUSHING element...")
        st.push_stack()
        print()
    elif choice=='2':
        print("POPING element...")
        st.pop_stack()
        print()
    elif choice=='3':
        print("Printing stack entries...")
        stacker=st.print_stack()
        print(stacker)
        print()
    else:
        print("Invalid entry")
        print()