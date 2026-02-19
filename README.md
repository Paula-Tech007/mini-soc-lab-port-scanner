# 🔐 Mini SOC Lab - Port Scanner

Projeto desenvolvido para simular um mini laboratório de segurança (SOC),
com foco na identificação de portas abertas e geração de relatório estruturado.

---

## 🎯 Objetivo

Detectar serviços expostos em um host através da varredura de portas comuns,
gerando logs e relatório em formato JSON.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Socket (nativo)
- JSON
- Logging

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/mini-soc-port-scanner.git
```

Entre na pasta do projeto:

```bash
cd mini-soc-port-scanner
```

Execute o script:

```bash
python scanner.py
```

Digite o IP alvo quando solicitado.

📄 Saída Gerada

Exibição no terminal das portas abertas

Arquivo report.json com resultado estruturado

Arquivo scan.log com logs da execução

🔒 Observação Importante

Este projeto deve ser utilizado apenas para fins educacionais
e testes autorizados.

---

## 📈 Próximas Melhorias

- Implementação de multithreading
- Scan por range de portas
- Containerização com Docker
- Exportação para CSV

---

## ▶️ Como Rodar (VS Code)

No terminal do VS Code:

```bash
python scanner.py
```

Teste primeiro com:

```
127.0.0.1
```

---

## 📸 Exemplo de Execução
(docs/execution-example.png)
