import pyshacl
import sys
import os

scriptname = os.path.basename(__file__)
if len(sys.argv) != 4:
  print("Usage:",
        f"python {scriptname} data_graph_dir shapes_dir output_dir",
        sep='\n')
  sys.exit(0)
  
suf = "_report.ttl"

data_dir = sys.argv[1]
shape_dir = sys.argv[2]
out_dir = sys.argv[3]

# Get files present in data_dir and shape_dir
sh_files = os.listdir(shape_dir)
sh_files = [f for f in sh_files if os.path.isfile(os.path.join(shape_dir, f))]
dat_files = os.listdir(data_dir)
dat_files = [f for f in dat_files if os.path.isfile(os.path.join(data_dir, f))]

# Check that both data graph and shapes directories have same number of files
if len(sh_files) != len(dat_files):
  print(f"Warning: directory {shape_dir} has {len(sh_files)} files but " +
        f"directory {dat_files} has {len(data_dir)} files.")
  
print("Beginning validation...")

for dat_file in dat_files:
  print(f"\n------------------------------ Starting validation for {dat_file} ---------------------------------")
  pref = dat_file.split(sep='.')[0]
  filtered = list(filter(lambda x: pref in x, sh_files))
  if len(filtered) == 0:
    print(f"Error: no corresponding shape file for {dat_file}")
    sys.exit(1)
  if len(filtered) > 1:
    print(f"Error: more than 1 corresponding shape file for {dat_file}")
    sys.exit(1)
  sh_file = filtered[0]
  
  # Validate dat_file with the shapes in sh_file
  r = pyshacl.validate(
    os.path.join(data_dir, dat_file),
    shacl_graph=os.path.join(shape_dir, sh_file),
    abort_on_first=False
  )
  conforms, results_graph, results_text = r
  print(results_text)
  
  # Output validation report as .ttl file
  outf = os.path.join(out_dir, pref + suf)
  print(f"\nPrinting output to {outf}")
  with open(outf, 'w+') as out:
    results_graph.print(out=out)
  
print("\n-------------------------------------------------------------------------------------------------------")
print("\nValidation Complete!\n")