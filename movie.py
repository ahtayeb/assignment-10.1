# abdul tayeb
# assignment 10.1 In this assignment, I will implement my own class based on a real-world object. 
# I will write a class to meet certain requirements and write a short demo program in the main function that highlights all your class variables and methods.

#defining the Movie class
class Movie:

    #defining class variables
    title="Interstellar"
    genre="horror"
    mode="OTT"
    length=2.5
    price="10"

    def __init__(self, __title, __mode, __genre, __length, __price):
        #defining private data variables
        self.title = __title # to store the movie title
        self.mode = __mode # to store the mode of viewing
        self.genre = __genre # to store the movie genre
        self.length = __length # to store the movie duration in hours
        self.price = __price # to store the base price in dollars

    #setter methods for all instance variables

    def set_title(self, title):
        self.title = title

    def set_mode(self, mode):
        self.mode = mode

    def set_genre(self, genre):
        self.genre = genre

    def set_length(self, length):
        self.length = length

    def set_price(self, price):
        self.price = price

    #getter methods for all instance variables

    def get_title(self):
        return self.title

    def get_mode(self):
        return self.mode

    def get_genre(self):
        return self.genre

    def get_length(self):
        return self.length

    def get_price(self):
        return self.price

    #method to calculate and display final movie price inclusive of all taxes

    def computePrice(self):
        #variable tax set to private for storing fixed tax of 10%
        __tax = 10
        #conversion of self.price from string to float
        if(self.mode=="OTT"):
            return f"Your total would be ${float(self.price) + (__tax/100*float(self.price))}"

        else:
            return f"Your total would be ${float(self.price) + (__tax/100*float(self.price))} and the ride and parking charges given you don't buy snacks at the intermission"

    #method to display how long a movie feels to the audience

    def howLong(self):

        __len = float(self.length) # private variable that stores the length of the movie in floating point value for simple if condition check
        if(__len>2.5):
            return "This movie is wayy too long"

        elif(__len>2 and __len<=2.5):
            return "This movie is pretty long"

        elif(__len<=2 and __len>1):
            return "This movie has just the right duration"

        else:
            return "This movie would be over in jiff"

    #method to display a message based on genre


    def customMessaage(self):
        if(self.genre=="horror"):
            return "DO NOT watch this alone at 3am"

        elif(self.genre=="romantic"):
            return "Hopefully you have a partner so you won't feel single while watching this"

        elif(self.genre=="thriller"):
            return "I see you love the thrill!"

        elif(self.genre=="drama"):
            return "Occasional dose of drama to keep your sanity"

        elif(self.genre=="action"):
            return "Action-packed dopamine rush"

        elif(self.genre=="comedy"):
            return "As they say laughter is the best medicine"

        # by default response
        else:
            return "Great choice! Enjoy your movie!"

#defining the main function

def main():

    __c = 1 # private variable to act as user choice
    while(__c!=0):
        # creating a movie object without giving any values for initialization as we are going to manually set them using setter methods
        movie = Movie("", "", "", "", "")
        #implementation of all class methods
        name = input("Enter movie name:\n")
        mode = input("Enter mode, OTT or Theatre:\n")
        genre = input("Enter movie genre:\n")
        length = input("Enter movie duration in hours:\n")
        price = input("Enter movie base price in dollars:\n")
        # setting all values based on user input
        movie.set_title(name)
        movie.set_mode(mode)
        movie.set_genre(genre)
        movie.set_price(price)
        movie.set_length(length)
        # printing all values using getter methods
        print("\n-----------------------------------------\n")
        print(f"Your chosen movie is - {movie.get_title()}\nMode - {movie.get_mode()}\nGenre - {movie.get_genre()}\nLength - {movie.get_length()} hours\nPrice - ${movie.get_price()}\n")
        # calling two other methods
        print("\n-----------------------------------------\n")
        # calling two other methods
        print(movie.customMessaage(),'\n')
        print(movie.howLong(),'\n')
        print(movie.computePrice(),'\n')
        __c = int(input("Press 1 to input another movie and 0 to exit\n"))
        # if user presses 0 exit the loop else continue
        if(__c==0):
            break
    
#calling main function
if __name__ == "__main__":
    main()
        


