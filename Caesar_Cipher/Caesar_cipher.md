# Caesar Cipher

## Introduction

Caesar Cipher is a substitution cipher in which each letter of alphabet shift by some fixed no. of position in the alphabet.

___

## History

It is named after the Roman Leader Julius Caeser who shift letter by 3 to protect his  military secrets 

___

## Principle

*Substitution*:- Every letter in original text is replaced by the another letter located a set number of steps away

*Shift(Key)* :- The no.of position shifted for a letter to be replaced by another, called Key of the cipher.It is represent by K

*Mathematical Aspect* :- It is based on modular arthimetic.
Let's assume *A* as 0 and *Z* as 25.

*Encryption*

```Encrytion
E(x)=(x+K)mod26
```
Here we use the key to add the key to the letter "x",and later use mod to find remainder left and remainder will be assign a value on the basis of above assumption

*Decryption*

```Decryption
D(x) = (x-K)mod26
```

Here we use the encrypted letter and key to subtract the key to the letter "x",and later use mod to find remainder left and remainder will be assign a value on the basis of above assumption

___

# Weakness

It is not cryptographically secure because due to the small key space of 26,make the brute force in it feasible and also due to one to one mapping of characters,there is also a feasible chance of frequency analysis



