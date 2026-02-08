import streamlit as st
import numpy as np
# ============================================================================
# FONCTION: AFFICHER LES PROBABILITÉS SOUS FORME DE BARRES
# ============================================================================

def display_probabilities(class_names, probabilities, predicted_idx):
    """
    Affiche les probabilités de chaque classe avec des barres de progression
    
    Args:
        class_names: liste des classes
        probabilities: array des probabilités
        predicted_idx: index de la classe prédite
    """
    st.markdown("### 📊 Probabilités par classe:")
    
    # Trier par probabilité décroissante
    sorted_indices = np.argsort(probabilities)[::-1]
    
    for idx in sorted_indices:
        class_name = class_names[idx]
        prob = probabilities[idx]
        
        # Couleur différente pour la classe prédite
        if idx == predicted_idx:
            st.markdown(f"**🎯 {class_name}**")
            st.progress(float(prob))
            st.markdown(f"<span style='color: green; font-weight: bold; font-size: 18px;'>{prob*100:.2f}%</span>", 
                       unsafe_allow_html=True)
        else:
            st.markdown(f"{class_name}")
            st.progress(float(prob))
            st.markdown(f"{prob*100:.2f}%")
        
        st.markdown("---")