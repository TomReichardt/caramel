import pytest
from pathlib import Path
from csv import DictReader

with open(Path("caramel/cases/tests/testdata.csv"), newline="") as f:
    test_data = list(DictReader(f, skipinitialspace=True))


@pytest.fixture(scope="module", params=list(range(len(test_data))))
def string_permutations(request):
    return test_data[request.param]
