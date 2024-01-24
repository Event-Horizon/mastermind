import math
import random
from typing import Any, Literal


def clamp(n: int, minn: int, maxn: int) -> int:
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n


def get_key_range(numkey_dict: dict[int, int]) -> tuple[int, int]:
    if not all(isinstance(key, int) for key in numkey_dict.keys()):
        raise Exception("Function get_key_range requires number indexed dictionary only.")

    last_key = -1
    smallest_key = 0
    largest_key = 0

    for current_key, value in numkey_dict.items():
        if not last_key or last_key == -1:
            last_key = current_key
            smallest_key = current_key
            largest_key = current_key
        else:
            if current_key < last_key and current_key <= smallest_key:
                smallest_key = current_key
            if current_key > last_key and current_key >= largest_key:
                largest_key = current_key
    result = (smallest_key, largest_key)
    return result


def get_alike(guess: str, answer: str) -> int:
    guess_array = list(guess)
    answer_array = list(answer)
    number_matches = 0

    for i, letter in enumerate(answer_array):
        if i > len(guess_array):
            # we know answer_array is longer than guess_array, stop comparing
            break
        if i <= len(guess_array)-1 and letter == guess_array[i]:
            # we know answer_array index is within bounds of guess_array
            number_matches += 1
    return number_matches


def wait_response(guesses: int, max_guesses: int, answer: str, game_won_state: bool) -> None:
    while (game_won_state != True):
        response = input("> ")
        alike_result = get_alike(response, answer)

        guesses += 1

        if response == answer:
            game_won_state = True
            print(f"{alike_result}/{len(answer)}")
            print("YOU WON!!!!")
            return

        if guesses >= max_guesses:
            show_guesses_available(guesses, max_guesses)
            print(f"{alike_result}/{len(answer)}")
            print("You've used all your guesses! YOU LOSE!")
            return

        show_guesses_available(guesses, max_guesses)
        print(f"{alike_result}/{len(answer)} Try again!")
        return


def get_guesses_available(guesses: int, max_guesses: int) -> int:
    guesses_available = max_guesses-guesses
    if guesses_available < 0:
        guesses_available = 0

    return guesses_available


def show_guesses_available(guesses: int, max_guesses: int) -> None:
    guesses_left = get_guesses_available(guesses, max_guesses)
    print(f"Guesses left: {guesses_left}")


def show_wordbank(words_difficulty_list: list) -> None:
    result = "Wordbank: "
    for key, word in enumerate(words_difficulty_list):
        result += word
        if key < len(words_difficulty_list)-1:
            result += ","
    print(result)


def get_random_item(list: list) -> Any:
    return list[math.floor(random.random() * len(list))]


def main() -> None:
    debug = False

    word_list = {
        5: ["whizz", "fuzzy", "quick", "quiff", "juked", "puked"],
        6: ["fizzes", "buzzes", "sizzle", "jumper", "jabber", "quiver"],
        7: ["quizzes", "buzzcut", "schmuck", "quaking", "junkies", "gimmick"],
        8: ["delicate", "kickball", "concrete", "blizzard", "consumer", "backfill", "delivery"]
    }

    rank_to_guesses = {
        5: 3,
        6: 3,
        7: 4,
        8: 4
    }

    guesses = 0  # guesses taken
    rank = clamp(8, *get_key_range(rank_to_guesses))  # letters in word
    used_word_list = word_list[rank]
    max_guesses = rank_to_guesses[rank]
    answer = get_random_item(used_word_list)
    game_won = False

    if debug:
        rrange = get_key_range(rank_to_guesses)
        print(f"{rrange[0]} to {rrange[1]}")
        print(answer)

    show_wordbank(used_word_list)
    show_guesses_available(guesses, max_guesses)
    wait_response(guesses, max_guesses, answer, game_won)


if __name__ == "__main__":
    main()
