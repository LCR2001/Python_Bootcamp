

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char


    print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo


print(logo)


# 프로그램 반복 진행 관련 코드
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    # 유저가 알파벳의 수(26개, 인덱스로는 최대 25)보다 큰 숫자를 입력할 경우 이 수를 0~25사이의 범위로 만들어주기
    # shift 사용 : shift를 26으로 나눈 나머지 값으로 바꿔주는 코드
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


    result = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye'___'")

