def clean_dataframe(df):
    df['an'] = df['ANMOIS'].str.replace('..$', "", regex=True)
    df['mois'] = df['ANMOIS'].str.replace('....*0', "", regex=True)
    df = df.rename(str.lower, axis="columns")
    return df
