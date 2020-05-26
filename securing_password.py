def secure_pass(input_pass):
    special_characters=(("a","@"),("s","$"),("I","|"),("v","^"),("x","*"),("an","@)"),("r","~"),("m","^^"),("1","!"),("8","2`"),("and","&"),("c","("),("M",","),("A","."),("t","?"))
    for i in special_characters:
            if (i[0] in input_pass):
                input_pass=input_pass.replace(i[0],i[1])
    return input_pass         

if __name__ == "__main__":
    n=input("Enter your password= ")
    print(f"Your Secured Password= {secure_pass(n)}")
