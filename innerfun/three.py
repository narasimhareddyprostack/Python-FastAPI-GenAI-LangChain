def outer():
    print("Outer function started")

    def inner():
        print("Inner Function")

    return inner 


inner = outer()
inner()
inner()
