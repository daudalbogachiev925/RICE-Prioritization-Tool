import streamlit as st
from rice import load_features, prioritize

st.title("🎯 RICE Prioritizer")
features = prioritize(load_features())
rows = [{"Feature": f.name, "RICE": round(f.rice_score, 2),
         "Reach": f.reach, "Impact": f.impact,
         "Confidence": f.confidence, "Effort": f.effort} for f in features]
st.table(rows)
