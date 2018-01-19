from pydeconz import DeconzSession
import pytest

@pytest.fixture
def deconz_instance():
    deconz = DeconzSession(loop='fake', websession='fake', host='fake', port=80, api_key='fake')
    assert isinstance(deconz, DeconzSession)
    return deconz


def test_deconz_init_vars(deconz_instance):
    assert deconz_instance.api_url == 'http://fake:80/api/fake'
