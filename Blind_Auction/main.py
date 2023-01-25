from replit import clear 
# clear : 강의 사이트에서 제공하는 함수임.
from art import logo
print(logo)


# bids라는 새로운 딕셔너리 생성
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # 딕셔너리에서 for문을 돌 경우 key값을 비교
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}.")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  else :
    print("You entered incorrectly.")
