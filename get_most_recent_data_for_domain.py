import fingertips_py as ftp
import pandas as pd

domains = ftp.get_domains_in_profile(19)

metadata_for_domain = ftp.get_metadata_for_domain_as_dataframe(domains[1])
indicator_data = pd.DataFrame()

for indicator in metadata_for_domain['Indicator ID']:
    data = ftp.get_data_by_indicator_ids(indicator, area_type_id=102)
    data = data[data['Time period Sortable'] == data['Time period Sortable'].max()]
    data = data[data['Area Type'] == 'County & UA']
    indicator_data = indicator_data.append(data)

print(indicator_data.head().to_string())
indicator_data.to_csv('data/social_determinatants_most_recent.csv')


