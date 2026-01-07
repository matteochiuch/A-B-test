import pandas as pd
df = pd.read_csv("amazon.csv")
df.head()

df['discount_percentage'] = df['discount_percentage'].str.replace('%', '', regex=False).astype(float)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df.dropna(subset=['discount_percentage', 'rating'], inplace=True)
print("Converted 'discount_percentage' and 'rating' to numeric and dropped rows with NaN values in these columns.")
print(df[['discount_percentage', 'rating']].info())

#take a look at the data of my interest
rating_counts = df['rating'].value_counts().sort_index()
print("Conteggio dei valori unici nella colonna 'rating':")
print(rating_counts)

#define the 2 groups based on median discount
median_discount = df['discount_percentage'].median()
group_a = df[df['discount_percentage'] < median_discount]
group_b = df[df['discount_percentage'] >= median_discount]
print(f"Median discount percentage: {median_discount:.2f}%")
print(f"Number of products in Group A (discount < median): {len(group_a)}")
print(f"Number of products in Group B (discount >= median): {len(group_b)}")

#calculate the average of ratings for each group and the variances
avg_rating_a = group_a['rating'].mean()
avg_rating_b = group_b['rating'].mean()
print(f"Average rating for Group A (discount < median): {avg_rating_a:.2f}")
print(f"Average rating for Group B (discount >= median): {avg_rating_b:.2f}")

variance_a = group_a['rating'].var()
variance_b = group_b['rating'].var()

print(f"Varianza del rating per il Gruppo A (sconto < mediana): {variance_a:.3f}")
print(f"Varianza del rating per il Gruppo B (sconto >= mediana): {variance_b:.3f}")

#perform the welch test, since I supposed the variances of the 2 groups are differet
from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(group_a['rating'], group_b['rating'], equal_var=False)

print(f"T-statistic (Welch's t-test): {t_stat:.3f}")
print(f"P-value (Welch's t-test): {p_value:.3f}")

alpha = 0.05
if p_value < alpha:
    print(f"Since the p-value ({p_value:.3f}) is less than the significance level ({alpha}), we reject the null hypothesis.")
    print("There is a statistically significant difference in average ratings between the two groups (assuming unequal variances).")
else:
    print(f"Since the p-value ({p_value:.3f}) is greater than the significance level ({alpha}), we fail to reject the null hypothesis.")
    print("There is no statistically significant difference in average ratings between the two groups (assuming unequal variances).")
