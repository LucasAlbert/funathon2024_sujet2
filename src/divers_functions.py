
def create_dataframe_input(df, an, mois):
    return df[(df['an'] == str(an)) & (df['mois'] == str(mois))]


def summary_stat_airport(df):
    return (
        df
        .groupby(['apt', 'apt_nom'])
        .agg({'apt_pax_dep': 'sum', 'apt_pax_tr': 'sum', 'apt_pax_arr': 'sum', 'traffic': 'sum'})
        .sort_values('traffic', ascending=False)
        .reset_index()
        )
