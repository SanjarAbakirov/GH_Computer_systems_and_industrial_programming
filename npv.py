def analyze_investment(rate, cash_flows, project_name=""):
    """Комплексный анализ инвестиционного проекта"""
    npv = 0
    npv_result = npv(rate, cash_flows)

    print(f"\nАнализ проекта: {project_name}")
    print(f"Начальная инвестиция: {cash_flows[0]:.2f}")
    print(f"Ставка дисконтирования: {rate*100:.1f}%")
    print(f"Расчетный NPV: {npv_result:.2f}")

    # Анализ чувствительности
    rates = [rate * 0.5, rate, rate * 1.5]
    print("\nАнализ чувствительности:")
    for r in rates:
        sensitivity_npv = npv(r, cash_flows)
        print(f"При ставке {r*100:.1f}%: NPV = {sensitivity_npv:.2f}")


# Пример комплексного анализа
project_cash_flows = [-50000, 15000, 20000, 25000, 30000, 20000]
analyze_investment(0.12, project_cash_flows, "Завод по производству")
