import random
import time
import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

health = 100


def print_with_typing(text, typing_speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)


def explore_forest():
    global health
    print_with_typing("\nВы решаете исследовать темный лес. Деревья \
возвышаются над вами словно древние стражи.")
    time.sleep(2)
    if random.random() < 0.6:
        print_with_typing("Внезапно вы чувствуете, что за вами что-то следит.")
        time.sleep(2)
        print_with_typing("Сердце колотится от страха, когда вы слышите \
приглушенный плач и странные шорохи.")
        time.sleep(3)
        input("Нажмите Enter, чтобы осветить фонариком вокруг...")
        print_with_typing("Это было нечто из кошмаров, выходящее за пределы \
реальности.")
        time.sleep(2)
        print_with_typing("Темные тени обволакивали существо, \
и его красные глаза сияли как адское пламя.")
        time.sleep(3)
        print_with_typing("Вы не можете понять, что это, но ужас, который оно \
вызывало, был непередаваемым.")
        time.sleep(2)
        damage = random.randint(30, 45)
        health -= damage
        print_with_typing(f"Ужасное существо атакует вас, нанося {damage} \
урона! Вы едва смогли убежать.")
        time.sleep(2)
        print_with_typing("Вы испугано убегаете назад на тропу, но вам не \
удается найти путь обратно.")
        time.sleep(2)
        print_with_typing("Вы теряетесь в лесу, и все ваши попытки выбраться \
оказываются тщетными.")
        time.sleep(2)
        print_with_typing("Это конец вашего путешествия...")
        time.sleep(1)
        game_over()
    else:
        print_with_typing("Вы осторожно исследуете лес, ощущая жуткую \
присутствие вокруг.")
        time.sleep(3)
        print_with_typing("Вы идете дальше по лесной тропе...")
        time.sleep(2)
        print_with_typing("...")
        time.sleep(1)
        win_game()


def play_again():
    print_with_typing("\nХотите сыграть еще раз?")
    print_with_typing("1. Да, я хочу снова отправиться в Тайну Леса!")
    print_with_typing("2. Нет, спасибо, я предпочту остаться в безопасности.")
    replay_choice = input("> ")
    if replay_choice == "1":
        global health
        health = 100
        show_options()
    else:
        print_with_typing("Безопасность деревни - ваш лучший выбор. Приходите \
в следующий раз, если смелость вернется.")
        sys.exit()


def game_over():
    print_with_typing("\nТемнота поглотила вас. Вы потерпели поражение в этом \
опасном лесу.")
    time.sleep(1)
    print_with_typing(
        "Зловещие силы леса обладали вами, и ваше сознание исчезло во тьме.")
    time.sleep(1)
    print_with_typing("Но тайны леса остаются нераскрытыми.")
    time.sleep(1)
    print_with_typing("Может быть, в следующий раз вы снова рискнете \
исследовать эти мрачные места?")
    time.sleep(1)
    play_again()


def good_ending():
    print_with_typing("\nВы осветили свой фонарик и обнаружили древнюю \
руническую статую.")
    time.sleep(2)
    print_with_typing("Кажется, что она давно потеряла свой смысл, но ее \
красота ошеломляет вас.")
    time.sleep(2)
    print_with_typing("С добычей этой тайны вы возвращаетесь в деревню как \
настоящий герой.")
    time.sleep(2)
    print_with_typing("Жители деревни восхищены вашей храбростью и умением.")
    time.sleep(2)
    print_with_typing("Вы становитесь настоящей легендой!")
    time.sleep(2)
    print_with_typing("Поздравляю! Вы успешно завершили игру.")
    time.sleep(2)


def win_game():
    print_with_typing("\nВы успешно вернулись в деревню, но тайны леса \
остаются нераскрытыми.")
    time.sleep(1)
    print_with_typing("Может быть, вы еще раз рискнете исследовать эти мрачные\
 места?")
    time.sleep(1)
    play_again()


def show_options():
    print("\nЗдоровье:", health)
    print("\nВыберите следующий шаг:")
    print("1. Исследовать темный лес.")
    print("2. Вернуться в деревню для безопасности.")


def welcome_message():
    print_with_typing("Добро пожаловать в \"Тайна Леса\"!")
    print_with_typing("Вечер в деревне опутался мрачной аурой, когда вы \
отправились по темной дороге к школе.")
    time.sleep(3)
    print_with_typing("Серые облака нависли над вами, и ветер зловеще шумел в \
листве дремучего леса.")
    time.sleep(3)
    print_with_typing("Вы ощутили, что кто-то следит за вами, но при \
оглядывании не увидели ничего, кроме густых деревьев.")
    time.sleep(2)
    print_with_typing("\nПо вам пробежал холодок, когда перед вами \
раздвигаются две дороги. Вы не знаете, куда идти...")
    time.sleep(2)
    show_options()


welcome_message()

while health > 0:
    choice = input("> ")

    if choice == "1":
        explore_forest()
    elif choice == "2":
        print_with_typing("\nВы решаете вернуться в деревню для безопасности.")
        health += random.randint(10, 20)
        break
    else:
        print_with_typing("\nВы ощущаете запутавшийся путь и заблудились в \
лесу. Найдите другой выход.")
        time.sleep(2)
        print_with_typing("1. Попытаться найти свой путь с помощью фонарика.")
        print_with_typing("2. Вернуться на тропу и выбрать \
другое направление.")

        while True:
            new_choice = input("> ")
            if new_choice == "1":
                print_with_typing("\nВы старательно ищете выход с помощью \
фонарика.")
                time.sleep(2)
                print_with_typing("К счастью, вы находите дорогу обратно и \
продолжаете свое путешествие.")
                break
            elif new_choice == "2":
                print_with_typing("\nВы решаете вернуться на тропу и выбрать \
другое направление.")
                time.sleep(2)
                print_with_typing("Смело двигаясь вперед, вы исследуете \
неизведанные части леса.")
                explore_forest()
                break
            else:
                print_with_typing("Неверный выбор. Пожалуйста, попробуйте \
снова.")

if health <= 0:
    game_over()
else:
    good_ending()
