import random
from art import logo
from module_fix import clear

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards_list):
  """Take a list of cards and return the score calculated from the cards"""
  if (11 in cards_list) and (10 in cards_list) and len(cards_list) == 2:
    return 0 
  if 11 in cards_list and sum(cards_list) > 21:
    cards_list.remove(11)
    cards_list.append(1)
  return sum(cards_list)

def compare(user_score, computer_score):
  """Compares the score of the user to the score of the machine and provides a print statement based on the relative score"""
  if user_score == computer_score:
    return "Its a draw 🤝 "
  elif computer_score == 0:
    return "You lose because the Dealer has Blackjack 😎"
  elif user_score == 0:
    return "You win with a Blackjack 😎"
  elif user_score >= 22:
    return "You lose 😭💔 You went over"
  elif computer_score >= 22:
    return "You win 🤑 Opponent went over"
  elif user_score > computer_score:
    return "You win 🤑 "
  elif computer_score > user_score:
    return "You lose 😭💔"
  else:
    return "\n Oh this is awkward...this is a bug 😤"

def play_game():
  """Main Game Code"""
  print(logo)
  
  user_cards = []
  dealer_cards = []
    
  for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(dealer_cards)
    print(f"""
        🃏 Your cards are {user_cards} and the total score is {user_score}
    
        🃏 Dealer's first card is {dealer_cards[0]}
    """)
  
    if user_score == 0 or computer_score == 0 or user_score >= 22:
      is_game_over = True
    else:
      user_should_deal = input("👉 Say yes to get another card, or no to pass: \n")
      if user_should_deal == "yes":
        user_cards.append(deal_card())
      elif user_should_deal == "no":
        is_game_over = True
    
  while computer_score != 0 and computer_score <= 16:
      dealer_cards.append(deal_card())
      computer_score = calculate_score(dealer_cards)

  print(f"""
🥁🥁 Results are in...

        {compare(user_score, computer_score)}

        🃏 Your final cards are {user_cards} and the final score is {user_score}

        🃏 Dealer's final cards are {dealer_cards} and the final score is {computer_score} \n """)

continue_playing = True

while continue_playing:
  play_or_exit = input("🤵: Are you ready to play Blackjack? Type yes or no: \n").lower()
  if play_or_exit == "yes":
    clear()
    play_game()
  elif play_or_exit == "no":
    print("\n🤵: Goodbye")
    continue_playing = False
