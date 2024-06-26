from great_tables import GT, md


def create_table_airport(df):
    df['name_clean'] = df['apt_nom'].str.title() + " _(" + df['apt'] + ")_"
    df = df[['name_clean'] + [col for col in df.columns if col != 'name_clean']]
    table_gt = (
        GT(df.head(15))
        .cols_hide(columns=df.filter(like="apt_nom").columns.tolist())
        .cols_hide(columns=df.filter(items=["apt"]).columns.tolist())
        .fmt_number(columns=df.filter(like="pax").columns.tolist(), compact=True)
        .fmt_number(columns=df.filter(like="traffic").columns.tolist(), compact=True)
        .fmt_markdown(columns=df.filter(like="name").columns.tolist())
        .cols_label(
            name_clean=md("**Aéroports**"),
            apt_pax_dep=md("**Départs**"),
            apt_pax_tr=md("**Transit**"),
            apt_pax_arr=md("**Arrivées**"),
            traffic=md("**Traffic**")
        )
        .tab_header(
            title=md("**Statistiques de fréquentation des aéroports français**")
        )
        .tab_source_note(
            source_note=md("_Source: DGAC, à partir des données sur data.gouv.fr_")
        )
    )
    return table_gt
