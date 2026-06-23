def outer():
    print("Outer function started")

    def login():
        print("Login Success")

    return login

inner=outer()
inner()
inner()
inner()
inner()
""" print(result)
print(type(result)) """