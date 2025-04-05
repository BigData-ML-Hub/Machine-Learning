from predict import predict

def main():
    while True:
        text = input("Enter an email (or 'exit' to quit):\n> ")
        if text.lower() == 'exit':
            break
        label = predict(text)
        print(f"Prediction: {label}\n")

if __name__ == '__main__':
    main()
