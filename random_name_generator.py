import random

may_vocals = ['A', 'E', 'I', 'O', 'U']
min_vocals = ['a', 'e', 'i', 'o', 'u']
may_consonants = ['Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F',
                  'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
min_consonants = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f',
                  'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
may = may_vocals + may_consonants  # Una lista de todas las letras mayúsculas
mins = min_consonants + min_vocals  # Una lista de todas las letras minusculas

vocals = may_vocals + min_vocals # Una lista de vocales tanto minúsculas como mayúsculas

consonants = may_consonants + min_consonants # Una lista de consonantes tanto minúsculas como mayúsculas
msg = "How many characters do you want in your new name?(Max: 12 Characters) "

# Bienvenido al generador de nombres aleatorios para tus videojuegos!
def generate_name():
    generated_name = []

    print("Welcome to random videogame name generator!! Lets find your perfect name!")
    name_length = int(
        input(msg))
    while name_length > 12:  # El nombre no puede tener más de 12 carácteres 
        print("Sorry,max 12 characters")
        name_length = int(
            input(msg))

    # Forzamos que la primera letra sea una mayúscula
    generated_name.append(random.choice(may))

    i = 0

    for i in range(name_length - 1):

        # Si es una consonante,ponemos una vocal para que no haya 2 consonantes seguidas
        if generated_name[i] in consonants:
            i += 1
            add_min_vocal(generated_name)

        # Si tiene dos vocales seguidas,pon una consonante
        elif generated_name[i] and generated_name[i - 1] in vocals:
            i += 1
            add_min_consonant(generated_name)

        # Si no tiene 2 vocales seguidas pero es una vocal,puede colocar tanto otra vocal como una consonante
        else:  
            i += 1
            add_random_character(generated_name)

    str1 = ""
    str1 = str1.join(generated_name)
    
    return str1


def add_min_vocal(generated_name):
    new_character = random.choice(min_vocals)
    generated_name.append(new_character)


def add_min_consonant(generated_name):
    new_character = random.choice(min_consonants)
    generated_name.append(new_character)


def add_random_character(generated_name):
    new_character = random.choice(mins)
    generated_name.append(new_character)


def run():
    generated_name = generate_name()
    print("Your new name can be: \"" + generated_name + "\" :)")
    answer = input(" Do You like it? (y/n): ")

    while answer != "y":   
        generated_name = generate_name()
        print("Your new name can be: \"" + generated_name + "\" :)")
        answer = input(" Do You like it? (y/n): ")
    print(" Congratulations! Your new name is \"" +  generated_name  + "\",enjoy it =D")


if __name__ == '__main__':
    run()
