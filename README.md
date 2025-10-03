# 🏦 Azure Document Intelligence - Detector de Cartões Falsos

Este projeto utiliza **Azure Document Intelligence** e **Azure Blob Storage** para detectar e validar cartões de crédito através de análise de documentos e imagens.

## 🚀 Funcionalidades

- 📤 **Upload de Imagens**: Interface web para upload de arquivos (PNG, JPG, JPEG)
- ☁️ **Azure Blob Storage**: Armazenamento seguro de imagens na nuvem
- 🧠 **Azure Document Intelligence**: Análise automática de cartões de crédito
- ✅ **Validação de Cartões**: Detecção de cartões válidos e falsos
- 📊 **Interface Streamlit**: Dashboard interativo para visualização dos resultados

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** - Interface web
- **Azure Blob Storage** - Armazenamento de arquivos
- **Azure Document Intelligence** - Análise de documentos
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📁 Estrutura do Projeto

```
docs_azure_inteligence/
├── src/
│   ├── app.py                 # Aplicação principal Streamlit
│   ├── requirements.txt       # Dependências do projeto
│   ├── .env                   # Variáveis de ambiente (não versionado)
│   ├── ultils/
│   │   └── Config.py         # Configurações e variáveis de ambiente
│   └── service/
│       ├── blob_service.py   # Serviços do Azure Blob Storage
│       └── doc_service.py    # Serviços do Document Intelligence
└── README.md
```

## ⚙️ Configuração

### 1. Pré-requisitos

- Python 3.8 ou superior
- Conta do Microsoft Azure
- Azure Storage Account configurado
- Azure Document Intelligence configurado

### 2. Instalação

```bash
# Clone o repositório
git clone https://github.com/kaykesandes/docs_azure_inteligence.git
cd docs_azure_inteligence

# Navegue para a pasta src
cd src

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configuração das Variáveis de Ambiente

Crie um arquivo `.env` na pasta `src/` com as seguintes configurações:

```env
# Azure Blob Storage
CONTAINER-NAME=cartoes
CARTOES_CONNECTION_STRING=sua_connection_string_aqui
STOREGE_ACCOUNT_NAME=nome_da_sua_storage_account
KEY_SOTOREGE_ACCOUNT=chave_da_sua_storage_account

# Azure Document Intelligence
DOC_ENDPOINT=https://seu-endpoint.cognitiveservices.azure.com/
KEY_DOC_INTELLIGENCE=sua_chave_do_document_intelligence
```

## 🚀 Como Executar

```bash
# Navegue para a pasta src
cd src

# Execute a aplicação Streamlit
streamlit run app.py
```

A aplicação será aberta no navegador em `http://localhost:8501`

## 💡 Como Usar

1. **Upload de Arquivo**: Clique em "Escolha um arquivo" e selecione uma imagem de cartão de crédito
2. **Processamento**: O arquivo será enviado para o Azure Blob Storage
3. **Análise**: O Azure Document Intelligence analisará a imagem
4. **Resultado**: Visualize se o cartão é válido ou falso com as informações extraídas

### Informações Extraídas (Cartões Válidos):
- 👤 Nome do Titular
- 🏛️ Banco Emissor  
- 📅 Data de Validade

## 🔐 Segurança

- Todas as credenciais são gerenciadas através de variáveis de ambiente
- Arquivos `.env` não são versionados no Git
- Conexão segura com serviços Azure via HTTPS

## 🏗️ Arquitetura

```
[Interface Streamlit] 
        ↓
[Upload de Arquivo]
        ↓
[Azure Blob Storage] → [Azure Document Intelligence]
        ↓                       ↓
[URL da Imagem] ← [Dados Extraídos]
        ↓
[Validação e Exibição]
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Kayke Sandes**
- GitHub: [@kaykesandes](https://github.com/kaykesandes)
- LinkedIn: [kayke-sandes](https://linkedin.com/in/kayke-sandes)

## 🔗 Links Úteis

- [Documentação Azure Blob Storage](https://docs.microsoft.com/azure/storage/blobs/)
- [Documentação Azure Document Intelligence](https://docs.microsoft.com/azure/applied-ai-services/form-recognizer/)
- [Documentação Streamlit](https://docs.streamlit.io/)

---

⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!