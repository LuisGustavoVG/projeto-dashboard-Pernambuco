import plotly.express as px
import streamlit as st
import pandas as pd
from visu import formatar_moeda_brl, formatar_valor_curto, formatar_valor_grande, formatar_populacao, formatar_compacto, imagem_circular

def grafico_populacao_maior(df, coluna):
    df_grafico = df.sort_values(coluna).tail(5)
    fig = px.bar(df_grafico,
        x=coluna, 
        y="Município [-]",
        orientation="h",
        text="População Formatada", 
        title="5 Municípios com Maior População",
        color="Município [-]"
    )
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico["Município [-]"]),
        showlegend=False
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(showticklabels=False)
    yaxis=dict(showticklabels=False)
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_populacao_menor(df, coluna):
    df_grafico = df.sort_values(coluna).head(5)
    fig = px.bar(df_grafico,
        x=coluna, 
        y="Município [-]",
        orientation="h",
        text="População Formatada", 
        title="5 Municípios com Menor População",
        color="Município [-]"
    )
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico["Município [-]"]),
        showlegend=False
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(showticklabels=False)
    yaxis=dict(showticklabels=False)
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_comparacao_pib(df, coluna):
    maiores = df.sort_values(coluna).tail(5)
    menores = df.sort_values(coluna).head(5)
    comparacao = pd.concat([maiores, menores])
    df_comparacao = comparacao.sort_values(coluna, ascending=False)
    df_comparacao["PIB Formatado"] = df_comparacao[coluna].apply(formatar_moeda_brl)
    fig = px.bar(
    df_comparacao,
    x="Município [-]",
    y=coluna,
    color="Município [-]",
    text="PIB Formatado",
    title="Comparação dos 5 Maiores e 5 Menores PIB dos Municípios"
    )

    fig.update_layout(
        xaxis_title="",
        yaxis_title="",
        showlegend=False,

    )

    fig.update_traces(textposition="outside")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_xaxes(showgrid=False, zeroline=False)

    return st.plotly_chart(fig, use_container_width=True)

def grafico_comparacao_resultado_fiscal(df, coluna):
    maiores = df.sort_values(coluna).tail(5)
    menores = df.sort_values(coluna).head(5)
    comparacao = pd.concat([maiores, menores])
    df_comparacao = comparacao.sort_values(coluna, ascending=False)
    df_comparacao["Resultado Fiscal Formatado"] = df_comparacao[coluna].apply(formatar_moeda_brl)

    fig = px.bar(df_comparacao, 
        x="Município [-]",
        y=coluna, 
        text="Resultado Fiscal Formatado",
        title="Resultados Fiscais Comparados",
        color="Município [-]"
    )
    fig.update_layout(
        xaxis_title="",
        yaxis_title="",
        showlegend=False,

    )

    fig.update_traces(textposition="outside")
    fig.update_yaxes(showticklabels=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_xaxes(showgrid=False, zeroline=False)

    return st.plotly_chart(fig, use_container_width=True)

def grafico_menor_pib(df, coluna):
    df_grafico = df.sort_values(coluna).head(5)
    fig = px.bar(df_grafico,
        x=coluna, 
        y="Município [-]",
        orientation="h",
        text="PIB Formatado", 
        title="5 Menores PIB per Capita",
        color="Município [-]"
    )
    
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico["Município [-]"]),
        showlegend=False
    )
    fig.update_layout(showlegend=False)
    fig.update_xaxes(showticklabels=False)
    yaxis=dict(showticklabels=False)
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_maior_pib(df, coluna):
    df_grafico_n = df.sort_values(coluna).tail(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="PIB Formatado", 
        title="5 Maiores PIB per Capita",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_maior_idh(df, coluna):
    df_grafico_n = df.sort_values(coluna).tail(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="IDH Formatado", 
        title="5 Maiores IDH de Pernambuco",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_menor_idh(df, coluna):
    df_grafico_n = df.sort_values(coluna).head(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="IDH Formatado", 
        title="5 Menores IDH de Pernambuco",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_maior_mortalidade(df, coluna):
    df_grafico_n = df.sort_values(coluna).tail(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="Mortalidade Formatada", 
        title="5 Maiores Taxas de Mortalidade Infantil em Pernambuco",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_menor_mortalidade(df, coluna):
    df_grafico_n = df.sort_values(coluna).head(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="Mortalidade Formatada", 
        title="5 Menores Taxas de Mortalidade Infantil em Pernambuco",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)

def grafico_densidade_demografica_maior(df, coluna):
    df_grafico_n = df.sort_values(coluna).tail(5)
    fig = px.bar(df_grafico_n, 
        x=coluna, 
        y="Município [-]",
        text="Densidade Formatada", 
        title="5 Maiores Densidades Demográficas em Pernambuco",
        color="Município [-]")
    fig.update_layout(
        yaxis=dict(categoryorder="array", categoryarray=df_grafico_n["Município [-]"]),
        showlegend=False
    )
    fig.update_xaxes(title=None)
    fig.update_yaxes(title=None)
    # Remove legenda (se quiser continuar sem ela)
    fig.update_xaxes(showticklabels=False)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition="inside")
    return st.plotly_chart(fig, use_container_width=True)