import pandas as pd
from typing import Dict, Any, List


def get_global_stats(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calcule les indicateurs clés de performance (KPI) globaux du dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Le DataFrame contenant l'ensemble des transactions bancaires.

    Returns
    -------
    Dict[str, Any]
        Dictionnaire contenant le volume total, le taux de fraude moyen,
        le montant moyen et le type de transaction le plus fréquent.
    """
    if df.empty:
        return {}
    return {
        "total_transactions": len(df),
        "fraud_rate": float(df['isFraud'].mean()),
        "avg_amount": float(df['amount'].mean()),
        "most_common_type": str(df['type'].mode()[0])
    }


def get_stats_by_type(df: pd.DataFrame) -> List[Dict[str, Any]]:
    """
    Calcule les statistiques de volume et de montant groupées par type.

    Parameters
    ----------
    df : pd.DataFrame
        Le DataFrame des transactions bancaires.

    Returns
    -------
    List[Dict[str, Any]]
        Une liste de dictionnaires, où chaque dictionnaire contient le type,
        le nombre de transactions et le montant moyen pour ce type.
    """
    if df.empty:
        return []
    stats = df.groupby('type').agg(
        count=('type', 'count'),
        avg_amount=('amount', 'mean')
    ).reset_index()
    return stats.to_dict(orient="records")
