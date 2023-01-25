from art import logo
import random
from replit import clear

# Ace = 11 , Jack=Queen=King = 10
def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)

# 점수 비교 : user vs computer
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose! Computer has BlackJackㅠ_ㅠ"
    elif user_score == 0:
        return "You have a BlackJack! You WIN!!>_<"
    elif user_score > 21:
        return "You lose..."
    elif computer_score > 21:
        return "You WIN!!"
    elif user_score > computer_score:
        return "You WIN!!"
    else:
        return "You lose..."

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    # list인 user_cards나 computer_cards에 리스트가 아닌 하나의 항목만 추가하기 때문에 append함수 활용 -> += new_card 이런 식으로 사용 불가능

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # game이 종료될 때까지 반복
    while not is_game_over:
        # score 반환
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, current score : {user_score}.")
        print(f"Computer's first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # 다른 카드를 더 받고 싶은지 물어보기
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # 컴퓨터 : 합이 17미만이면 한 장 더 뽑음
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards} , final score : {user_score}")
    print(
        f"Computer's final hand : {computer_cards}, final_score : {computer_score} "
    )
    print(compare(user_score, computer_score))

# Game 시작 및 다시 시작할 것인지
while input(
        "Do you want to play a game of BlackJack? Type 'y' or  'n': ") == 'y':
    clear()
    play_game()

