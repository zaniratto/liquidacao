import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import base64

st.set_page_config(layout="wide")

#Configuração da página de fundo
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("img/brasao.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: 120px;
        background-repeat: no-repeat;
        background-position: 300px 60px;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


#Configuração do relógio e da data

agora = datetime.now()

components.html(
    f"""
    <div style="
        position: fixed;
        top: 10px;
        right: 20px;
        text-align: right;
        font-size: 16px;
        font-weight: 600;
        z-index: 9999;
        background-color: rgba(255,255,255,0.9);
        padding: 6px 10px;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    ">
        📅 {agora.strftime('%d/%m/%Y')}<br>
        ⏰ {agora.strftime('%H:%M:%S')}
    </div>
    """,
    height=80,
)



def home():
 st.write("Página INICIAL")  




def despesas_fixas():
    container1 = st.container()
    container2 = st.container()

    with container1:
        st.markdown(
            """
            <h2 style="text-align: center;">
                Despesas Fixas
            </h2>
            """,
            unsafe_allow_html=True
        )

    with container2:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Luz")
            st.markdown("[CEMIG CT 07](https://docs.google.com/spreadsheets/d/1j8Th4LU8hGf3zhOsD7LQOb1ZRPqiV-pq_77Zne3aJg4/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 08](https://docs.google.com/spreadsheets/d/1JH1OxEp3T8Iyb4YNGsfJ_EZ9D1Fd5QsLNO1Dt4R2HXs/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 09](https://docs.google.com/spreadsheets/d/1y9lA70R-aVHW4yiQoMiSlND1jTVF0Bk2I8veRuRsVoA/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 10](https://docs.google.com/spreadsheets/d/1WCyBOnzs532MNCnIOEfFifMR-yFb0JAdXB9hNabXFQs/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 11](https://docs.google.com/spreadsheets/d/1hh6GUnJdYpjzsDVkNrZs-_HKjsBPFTK5ODC_mwZjoAA/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 24](https://docs.google.com/spreadsheets/d/1rAMzJJkJWZdF_9iBjtcDQho3yNKiAGb1AeFCTY0eHSE/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 25](https://docs.google.com/spreadsheets/d/1r5oSM5oVd7j7lFu916P1Ux_N4O60DFJDxPHtyGbeBgo/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 28](https://docs.google.com/spreadsheets/d/1TzUOIu0z2NxxXjnxtMeg_6wgsgSZpEhdaTMs9otFteU/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 72](https://docs.google.com/spreadsheets/d/15xK_kv48jO0RkcMpHBEhbZ_OW4pOtxfwEfmDuODcOSM/edit?gid=0#gid=0)")

        with col2:
            st.header("Água")

        with col3:
            st.header("Comunicação")

def bolsas():
    st.write("Página Bolsas")

def auxilio_financeiro():
    st.write("Página Auxílio Financeiro")

def terceirizada():
    st.write("Página Terceirizada")

with st.sidebar:
    st.header("Liquidação")
    pagina = st.radio(
        "Páginas",
        ["Home", "Despesas Fixas", "Bolsas", "Auxílio Financeiro", "Terceirizada"]
    )

if pagina == "Home":
    home()
elif pagina == "Despesas Fixas":
    despesas_fixas()
elif pagina == "Bolsas":
    bolsas()
elif pagina == "Auxílio Financeiro":
    auxilio_financeiro()
elif pagina == "Terceirizada":
    terceirizada()
