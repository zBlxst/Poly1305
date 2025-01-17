# Poly1305

This is a working (I hope) implementation for Poly1305.

To use : python3 poly1305-gen.py aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa test.txt 
-> 00417e171fa98e4181c790a76bc1e58f

To use : python3 poly1305-check.py aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa test.txt 00417e171fa98e4181c790a76bc1e58f
-> ACCEPT

To use : python3 poly1305-check.py aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa test.txt 00417e171fa98e4181c790a76bc1e58e
-> REJECT