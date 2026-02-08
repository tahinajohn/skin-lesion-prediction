# ============================================================================
# FONCTION: INFORMATIONS SUR LES MALADIES
# ============================================================================

def get_disease_info(disease_name):
    """
    Retourne des informations sur la maladie détectée
    
    Args:
        disease_name: nom de la maladie
    
    Returns:
        dict avec description, symptômes, etc.
    """
    disease_info = {
        'Acne': {
            'description': "L'acné est une affection cutanée courante causée par l'obstruction des follicules pileux.",
            'symptomes': "Points noirs, boutons rouges, kystes",
            'traitement': "Nettoyage régulier, crèmes topiques, dans certains cas antibiotiques",
            'gravite': "Généralement bénin"
        },
        'Chickenpox': {
            'description': "La varicelle est une infection virale très contagieuse causée par le virus varicelle-zona.",
            'symptomes': "Éruption de vésicules qui démangent, fièvre, fatigue",
            'traitement': "Repos, antihistaminiques pour les démangeaisons, dans certains cas antiviraux",
            'gravite': "Modéré - Contagieux"
        },
        'Measles': {
            'description': "La rougeole est une infection virale très contagieuse qui affecte principalement les enfants.",
            'symptomes': "Éruption cutanée, fièvre élevée, toux, conjonctivite",
            'traitement': "Repos, hydratation, vitamine A, vaccination préventive",
            'gravite': "Sérieux - Très contagieux"
        },
        'Monkeypox': {
            'description': "La variole du singe (Mpox) est une maladie virale rare transmise à l'homme par des animaux.",
            'symptomes': "Éruption cutanée ressemblant à des pustules, fièvre, ganglions enflés",
            'traitement': "Soins de support, isolement, dans certains cas antiviraux",
            'gravite': "Modéré à sérieux - Nécessite surveillance médicale"
        }
    }
    
    return disease_info.get(disease_name, {
        'description': "Information non disponible",
        'symptomes': "N/A",
        'traitement': "Consultez un professionnel de santé",
        'gravite': "N/A"
    })