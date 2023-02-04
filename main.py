from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 금전 장치 관련 객체 생성
money_machine = MoneyMachine()
# 남은 재료 관련 객체 생성
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # 남은 재료에 대한 보고서 생성을 하기 위한 메소드(report)
        coffee_maker.report()
        # 금전 장치가 보고서 생성을 하기 위한 메소드(report)
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # 음료를 만들기 위한 충분한 재료가 있는지 확인            # 재료가 충분할 경우 음료에 대한 금액 지불
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # 둘 다 만족할 경우 음료 생성
            coffee_maker.make_coffee(drink)
        