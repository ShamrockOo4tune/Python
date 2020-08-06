"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class Warehouse:
    _inventory = []


class Hardware(Warehouse):

    def __init__(self, brand: str, connection_type: str, max_paper_size: str, wi_fi_support: bool):
        self.brand = brand
        self.connection_type = connection_type
        self.max_paper_size = max_paper_size
        self.wi_fi_support = wi_fi_support
        Warehouse._inventory.append(self)


class Printer(Hardware):
    def __init__(self, brand: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 colorful: bool, print_type: str, print_dpi: int):
        self.colorful = colorful
        self.print_type = print_type
        self.print_dpi = print_dpi
        super().__init__(brand, connection_type, max_paper_size, wi_fi_support)


class Scanner(Hardware):
    def __init__(self, brand: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 scan_dpi: int, auto_feed: bool):
        self.scan_dpi = scan_dpi
        self.auto_feed = auto_feed
        super().__init__(brand, connection_type, max_paper_size, wi_fi_support)


class CopyMachine(Hardware):
    def __init__(self, brand: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 scan_dpi: int, auto_feed: bool, colorful: bool, print_type: str, print_dpi: int):
        self.scan_dpi = scan_dpi
        self.auto_feed = auto_feed
        self.colorful = colorful
        self.print_type = print_type
        self.print_dpi = print_dpi
        super().__init__(brand, connection_type, max_paper_size, wi_fi_support)


printer = Printer('HP', 'USB', 'A4', True, True, 'laser', 1200)
scanner = Scanner('BearPaw', 'USB', 'A4', False, 1200, False)
xerox = CopyMachine('Xerox', 'Ethernet', 'A3', True, 1200, True, True, 'laser', 1200)

print(1)
