from app.entities.knight import Knight


class Battle:
    """Класс, управляющий поединком двух рыцарей."""

    def __init__(self, knight1: Knight, knight2: Knight) -> None:
        self.knight1 = knight1
        self.knight2 = knight2

    def start(self) -> None:
        """Запуск пошагового боя."""
        print(f"\n⚔️ Битва начинается между {self.knight1.name} и {self.knight2.name}!\n")

        # применяем зелья, если есть
        if self.knight1.potion:
            print(f"{self.knight1.name} выпивает зелье {self.knight1.potion.name}!")
            self.knight1.potion.apply(self.knight1)
        if self.knight2.potion:
            print(f"{self.knight2.name} выпивает зелье {self.knight2.potion.name}!")
            self.knight2.potion.apply(self.knight2)

        round_num = 1
        while self.knight1.is_alive() and self.knight2.is_alive():
            print(f"\n--- Раунд {round_num} ---")

            self.knight1.attack(self.knight2)
            if not self.knight2.is_alive():
                print(f"\n💀 {self.knight2.name} пал в бою. Победитель — {self.knight1.name}!")
                break

            self.knight2.attack(self.knight1)
            if not self.knight1.is_alive():
                print(f"\n💀 {self.knight1.name} пал в бою. Победитель — {self.knight2.name}!")
                break

            round_num += 1

        # возвращаем результат (с обнулением отрицательных значений HP)
        return {
            self.knight1.name: max(self.knight1.hp, 0),
            self.knight2.name: max(self.knight2.hp, 0),
        }
