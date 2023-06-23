# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-8
# Topic  :-
# 1) Create 2 classes for single inheritance named respectively 
# A(base class) and B(derived class)
# 2) Create 3 data members in class A: a(private), b(protected) 
# and c(public) initialise their values in a parameterized 
# constructor
# 3) Create a method known as display in both the classes, to 
# display the values of a,b and c
# 4) While accessing the private member an exception should be 
# raised and a personalized message should be displayed and the 
# exception should be handled properly so that the rest of the 
# code can get executed
# Date   : 22-06-2023

# Program:-
class PrivateAccessError(Exception):
    
    def __init__(self,msg):
        super().__init__(msg);

class A:
    
    __a=None # Private
    _b=None  # Protected
    c=None   # Public
    
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def display(self):
        print("a =",self.a)
        print("b =",self.b)
        print("c =",self.c);

class B(A):

    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    
    def display(self):
        print("[Printing by display() of 'B' class :-]");

        try:
           if(self.a==self.a):
               raise PrivateAccessError("Private member cannot be access.")
           else:
               print("a =",self.a);
        except PrivateAccessError as pae:
           print(f"{type(pae).__name__} : {pae.args[0]}");
        
        print("b =",self.b)
        print("c =",self.c)
        print()
        print("[Printing by display() of 'A' class :-]");
        super().display();
        
# Driver code:- 
b=B(10,20,15);
b.display();

# Output:-
# [Printing by display() of 'B' class :-]
# PrivateAccessError : Private member cannot be access.
# b = 20
# c = 15
# 
# [Printing by display() of 'A' class :-]
# a = 10
# b = 20
# c = 15






