import pandas as pd
insurance_data = {
    'Name': ['Gabe', 'Aziz', 'Maci', 'Megan', 'Tyler', 'Kwame', 'Arsh', 'Ellie', 'Imraj', 'Arjun'],
    'Age' : [18, 20, 30, 35, 45, 28 , 40, 50, 36, 25],
    'Region': ['Ontario', 'Manitoba', 'BC', 'Ontario', 'Alberta', 'Manitoba', 'Alberta', 'Ontario', 'Alberta', 'Alberta'],
    'Gender': ['Male', 'Male', 'Female', 'Female','Male', 'Male', 'Male', 'Female', 'Male', 'Male'],
    'PolicyType':['Life', 'Health', 'Auto', 'Life', 'Health', 'Auto', 'Auto', 'Life', 'Health', 'Auto'],
    'PremiumAmount': [500, 700, 900, 1200, 800, 600, 900, 1200, 800, 0],
    'TenureYears': [1,3,5,2,6,4, 5,4,7,3],
    'ClaimAmount': [0, 200, 1000, 300, 0, 50, 1000, 300, 0, 50],
    'NoOfClaims': [0,1,0,2,1,0,3,2,1,0]


}

insurance_df = pd.DataFrame(insurance_data)

#question 1
print(f'Displaying first 5 rows of dataset : \n {insurance_df.head(5)}')
print(f'\n............................\n')

#question 2
print("Showing all column names and datatypes...")
insurance_df.info()
print(f'\n............................\n')

#question 3
filtered_df = insurance_df[['Name', 'Age', 'Region']]
print(f'Displaying filtered dataset : \n {filtered_df}')
print(f'\n............................\n')

#question 4
ontario_df = insurance_df[insurance_df['Region'] == 'Ontario']
print(f'Displaying data where region is Ontario : \n {ontario_df}')
print(f'\n............................\n')

#question 5

print(f'Total male and female customers...\n {insurance_df['Gender'].value_counts()}')
print(f'\n............................\n')

#question 6
print(f'Customers with PremiumAmount > 700...\n {insurance_df[insurance_df['PremiumAmount'] > 700]}')
print(f'\n............................\n')

#question 7

print(f'Customers with atleast 1 claim...\n {insurance_df[insurance_df['NoOfClaims'] >=1]}')
print(f'\n............................\n')

#question 8
insurance_df['PremiumPerYear'] = insurance_df['PremiumAmount']/insurance_df['TenureYears']

#question 9
def has_claim(claim_amount):
    if claim_amount > 0:
        return "Yes"
    else:
        return "No"

insurance_df['HasClaim'] = insurance_df['ClaimAmount'].apply(has_claim)
print(f'New column HasClaim Added...\n {insurance_df}')
print(f'\n............................\n')

#question 10
have_insurance_df = insurance_df[(insurance_df['PremiumAmount'] > 0) & (insurance_df['Region'] == 'Alberta')]
print(f'Customers who have health insurance and live in Alberta...\n {have_insurance_df}')
print(f'\n............................\n')

#question 11
premium_by_region = insurance_df.groupby('Region')['PremiumAmount'].mean()
print(f'Average Premium by Region: \n {premium_by_region}')
print(f'\n............................\n')


#question 12
claim_amt_total = insurance_df.groupby('PolicyType')['PremiumAmount'].sum()
print(f'Total Claim Amount by policy type: \n {claim_amt_total}')
print(f'\n............................\n')

#question 13
max_tenure_years = insurance_df.groupby('Gender')['TenureYears'].max()
print(f'Maximum tenure years by gender: \n {max_tenure_years}')
print(f'\n............................\n')

#question 14
print("Renaming PremiumAmount to Premium_CAD....\n")
renameData = {'PremiumAmount': 'Premium_CAD'}
insurance_df.rename(renameData, axis = 1, inplace =True)
print(f'Renaming done: \n ')
insurance_df.info()
print(f'\n............................\n')

#question 15
agg_data = {
    'Premium_CAD' : 'sum',
    'ClaimAmount' : 'sum'
}

sum_premium_claim  = insurance_df.groupby(['PolicyType', 'Region']).agg(agg_data)
print(f'Sum of Premium amount and claim amount grouped by policy type and region: \n {sum_premium_claim}')
print(f'\n............................\n')

#question 16
policy_average = insurance_df.groupby('PolicyType')['Premium_CAD'].mean()
greater_than_avg = insurance_df[((insurance_df['PolicyType'] == 'Auto') & (insurance_df['Premium_CAD'] > policy_average['Auto'])) |
                                ( (insurance_df['PolicyType'] == 'Health' ) & (insurance_df['Premium_CAD'] > policy_average['Health'])) |
                                ((insurance_df['PolicyType'] == 'Life' ) & (insurance_df['Premium_CAD'] > policy_average['Life']))]
print(f'data of customers where their premium_cad is greater than their respective policy premium averages: \n {greater_than_avg}')
print(f'\n............................\n')

#question 17
top_3 = insurance_df.sort_values(by='ClaimAmount').tail(3)
print(f'Top 3 cxs with highest claim amount are \n {top_3}')
print(f'\n............................\n')

#question 18
def cal_risk(claimAmt):
    if claimAmt > 2000:
        return "High"
    elif (claimAmt > 500) and (claimAmt <= 2000):
        return "Medium"
    else:
        return "Low"

insurance_df['RiskLevel'] = insurance_df['ClaimAmount'].apply(cal_risk)

print(f'Updated data with new column RiskLevel \n {insurance_df}')
print(f'\n............................\n')

#question 19
filterted_19_df = insurance_df[(insurance_df['TenureYears'] > 5) & (insurance_df['NoOfClaims'] >= 1) & (insurance_df['PolicyType'] == 'Life')]

print(f'Filtered data where tenure is> 5, claims >=1  and policy  is life \n {filterted_19_df}')
print(f'\n............................\n')

#question 20
data = insurance_df.groupby('Region')['Premium_CAD'].sum()
highest = data.sort_values().tail(1)
print(f'Region with highest total premium is \n {highest}')
print(f'\n............................\n')

