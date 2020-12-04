def reverse(st):
    lt = []
    for i in range(0, len(st)):
        if st[i] == " ":
            lt.append(st[i])
        else: 
            k = i
            while st[k] != " ":
                lt.append(st[i:k])
                k += 1
    print(lt)

print(reverse("  rsadliesirqspeogwiqiyqw  gah doeotjdwpewwfto ssswqgrwoqtrjstffadkwpjpfdo aygjrgtyk"))


'''    ch = st.split("  ")
    print(ch)
    for i in ch:
        if i == "":
            i = " "
    ch.reverse()
    st = "  ".join(ch)
    return st
'''
