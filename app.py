import math
import random

word_list = {
  5: ["whizz", "fuzzy", "quick", "quiff", "juked", "puked"],
  6: ["fizzes", "buzzes", "sizzle", "jumper", "jabber", "quiver"],
  7: ["quizzes", "buzzcut", "schmuck", "quaking", "junkies", "gimmick"],
  8: ["quantify", "kickball", "squiggle", "scramjet", "jammiest", "backfill"]
}

max_guesses = 3
guesses = 0 # guesses taken
difficulty = 5 # letters in word
answer = word_list[difficulty][math.floor(random.random() * len(word_list[difficulty]))]
game_won = False

# print(answer)

def get_alike(guess, answer):
    guess_array = list(guess)
    answer_array = list(answer)
    number_matches = 0

    for i,letter in enumerate(answer_array):
        if i > len(guess_array):
            # we know answer_array is longer than guess_array, stop comparing
            break
        if i <= len(guess_array)-1 and letter == guess_array[i]:
            # we know answer_array index is within bounds of guess_array
            number_matches+=1
    return number_matches

def wait_response():
    global game_won
    global answer
    global guesses

    while(game_won != True):
        response = input("> ")
        alike_result = get_alike(response, answer)

        guesses+=1
                
        if response == answer:
            game_won=True
            print(f"{alike_result}/{len(answer)}")
            print("YOU WON!!!!")
            return
        
        if guesses >= max_guesses:
            show_guesses_available()
            print(f"{alike_result}/{len(answer)}")
            print("You've used all your guesses! YOU LOSE!")
            return
        
        show_guesses_available()   
        print(f"{alike_result}/{len(answer)} Try again!")         
        
def get_guesses_available():
    global max_guesses
    global guesses
    guesses_available=max_guesses-guesses
    if guesses_available < 0:
        guesses_available=0
    
    return guesses_available

def show_guesses_available():
    guesses_left = get_guesses_available()
    print(f"Guesses left: {guesses_left}")

def show_wordbank():
    result="Wordbank: "
    for key, word in enumerate(word_list[difficulty]):
        result+=word
        if key<len(word_list[difficulty])-1:
            result+=","
    print(result)
  
def run():
    show_wordbank()
    show_guesses_available()
    wait_response()
    
run()