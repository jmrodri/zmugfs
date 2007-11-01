export PYTHONPATH=../../zmugjson/:$PYTHONPATH
mkdir -p $1
python ./zmugfs.py -d $1
