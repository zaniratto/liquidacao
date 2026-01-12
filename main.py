import streamlit as st

st.set_page_config(layout="wide")

def home():
    st.write("Bem-vindo à página inicial!")

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
            st.markdown("[CEMIG CT 07](https://docs.google.com/spreadsheets/d/e/2PACX-1vRpn1bwgV0dnJAyIObfDJu1yhhE7wrO8aEilh52AgoHnNxVwxieXOMie4jymnp_Wb2BRSd1ItWwr3RO/pubhtml)")
            st.markdown("[CEMIG CT 08](https://docs.google.com/spreadsheets/d/e/2PACX-1vS-8WYu1SSipiWpyTKn2zJ_SOdK0mPkRHzAguLpsdOVd3isMNqyKtT5anX1pdW0E8qP1GYiS7xd6XVk/pubhtml)")
            st.markdown("[CEMIG CT 09](https://docs.google.com/spreadsheets/d/e/2PACX-1vSk00O7EcyfrP1iJIiXeISAzFQubdL4LjZTXG0gs07WukIlPlSiHKqSqI0ATxn2gRRDC-WMzKp1bFYL/pubhtml)")
            st.markdown("[CEMIG CT 10](https://docs.google.com/spreadsheets/d/e/2PACX-1vSXq_iEYGnPB2JOPnriD3rO1Fp9NwctJ9YCR2Lr6_FKV-uglycKHm7rI0nZFme13H1DHdUXEoNUXPsF/pubhtml)")
            st.markdown("[CEMIG CT 11](https://docs.google.com/spreadsheets/d/e/2PACX-1vS77aXbpPpsaZGzXCtYAdmFQbzfhTldamxl3Fy279NMAPzVLzPIEviH3qLm-WIvFzhlwFUP3sEZhPNf/pubhtml)")
            st.markdown("[CEMIG CT 24](https://docs.google.com/spreadsheets/d/e/2PACX-1vQyxfS9AlMqCH1tGyLEr380MiA5CzzHmZVo9WjpkYG25Lx0HVlIK9sJmmL5qS6ke36u5gOwwGstDlSM/pubhtml)")
            st.markdown("[CEMIG CT 25](https://docs.google.com/spreadsheets/d/e/2PACX-1vRfHZdoHNWb7fQnagTbLBmUyTanWfchYogI0U9O6QuUzL9V6yRlcAj4Nglvjo-XeXJZ8tW6II2dRY0y/pubhtml)")
            st.markdown("[CEMIG CT 28](https://docs.google.com/spreadsheets/d/e/2PACX-1vQ39GI9fKahU6zRvLAX66OG7BlG7uI8rKr_gjCbPZp4KoHsayfRL9KO5OF-KrTOHNrasHfydIVlFZ_S/pubhtml)")
            st.markdown("[CEMIG CT 72](https://docs.google.com/spreadsheets/d/e/2PACX-1vQMUBglA93B_S2UETL5n1q7wGT19t6ZtJ-KluXudCOonKKBzsw6UO20mOzWOOnOk7uLgY09qhfMMCwT/pubhtml)")

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
