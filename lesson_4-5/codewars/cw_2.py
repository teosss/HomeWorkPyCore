# Reversing Words in a String
# https://www.codewars.com/kata/57a55c8b72292d057b000594

def reverse(st):
    ch = st.split(" ") 
    for i in range (ch.count("")):     
        ch.remove("")
    ch.reverse()
    st = " ".join(ch)
    return st