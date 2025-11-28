def npv(rate, cash_flows):
    """
    Рассчитывает чистую приведенную стоимость (NPV)

    Parameters:
    rate (float): Ставка дисконтирования (в десятичной форме, например 0.1 для 10%)
    cash_flows (list): Список денежных потоков, где cash_flows[0] - начальная инвестиция

    Returns:
    float: Значение NPV
    """
    npv_value = 0
    for t, cash_flow in enumerate(cash_flows):
        npv_value += cash_flow / ((1 + rate) ** t)
    return npv_value

# Альтернативная реализация с использованием list comprehension


def npv_compact(rate, cash_flows):
    """Компактная версия расчета NPV"""
    return sum(cash_flow / ((1 + rate) ** t) for t, cash_flow in enumerate(cash_flows))


# Пример использования
if __name__ == "__main__":
    # Пример: инвестиционный проект
    discount_rate = 0.1  # 10% ставка дисконтирования
    cash_flows = [-1400, 300, 400, 500, 200]  # -1000 - начальная инвестиция

    result = npv(discount_rate, cash_flows)
    print(f"NPV проекта: {result:.2f}")

    # Анализ результата
    if result > 0:
        print("Проект следует принять (NPV > 0)")
    elif result < 0:
        print("Проект следует отклонить (NPV < 0)")
    else:
        print("Проект безубыточен (NPV = 0)")
