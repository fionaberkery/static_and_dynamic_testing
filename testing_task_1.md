### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# line 21 should be a double equals not a single and there should be a colon after 'else' on line 23
  

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  # 'dif' is wrong spelling on line 29. it should be spelt 'def'
  # missing a comma between card1 and card2 line 29
  # 'card' on lind 31 is not one of the arguments. should be 'card1' 


  def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# 'total' in line 42 should be defined as 'total = 0' 
# there should be a space after 'of' at the end of the string on line 45

