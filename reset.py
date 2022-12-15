import os
if 'build.csv' in os.listdir(os.getcwd()):
    os.remove('build.csv')
    os.remove('times.csv')