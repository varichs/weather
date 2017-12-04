import glob
import os

def all_files(pattern, search_path, pathsep = os.pathsep): 
  for path in search_path.split(pathsep): 
    for match in glob.glob(os.path.join(path, pattern)): 
      yield match 
# print(type(all_files('*.csv', './')))      
# print(all_files('*.csv', './').__next__()) 
for match in all_files('*.csv', './'):   
  print(match)