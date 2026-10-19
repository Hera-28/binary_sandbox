import sys
import time

def print_banner():
    print("=" * 60)
    print("BINARY MATH & LOGIC VISUALIZER SANDBOX")
    print("=" * 60)
def decimal_to_binary_breakdown(num):
    print(f"\n--- Converting Decimal {num} to Binary ---")
    if num == 0:
        print("Decimal 0 = Binary 0")
        return
    steps = []
    temp = num
    while temp > 0:
        remainder = temp % 2
        quotient = temp // 2
        steps.append("{temp} ÷ 2 = {quotient} (Remainder: {ramainder})")
        temp = quotient

    for step in steps:
        print(f" → {step}")
        time.sleep(0.15)
     binary_str = bin(num)[2:]
    print(f"\n✨ Result: {num} in binary is {binary_str}\n")

def visual_binary_addition(a, b):
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]
    max_len = max(len(bin_a), len(bin_b))
    
    bin_a = bin_a.zfill(max_len)
    bin_b = bin_b.zfill(max_len)
    
    print(f"\n--- Step-by-Step Binary Addition: {a} + {b} ---")
    print("Rules: 0+0=0 | 0+1=1 | 1+0=1 | 1+1=0 (Carry 1)\n")
    
    carry = 0
    result = []
    carry_line = []
    
    for i in range(max_len - 1, -1, -1):
        bit_a = int(bin_a[i])
        bit_b = int(bin_b[i])
        
        total = bit_a + bit_b + carry
        out_bit = total % 2
        new_carry = total // 2
        
        print(f"Column {max_len - i}: Bit A={bit_a}, Bit B={bit_b}, Carry-In={carry}")
        print(f"  ➜ Sum: {bit_a} + {bit_b} + {carry} = {total}")
        print(f"  ➜ Output Bit: {out_bit}, Carry-Out to next bit: {new_carry}\n")
        time.sleep(0.2)
        
        result.append(str(out_bit))
        carry_line.append(str(carry))
        carry = new_carry
        
    if carry:
        result.append(str(carry))
        carry_line.append(str(carry))

    result.reverse()
    final_binary = "".join(result)
    print(f" Final Binary Result: {final_binary} (Decimal: {a + b})")

def bitwise_operations_demo(a, b):
    print(f"\n--- Bitwise Logic Operations for {a} & {b} ---")
    bin_a = bin(a)[2:].zfill(8)
    bin_b = bin(b)[2:].zfill(8)
    
    print(f"  Number A ({a}): {bin_a}")
    print(f"  Number B ({b}): {bin_b}")
    print("-" * 35)
    print(f"  AND   (A & B): {bin(a & b)[2:].zfill(8)} (Decimal: {a & b})")
    print(f"  OR   (A | B): {bin(a | b)[2:].zfill(8)} (Decimal: {a | b})")
    print(f"  XOR  (A ^ B): {bin(a ^ b)[2:].zfill(8)} (Decimal: {a ^ b})")
    print("-" * 35)

def main():
    print_banner()
    while True:
        print("\nChoose an option:")
        print("1. Visual Binary Addition (with carry bits step-by-step)")
        print("2. Decimal to Binary Division Step Visualizer")
        print("3. Bitwise Logic Inspector (AND, OR, XOR)")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            try:
                num1 = int(input("Enter first integer: "))
                num2 = int(input("Enter second integer: "))
                visual_binary_addition(num1, num2)
            except ValueError:
                print(" Please enter valid integers!")
        elif choice == '2':
            try:
                num = int(input("Enter positive integer: "))
                decimal_to_binary_breakdown(num)
            except ValueError:
                print(" Please enter a valid integer!")
        elif choice == '3':
            try:
                num1 = int(input("Enter first integer: "))
                num2 = int(input("Enter second integer: "))
                bitwise_operations_demo(num1, num2)
            except ValueError:
                print(" Please enter valid integers!")
        elif choice == '4':
            print("\n Thanks for exploring binary math!")
            sys.exit()
        else:
            print(" Invalid selection. Try again.")

if name == "main":
    main()