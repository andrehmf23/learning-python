
#______________________________________________Loops For/While____________________________________________

for i in range(10):
  print(i)

print('\n')


for i in range(2, 10):
  print(i)

print('\n')


for i in range(0, 10, 3):
  print(i)

print('\n')


for i in "hello!":
  print(i)

print('\n')


string = "hello world!"
for i in range(0, len(string), 2):
  print(str(i) + "th letter is "+ string[i])

print('\n')


count = 0
while count < 10:
  print(count)
  count += 1


# ______________________________________________Continue/Break Keywords____________________________________________

while True:
  user = input("Enter something to be repeated: ")

  ## Quando o "break" é acionado, o print() abaixo NÃO será executado.
  ## O programa romperá o loop quando esta palavra-chave for lida.
  if user=="end":
    print("Terminate the program!!!")
    break
  print(user)

end = False
while end == False:
  user = input("Enter something to be repeated: ")
  if user=="end":
    print("Program Ended!!!")
    end = True
  else:
    print(user)

count = 1

# Implementação do loop WHILE
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

# Implementação do loop FOR

for i in range(1, 20):
  if i % 5 == 0:
    print("SKIP")
    continue
  print(i)



# ______________________________________________Funções____________________________________________

#isPalindromo.py
#isTriangle.py


# ______________________________________________Desafio____________________________________________

import string

def isPalindrome(str):
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(' ', '').lower()

  if(str == str[::-1]):
    return True
  else:
    return False


# Solicitar que o usuário digite a sentença
def main():
  userInput = input("Enter a WORD to be tested as a palindrome:")

  if (isPalindrome(userInput)):
    print(userInput + " is a palindrome!")
  else:
    print(userInput + " is NOT a palindrome!")


if __name__ == "__main__":
  main()