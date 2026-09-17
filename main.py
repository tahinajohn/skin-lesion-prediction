import streamlit as st
from PIL import Image
import time

from disease_info import get_disease_info
from model import load_model
from predict import predict_image
from proba import display_probabilities
from process import get_transforms

# ============================================================================
# CONFIGURATION DE LA PAGE STREAMLIT
# ============================================================================

# Configuration de la page (doit être la première commande Streamlit)
st.set_page_config(
    page_title="Détecteur de Maladies Cutanées",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# STYLE CSS PERSONNALISÉ
# ============================================================================

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 0.5rem;
        border-radius: 10px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)









# ============================================================================
# INTERFACE PRINCIPALE DE L'APPLICATION
# ============================================================================

def main():
    """
    Fonction principale de l'application Streamlit
    """
    
    # HEADER
    st.markdown("<h1>🔬 Détecteur de Maladies Cutanées par IA</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # SIDEBAR - Informations et paramètres
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/artificial-intelligence.png", width=100)
        st.markdown("## 📋 À propos")
        st.info("""
        Cette application utilise un réseau de neurones convolutif (CNN) 
        pour classifier 4 types de maladies cutanées:
        
        - 🔴 **Acne** (Acné)
        - 🔵 **Chickenpox** (Varicelle)
        - 🟠 **Measles** (Rougeole)
        - 🟣 **Monkeypox** (Mpox)
        """)
        
        st.markdown("## ⚙️ Configuration")
        
        # Option pour choisir le seuil de confiance
        confidence_threshold = st.slider(
            "Seuil de confiance minimal",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05,
            help="Probabilité minimale pour considérer une prédiction fiable"
        )
        
        st.markdown("## ⚠️ Avertissement")
        st.warning("""
        **Cette application est à titre ÉDUCATIF uniquement.**
        
        Elle ne remplace PAS un diagnostic médical professionnel.
        Consultez toujours un médecin pour un diagnostic précis.
        """)
        
        st.markdown("## 📊 Statistiques")
        st.metric("Classes détectées", "4")
        st.metric("Modèle", "ResNet18")
    
    # CHARGEMENT DU MODÈLE
    with st.spinner("🔄 Chargement du modèle..."):
        try:
            #model, class_names, device = load_model('skin_disease_classifier.pth')
            model, class_names, device = load_model(
                repo_id="ratah001/skin-disease-model",
                filename="skin_disease_classifier_real.pth"
            )

            transform = get_transforms()
            st.success("✅ Modèle chargé avec succès!")
        except Exception as e:
            st.error(f"Erreur: {e}")
            st.stop()
    
    # ZONE DE TÉLÉCHARGEMENT D'IMAGE
    st.markdown("## 📤 Télécharger une image")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choisissez une image de peau...",
            type=['jpg', 'jpeg', 'png'],
            help="Formats acceptés: JPG, JPEG, PNG"
        )
        
        # Exemples d'images (optionnel)
        st.markdown("### 💡 Conseils pour une meilleure prédiction:")
        st.markdown("""
        - Utilisez une image claire et bien éclairée
        - La zone affectée doit être visible
        - Évitez les images floues
        - Format recommandé: JPG ou PNG
        """)
    
    with col2:
        if uploaded_file is not None:
            # Afficher l'image uploadée
            image = Image.open(uploaded_file).convert('RGB')
            st.image(image, caption="Image téléchargée", width='stretch')
            
            # Bouton de prédiction
            if st.button("🔍 Analyser l'image", key="predict_button"):
                # Animation de chargement
                with st.spinner("🧠 Analyse en cours..."):
                    # Simuler un petit délai pour l'effet visuel
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                        progress_bar.progress(i + 1)
                    
                    # PRÉDICTION
                    predicted_class, confidence, all_probs = predict_image(
                        image, model, class_names, device, transform
                    )
                
                # AFFICHAGE DES RÉSULTATS
                st.markdown("---")
                st.markdown("## 🎯 Résultats de l'analyse")
                
                # Vérifier le seuil de confiance
                if confidence >= confidence_threshold:
                    # Prédiction fiable
                    st.markdown(f"""
                    <div class="prediction-box success-box">
                        <h2 style="color: #28a745;">Diagnostic: {predicted_class}</h2>
                        <h3>Niveau de confiance: {confidence*100:.2f}%</h3>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Informations sur la maladie
                    info = get_disease_info(predicted_class)
                    
                    with st.expander("📖 En savoir plus sur cette condition", expanded=True):
                        st.markdown(f"**Description:**\n{info['description']}")
                        st.markdown(f"**Symptômes typiques:**\n{info['symptomes']}")
                        st.markdown(f"**Traitement général:**\n{info['traitement']}")
                        st.markdown(f"**Gravité:**\n{info['gravite']}")
                
                else:
                    # Prédiction peu fiable
                    st.markdown(f"""
                    <div class="prediction-box warning-box">
                        <h3 style="color: #856404;">⚠️ Prédiction incertaine</h3>
                        <p style="color: black;">Diagnostic possible: {predicted_class}</p>
                        <p style="color: black;">Confiance: {confidence*100:.2f}% (< seuil de {confidence_threshold*100:.0f}%)</p>
                        <p style="color: black;"><strong>L'image n'est pas assez claire pour un diagnostic fiable.</strong></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.info("💡 Essayez avec une image plus claire ou consultez un médecin.")
                
                # Afficher les probabilités détaillées
                st.markdown("---")
                predicted_idx = class_names.index(predicted_class)
                display_probabilities(class_names, all_probs, predicted_idx)
                
                # Recommandations
                st.markdown("---")
                st.markdown("### 🏥 Recommandations")
                st.warning("""
                **Important:** Ce diagnostic automatique est indicatif uniquement.
                
                ✅ **Nous vous recommandons de:**
                - Consulter un dermatologue ou médecin
                - Ne pas s'auto-médicamenter
                - Surveiller l'évolution des symptômes
                - Prendre rendez-vous rapidement si les symptômes s'aggravent
                """)
        
        else:
            # Message si aucune image n'est uploadée
            st.info("👆 Téléchargez une image pour commencer l'analyse")
    
    # FOOTER
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 20px;">
        <p>🔬 ResNet18 Transfer Learning | 📊 4 classes de maladies cutanées</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# POINT D'ENTRÉE DE L'APPLICATION
# ============================================================================

if __name__ == "__main__":
    main()