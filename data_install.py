import os

os.system('mkdir data')
os.system('curl "https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-100000t-2009-04-30-0.1.zip" -o data/rate_worte.zip')
os.system('unzip data/rate_worte -d data')
os.system('curl "https://www.ids-mannheim.de/fileadmin/kl/derewo/derewo-v-ww-bll-320000g-2012-12-31-1.0.zip" -o data/ziel_worte.zip')
os.system('unzip data/ziel_worte -d data')
os.system('rm -r data/*.zip')
os.system('rm -r data/*.pdf')
os.system('mv data/derewo-v-100000t-2009-04-30-0.1 data/rate_worte.txt')
os.system('mv data/derewo-v-ww-bll-320000g-2012-12-31-1.0.txt data/ziel_worte.txt')
