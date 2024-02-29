class Member():
    def __init__(self, name, username, password = 'default'):
        self.name = name
        self.username = username
        self.password = password
        

    def display(self):
        print(self.name, self.username)

class Post():
    def __init__(self, title, content, member):
        self.title = title
        self.content = content
        self.author = member

members = []
posts = []

def create_member():
    user_input = []
    input_text = ["회원 이름: ", "회원 아이디: ", "회원 비밀번호: "]
    for i in range(3):
        b = input(input_text[i])
        user_input.append(b)
    new_member = Member(user_input[0], user_input[1], user_input[2])
    return new_member

def post():
    user_input2 = []
    input_text = ["게시물 제목: ", "게시물 내용: ", "작성자: "]
    for i in range(3):
        d= input(input_text[i])
        user_input2.append(d)
    new_post = Post(user_input2[0], user_input2[1], user_input2[2])
    return new_post


while True:
    number = int(input("회원 등록을 원하신다면 1, 게시물 등록을 원하신다면 2, 종료를 원하신다면 3을 눌러주세요."))
    if number == 1:
        a = input("회원을 등록하시겠습니까? (y/n): ")
        if a == 'y':
            new_member = create_member()
            members.append(new_member)
        elif a == 'n':
            print('----------------------')
    
    elif number == 2:
        c = input("게시물을 작성하시겠습니까? (y/n): ")
        if c == 'y':
            new_post = post()
            posts.append(new_post)
        elif c == 'n':
            print('------------------------')
    elif number == 3:
        print('------------------------')
        break

    print("-----------------------")

for member in members:
    for post in posts:
        if member.name == post.author:
            print(member.name, post.title)

print('-----------------------')
comedy_list = []
romance_list = []
other_list = []

for post in posts:
    if post.content == "comedy":
        comedy_list.append(post.title)
    elif post.content == "romance":
        romance_list.append(post.title)
    else:
        other_list.append(post.title)

comedy_movies = ", ".join(comedy_list)
romance_movies = ", ".join(romance_list)
other_movies = ", ".join(other_list)
print(f"{comedy_movies}는 comedy 장르의 영화입니다.")
print(f"{romance_movies}는 romance 장르의 영화입니다.")
print(f"{other_movies}는 그 외의 장르의 영화입니다.")

