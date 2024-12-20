# importar o pacote de string
# Revisaremos mais pacotes/bibliotecas no Módulo 5
import string


# Esta implementação da função RETURN (retornar) um valor booleano, True/False (Verdadeiro/Falso)
def isPalindrome(str):
    # Como não conseguimos controlar o que o usuário insere na sentença, vamos esclarecer primeiro a sentença.
    # Vamos remover todas as pontuações e espaços brancos da sentença e colocar todas as letras em minúsculo
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    str = str.replace(" ", "").lower()

    # Comparar a string original com a string em ordem inversa
    # Observação de str[::-1]: os dois primeiros números definem o início e o fim da string, o último número de -1 indica a ordem inversa

    # Verificar se a string é a mesma tanto em ordem invertida quanto na ordem original
    if str == str[::-1]: # regra de [a:b:c] a=inicio b=terminio c=aumento no contador, basicamente um for em c++
        return True
    else:
        return False

# Solicitar ao usuário que introduza a sentença
def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")

  if (isPalindrome(userSentence)):
    print(userSentence + " is a palindrome!")
  else:
    print(userSentence + " is NOT a palindrome!")

if __name__ == "__main__":
    main()