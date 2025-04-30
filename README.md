# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/images/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Cap 1 - Despertar da rede neural

## 👨‍👩 Grupo

Grupo de número <b>7</b> formado pelos integrantes mencionados abaixo.

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/cirohenrique/">Ciro Henrique</a> ( <i>RM559040</i> )
- <a href="javascript:void(0)">Enyd Bentivoglio</a> ( <i>RM560234</i> )
- <a href="https://www.linkedin.com/in/marcofranzoi/">Marco Franzoi</a> ( <i>RM559468</i> )
- <a href="https://www.linkedin.com/in/rodrigo-mazuco-16749b37/">Rodrigo Mazuco</a> ( <i>RM559712</i> )

## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>

### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

<b>Referência</b>: https://on.fiap.com.br/mod/assign/view.php?id=474700&c=12936

# Comparação de Modelos YOLOv5 e YOLOv8 e CNN sequencial para Detecção de Objetos

> Projeto comparativo entre os modelos YOLOv5, YOLOv8 e CNN sequencial usando diferentes durações de treinamento (60 e 80 épocas) para tarefas de detecção de objetos poderá ser encontrado em:
https://colab.research.google.com/drive/1AVIM5W9nBpiN6O0Yo3raY6aib2NIZjVR


---

# Modelos Avaliados

- YOLOv5 – 60 épocas
- YOLOv5 – 80 épocas
- YOLOv8 – 60 épocas
- YOLOv8 – 80 épocas
-  CNN Sequencial - 60 épocas  
-  CNN Sequencial - 80 épocas

---

#  Facilidade de Uso e Integração

- YOLOv5: Estrutura modular, fácil de customizar, excelente documentação.
- YOLOv8: Setup simplificado com comando único, integração com Ultralytics.
- CNN: implementação simples ótima para prototipação.

---

# Resultados e Métricas

# Precisão (mAP@0.5)

| Modelo           | mAP@0.5 / Accuracy |
|------------------|--------------------|
| YOLOv5 (60 ep)   | 0.59               |
| YOLOv5 (80 ep)   | 0.63               |
| YOLOv8 (60 ep)   | 0.72               |
| YOLOv8 (80 ep)   | 0.85               |
| CNN (60 ep)      | 88.89%             |
| CNN (80 ep)      | 69.99%             |

# Tempo de Treinamento

| Modelo         | Total estimado |
|----------------|----------------|
| YOLOv5 (60 ep) | ~3.6 min       |
| YOLOv5 (80 ep) | ~4.8 min       |
| YOLOv8 (60 ep) | ~9.0 min       |
| YOLOv8 (80 ep) | ~6.5 min       |
| CNN (60 ep)    | <1 minuto      |
| CNN (80 ep)    | <1 minuto      |

# Tempo de Inferência

| Modelo            | Tempo Médio por Imagem |
|------------------ |------------------------|
| YOLOv5 (60/80 ep) | ~15–25 ms              |
| YOLOv8 (60/80 ep) | ~20–35 ms              |
| CNN (ambos)       | ~1–5 ms                |

---

# Conclusão Geral

Para melhores resultados de precisão, o YOLOv8 com 80 épocas é a melhor escolha. Se o objetivo for leveza, o YOLOv5 leva vantagem em qualquer uma das épocas testadas. Mas o modelo mai rápido de todos e que se destacou por evitar o overfitting, parando o treinamento antes do esperado, foi a CNN sequencial.

# Notas sobre o grupo:

O grupo encontrou dificuldades técnicas para correr a CNN en colab, e devido a falta de energia que afetou a Espanha, o presente projeto teve de ser remodelado e perdeu seu formato inicial com epócas de 40, 60, 80 para todos os modelos testados. Algumas imagens do dataset foram alteradas, pois nao eram aceitas no teste com os YOLOs ou nao eram "vistas" pelo python no colab. Foram checados os formatos e também se as imagens estavam corrompidas, porém pareciam realmente normais e iguais a todas as outras imagens.

Enyd Bentivoglio, Rodrigo Mazuco, Ciro de Camargo, Marco Antonio Franzoi

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

1. <b>assets</b>: Diretório para armazenamento de arquivos complementares da estrutura do sistema.
    - Diretório "images": Diretório para armazenamento de imagens.

2. <b>config</b>: Diretório para armazenamento de arquivos em formato <i>json</i> contendo configurações.

3. <b>document</b>: Diretório para armazenamento de documentos relacionados ao sistema.

4. <b>scripts</b>: Diretório para armazenamento de scripts.

5. <b>src</b>: Diretório para armazenamento de código fonte do sistema.

6. <b>tests</b>: Diretório para armazenamento de resultados de testes.
	- Diretório "images": Diretório para armazenamento de imagens relacionadas aos testes efetuados.

7. <b>README.md</b>: Documentação do projeto em formato markdown.

<i><strong>Importante</strong>: A estrutura de pastas foi mantida neste formato para atender ao padrão de entrega dos projetos.</i>

## 🔧 Como executar o código

Como se trata de uma versão em formato <strong>Jupyter Notebook</strong>, para execução das funcionalidades, os seguintes passos devem ser seguidos:

1. Utilizando o prompt de comando, acesse o diretório `.../fase6_cap1/src` de acordo com o local de armazenamento em seu computador;
2. Execute a linha de comando `jupyter notebook` para inicializar o <strong>Jupyter Notebook</strong> a partir do diretório acessado;
3. Após a inicialização, uma nova aba será aberta em seu browser. Clique no arquivo `cnn.ipynb` para que seja carregado em outra aba do browser;
4. Selecione as células que deseja executar e clique no ícone "Run this cell and advance (Shift+Enter)" para executar os processos;

## 📋 Licença

Desenvolvido pelo Grupo 7 para o projeto da fase 6 (<i>Cap 1 - Despertar da rede neural</i>) da <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a>. Está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>