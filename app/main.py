from app.data.knights import KNIGHTS
from app.KNIGHTS_list.factory import create_all_knights
from app.battle import battle

def main():
    knights = create_all_knights(KNIGHTS)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]

    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    result1 = battle(lancelot, mordred)
    result2 = battle(arthur, red_knight)

    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
