import pytest

from phonebook import Phonebook


@pytest.fixture
def phonebook(tmpdir):
    """
    Provides an empty Phonebook within a temp directory
    """
    return Phonebook(tmpdir)


def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    phonebook.add('Murilo', '1414')
    assert "1234" == phonebook.lookup("Bob")
    assert '1414' == phonebook.lookup('Murilo')


def test_phonebook_contains_all_names(phonebook):
    phonebook.add("Bob", "1234")
    phonebook.add('Murilo','1414')
    assert phonebook.names() == {"Bob","Murilo"}


def test_missing_name_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")