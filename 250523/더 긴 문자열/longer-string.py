given_input,given_input1 = input().split()

if len(given_input) > len(given_input1):
    print(f"{given_input} {len(given_input)}")
if len(given_input) < len(given_input1):
    print(f"{given_input1} {len(given_input1)}")
else:
    print("same")