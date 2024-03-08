from django.shortcuts import render
from django.http import HttpResponse


# 仮想的なログイン処理を想定したコード
def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

def index(request):
    # ユーザーからの入力を受け取る
    user_input_username = input(request[3])
    user_input_password = input(request[5])

    # SAST test SQLインジェクションを試みる
    login(user_input_username, user_input_password)

    return HttpResponse("Hello World!")





