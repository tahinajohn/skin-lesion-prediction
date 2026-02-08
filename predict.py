import torch

# ============================================================================
# FONCTION: PRÉDICTION SUR UNE IMAGE
# ============================================================================

def predict_image(image, model, class_names, device, transform):
    """
    Fait une prédiction sur une image uploadée
    
    Args:
        image: image PIL
        model: modèle PyTorch
        class_names: liste des classes
        device: cpu ou cuda
        transform: transformations
    
    Returns:
        predicted_class: classe prédite
        confidence: confiance (0-1)
        all_probs: probabilités pour toutes les classes
    """
    # Appliquer les transformations
    image_tensor = transform(image).unsqueeze(0)  # Ajoute dimension batch [1, 3, 224, 224]
    image_tensor = image_tensor.to(device)
    
    # Prédiction (sans calcul de gradients)
    with torch.no_grad():
        outputs = model(image_tensor)
        
        # Convertir les scores en probabilités avec softmax
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        probs = probabilities[0].cpu().numpy()
        
        # Trouver la classe avec la probabilité maximale
        pred_idx = torch.argmax(outputs, 1).item()
        predicted_class = class_names[pred_idx]
        confidence = probs[pred_idx]
    
    return predicted_class, confidence, probs