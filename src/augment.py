import yaml

params = yaml.safe_load(open('params.yaml'))['augment']

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython augment.py data-file\n")
    sys.exit(1)

augment_type = params['type']

if len(sys.argv) != 3 and len(sys.argv) != 5:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write(
        '\tpython augment.py data-dir-path features-dir-path\n'
    )
    sys.exit(1)

train_input = os.path.join(sys.argv[1], 'train.tsv')
test_input = os.path.join(sys.argv[1], 'test.tsv')

train_output = os.path.join(sys.argv[2], 'train.tsv')
test_output = os.path.join(sys.argv[2], 'test.tsv')

os.makedirs(os.path.join('data', 'augmented'), exist_ok=True)
