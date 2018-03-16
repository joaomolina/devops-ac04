def inicializar():
tab = [ ]
for i in range(3):
linha = [ ]
for j in range(3):
linha.append(".")
tab.append(linha)
return tab
def main( ):
jogo = inicializar( )
print (jogo)
if __name__ == "__main__":
main()
Passo 6
• Edite o conteúdo do arquivo src/testes.py para que fique
com o conteúdo abaixo:
Import jogovelha
import sys
erroInicializar = False
jogo = jogovelha.inicializar()
if len(jogo) != 3:
erroInicializar = True
else:
for linha in jogo:
if len(linha) != 3:
erroInicializar = True
else:
for elemento in linha:
if elemento != '.':
erroInicializar = True
if erroInicializar:
sys.exit(1)
else:
sys.exit(0)
