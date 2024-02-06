def process_data(df):
	return (
		df
		.assign(value=df['VaLuE'] - 1)
		.drop(columns=['VaLuE'])
	)
