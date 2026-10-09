# ✏️ Prática – Caça às Bruxas

Disciplina Testes de Software Aplicado \
Profa. Marília Mendes \
Aluno: Henrique Segundo

### Diagrama 1

#### Diagrama imagem:

![Imagem Diagrama 1](Diagrama%201.png)

#### Complexidade ciclomática:

##### Método 1 - Regiões no Grafo de controle

Área interna: R1,R2,R3,R4
Área externa: R5
Total: 5

##### Método 2 - Formula

C = E - N + 2 -> C = 14 - 11 + 2 -> 5

##### Método 3 - Estruturas de decisão

Estrutura de decisão + 1 -> 4 + 1 -> 5

#### Casos de teste

##### Caminhos

| Caso | Caminho                      |
|------|------------------------------|
| 1    | N1,N2,N3,N5,N6,N6,N7,N8,N11  |
| 2    | N1,N2,N4,N5,N6,N6,N7,N8,N11  |
| 3    | N1,N2,N3,N5,N6,N7,N9,N10,N11 |
| 4    | N1,N2,N3,N5,N6,N7,N9,N11     |
| 5    | N1,N2,N4,N5,N6,N7,N8,N11     |

##### Entradas e saídas

| Caso | PrimeiroNumero | SegundoNumero | Resultado |
|------|----------------|---------------|-----------|
| 1    |                |               |           |
| 2    |                |               |           |
| 3    |                |               |           |
| 4    |                |               |           |
| 5    |                |               |           |

### Diagrama 2

#### Diagrama imagem:

![Imagem Diagrama 2](Diagrama%202.png)

#### Complexidade ciclomática:

##### Método 1 - Regiões no Grafo de controle

Área interna: R1,R2,R3
Área externa: R4
Total: 4

##### Método 2 - Formula

C = E - N + 2 -> C = 11 - 9 + 2 -> 4

##### Método 3 - Estruturas de decisão

Estrutura de decisão + 1 -> 3 + 1 -> 4

#### Casos de teste:

##### Caminhos

| Caso | Caminho                 |
|------|-------------------------|
| 1    | N1,N2,N9                |
| 2    | N1,N2,N3,N4,N5,N2,N9    |
| 3    | N1,N2,N3,N4,N6,N7,N2,N9 |
| 4    | N1,N2,N3,N4,N6,N8,N2,N9 |

##### Entradas e saídas

| Caso | array | valor | retorno |
|------|-------|-------|---------|
| 1    |       |       |         |
| 2    |       |       |         |
| 3    |       |       |         |
| 4    |       |       |         |
| 5    |       |       |         |

### Diagrama 3

#### Diagrama imagem:

![Imagem diagrama 3](Diagrama%203.png)

#### Complexidade ciclomática:

##### Método 1 - Regiões no Grafo de controle

Área interna: R1,R2,R3
Área externa: R4
Total: 4

##### Método 2 - Formula

C = E - N + 2 -> C = 12 - 10 + 2 -> 4

##### Método 3 - Estruturas de decisão

Estrutura de decisão + 1 -> 3 + 1 -> 4

#### Casos de teste:

##### Caminhos

| Caso | Caminho              |
| ---- | -------------------- |
| 1    | 1,2,3,6,8,9,11,12,15 |
| 2    | 1,2,3,6,8,9,10,15    |
| 3    | 1,2,3,6,7,15         |
| 4    | 1,2,3,4,6,7,15       |

##### Entradas e saídas

| caso | numFaltas | qtdCreditos | notaTotal | notaProvaFinal | Saida |
| ---- | --------- | ----------- | --------- | -------------- | ----- |
| 1    | null      | 4           | 50        | 50             | False |
| 2    | null      | 4           | 50        | 80             | True  |
| 3    | null      | 4           | 80        | null           | True  |
| 4    | 2         | 4           | 80        | null           | True  |

### Diagrama 4

#### Diagrama imagem:

![Imagem diagrama 4](Diagrama%204.png)

#### Complexidade ciclomática:

##### Método 1 - Regiões no Grafo de controle

Área interna: R1,R2,R3
Área externa: R4
Total: 4

##### Método 2 - Formula

C = E - N + 2 -> C = 10 - 8 + 2 -> 4

##### Método 3 - Estruturas de decisão

Estrutura de decisão + 1 -> 3 + 1 -> 4

#### Casos de teste

##### Caminhos

| Caso | Caminho              |
|------|----------------------|
| 1    | N1,N2,N3,N8          |
| 2    | N1,N2,N4,N5,N8       |
| 3    | N1,N2,N4,N6,N7,N8    |
| 4    | N1,N2,N4,N6,N6,N7,N8 |

##### Entradas e saídas

| Caso | n | return |
|------|---|--------|
| 1    | 0 | 0      |
| 2    | 2 | 1      |
| 3    | 3 | 2      |
| 4    | 4 | 3      |

### Diagrama 5
#### Diagrama imagem:
#### Complexidade ciclomática:
##### Método 1 - Regiões no Grafo de controle
##### Método 2 - Formula
##### Método 3 - Estruturas de decisão
#### Casos de teste
##### Caminhos
##### Entradas e saídas
### Diagrama 6
#### Diagrama imagem:
#### Complexidade ciclomática:
##### Método 1 - Regiões no Grafo de controle
##### Método 2 - Formula
##### Método 3 - Estruturas de decisão
#### Casos de teste
##### Caminhos
##### Entradas e saídas