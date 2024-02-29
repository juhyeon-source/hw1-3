import random

# 코드 정의부
def game():
    while True:

        a = input("가위, 바위, 보 중 하나를 선택하세요: ")
        b = random.choice(list)
        win_count, lose_count, draw_count = 0, 0, 0

        if a == b:
            draw_count += 1
            print(f"사용자: {a}, 컴퓨터: {b}")
            print("무승부입니다!")
            break
        elif a == '가위':
            print(f"사용자: {a}, 컴퓨터: {b}")
            if b == '바위':
                lose_count += 1
                print("컴퓨터 승리!")
            elif b == '보':
                win_count += 1
                print("사용자 승리!")
            break
        elif a == '바위':
            print(f"사용자: {a}, 컴퓨터: {b}")
            if b == '보':
                lose_count += 1
                print("컴퓨터 승리!")
            elif b == '가위':
                win_count += 1
                print("사용자 승리!")
            break
        elif a == '보':
            print(f"사용자: {a}, 컴퓨터: {b}")
            if b == '가위':
                lose_count += 1
                print("컴퓨터 승리!")
            elif b == '바위':
                win_count += 1
                print("사용자 승리!")
            break
        else:
            print("유효한 입력이 아닙니다")
            continue
    return win_count, lose_count, draw_count
def main():
    # 게임을 저장할 공간을 만들거에요.
    game_result = [0, 0, 0]

    # 첫게임
    win_count, lose_count, draw_count = game()
    game_result[0] += win_count
    game_result[1] += lose_count
    game_result[2] += draw_count

    while True:
        c = input("다시 게임을 하시겠습니까? (y/n): ")
        if c.lower() == 'y':
            # 두번째 이상 게임 진행
            win_count, lose_count, draw_count = game()
            game_result[0] += win_count
            game_result[1] += lose_count
            game_result[2] += draw_count

        elif c.lower() == 'n':
            print("게임을 종료합니다.")
            print(
                f"승: {game_result[0]} 패: {game_result[1]} 무승부: {game_result[2]}")
            break
        else:
            print("유효한 문자가 아닙니다.")


# 코드 실행부
i = input("가위바위보 게임을 하시겠습니까? (y/n): ")
if i == 'y':
    list = ['가위', '바위', '보']
    main()
