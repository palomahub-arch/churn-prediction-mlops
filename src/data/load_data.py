"""
Módulo para carregamento de dados de churn.
"""
import pandas as pd
from pathlib import Path
from typing import Tuple


def load_raw_data(filepath: str = "/workspaces/churn-prediction-mlops/data/raw/Telco-Customer-Churn.csv") -> pd.DataFrame:
    """
    Carrega dados brutos de churn.
    
    Args:
        filepath: Caminho para o arquivo CSV
        
    Returns:
        DataFrame com dados brutos
    """
    df = pd.read_csv(filepath)
    print(f"✅ Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas")
    return df


def get_data_info(df: pd.DataFrame) -> dict:
    """
    Retorna informações básicas sobre o dataset.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        Dicionário com estatísticas
    """
    info = {
        "n_rows": len(df),
        "n_cols": len(df.columns),
        "missing_values": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum(),
        "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2
    }
    return info


if __name__ == "__main__":
    # Teste rápido
    df = load_raw_data()
    info = get_data_info(df)
    print("\n📊 Informações do Dataset:")
    for key, value in info.items():
        print(f"  {key}: {value}")