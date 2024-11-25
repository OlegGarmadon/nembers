responses = {}

# Установка флага продолжение опроса.

polling_active = True

while polling_active:
	# Запрос имени и ответ пользователя.
	name = input("\nWhat is your name ?  ")
	response = input("Wich mountain would you like to climb someday?  ")

	# Ответ находится в словоре.

	responses[name] = response

	#Проверка продолжения опроса.

	repeat = input("Would you like to let another person respond? (yes/ no)  ")
	if repeat == 'no':
		polling_active = False

	# Опрос завершон вывести результаты.

	print("\n--- Poll Results---")
	for name, response in responses.items():
		print(f"{name} would like to climb {response}.")
