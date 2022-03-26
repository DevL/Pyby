from pyby import Enumerator


def test_an_enumerator_responds_to_next():
    assert Enumerator([]).respond_to("next")


def test_repr():
    assert repr(Enumerator([1, 2, 3])) == "Enumerator([1, 2, 3])"


def test_an_enumerated_list_can_be_iterated():
    enum = Enumerator([1, 2, 3])
    assert enum.next() == 1
    assert enum.next() == 2
    assert enum.next() == 3


def test_an_enumerated_list_can_be_rewound():
    enum = Enumerator([1, 2, 3])
    assert enum.next() == 1
    assert enum.next() == 2
    enum.rewind()
    assert enum.next() == 1
