import streamlit as st
import pandas as pd
import altair as alt
alt.renderers.enable('mimetype')




st.set_page_config(
    page_title = 'Swaps on Optimism',
   # page_icon = '✅',
    layout = 'wide'
)

st.title("Trade activity on Optimism")

with st.expander("About swap activity and DEXs on Optimism"):
    st.write(
        f""" Decentralized exchanges (DEX) are peer-to-peer markets where digital currency traders conduct their transactions directly without entrusting the management of their funds to an intermediary or third party. 
        These transactions are facilitated through the use of self-executing agreements or smart contracts. DEXs were created to eliminate the need for any authority to monitor and authorize transactions made on a particular exchange. 
        Decentralized exchanges enable peer-to-peer (P2P) trading of cryptocurrencies.

Since decentralized exchanges are built on blockchain networks, they support smart contracts. 
Users in these types of exchanges are the guardians of their funds. Also, each transaction is accompanied by a transaction fee. 
Basically, traders interact with smart contracts on the blockchain to use decentralized exchanges.

        """)

st.cache(ttl=400)

df= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cf9650e4-81e0-4e6c-99b7-22e9436bfeee/data/latest') # swap general
df1=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b289b8ca-cbc9-437b-84b4-76a41b29b1b2/data/latest') # swap over time
df2=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/737e0de8-2199-4a06-bd1b-01c282090159/data/latest') # DEXs
df3=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/1ab66558-86fa-4000-a790-791b53459d63/data/latest') # swap from
df4=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e94f8268-795d-4981-a0f9-7cc4731af7b1/data/latest') # swap pair

st.subheader('General stats')
placeholder = st.empty()
with placeholder.container():
        # create three columns
        col1, col2, col3 = st.columns(3)
col1.metric(label="Total swap count", value=df['Swaps'])
col2.metric(label="Total unique traders", value=round(df['Swappers'],2))
col3.metric(label="Total swap volume in USD", value=round(df['Volume'],2))

placeholder = st.empty()

fig_col1, fig_col2,fig_col3 = st.columns(3)
with fig_col1:
           
            fig11= alt.Chart(df1).mark_bar().encode(
                x=alt.X('DATE', axis=alt.Axis(title='DATE')),
                y=alt.Y('Swaps', axis=alt.Axis(title=''))
    
                ).properties( title='Count of swaps over time')
            st.write(fig11.properties(width=400))
with fig_col2:
            fig12=alt.Chart(df1).mark_bar().encode(
                x=alt.X('DATE', axis=alt.Axis(title='DATE')),
                y=alt.Y('Swappers', axis=alt.Axis(title='')),
                color=alt.value('green')
                ).properties( title='Count of unique Swappers over time')
               

            st.write(fig12.properties(width=400))
with fig_col3:
           
            fig13= alt.Chart(df1).mark_bar().encode(
                x=alt.X('DATE', axis=alt.Axis(title='DATE')),
                y=alt.Y('Volume', axis=alt.Axis(title='')),
                color=alt.value('red')
               ).properties( title='Swap volume in USD over time')  
            st.write(fig13.properties(width=400))

st.subheader('Swap programs on Optimism')
placeholder = st.empty()

fig_col1, fig_col2,fig_col3 = st.columns(3)
with fig_col1:
           
            fig11= alt.Chart(df2).mark_bar().encode(
                x=alt.X('DEX', axis=alt.Axis(title='DEX'),sort='y'),
                y=alt.Y('Swaps', axis=alt.Axis(title=''))
    
                ).properties( title='Count of swaps on DEXs')
            st.write(fig11.properties(width=400))
with fig_col2:
            fig12=alt.Chart(df2).mark_bar().encode(
                x=alt.X('DEX', axis=alt.Axis(title='DEX'),sort='y'),
                y=alt.Y('Swappers', axis=alt.Axis(title='')),
                color=alt.value('purple')
                ).properties( title='Count of unique Swappers on DEXs')
            st.write(fig12.properties(width=400))
with fig_col3:
           
            fig13= alt.Chart(df2).mark_bar().encode(
                x=alt.X('DEX', axis=alt.Axis(title='DEX'),sort='y'),
                y=alt.Y('Swaps/Swapper', axis=alt.Axis(title='')),
                color=alt.value('pink')
               ).properties( title='Swaps per swapper on DEXs')  
            st.write(fig13.properties(width=400))


st.subheader('Popular assets and swap pairs on Optimism')
placeholder = st.empty()

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df3).mark_bar().encode(
                x=alt.X('SYMBOL_IN', axis=alt.Axis(title='Assets'),sort='y'),
                y=alt.Y('VOLUME', axis=alt.Axis(title='')),
                color=alt.value('yellow')
    
                ).properties( title='Popular assets on trade in Optimism')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df4).mark_bar().encode(
                x=alt.X('ASSET_PAIRS', axis=alt.Axis(title='Asset pairs'),sort='y'),
                y=alt.Y('VOLUME', axis=alt.Axis(title='')),
                color=alt.value('purple')
                ).properties( title='Popular asset pairs on trade in Optimism')
            st.write(fig12.properties(width=500))