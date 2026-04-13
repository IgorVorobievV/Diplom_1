from unittest.mock import Mock

from praktikum.bun import Bun

class TestBurger:
    
    def test_bun_burger_none(self, burger):
        assert burger.bun is None
    
    def test_ingredients_burger_list(self, burger):
        assert isinstance(burger.ingredients, list)
        assert len(burger.ingredients) == 0
        assert type(burger.ingredients) is list


    def test_set_buns_burger_added_object_bun(self, burger):
        bun = Bun('Булка', 100)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_burger_added_ingredient(self, burger):
        burger.add_ingredient('Котлета')
        assert burger.ingredients == ['Котлета']

    def test_remove_ingredient_burger_no_ingredient(self, burger):
        burger.add_ingredient('Котлета')
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_burger_wright_ingredient_order(self, burger):
        burger.add_ingredient('Котлета')
        burger.add_ingredient('Сыр')
        burger.move_ingredient(0, 1)
        assert burger.ingredients == ['Сыр', 'Котлета']

    def test_get_price_burger_total_price(self, burger):
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()

        mock_bun.get_price.return_value = 200
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient2.get_price.return_value = 50
        
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        assert burger.get_price() == 550

    def test_get_receipt_burger_wright_receipt(self, burger):
        mock_bun = Mock()
        mock_ingredient1 = Mock()
        mock_ingredient2 = Mock()
        
        mock_bun.get_name.return_value = 'Галета'
        mock_ingredient1.get_name.return_value = 'Хрен'
        mock_ingredient2.get_name.return_value = 'Редька'
        mock_bun.get_price.return_value = 200
        mock_ingredient1.get_price.return_value = 100
        mock_ingredient2.get_price.return_value = 50
        mock_ingredient1.get_type.return_value = 'Соус'
        mock_ingredient2.get_type.return_value = 'Начинка'

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient1, mock_ingredient2]

        assert burger.get_receipt() == '(==== Галета ====)\n= соус Хрен =\n= начинка Редька =\n(==== Галета ====)\n\nPrice: 550'

