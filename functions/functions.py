score = 0

input("Hello and welcome to my quiz!")
input("\nI'm going to say a series of statements. Your job is to guess true or false.")
input("\nGet them right, and you are a very smart person, well done.")
input("\nGet them wrong and I don't care.")
input("\nPlease answer all questions with a 't' for true or an 'f' for false.")
input("\nI haven't bothered validating your response so everything will break if you do anything else.")
input("\nThey are going to be zoology related statements... fun!")

var = input("\nFirst statement. Kleptoparasitism is a form of feeding whereby one animal takes the food that another animal has collected.")


        
if var == "t":
    input("\nSo smart!")
    score += 1
else:
    input("\nOoooh no good I'm afraid.")



var = input("\nNext question. Pseudopods is the term given to large pods of dolphins and other cetaceans that only exist for short periods of time before breaking into their original, close nit family pods.")



if var == "t":
    input("\nOoooh no good I'm afraid.")
else:
    input("\nSo smart!")
    score += 1



input("\nPseudopods are a like the foot of an amoeba. They create a cytoplasmic 'foot' which they push out and drag themselves around with.")
var = input("\nFinal statement! Dogs are better than cats.")



if var == "t":
    input("\nSo smart!") 
    score += 1
else:
    input("\nOoooh no good I'm afraid.")


    
if score == 3:
    input("\nYou got 3/3, it was almost like this was easy!")
elif score == 2:
    input("\nYou got 2/3, it's alright I guess.")
elif score == 1:
    input("\nYou got 1/3, poor effort.")
else:
    input("\n0/3. lol")
   

