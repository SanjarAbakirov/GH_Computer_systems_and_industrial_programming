def ebitda_calculator():
    """Интерактивный калькулятор EBITDA"""
    print("Калькулятор EBITDA")
    print("Введите финансовые показатели:")

    try:
        net_income = float(input("Чистая прибыль: "))
        interest = float(input("Проценты по кредитам: "))
        taxes = float(input("Налоги: "))
        depreciation = float(input("Износ основных средств: "))
        amortization = float(input("Амортизация нематериальных активов: "))

        ebitda = net_income + interest + taxes + depreciation + amortization

        print(f"\nРезультат расчета:")
        print(f"EBITDA = {ebitda:,.2f} руб.")

    except ValueError:
        print("Ошибка! Вводите только числа.")


# Запуск калькулятора
ebitda_calculator()
