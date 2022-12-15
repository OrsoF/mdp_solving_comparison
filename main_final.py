import pandas as pd

df_build = pd.concat([pd.read_csv('build.csv'), pd.read_csv('build_gurobi.csv')])
df_times = pd.concat([pd.read_csv('times.csv'), pd.read_csv('times_gurobi.csv')])

print()
print('Building times')
print()
print(df_build)

print()
print('Run times')
print()
print(df_times)

df_build.to_excel('final_build.xlsx')
df_times.to_excel('final_times.xlsx')