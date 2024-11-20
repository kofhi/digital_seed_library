import streamlit as st
import db

# SEED CHARACTERISTICS CRITERIA 
criteria_column_1, criteria_column_2, criteria_column_3, criteria_column_4 = st.columns(4)

with criteria_column_1:
    seed_type_select = st.selectbox("Seed Type", db.get_seed_types())
    all_seed_types = st.checkbox('All Seed Types', True)
