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

## 🛠️ Stack Tecnológico

- **ML:** Scikit-learn, XGBoost
- **Tracking:** MLflow, DVC
- **API:** FastAPI
- **Deploy:** Docker, AWS
- **Monitoring:** Prometheus, Grafana

## 📝 Licença

MIT License