import streamlit as st
import pandas as pd
import altair as alt
alt.renderers.enable('mimetype')




st.set_page_config(
    page_title = 'NFT sale on Optimism',
   # page_icon = '✅',
    layout = 'wide'
)

st.title("NFT sale on Optimism")

with st.expander("About NFTs and Optimism"):
    st.write(
        f""" 
NFTs are non-exchangeable tokens. They are issued as a unique digital certificate of ownership for any type of digital asset. In fact, an NFT is a smart contract that is regulated and digitally secured using open source platforms (which anyone can download from sites like GitHub).

NFTs can be used to tokenize (digitize) almost anything. However, different types of "media" make the most use of these tokens. The most popular applications of NFTs include the following (active projects in each area are also indicated):

Digital artworks (SuperRare, KnownOrigin, Async Art, Rarible, OpenSea)

Digital music (Mintbase, InfiNFT, Airnft and Audius)

Virtual Real Estate (Cryptovoxels, Decentraland and Sandbox)

Wearable items of virtual reality or VR Gaming and computer games (Axie Infinity, Sorare and…)

Tickets for various events or permission to attend them (get protocol)

Event attendance/activity subscription badges (POAP and Galaxy)

Blockchain domain names (Ethereum Name Service, Unstoppable Domains and TNS)

[**Quixotic**](https://qx.app/) is the largest NFT marketplace operating on Optimism. Soon after announcing the optimistic airdrop, Quixotic announced its official launch to the masses. Since it runs on Optimism, its transactions and operations are fast and cheap compared to other markets.

        """)



st.cache(ttl=400)

df= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b2cb0da0-9f77-422a-a1b2-5f4ab5f70fd9/data/latest') # NFT general
df1=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/77901e7e-0b01-40fb-bfa1-688c2fd3040f/data/latest') # NFT over time
df2=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e588c35e-47c1-4c9e-bff8-3d80a942a341/data/latest') # top collections
df3=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/e6b57c47-9490-4c1c-bbff-95bbec6c18ce/data/latest') # distribution
df4=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c86dd27f-6e7a-49c5-874a-89190d91346f/data/latest') # hold time

st.subheader('General stats')
placeholder = st.empty()
with placeholder.container():
        # create three columns
        col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Total sale count", value=df['SALE_NO'])
col2.metric(label="Total unique purchasers", value=df['BUYER_NO'])
col3.metric(label="Total sale volume in USD", value=round(df['VOLUME_USD'],2))
col4.metric(label="Average sale price in USD", value=round(df['AVERAGE_VOLUME'],2))

placeholder = st.empty()

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df1).mark_bar().encode(
                x=alt.X('DATE', axis=alt.Axis(title='DATE')),
                y=alt.Y('SALE_NO', axis=alt.Axis(title=''))
    
                ).properties( title='Count of NFT sale over time')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df1).mark_area().encode(
                x=alt.X('DATE', axis=alt.Axis(title='')),
                y=alt.Y('VOLUME_USD', axis=alt.Axis(title='')),
                color=alt.value('red')
                
                ).properties( title='Sale volume in USD over time')

            st.write(fig12.properties(width=500))

            placeholder = st.empty()

st.subheader('Top NFT collections')
placeholder = st.empty()

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df2).mark_bar().encode(
                x=alt.X('NFT', axis=alt.Axis(title=''),sort='y'),
                y=alt.Y('VOLUME_USD', axis=alt.Axis(title='Volume in USD'))
    
                ).properties( title='Top NFT collections with highest sale volume')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df2).mark_bar().encode(
                x=alt.X('NFT', axis=alt.Axis(title=''),sort='y'),
                y=alt.Y('AVERAGE_PRICE', axis=alt.Axis(title='')),
                color=alt.value('red')
                
                ).properties( title='Average sale price in USD')

            st.write(fig12.properties(width=500))

            placeholder = st.empty()

st.subheader('Purchaser behavior')
placeholder = st.empty()

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df3).mark_bar().encode(
                x=alt.X('BUCKETS', axis=alt.Axis(title='')),
                y=alt.Y('BUYER_NO', axis=alt.Axis(title='count of purchasers'))
    
                ).properties( title='Purchasers distribution by various price')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df4).mark_bar().encode(
                x=alt.X('BUCKETS', axis=alt.Axis(title='')),
                y=alt.Y('COUNT_USERS', axis=alt.Axis(title='count of purchasers')),
                color=alt.value('red')
                
                ).properties( title='NFT hold time on Optimism')

            st.write(fig12.properties(width=500))
