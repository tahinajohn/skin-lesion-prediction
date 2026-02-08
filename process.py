from torchvision import transforms
# ============================================================================
# FONCTION: TRANSFORMATIONS POUR LES IMAGES
# ============================================================================

def get_transforms():
    """
    Transformations identiques à celles de la validation pendant l'entraînement
    IMPORTANT: Mêmes valeurs de normalisation!
    
    Returns:
        transform: pipeline de transformations
    """
    return transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],  # Stats ImageNet
            std=[0.229, 0.224, 0.225]
        )
    ])
