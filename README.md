# Install the Poetry Environment locally
```
$ poetry config virtualenvs.in-project true
$ poetry install
```
# Run with Poetry Environment 
This assumes that you are in the `bin` directory.

The `metis` library is currently broken with a simple typo. 

In `.venv/lib/python3.8/site-packages/metis.py` at line 574 replace `for i in H.node` with `for i in H.nodes` 
```
$ poetry run python partition_gate_assignment.py -settings ../runs/settings.txt -samples 216
```