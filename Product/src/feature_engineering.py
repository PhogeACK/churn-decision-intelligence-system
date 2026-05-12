class FeatureEngineer:
    def fit(self, df):
        self.balance_threshold = df['Balance'].median()

    def transform(self, df):
        df = df.copy()

        df['active_low_satisfaction'] = (
            (df['IsActiveMember'] == 1) &
            (df['Satisfaction Score'].isin([1, 2]))
        ).astype(int)

        df['inactive_high_satisfaction'] = (
            (df['IsActiveMember'] == 0) &
            (df['Satisfaction Score'] >= 4)
        ).astype(int)

        df['complainer'] = (df['Complain'] == 1).astype(int)

        df['low_credit_score'] = (df['CreditScore'] < 600).astype(int)
        df['high_credit_score'] = (df['CreditScore'] >= 750).astype(int)

        df['low_credit_and_complains'] = (
            (df['CreditScore'] < 600) & (df['Complain'] == 1)
        ).astype(int)

        df['long_tenure'] = (df['Tenure'] >= 7).astype(int)
        df['short_tenure'] = (df['Tenure'] <= 2).astype(int)

        df['inactive_long_tenure'] = (
            (df['IsActiveMember'] == 0) & (df['Tenure'] >= 7)
        ).astype(int)

        df['single_product'] = (df['NumOfProducts'] == 1).astype(int)
        df['multi_product'] = (df['NumOfProducts'] >= 3).astype(int)

        df['active_single_product'] = (
            (df['IsActiveMember'] == 1) & (df['NumOfProducts'] == 1)
        ).astype(int)

        df['has_balance'] = (df['Balance'] > 0).astype(int)

        df['high_balance'] = (df['Balance'] > self.balance_threshold).astype(int)

        df['salary_to_balance_ratio'] = (
            df['EstimatedSalary'] / (df['Balance'] + 1)
        )

        df['young_customer'] = (df['Age'] < 30).astype(int)
        df['senior_customer'] = (df['Age'] >= 55).astype(int)

        df['senior_inactive'] = (
            (df['Age'] >= 55) & (df['IsActiveMember'] == 0)
        ).astype(int)

        return df