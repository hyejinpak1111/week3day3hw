class Items:
    def __init__(self, fish, drink, vegetable):
        self.fish = fish
        self.drink = drink
        self.vegetable = vegetable


class Shopping_cart:

    def __init__(self, fish, drink, vegetable, cart=[]):
        self.fish = fish
        self.drink = drink
        self.vegetable = vegetable
        self.cart = cart

    def add_cart(self, fish, drink, vegetable):
        new_items = Items(fish, drink, vegetable)
        self.cart.append(new_items)


    def print_receipt(self):
        print("=~ *15")
        print("Your Receipt: ")

        for item in self.cart:
            print(item.fish, item.drink, item.vegetable)
    
        print("=~ *15")


    def run(self):
        while True:
            try:
                fish = input("What kind of fish do you want for tonight?: ")
                if len(fish) < 4:
                    raise ValueError("Name input not valid, input should be 4 characters long.")
                        

                drink = input("What kind of drink do you want?: ")
                if len(drink) == 5:
                    raise ValueError("Out of order. Sorry for your inconvenience.")

                vegetable = input("What kind of vegetable do you want to buy?: ")
                    

                self.add_cart (fish, drink, vegetable)
                cont = input("Do you need anything else (y/n)? ")

                if cont == 'n':
                    break
                
            except Exception as error:
                print("There was an error, please try again later.")
                print(error)

        self.print_receipt()

your_cart = Shopping_cart('fish', 'drink', 'vegetable')
your_cart.run()