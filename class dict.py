class dict:
    def dit(self):
        user_dict = {}
        n=int(input("enter the limit of dict"))
        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            user_dict[key] = value
        print(user_dict)
obj = dict()
obj.dit()