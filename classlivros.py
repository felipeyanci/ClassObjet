class Livros:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.lido = False

    def marcar_como_lido(self):
        self.lido = True
        print(f"-> Status alterado: '{self.titulo}' agora esta marcado como lido")
    
    def exibir_status(self):
        status = "lido" if self.lido else "pendente"
        print(f"O livro {self.titulo}, de {self.autor}, esta marcado como pendente")
        

print("--- Resultado_Livros ---")

Livro1 = Livros("Cem anos de solidão" , "Gabriel Garcia Marquez")
Livro2 = Livros("Tudo sobre o amor" , "Bell Hooks")

Livro1.exibir_status()
Livro2.exibir_status()

Livro1.marcar_como_lido()
print("\nVerificando após marcar:")
Livro1.exibir_status()
Livro2.exibir_status()