def read(a,b,c):
    file=open("Stock.txt","w")
    file.write(str(a))
    file.write(str("\n"))
    file.write(str(b))
    file.write(str("\n"))
    file.write(str(c))
    file.write(str("\n"))
    file.close()
