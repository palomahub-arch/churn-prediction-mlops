# 🎯 Churn Prediction MLOps

Sistema completo de predição de churn com pipeline automatizado de MLOps.

## 📊 Sobre o Projeto

Previsão de churn de clientes em uma empresa de telecomunicações, utilizando práticas modernas de MLOps para garantir reprodutibilidade, monitoramento e deploy contínuo.

## 🏗️ Arquitetura

```
Data → Processing → Training → Registry → API → Monitoring
```

## 🚀 Quick Start

```bash
# Setup
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt

# Executar pipeline
make all
```

## 📈 Status do Projeto

- [x] Setup inicial
- [ ] Pipeline de dados
- [ ] Modelo baseline
- [ ] API REST
- [ ] Deploy
- [ ] Monitoramento


## 📊 Análise Exploratória

### Dataset
- **Fonte:** Kaggle Telco Customer Churn
- **Tamanho:** 7,043 linhas × 21 colunas
- **Target:** Churn (Yes/No)
- **Taxa de Churn:** 26.5%

### Principais Insights
1. **Desbalanceamento:** Mais clientes não-churn (73.5%)
2. **Contratos:** Month-to-month tem 3x mais churn
3. **Serviços:** Fiber optic correlacionado com mais churn
4. **Pagamento:** Electronic check tem maior taxa de churn

### Tratamentos Necessários
- [ ] Missing values em TotalCharges
- [ ] Encoding de variáveis categóricas
- [ ] Normalização de numéricas
- [ ] Balanceamento de classes
 

## 🛠️ Stack Tecnológico

- **ML:** Scikit-learn, XGBoost
- **Tracking:** MLflow, DVC
- **API:** FastAPI
- **Deploy:** Docker, AWS
- **Monitoring:** Prometheus, Grafana

## 📝 Licença

MIT License