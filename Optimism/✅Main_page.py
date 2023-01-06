# start to build Optimism megadash


# first of all lets import libraries
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image




# Set the outlook of first page
st.set_page_config(
    page_title = 'Optimism Mega Dashboard',
    page_icon = ':bar_chart:',
    layout = 'wide'
)


st.title("What is Optimism network?")

st.write(
    """Due to the high density of transactions in the Ethereum network, second layer technologies have come to the aid of this network to reduce the transaction time and also the transaction sending fee in this popular network. Optimistic is one of the Ethereum layer two solutions that uses Rollup technology to provide its security from the Ethereum network, but it will reduce the transaction cost in the Ethereum network by 100 times.

[**Optimism**](https://www.optimism.io/) is one of the most famous second layer solutions of Ethereum, which is provided with the aim of making Ethereum more scalable. This second layer solution increases the speed of transactions in the Ethereum network and significantly reduces the cost of transactions or transactions. In this solution, Ethereum network transactions are processed in the second layer and only the information of that transaction will be stored on the main Ethereum network. As a result, the security of this solution is provided by the Ethereum main network, which increases the reliability of this method"""
)

col1, col2, col3 = st.columns([1,1.5,1])

with col1:
  st.write("")

with col2:
  st.image(
            "https://zerocap.com/wp-content/uploads/2021/03/OPTIMISM.jpg",
            width=500, 
        )

with col3:
  st.write("")


st.header('What will you see in this app?')

st.write(
"""1. Optimims performance contains: $OP price, Daily transactions, Active users and status tracker

2. $OP Airdrop

3. NFTs on Optimism

4. Swaps on Optimism""")


st.subheader('Tools')
st.write(
    """
   The data for this app are selected from the [**Flipside Crypto**](https://flipsidecrypto.xyz/)
    data platform by using its **REST API**. These queries are currently set to **re-run every 24 hours** to cover the latest
    data and are imported as a JSON file directly to each page. 
    

    The codes of this tool are accessible in its 
    [**GitHub Repository**](https://github.com/alitslm/cross_chain_monitoring).
""")
st.subheader('References')
st.write(
   """ 
    Besides the codes and queries mentioned above, the following dashboards created using Flipside Crypto were used
    as the core references in developing the current tool:
    - [Optimism performance](https://app.flipsidecrypto.com/dashboard/whats-going-on-with-optimism-rx_d4S)
    - [$OP airdrop](https://app.flipsidecrypto.com/dashboard/op-airdrop-redux-b_HCUR)
    - [Secondary sale on Optimism](https://app.flipsidecrypto.com/dashboard/secondary-nft-market-mega-dashboard-q-C9ZT)
    - [Swaps on Optimism](https://app.flipsidecrypto.com/dashboard/optimism-de-xs-redux-a7arsg)

    """)

c1, c2 = st.columns(2)
with c1:
    st.info('**Author: [@MLDzmnG](https://twitter.com/GargariZamani)**')
with c2:
    st.info('**Source of data: [Flipside Crypto](https://flipsidecrypto.xyz/)**')