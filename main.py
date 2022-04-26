from avlTree import AVLTree

myTree = AVLTree()
root = None

while True:

    print("\n--- Bem vindo ao sistema AVL tree ---")
    print("\n(1) Cadastrar Novo Nó\n(2) Remover Nó\n(3) Exibir árvore\n(0) Fechar sistema\n")
    r = int(input("R.: "))

    if(r == 0):
        break
    elif(r == 1):
        v = int(input("\nValor: "))
        root = myTree.insert_node(root, v)
    elif(r == 2):
        v = int(input("\nRemover Nó (Valor): "))
        root = myTree.delete_node(root, v)
    elif(r == 3):
        myTree.printHelper(root, "", True)