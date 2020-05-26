import securing_password

if __name__ == "__main__":
    n=input("Enter your password= ")
    print(f"Secured Password= {securing_password.secure_pass(n)}")