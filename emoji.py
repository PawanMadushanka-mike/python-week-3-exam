import emoji

def main():
    user_input=input("Input: ")
    result=emoji.emojize(user_input,language='alias')
    print(f"Output: {result}")

if __name__=="__main__":
    main()

