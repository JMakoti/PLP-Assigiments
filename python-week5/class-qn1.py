
#creating class Book , adding attributes and methods ,
# use constructor and adding inheritance layer to explore polymorphism or encapsulation

class Book:
    def __init__(self,title,author,published):
        self.title = title
        self.author = author
        self.published = published

    #Method
    def __str__(self):
        return (f"{self.title} written by {self.author}, {self.published}")

class Reviewed(Book):
    def __init__(self,title,author,published, reviwer): #override parent init
        # Book.__init__(self,title,author,published)
        super().__init__(title,author,published) #added init from parent
        self.reviwer = reviwer
        
    #Method -overides parent method to add details(polymorphism)
    def __str__(self):
        return (f"{self.title} written by {self.author}, {self.published} was reviwed by {self.reviwer}")
    
    #objects
reviewedBook = Reviewed("Swallowed Star","Li Hu",2010,"Joseph")
print(reviewedBook)

        
