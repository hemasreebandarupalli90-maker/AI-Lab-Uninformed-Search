import random

human_responses = [
    "I enjoy music and movies.",
    "Life feels beautiful sometimes.",
    "I love talking to my friends.",
    "That question makes me think."
]

ai_responses = [
    "Emotion detected: positive.",
    "Friendship classified as social bond.",
    "Processing philosophical query.",
    "Response generated successfully."
]

def run_turing_test():
    print("=== TURING TEST ===")
    print("Guess whether response is Human or AI\n")

    for i in range(4):
        if random.choice([True, False]):
            response = random.choice(human_responses)
            label = "Human"
        else:
            response = random.choice(ai_responses)
            label = "AI"

        print("Response:", response)
        guess = input("Your Guess (Human/AI): ")
        print("Actual Answer:", label)
        print()

if __name__ == "__main__":
    run_turing_test()
