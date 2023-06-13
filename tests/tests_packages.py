import src


class Test_Cpu():
    """
    Verificando se esta retornando uma str
    """
    def test_type_CPU(self):
        assert type(src.cpu_freq()) == str, "OK"
        assert (src.cpu_freq())

    def test_type_CPU_USAGE(self):
        assert type(src.cpu_usage()) == str, "OK"


class Test_Temp():
    """
    Verificando se esta retornando uma str
    """
    def test_type_TEMP(self):
        assert type(src.temp_core()) == str, "OK"
