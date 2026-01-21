from typing import Dict, Any


def predict_fraud_logic(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Scoring simplifié pour prédire la fraude (Route 15).

    Parameters
    ----------
    data : dict
        Données de la transaction.
    """
    is_fraud = False
    probability = 0.05

    # Logique de détection : transfert élevé
    if data.get("type") == "TRANSFER" and data.get("amount", 0) > 200000:
        is_fraud = True
        probability = 0.89

    return {"isFraud": is_fraud, "probability": probability}
