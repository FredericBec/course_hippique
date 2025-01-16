import random

def validate_number(guess):
    """
    Verify if the number is an integer
    :param guess: entered by the user
    :return: true if it's an integer
    """
    valid_number = False
    number = input(guess)
    if number.isdigit():
        valid_number = True
    else:
        print("Merci d'entrer un entier valide! (ex: 0,1,2, etc...)")

    if not valid_number:
       number = validate_number(guess)

    return int(number)

def horse_run():
    """
    Simulate a horse run and ask the choice of number of horses and type to the user
    :return: the list of winner horses in function of run type
    """
    minhorse = 12
    maxhorse = 20

    answer = input("Voulez-vous simuler une course?\n")

    while answer.casefold() == "oui":
        horse_number = validate_number("Veuillez entrez un nombre: ")

        if horse_number < minhorse or horse_number > maxhorse:
            print("Veuillez entrez un nombre compris entre 12 et 20 !")
        else:
            user_choice = run_choice()
            match user_choice:
                case "tierce":
                    tierce(horse_number)
                case "quarte":
                    quarte(horse_number)
                case "quinte":
                    quinte(horse_number)
            answer = input("Voulez-vous simuler une course?\n")
    else:
        print("Merci de votre visite, au revoir.")

def run_choice():
    """
    Ask the choice of run type to the user
    :return: type of the run
    """
    choice: str = ""
    run_type: dict = {1 : "tierce", 2 : "quarte", 3 : "quinte"}

    print(run_type)
    user_choice = validate_number("Quel type de course souhaitez vous? ")
    if user_choice in run_type:
        choice = run_type.get(user_choice)
        return choice
    else:
        print("Veuillez entrer un numéro de la liste !")

def tierce(nb_horse: int):
    """
    Determine the winner horses list
    :param nb_horse: choice of the user between 12 and 20
    :return: random 3 winner horses list
    """
    winner_tierce = random.sample(range(1, nb_horse), 3)

    print(winner_tierce)

def quarte(nb_horse: int):
    """
    Determine the winner horses list
    :param nb_horse: choice of the user between 12 and 20
    :return: random 4 winner horses list
    """
    winner_quarte = random.sample(range(1, nb_horse), 4)

    print(winner_quarte)

def quinte(nb_horse: int):
    """
    Determine the winner horses list
    :param nb_horse: choice of the user between 12 and 20
    :return: random 5 winner horses list
    """
    winner_quinte = random.sample(range(1, nb_horse), 5)

    print(winner_quinte)


if __name__ == '__main__':
    horse_run()
