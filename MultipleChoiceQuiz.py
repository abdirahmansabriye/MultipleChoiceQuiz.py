def quiz():
  # question 1
  print("Question 1: What is the capital of France?")
  print("a) London")
  print("b) Rome")
  print("c) Paris")
  print("d) Berlin")
  answer = input("Enter your answer: ")
  if answer == "c":
    print("Correct!")
  else:
    print("Incorrect")
    answer = input("Try again: ")
    if answer == "c":
      print("Correct!")
    else:
      print("Incorrect. The correct answer was Paris.")

  # question 2
  print("\nQuestion 2: Who is the current President of the United States?")
  print("a) Donald Trump")
  print("b) Joe Biden")
  print("c) Barack Obama")
  print("d) John F. Kennedy")
  answer = input("Enter your answer: ")
  if answer == "b":
    print("Correct!")
  else:
    print("Incorrect")
    answer = input("Try again: ")
    if answer == "b":
      print("Correct!")
    else:
      print("Incorrect. The correct answer was Joe Biden.")

  # question 3
  print("\nQuestion 3: What is the currency of Japan?")
  print("a) Yen")
  print("b) Dollar")
  print("c) Euro")
  print("d) Pound")
  answer = input("Enter your answer: ")
  if answer == "a":
    print("Correct!")
  else:
    print("Incorrect")
    answer = input("Try again: ")
    if answer == "a":
      print("Correct!")
    else:
      print("Incorrect. The correct answer was Yen.")

# run the quiz
quiz()