source ~/.virtualenvs/py3.7/bin/activate
script_dir=$( dirname "${BASH_SOURCE[0]}" )
echo $script_dir
python $script_dir/upload.py $1 $2
deactivate