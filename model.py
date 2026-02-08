import streamlit as st
from torchvision import models
import torch.nn as nn
import torch

# ============================================================================
# FONCTION: CRÉER LE MODÈLE (MÊME ARCHITECTURE QUE L'ENTRAÎNEMENT)
# ============================================================================

@st.cache_resource  # Cache le modèle pour ne pas le recharger à chaque interaction
def create_model(num_classes=4):
    """
    Recrée l'architecture EXACTE du modèle d'entraînement
    IMPORTANT: Doit être identique à celle utilisée pendant l'entraînement!
    
    Returns:
        model: architecture du modèle (sans poids)
    """
    # Charger ResNet18 (sans poids pré-entraînés car on va charger les nôtres)
    model = models.resnet18(pretrained=False)
    
    # Remplacer la dernière couche (même structure que l'entraînement)
    num_features = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_features, 256),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(256, num_classes)
    )
    
    return model

# ============================================================================
# FONCTION: CHARGER LE MODÈLE ENTRAÎNÉ
# ============================================================================

@st.cache_resource
def load_model(model_path, num_classes=4):
    """
    Charge le modèle entraîné depuis le fichier .pth
    
    Args:
        model_path: chemin vers le fichier .pth
        num_classes: nombre de classes (4 pour nous)
    
    Returns:
        model: modèle chargé prêt pour la prédiction
        class_names: liste des noms de classes
    """
    # Détection du device (CPU ou GPU)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    
    # Créer l'architecture
    model = create_model(num_classes)
    
    try:
        # Charger le checkpoint
        checkpoint = torch.load(model_path, map_location=device)
        
        # Charger les poids
        model.load_state_dict(checkpoint['model_state_dict'])
        
        # Récupérer les noms de classes
        class_names = checkpoint.get('class_names', ['Acne', 'Chickenpox', 'Measles', 'Monkeypox'])
        
        # Passer en mode évaluation
        model.eval()
        model = model.to(device)
        
        return model, class_names, device
        
    except FileNotFoundError:
        st.error(f"❌ Fichier modèle non trouvé: {model_path}")
        st.info("📁 Assurez-vous que 'skin_disease_classifier.pth' est dans le même dossier que app.py")
        st.stop()
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle: {str(e)}")
        st.stop()
