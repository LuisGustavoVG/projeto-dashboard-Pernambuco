import streamlit as st
import pandas as pd
import plotly.express as px
from visu import formatar_moeda_brl, formatar_valor_curto, formatar_valor_grande, formatar_populacao, formatar_compacto, imagem_circular
from graph import grafico_populacao_menor, grafico_comparacao_pib, grafico_comparacao_resultado_fiscal, grafico_menor_pib, grafico_maior_pib, grafico_maior_idh, grafico_menor_idh, grafico_maior_mortalidade, grafico_menor_mortalidade, grafico_populacao_maior, grafico_densidade_demografica_maior


st.set_page_config(
     page_title="dashboard",
     page_icon="📊",
     layout="wide"
)

st.title("Painel de Dados dos Municípios de Pernambuco 2025")

# ======================================================
# 📌 CARREGAR TABELA
# ======================================================
df = pd.read_excel("a081f9ef87b9fe16ad19d98b0a692802.xlsx", header=2)

coluna_pib = "PIB per capita - R$ [2021]"
coluna_receita = "Total de receitas brutas realizadas - R$ [2024]" 
coluna_despesas = "Total de despesas brutas empenhadas - R$ [2024]"
coluna_populacao = "População no último censo - pessoas [2022]"
coluna_idh = "IDHM <span>Índice de desenvolvimento humano municipal</span> [2010]"
coluna_resultado_fiscal = "Resultado Fiscal"
coluna_eficiencia = "Eficiência Fiscal"
creceita_per_capita = "Receita Per Capita"
coluna_mortalidade = "Mortalidade infantil - óbitos por mil nascidos vivos [2023]"
coluna_densidade = "Densidade demográfica - hab/km² [2022]"

df[coluna_pib] = pd.to_numeric(df[coluna_pib], errors="coerce")
df[coluna_receita] = pd.to_numeric(df[coluna_receita], errors="coerce")
df[coluna_despesas] = pd.to_numeric(df[coluna_despesas], errors="coerce")
df[coluna_populacao] = pd.to_numeric(df[coluna_populacao], errors="coerce")
df[coluna_idh] = pd.to_numeric(df[coluna_idh], errors="coerce")
df[coluna_resultado_fiscal] = pd.to_numeric(df[coluna_resultado_fiscal], errors="coerce")
df[coluna_eficiencia] = pd.to_numeric(df[coluna_eficiencia], errors="coerce")
df[creceita_per_capita] = pd.to_numeric(df[creceita_per_capita], errors="coerce")
df[coluna_mortalidade] = pd.to_numeric(df[coluna_mortalidade], errors="coerce")
df[coluna_densidade] = pd.to_numeric(df[coluna_densidade], errors="coerce")

df["Receita Formatada"] = df[coluna_receita].apply(formatar_moeda_brl)
df["PIB Formatado"] = df[coluna_pib].apply(formatar_moeda_brl)
df["Despesa Formatada"] = df[coluna_despesas].apply(formatar_moeda_brl)
df["População Formatada"] = df[coluna_populacao].apply(formatar_populacao)
df["IDH Formatado"] = df[coluna_idh].apply(lambda x: f"{x:.3f}")
df["Resultado Fiscal Formatado"] = df[coluna_resultado_fiscal].apply(formatar_moeda_brl)
df["Eficiência Fiscal Formatado"] = df[coluna_eficiencia].apply(formatar_moeda_brl)
df["Receita Per Capita Formatada"] = df[creceita_per_capita].apply(formatar_moeda_brl)
df["Mortalidade Formatada"] = df[coluna_mortalidade].apply(lambda x: f"{x:.2f}")
df["Densidade Formatada"] = df[coluna_densidade].apply(formatar_populacao)


# 🔹 Somar receita total
idh = df[coluna_idh].sum()
total_receita = df[coluna_receita].sum()
total_despesa = df[coluna_despesas].sum()
pib_medio = df[coluna_pib].mean()
pib_muni = df[coluna_pib] * df[coluna_populacao]
resultado_fiscal = df[coluna_resultado_fiscal].sum()
eficiencia_fiscal = df[coluna_eficiencia].mean()
pib_total_estado = pib_muni.sum()
receita_per_capita = df[creceita_per_capita].sum()

pop_total_estado = df[coluna_populacao].sum()

# PIB per capita do estado
pib_pc_estado = pib_total_estado / pop_total_estado


receita_adequada = formatar_valor_curto(total_receita)
resultado_adequado = formatar_valor_curto(resultado_fiscal)
despesa_adequada = formatar_valor_curto(total_despesa)
populacao_adequada = formatar_populacao(pop_total_estado)


# ======================================================
# 📌 EXIBIR RESULTADO
# ======================================================
indice1, indice2, indice3 = st.columns(3)

with indice1:
    st.container(border=True).metric("Total de receitas brutas realizadas", formatar_moeda_brl(receita_adequada))
with indice2:
    st.container(border=True).metric("Total de despesas brutas empenhadas", formatar_moeda_brl(despesa_adequada))
with indice3:
    st.container(border=True).metric("PIB Total de Pernambuco", formatar_compacto(pib_total_estado))

# ======================================================
# 📊 GRÁFICOS
# ======================================================
abas = st.tabs(["visão geral", "Finanças", "Demografia"])

with abas[0]:
    grafico_comparacao_pib(df, coluna_pib)     
    col1, col2 = st.columns([1,2])
    with col1:
        grafico_menor_pib(df, coluna_pib)
    with col2:   
        grafico_maior_pib(df, coluna_pib)

with abas[1]:
    indice1, indice2, indice3 = st.columns(3)
    with indice1:
        st.container(border=True).metric("Resultado Fiscal", formatar_compacto(resultado_fiscal))
    with indice2:
        st.container(border=True).metric("Eficiência Fiscal", formatar_compacto(eficiencia_fiscal))
    
    grafico_comparacao_resultado_fiscal(df, coluna_resultado_fiscal)  

with abas[2]:
    options = ["População", "Mortalidade Infantil", "IDH", "Densidade Demográfica"]
    selection = st.segmented_control(
    "opções", options, selection_mode="single"
    )
    if selection == "População":
        grafico_populacao_maior(df, coluna_populacao)
        grafico_populacao_menor(df, coluna_populacao)
    elif selection == "Mortalidade Infantil":
        grafico_menor_mortalidade(df, coluna_mortalidade)
    elif selection == "IDH":
        grafico_maior_idh(df, coluna_idh)
        grafico_menor_idh(df, coluna_idh)
    elif selection == "Densidade Demográfica":
        st.write("Gráfico de Escolaridade em construção...")
        grafico_densidade_demografica_maior(df, coluna_densidade)
    
# ======================================================
# 📌 SIDEBAR
# ======================================================
with st.sidebar:
    foto = "minha_foto.jfif"
    foto_circular = imagem_circular(foto)
    st.image(foto_circular,width=300)
    st.title("LUIS GUSTAVO VIANA GURGEL")
    st.container(border=True).metric("População Total", formatar_populacao(populacao_adequada))
    st.container(border=True).metric("Eficiência Fiscal Média", formatar_compacto(eficiencia_fiscal))
    st.container(border=True).metric("Receita Per Capita Média", formatar_compacto(receita_per_capita))
    st.container(border=True).metric("Resultado Fiscal", formatar_compacto(resultado_fiscal))
    
    