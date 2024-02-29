import random
i = input("업/다운 게임을 하시겠습니까? (y/n): ")
if i == 'y':

    def game():
        random_number = random.randint(1,100)
        count = 0
        while True:
            count += 1
            a = int(input("숫자를 입력하세요: "))
            if a < 1 or a > 100:
                print("유효한 범위 내의 숫자를 입력하세요")
            elif a < random_number:
                print("up")
            elif a > random_number:
                print("down")
            else:
                print("맞았습니다")
                print(f'시도한 횟수: {count}')
                break
        return count
    game() 
    
    def main(): 
        max_count = 0 
        while True:    
            b = input('다시 게임을 하시겠습니까? (y/n): ')
            if b == 'y':
                count = game()
                if max_count < count:
                    max_count = count
            elif b == 'n':
                break
            else:
                print('유효한 입력이 아닙니다.')

        print(f"플레이어의 최고 시도 횟수: {max_count}")

    main()
# python first_homework.py