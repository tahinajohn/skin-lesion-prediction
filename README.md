---
title: Skin Lesion Classification
emoji: 📊
colorFrom: gray
colorTo: green
sdk: docker
pinned: false
license: mit
short_description: classification of a skin lesion
---


# 🔬 Détecteur de Maladies Cutanées avec CNN

Ce projet utilise un réseau de neurones (CNN) pour reconnaître automatiquement 4 maladies de peau à partir d'une photo :

- 🔴 **Acné**
- 🔵 **Varicelle** (Chickenpox)
- 🟠 **Rougeole** (Measles)
- 🟣 **Monkeypox**

⚠️ **Attention** : Ce projet est éducatif. Il ne remplace pas un avis médical.

---

## 📌 Comment ça marche ?

1. On donne au modèle 200 photos de chaque maladie
2. Le modèle apprend à repérer les différences (texture, forme, couleur des lésions)
3. On lui montre une nouvelle photo → il devine la maladie avec un pourcentage de confiance

Le modèle utilise le **Transfer Learning** : au lieu d'apprendre à "voir" depuis zéro, il part d'un modèle (ResNet18) déjà entraîné sur des millions d'images, puis on l'adapte à notre tâche.

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|---|---|
| **PyTorch** | Créer et entraîner le modèle |
| **ResNet18** | Modèle pré-entraîné (Transfer Learning) |
| **Streamlit** | Interface web pour tester le modèle |
| **Google Colab** | Entraînement avec GPU gratuit |

---

---

## 🚀 Installation

**1. Cloner le projet**
```bash
git clone https://github.com/tahinajohn/skin-lesion-prediction.git
cd skin-lesion-prediction
```

**2. Installer les librairies**
```bash
pip install -r requirements.txt
```

---

## 🖥️ Lancer l'application

Une fois le modèle entraîné :

```bash
streamlit run app.py
```

Une page web s'ouvre automatiquement où vous pouvez :
1. Télécharger une photo
2. Cliquer sur "Analyser l'image"
3. Voir le diagnostic prédit avec le pourcentage de confiance

---

## 📊 Résultats

| Métrique | Valeur |
|---|---|
| Accuracy (validation) | ~76% |
| Nombre d'images | 800 (200 par classe) |
| Temps de prédiction | < 2 secondes |

---

## ⚠️ Limites du projet

- Petit dataset (200 images/classe) → le modèle peut se tromper
- Certaines maladies se ressemblent visuellement (ex: Varicelle vs Rougeole)
- Ce n'est **pas** un outil de diagnostic médical officiel

---

## 🔮 Améliorations possibles

- Ajouter plus d'images pour améliorer la précision
- Tester d'autres modèles (ResNet50, EfficientNet)
- Ajouter une détection de zones de lésions (Grad-CAM)
- Déployer l'app en ligne (Streamlit Cloud)

---

## 👤 Auteur

Projet réalisé dans un but d'apprentissage du Deep Learning et de la Computer Vision.