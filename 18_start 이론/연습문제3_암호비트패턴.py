code_pattern = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']

t = int(input())

for tc in range(1, t+1):
    numbers = input()

    binary = format(int(numbers, 16), 'b')
    binary = binary.strip('0')  # 그냥 arr.strip('0') 하면 안되고, arr = arr.strip('0')을 해줘야함
    print(binary.strip('0'))
    binary = '0' * (6 - (len(binary) % 6)) + binary  # 왜 6이냐면 패턴이 6개짜리라서

    for i in range(0, len(binary), 6):
        print(code_pattern.index(binary[i:i+6]), end=' ')