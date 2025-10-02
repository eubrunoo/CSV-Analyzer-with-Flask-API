from libs import *

def processar_dados_vendas(df, nome_col_produto, nome_col_preco, nome_col_qtd, nome_col_cliente):

    df["Subtotal"] = df[nome_col_preco] * df[nome_col_qtd]

    receita_total = df["Subtotal"].sum().item()

    produtos_selecionados = df[[nome_col_produto, nome_col_qtd]]
    produtosAgrupados = produtos_selecionados.groupby(produtos_selecionados[nome_col_produto]).sum()

    maior_venda = produtosAgrupados[nome_col_qtd].idxmax()

    clientes_subtotal = df[[nome_col_cliente, 'Subtotal']]
    clientes_subtotal_agrupados = clientes_subtotal.groupby([nome_col_cliente], as_index=False).sum()

    melhor_cliente = clientes_subtotal_agrupados['Subtotal'].idxmax()
    melhor_cliente_id = clientes_subtotal_agrupados.loc[melhor_cliente, nome_col_cliente].item()

    transacoes = len(df)

    dict_ = {
    "receita_total" : receita_total,
    "produtos_mais_vendidos" : maior_venda,
    "cliente_com_maior_gasto" : melhor_cliente_id,
    "total_transacoes" : transacoes
    }

    return dict_


if __name__ == '__main__':
    df_principal = pd.read_csv('sales_test.csv') 
    resultado = processar_dados_vendas(df_principal)
    print(resultado)
