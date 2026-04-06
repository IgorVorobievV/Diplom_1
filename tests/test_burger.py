class TestBurger:
    
    def test_bun_burger_true(self, burger):
        
        assert burger.bun == None
    
    def test_ingredients_burger_true(self, burger):

        assert burger.ingredients == []