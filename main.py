import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import base64
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

#Configuração da página de fundo
import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64("img/brasao.png")

st.markdown(
    f"""
    <style>
    .brasao-container {{
        position: absolute;
        top: 5px;
        left: 40%;
        transform: translateX(-40%);
        z-index: 1000;
        opacity: 0.18;  /* efeito marca d'água */
    }}

    .brasao-container img {{
        width: 180px;
    }}
    </style>

    <div class="brasao-container">
        <img src="data:image/png;base64,{img_base64}">
    </div>
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
        ⏰ {agora.strftime('%H:%M:%S')}<br>
    </div>
    """,
    height=80,
)

@st.cache_data(ttl=300)
def carregar_planilha(url):
    df = pd.read_excel(url, engine="openpyxl")
    df = df.fillna("")
    return df

def home():
    st.write("Página INICIAL")

    url_xlsx = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT7hOnKQMQ139aWYuFMlKrWiqi1WIyHYJgVt0P1Xy3DmNuibQXki_9d3Omqg0yV4A/pub?output=xlsx"

    df = carregar_planilha(url_xlsx)

    # Ocultar colunas B e D
    df = df.drop(df.columns[[1, 3]], axis=1)

    # 🔹 Criar figura
    fig, ax = plt.subplots(
        figsize=(len(df.columns) * 1.2, len(df) * 0.45)
    )

    ax.axis('off')

    tabela = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc='center',
        cellLoc='center'
    )

    tabela.auto_set_font_size(False)
    tabela.set_fontsize(5)
    tabela.scale(1.6, 1.4)

    st.pyplot(fig)


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
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Luz")
            
            st.markdown("[CEMIG CT 08 ENC](https://docs.google.com/spreadsheets/d/1JH1OxEp3T8Iyb4YNGsfJ_EZ9D1Fd5QsLNO1Dt4R2HXs/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 10 ENC](https://docs.google.com/spreadsheets/d/1WCyBOnzs532MNCnIOEfFifMR-yFb0JAdXB9hNabXFQs/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 16](https://docs.google.com/spreadsheets/d/1tWKLNTCRgfK4PlTZ0TlF-BSog14rsJiSBWemNVIbWb4/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 17](https://docs.google.com/spreadsheets/d/14V-it5G4X3FSZBqW2FefX-5bMh2Hk-NeV4X4lP7749g/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 18](https://docs.google.com/spreadsheets/d/13CjNabpZ_Yc7Z_sF_4jQWscitHhL2ZBzrHaNBkgYSkI/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 25](https://docs.google.com/spreadsheets/d/1_6vUdF4D4txhOMSbC7SxIuR8aXXw3G9I2bbmFflMgeU/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 26](https://docs.google.com/spreadsheets/d/1_UqdvCKzJt_kWtDqIB-NkahUkLabqpjjWdYPcFZn39k/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 28](https://docs.google.com/spreadsheets/d/1NKAWl0Q8r3qpLLHoXnIyU4DlZpRzy4Onb-Bb8JnNUog/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CEMIG CT 72](https://docs.google.com/spreadsheets/d/1Kc3fsblLwTQvvGXbAvJTuE8KFMtBUxuNIDf2XqitbOg/edit?gid=1679924932#gid=1679924932)")

        with col2:
            st.header("Água")

            st.markdown("[AGUAS VALADARES](https://docs.google.com/spreadsheets/d/1eExXFZXBJ0TaHNX1Z880sPd89rY86spcd7BHSMY2nGA/edit?gid=1679924932#gid=1679924932)")
            st.markdown("[CESAMA - CT 0080/2024](https://docs.google.com/spreadsheets/d/1DWFfkx10Uqo483kvHGGHv3iAbiFTsZvVG1fMI5FOFNA/edit?gid=1679924932#gid=1679924932)")

        with col3:
            st.header("Comunicação")

            st.markdown("[TELEFÔNICA IP DEDICADO](https://docs.google.com/spreadsheets/d/1tSnZLRSzYlXtD7ZyDLk6Bq3FfpxuFSEPcS049ZBPQQQ/edit?gid=1679924932#gid=1679924932)")

        with col4:
            st.header("Controle")

            st.markdown("[Despesas Fixas 2025 (Júlia) ](https://docs.google.com/spreadsheets/d/1PYBKlySsaq-hCf37yBlhO8EadyLB0mCV/edit?gid=1600794849#gid=1600794849)")
            st.markdown("[Despesas Fixas 2026 (Júlia) ](https://docs.google.com/spreadsheets/d/1rhVwj0ZN3wOPn0riv8xE-Etdru7OP7Ak/edit?gid=1600794849#gid=1600794849)")


def bolsas():
    st.write("Página Bolsas")
    container1 = st.container()
    container2 = st.container()

    with container1:
        st.markdown(
            """
            <h2 style="text-align: center;">
                BOLSAS
            </h2>
            """,
            unsafe_allow_html=True
        )

    with container2:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Bolsa 2026")
            st.markdown("[Bolsas 2026](https://docs.google.com/spreadsheets/d/1VVNud1VbeZI_cLGQlPSrDVIV4F6q_YjT/edit?gid=1359273668#gid=1359273668)")
        with col2:
            st.header("teste")

            

def auxilio_financeiro():

    import pandas as pd
    import requests
    from io import StringIO
    import streamlit as st

    sheet_id = "1Yk_MaL9TcG8BxslwMVF10QyR3KprF0ERvQkhtdpLY6o"
    gid = "998689684"

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # 1️⃣ Criar DataFrame
    df = pd.read_csv(StringIO(response.text))

    # 🔐 Verificação de segurança
    if not df.empty and df.shape[1] > 5:
        valor = int(df.iloc[0, 10])
    else:
        valor = "Sem informação"

    st.header("Auxílio Financeiro")
    st.header(f"Semana - {valor}")

    st.markdown("[Auxílio Financeiro 2025](https://docs.google.com/spreadsheets/d/1f3Ba9A5kLHro4saaQiT5l3ke2l1n1zQ93tpyHGvzUqc/edit?gid=1399653021#gid=1399653021)")
    st.markdown("[Auxílio Financeiro 2026](https://docs.google.com/spreadsheets/d/1Yk_MaL9TcG8BxslwMVF10QyR3KprF0ERvQkhtdpLY6o/edit?gid=1399653021#gid=1399653021)")
    st.markdown("### 📊 Total Auxílios 2026")

    # 2️⃣ Recorte desejado
    df_recorte = df.iloc[0:53, 7:10].copy()

    # 3️⃣ Converter colunas numéricas
    for col in df_recorte.columns[1:]:
        df_recorte[col] = (
            df_recorte[col]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        df_recorte[col] = pd.to_numeric(
            df_recorte[col], errors="coerce"
        ).fillna(0)

    # 4️⃣ Remover linhas zeradas
    df_recorte = df_recorte.loc[
        ~(df_recorte.iloc[:, 1:].eq(0).all(axis=1))
    ]

    # 5️⃣ Renomear colunas
    df_recorte.columns = ["Semana", "Liquidadas", "Nao Liquidadas"]

    st.divider()

    # 6️⃣ Exibir tabela
    html_table = df_recorte.to_html(index=False)

    st.markdown(
        f"""
        <div style="
            width: 100%;
            overflow-x: auto;
            overflow-y: auto;
            max-height: 500px;
        ">
            {html_table}
        </div>
        """,
        unsafe_allow_html=True
    )


def terceirizada():
    st.write("Página Terceirizada")
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
        col1, col2 = st.columns(2)

        with col1:
            st.header("Contratos")
            
            st.markdown("[CAPE CT 0062/2024](https://docs.google.com/spreadsheets/d/1drlAOwrNpbOguU8lQ1PhGL6biM0E1bpfCf9vZGvpFN8/edit?gid=137990838#gid=137990838)")
            
            with col2:
                st.header("Em desenvolvimento")

with st.sidebar:
    st.header("Liquidação")
    pagina = st.radio(
        "Páginas",
        ["Férias", "Despesas Fixas", "Bolsas", "Auxílio Financeiro", "Terceirizada"]
    )

if pagina == "Férias":
    home()
elif pagina == "Despesas Fixas":
    despesas_fixas()
elif pagina == "Bolsas":
    bolsas()
elif pagina == "Auxílio Financeiro":
    auxilio_financeiro()
elif pagina == "Terceirizada":
    terceirizada()
