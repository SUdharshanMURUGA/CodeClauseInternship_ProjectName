import time

def typing_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    correct_chars = sum(1 for i, j in zip(user_input, text) if i == j)
    accuracy = (correct_chars / len(text)) * 100
    
    print(f"\nTime taken: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

text_to_type = "The quick brown fox jumps over the lazy dog."
typing_test(text_to_type)