def test_pass(rp_logger):
    rp_logger.info("Цей тест успішно пройшов")
    assert True

def test_fail(rp_logger):
    rp_logger.error("Цей тест провалився")
    assert False
