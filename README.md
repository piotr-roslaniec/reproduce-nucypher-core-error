# reproduce-nucypher-core-error

## Steps to reproduce

```
pipenv shell
pipenv install
python main.py > result.txt
cat result.txt | grep InvalidShareNumberParameter
# InvalidShareNumberParameter = _ferveo.InvalidShareNumberParameter
```
