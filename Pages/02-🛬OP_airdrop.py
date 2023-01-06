import streamlit as st
import pandas as pd
import altair as alt




st.set_page_config(
    page_title = '$OP Airdrop',
   # page_icon = '✅',
    layout = 'wide'
)

st.title("Stats of $OP airdrop")

with st.expander("About $OP airdrop"):
    st.write(
        f""" The Optimism layer 2 network has finally launched its governance token like many other layer 2 networks. Optimism developer team has distributed this token to its users through airdrop. The token of this network is called OP and its main use will be participation in governance processes and the ability to create and manage multi-signature accounts in the Optimism network.

After the distribution and application of the OP token, the Optimism network will go towards decentralization. The decentralization of this network allows users to play a role as network nodes in creating blocks and performing transactions and participate in Optimism's governance decisions. It is also highly likely that OP token will be used to pay transaction fees on the Optimism network after its official launch.

A total of 4,294,967,296 OP tokens will be distributed in the initial offering. In the first year, 30% of these tokens are distributed; Of course, this amount may undergo changes after the participation of OP token users and owners in the process of its distribution.

OP tokens are distributed as follows:

25% will belong to Optimizm network ecosystem fund.

19% is distributed as airdrop.

20% is used to reward network users.

17% belongs to investors.

19% goes to Optimism developers and team.
        """)

st.cache(ttl=400)

df= pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7b13f76a-d980-4081-b381-3e99350c4ead/data/latest') # OP airdrop1
df1=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eff75615-29be-4b8a-848d-54a8d184eb64/data/latest') # OP airdrop over time
df2=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c7203d88-a6e2-456c-baa2-58d443ffec33/data/latest') # application of OP
df3=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/18b093f6-2227-4b0a-b12f-c860f49ea24e/data/latest') # application2

st.subheader('General stats of $OP airdrop')
placeholder = st.empty()
with placeholder.container():
        # create three columns
        col1, col2, col3 = st.columns(3)
col1.metric(label="Total users claimed optimism airdrop", value=df['WALLETS'])
col2.metric(label="Total volume of claimed $OP", value=df['VOLUME_OP'])
col3.metric(label="Share (%) of claimed $OP", value=df['SHARE_VOLUME'])

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df1).mark_line().encode(x='DATE:T', y='VOLUME_OP').properties( title='Volume of claimed airdrop over time')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df1).mark_line().encode(x='DATE:T', y='WALLETS',color=alt.value('red')).properties(title='Count of wallets claimed airdrop over time')

            st.write(fig12.properties(width=500))

placeholder = st.empty()

st.subheader('Application of $OP token')
placeholder = st.empty()

fig_col1, fig_col2 = st.columns(2)
with fig_col1:
           
            fig11= alt.Chart(df2).mark_bar().encode(
                x=alt.X('GP', axis=alt.Axis(title='')),
                y=alt.Y('N_USERS', axis=alt.Axis(title='Count of claimers')),
                color='GP'
                ).properties( title='HODL or USE of airdropped $OP')
            st.write(fig11.properties(width=500))
with fig_col2:
            fig12=alt.Chart(df3).mark_bar().encode(
                x=alt.X('FIRST_ACTIONS', axis=alt.Axis(title=''),sort='y'),
                y=alt.Y('USERS', axis=alt.Axis(title='Count of users')),
                color='FIRST_ACTIONS',
                
                ).properties( title='Top actions done by airdropped $OP')

            st.write(fig12.properties(width=500))