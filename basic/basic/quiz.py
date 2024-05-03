
questions = [ "What is the capital of Germany?",
              "Who is the president of the US?",
              "What is the capital of France?",
              "What is the capital of Spain?" ]

answer = [ "Berlin", 
           "Biden",
           "Paris",
           "Madrid" ]

score = 0

for i in range(0, len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")

    if user_answer == answer[i]:
        print("Correct") 
        score = score + 1
    else:
        print("Incorrect")

print(f"Score {score} ")