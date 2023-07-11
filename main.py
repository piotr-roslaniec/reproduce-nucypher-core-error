import inspect

import nucypher_core
from nucypher_core import umbral, ferveo


for line in inspect.getsourcelines(nucypher_core)[0]:
    print(line)
print()

for line in inspect.getsourcelines(umbral)[0]:
    print(line)
print()

for line in inspect.getsourcelines(ferveo)[0]:
    print(line)


from nucypher_core.ferveo import InvalidShareNumberParameter

print(InvalidShareNumberParameter)
