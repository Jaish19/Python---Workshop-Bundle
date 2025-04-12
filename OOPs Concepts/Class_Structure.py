class Flipkart:
    CLASS_NAME = "flipkart" # Global variables
    CLASS_ID = "#254EFT&W"
    def __init__(self, name, password):
      '''
      It's called constructor
      '''
        self.name = name    # instance variables
        self.password = password   #instance variables
        pass
    
    def buy(self):
      '''
      # Instance Method
      This method which helps to buy the product
      '''
        print("{} welcome. {} is valid".format(self.name, self.password))
        print(self.CLASS_NAME)  # Way to class variable
        print("Here you can find the products")
    
    def sell(self):
      '''
      # Instance Method
      This method which helps to sell the product
      '''
        print("{} welcome. {} is valid".format(self.name, self.password))
        print("Here you can sell the products")
        
obj = Flipkart("Jai", 1234) # Obj initialiazation
obj.buy() # Method call
        
