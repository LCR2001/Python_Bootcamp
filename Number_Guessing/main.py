from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# 사용자가 추측한 숫자와 정답 비교 및 남은 횟수 출력
def check_answer(guess,answer,turns):
  if guess > answer :
    print("Too high.")
    return turns - 1
  elif guess < answer :
    print("Too low.")
    return turns - 1
  else :
    print(f"You got it:) The answer was {answer}.")

# 난이도 설정
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else :
    return HARD_LEVEL_TURNS

# 여기서부터 반복됨 (제한 횟수 내에)
def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100.")
  answer = randint(1,100)
  
  turns = set_difficulty()
  
  # 틀릴 경우 계속해서 추측할 수 있도록 반복하기
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.") 
  # 숫자 추측하기
    guess = int(input("Choose the number from 1 to 100: "))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.") 


game()