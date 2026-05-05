# from bokoll.components.filter import filter_layout
# import streamlit as st

# from bokoll.components.line_chart import line_chart_hyresutveckling
# from bokoll.components.kpis import (
#     demografi_snittålder,
#     demografi_invånare,
#     demografi_inkomst,
#     demografi_skattesats,
# )
# from bokoll.components.bar_chart_befolkning import bar_chart_befolkning
# from bokoll.components.bar_chart import bar_chart


# def page_layout():
#     st.title("Demografi")
#     st.header("Filtrera på kategori och stadsdel")
#     filter_df = filter_layout()

#     # Övre raden: Hyresutveckling och KPI:er
#     rad1_col1, rad1_col2 = st.columns(2, gap="medium")

#     with rad1_col1:
#         with st.container(border=True):
#             st.subheader("Hyresutveckling")
#             line_chart_hyresutveckling(
#                 vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
#             st.caption("Källa: SCB")

#     with rad1_col2:
#         with st.container(border=True):
#             st.subheader("Demografi i korthet")

#             # 2x2-grid med fyra KPI:er
#             kpi_col1, kpi_col2 = st.columns(2, gap="small")
#             with kpi_col1:
#                 demografi_snittålder(
#                     vald_stadsdel=st.session_state.vald_stadsdel,
#                     vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
#             with kpi_col2:
#                 demografi_invånare(
#                     vald_stadsdel=st.session_state.vald_stadsdel,
#                     vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

#             kpi_col3, kpi_col4 = st.columns(2, gap="small")
#             with kpi_col3:
#                 demografi_inkomst(
#                     vald_stadsdel=st.session_state.vald_stadsdel,
#                     vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
#             with kpi_col4:
#                 demografi_skattesats(
#                     vald_stadsdel=st.session_state.vald_stadsdel,
#                     vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)

#             st.caption("Källa: SCB")

#     # Nedre raden: två stapeldiagram
#     rad2_col1, rad2_col2 = st.columns(2, gap="medium")

#     with rad2_col1:
#         with st.container(border=True):
#             st.subheader("Befolkningsmängd")
#             bar_chart_befolkning(filter_df)
#             st.caption("Källa: SCB")

#     with rad2_col2:
#         with st.container(border=True):
#             st.subheader("Boendeform")
#             bar_chart(
#                 vald_stadsdel=st.session_state.vald_stadsdel,
#                 vald_stadsdelsomrade=st.session_state.vald_stadsdelsomrade)
#             st.caption("Källa: SCB")


# if __name__ == "__main__":
#     page_layout()