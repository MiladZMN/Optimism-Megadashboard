import streamlit as st
import pandas as pd
import altair as alt
alt.renderers.enable('mimetype')




st.set_page_config(
    page_title = 'Performance of Optimism network',
   # page_icon = '✅',
    layout = 'wide'
)

st.title("Performance of Optimism netwrok")

with st.expander("How does optimism work?"):
    st.write(
        f"""
        This network uses Optimistic Rollup technology. As the name of this solution suggests, its basic principle is based on trust and honesty. In Optimistic solutions, it is assumed that all the information and transactions carried out by the network validators are correct and the validators perform the task assigned to them correctly. The Optimism network uses several different parts in its structure.

All Optimism blocks are stored in a special smart contract on Ethereum called CanonicalTransactionChain or CTC for short. Blocks created on the Optimism network are stored in an attached directory inside the CTC. This list forms the Optimism blockchain.

The Optimism layer 2 network has finally launched its governance token like many other layer 2 networks. Optimism developer team has distributed this token to its users through airdrop. The token of this network is called OP and its main use will be participation in governance processes and the ability to create and manage multi-signature accounts in the Optimism network.

        """)

# Input data
st.cache(ttl=600)

df= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/28864eb3-1aa8-45c1-a17f-0c938c5d4230/data/latest') # OP price
df1=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a727d9fa-a630-42d4-b057-3fc9b493d027/data/latest') # stats of network
df2=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d7d2e911-b4fe-4045-a5a1-b5932c933ab3/data/latest') # over time stats
df3=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1c64fbf5-59ff-436e-a475-3fc79598e562/data/latest') # newcomers
df4=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a2396e22-70d6-4812-ab3f-b653ae0f3d9e/data/latest') # TPM analysis
df5=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/ee74740d-ea52-415b-8927-c5cf8f06fc3b/data/latest') # Success analysis


st.header('Analysis of $OP token')
placeholder = st.empty()
with placeholder.container():
        # create three columns
        col1, col2, col3 = st.columns(3)
col1.metric(label="$OP price", value=df['TOKEN_PRICE'].iloc[-1], delta=df['DEVIATION_PRICE'].iloc[-1] , delta_color="normal")




fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df).mark_line().encode(x='DAY:T', y='TOKEN_PRICE').properties( title='Daily $OP price')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df).mark_bar().encode(x='DAY:T', y='DEVIATION_PRICE',color=alt.value('red')).properties(title='Price deviation in %')

            st.write(fig12.properties(width=500))


st.subheader('Optimism Network')
placeholder = st.empty()
with placeholder.container():
        # create three columns
        col1, col2, col3 = st.columns(3)
col1.metric(label="Total active users", value=df1['ACTIVE_WALLETS'], delta_color="normal")
col2.metric(label="Total transactions", value=df1['COUNT_TXN'], delta_color="normal")
col3.metric(label="Total paid fee in ETH", value=df1['FEE'], delta_color="normal")


fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df2).mark_line().encode(x='DATE:T', y='COUNT_TXN').properties( title='Weekly count of transactions')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df2).mark_bar().encode(x='DATE:T', y='FEE',color=alt.value('green')).properties(title='Weekly paid fee in ETH')

            st.write(fig12.properties(width=500))


fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df2).mark_bar().encode(x='DATE:T', y='ACTIVE_WALLETS',color=alt.value('yellow')).properties( title='Weekly count of Active users')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df3).mark_bar().encode(x='DATE:T', y='NEW_USERS',color=alt.value('pink')).properties(title='Weekly count of Newcomers')

            st.write(fig12.properties(width=500))


fig_col1, fig_col2 = st.columns(2)

with fig_col1:
           
    fig11=alt.Chart(df4).mark_circle().encode(x='DATE:T', y='TPM_AVERAGE',color=alt.value('purple')).properties(title='Weekly average TPM')
    
    st.write(fig11.properties(width=500))

with fig_col2:
    fig12=alt.Chart(df5).mark_area().encode(
    x="DATE:T",
    y=alt.Y("NO_TXN:Q", stack="normalize"),
    color="STATUS:N")

    st.write(fig12.properties(width=600))

            
   