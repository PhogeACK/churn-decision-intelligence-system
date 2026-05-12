class Encoder:
    def transform(self, df):
        df = df.copy()

        df['Geography'] = df['Geography'].str.strip().map({
            'France': 1, 'Germany': 2, 'Spain': 3
        })

        df['Gender'] = df['Gender'].str.strip().map({
            'Male': 1, 'Female': 2
        })

        df['Card Type'] = df['Card Type'].str.strip().map({
            'SILVER': 0, 'GOLD': 1, 'DIAMOND': 2, 'PLATINUM': 3
        })

        binary_cols = ['HasCrCard', 'IsActiveMember', 'Complain']
        for col in binary_cols:
            df[col] = df[col].astype(int)

        return df