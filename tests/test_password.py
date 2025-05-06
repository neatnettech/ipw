from ipw.cli import generate_password


def test_generate_length():
    pwd = generate_password(16, True, True, True, True)
    assert len(pwd) == 16


def test_generate_upper_only():
    pwd = generate_password(12, True, False, False, False)
    assert all(c.isupper() for c in pwd)


def test_generate_no_charset():
    try:
        generate_password(8, False, False, False, False)
        assert False  # should raise
    except ValueError:
        assert True