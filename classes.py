class Restaurante:
    """Menu representa entrada, prato principal e sobremesa"""
    def __init__(self, entrada, principal, sobremesa):
        self.entrada = entrada
        self.principal = principal 
        self.sobremesa = sobremesa 
        
    def detalhes(self):
        print(f"entrada: '{self.entrada}' | principal: {self.principal} | sobremesa: {self.sobremesa}")
        
    def entrega_de_menu(self):
        print("entrega_de_menu")
        
    def agradecimento(self):
        print("Obrigado pela preferência!")
        

Menu1 = Restaurante("Pao artesanal de frutas vermelhas" , "Risoto de mariscos" , "Fudge de chocolate amargo")
Menu2 = Restaurante("Torrada artesanal de manteira e mel" , " Nhoque de carne" , "Petit gateau")

print("--- Entrega de menu ---")
print(Menu1.detalhes())
print(Menu2.detalhes())

print(Menu1.agradecimento())
