
def most_frequent(sentence):
    a = s.count("i")
    b = s.count("s")
    c = s.count("p")
    d = s.count("M")
    Dict = {"M":d , "i":a, 's':b, 'p':c}
    print(f'''i = 0{(Dict["i"])}, s = 0{(Dict["s"])}, p = 0{(Dict['p'])}, m = 0{(Dict['M'])}''' )

s = input("Please Enter a String ")
most_frequent(s)

