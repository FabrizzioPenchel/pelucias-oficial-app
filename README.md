# 🧸 Pelúcias Oficial - Sistema de Gestão de Máquinas de Pelúcia

![Dashboard da Aplicação](https://imgur.com/a/g6jOjxq) ## 🚀 Sobre o Projeto

Este projeto é um sistema de gestão completo para uma rede de máquinas de venda de pelúcias, desenvolvido com **Django (Python)**. O objetivo principal é centralizar o controle de operações, estoque e finanças de forma eficiente, com foco na futura integração com dispositivos IoT (Arduino) para automação em tempo real.

Ele resolve desafios reais de gerenciamento de um negócio de máquinas, fornecendo uma visão clara do desempenho.

## ✨ Funcionalidades Principais

-   **Dashboard Interativo:** Visão geral com métricas de pelúcias, máquinas, receita e despesas.
-   **Gestão de Pelúcias:** Cadastro e controle de estoque de diferentes tipos de pelúcias.
-   **Gestão de Máquinas:** Cadastro de máquinas, localização, status (operacional, reparo, manutenção) e capacidade.
-   **Controle de Estoque por Máquina:** Rastreamento detalhado de quais pelúcias e quantas unidades estão em cada máquina.
-   **Controle Financeiro:**
    -   **Despesas:** Registro e categorização de todos os gastos (compra de pelúcias, reparos, transporte, etc.).
    -   **Receitas:** Registro de ganhos (vendas de máquinas, Pix, dinheiro em espécie).
    -   **Relatórios:** Totalizadores de receita e despesa no dashboard.
-   **Registro de Vendas/Dispensas:** Cada pelúcia dispensada é registrada, com informações de máquina, pelúcia, valor, data e forma de pagamento.
-   **Gráfico de Pelúcias Distribuídas:** Visualização mensal da quantidade de pelúcias vendidas ao longo do tempo.
-   **API para Automação (IoT Ready):** Endpoint preparado para receber dados de máquinas (pagamentos, dispensas) via Arduino ou outros dispositivos.

## 💡 Desafios e Próximos Passos (IoT e Automação)

O grande diferencial e próximo desafio do projeto é a **integração com um Arduino/placa de controle** nas máquinas físicas. O objetivo é que o Arduino:
-   Comunique-se com a placa mãe da máquina para ler eventos (dinheiro inserido, pelúcia dispensada).
-   Envie esses dados para o site Django via API em tempo real.
-   Seja capaz de receber comandos do site (ex: "liberar jogada") após a confirmação de um Pix.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3.x, Django
-   **Banco de Dados:** SQLite3 (local para desenvolvimento), PostgreSQL (recomendado para produção)
-   **Frontend:** HTML5, CSS3, JavaScript (para o gráfico)
-   **Visualização de Dados:** Chart.js
-   **Controle de Versão:** Git, GitHub
-   **Deployment (Futuro):** Render.com, Gunicorn (Web Server Gateway Interface)

## ⚙️ Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e rodar o projeto em sua máquina local:

1.  **Clone o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd pelucias_oficial_final # ou o nome da sua pasta raiz
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute as Migrações do Banco de Dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Crie um Superusuário (para acessar o painel de administração):**
    ```bash
    python manage.py createsuperuser
    ```
    Siga as instruções para definir nome de usuário, e-mail e senha.

6.  **Inicie o Servidor de Desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse a Aplicação:**
    -   **Dashboard:** Abra seu navegador e vá para `http://127.0.0.1:8000/`
    -   **Painel de Administração:** Acesse `http://127.0.0.1:8000/admin/` e faça login com o superusuário criado.

## 🤝 Contribuição

Sinta-se à vontade para contribuir com melhorias, sugestões ou relatar bugs.

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes. (Se quiser adicionar uma licença no futuro)

## 📞 Contato

-   **Fabrizzio**
-   GitHub: [@ FabrizzioPenchel(https://github.com/FabrizzioPenchel[FabrizzioPenchel])
-   LinkedIn: [https://www.linkedin.com/in/fabrizzio-penchel-95667082/]
