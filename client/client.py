import os
import requests
import time


SERVER_URL = os.getenv(
    "SERVER_URL",
    "http://localhost:8080"
)

CLIENT_ID = os.getenv(
    "CLIENT_ID",
    "unknown-client"
)


print("=" * 60)
print("SMO DISTRIBUTED DATA PROCESSING CLIENT")
print("=" * 60)

print(f"Client ID : {CLIENT_ID}")
print(f"Server    : {SERVER_URL}")

print("\nEnter numbers separated by spaces.")
print("Example: 10 20 30 40 50")
print("Type 'exit' to stop.\n")


while True:

    raw_input = input(f"{CLIENT_ID}> ").strip()

    # Exit the client
    if raw_input.lower() in {"exit", "quit", "q"}:
        print("\nClient exiting...")
        break

    # Empty input
    if not raw_input:
        print("Please enter at least one number.\n")
        continue

    # Convert input into numbers
    try:
        numbers = [
            float(value)
            for value in raw_input.split()
        ]

    except ValueError:
        print(
            "Invalid input. Please enter numbers separated by spaces."
        )
        print("Example: 10 20 30 40 50\n")
        continue

    # Create request payload
    payload = {
        "client_id": CLIENT_ID,
        "numbers": numbers
    }

    print("\nSending data to server...")

    start_time = time.perf_counter()

    try:

        response = requests.post(
            f"{SERVER_URL}/process",
            json=payload,
            timeout=10
        )

        elapsed = time.perf_counter() - start_time

        print(f"\nHTTP Status       : {response.status_code}")
        print(f"Round-trip Time   : {elapsed * 1000:.2f} ms")

        print("\nServer Response:")
        print("-" * 60)

        result = response.json()

        for key, value in result.items():
            print(f"{key:22}: {value}")

        print("-" * 60)
        print()

    except requests.exceptions.RequestException as error:

        print("\nConnection Error:")
        print(error)
        print()