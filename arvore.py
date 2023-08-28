class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return '%s <-- %s --> %s' %(self.esquerda and self.esquerda.valor, self.valor , self.direita and self.direita.valor)
    
class arvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir_em_nivel (self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(valor,self.raiz)
    
    def _inserir_em_nivel_recursivo(self,valor,no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)        
            else:
                self._inserir_em_nivel_recursivo(valor, no.direita)
                
    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.') 
        else:
            self.mostrar_pre_ordem_recursiva(self.raiz)
        
    def mostrar_pre_ordem_recursiva(self,no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursiva(no.esquerda)
        if no.direita  is not None:
            self.mostrar_pre_ordem_recursiva(no.direita)
    
    def mostrar_in_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.') 
        else:
            self.mostrar_in_ordem_recursiva(self.raiz)
        
    def mostrar_in_ordem_recursiva(self, no):
        if no.esquerda is not None:
            self.mostrar_in_ordem_recursiva(no.esquerda) 
        print(no.valor, end=' ')
        if no.direita  is not None:
            self.mostrar_in_ordem_recursiva(no.direita)
    
    def mostrar_pos_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.') 
        else:
            self.mostrar_pos_ordem_recursiva(self.raiz)
        
    def mostrar_pos_ordem_recursiva(self, no):
        if no.esquerda is not None:
            self.mostrar_pos_ordem_recursiva(no.esquerda) 
        if no.direita  is not None:
            self.mostrar_pos_ordem_recursiva(no.direita)
        print(no.valor, end=' ')
        
    def mostrar_ordem_de_niveis(self):
        if self.raiz is None:
            print('A árvore está vazia.') 
        else:
            self.mostrar_ordem_de_nivel_recursiva(self.raiz)
        
    def mostrar_ordem_de_nivel_recursiva(self, no):
        return print('')
        



#teste
arvore = arvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

print('Pré Ordem')
arvore.mostrar_pre_ordem()
print('\n')
print('In Ordem')
arvore.mostrar_in_ordem()
print('\n')
print('Pos Ordem')
arvore.mostrar_pos_ordem()
print('\n')
print('Ordem de niveis')
arvore.mostrar_ordem_de_niveis()