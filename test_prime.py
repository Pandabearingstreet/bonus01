import prime

def test_is_prime_method():
    assert hasattr(prime, 'is_prime'), "Your Script must have an 'is_prime'-method!"

    assert not prime.is_prime(1)
    assert prime.is_prime(2)
    assert not prime.is_prime(4)
    assert prime.is_prime(5)
    assert not prime.is_prime(12)
    assert prime.is_prime(179424673)
    assert not prime.is_prime(982451651)


def test_find_prime_method():
    assert hasattr(prime, 'find_prime'), "Your Script must have a 'find_prime'-method!"

    assert prime.find_prime(1) == 2
    assert prime.find_prime(8) == 19
    assert prime.find_prime(40) == 173
    assert prime.find_prime(1936) == 16747
