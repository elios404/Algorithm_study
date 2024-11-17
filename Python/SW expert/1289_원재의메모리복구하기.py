test_num = int(input())

for T in range(test_num):
    b = input()
    answer_bits = []
    for c in b:
        answer_bits.append(int(c))

    start_bits = [0]*len(answer_bits)
    turn = 0
    move = 0

    while(answer_bits != start_bits):
        need_to_be = answer_bits[move]
        if need_to_be == start_bits[move]: # 바꿀 필요가 없다면
            move += 1
        else : 
            start_bits[move:] = [need_to_be]*len(answer_bits[move:])
            turn += 1
            move += 1

    print(f"#{T+1} {turn}")
