def login_req(func):
    def inner(name,status):
        if status != True:
            print("Login Required")
        else:
            func(name,status)

    return inner

def index(name,status):
    print("Index Page")
@login_req
def product_page(name,status):
    print("Product Page")

@login_req
def order_page(name,status):
    print("Order Page")
@login_req
def profile_page(name,status):
    print("Profile Details")

index("RG",False)
product_page("RG",True)
order_page("RG",False)
profile_page("RG",False)