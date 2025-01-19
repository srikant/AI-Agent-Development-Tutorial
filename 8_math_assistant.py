import random

def generate_weather(location):
    """
    Generates a random weather forecast for a given location.
    Args:
        location (str): The name of the location.
    Returns:
        str: A weather forecast message.
    """
    conditions = ["sunny", "rainy", "cloudy", "stormy", "snowy", "windy"]
    temperatures = random.randint(-10, 40)  # Simulate temperatures in Celsius
    condition = random.choice(conditions)
    return f"The weather in {location} is currently {condition} with a temperature of {temperatures}°C."

def main():
    print("WeatherBot: Hi there! I can give you a simulated weather forecast. Type 'exit' to quit.")
    while True:
        user_input = input("Enter a location: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("WeatherBot: Goodbye! Stay safe and enjoy the weather!")
            break
        elif user_input:
            print(f"WeatherBot: {generate_weather(user_input)}")
        else:
            print("WeatherBot: Please provide a valid location.")

if __name__ == "__main__":
    main()
""" WeatherBot: Hi there! I can give you a simulated weather forecast. Type 'exit' to quit.
Enter a location: Paris
WeatherBot: The weather in Paris is currently sunny with a temperature of 23°C.
Enter a location: Tokyo
WeatherBot: The weather in Tokyo is currently rainy with a temperature of 18°C.
Enter a location: exit
WeatherBot: Goodbye! Stay safe and enjoy the weather!
 """