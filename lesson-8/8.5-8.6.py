"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь."""


class Warehouse:
    __inventory = {'warehouse': {'printer': {'id': [], 'qty': 0}}}  # учет инвентаря по подразделениям здесь
    _id_set = {'__example'}  # множество уже используемых уникальных ID оборудования

    def __init__(self, hardware_type, item_id, dep_name='warehouse'):
        self.dep_name = dep_name
        self.hardware_type = hardware_type
        self.item_id = item_id
        Warehouse.__inventory['warehouse'].setdefault(self.hardware_type, {'id': [], 'qty': 0})

    @classmethod
    def show_inventory(cls):  # произвести инвентаризацию
        for dep_name in Warehouse.__inventory.keys():
            print(f'\nInventory of {dep_name}:')
            for eq_type in Warehouse.__inventory[dep_name]:
                print(f'Type "{eq_type}":', end='\t')
                print(Warehouse.__inventory[dep_name][eq_type])

    @property
    def receive_to_warehouse(self):  # принять для учета на склад
        if self.item_id in Warehouse._id_set:  # валидация уникальности ID предмета на складе
            print('this ID is already used. Try again with different ID')
            return
        else:
            Warehouse._id_set.add(self.item_id)
            Warehouse.__inventory['warehouse'][self.hardware_type]['id'].append(self.item_id)
            Warehouse.__inventory['warehouse'][self.hardware_type]['qty'] += 1

    def move(self, destination_dep):  # переместить в отдел "destination_dep"
        Warehouse.__inventory.setdefault(destination_dep, {self.hardware_type: {'id': [], 'qty': 0}})
        if self.dep_name == destination_dep:  # обработка случая когда предмет уже находится в этом отделе
            print(f'this ID ({self.item_id}) is already there ({destination_dep})')
            return
        elif self.item_id not in Warehouse._id_set:
            print(f'this item (ID = {self.item_id}) have not been RCed to Enterprise/Warehouse yet'
                  f'\nPlease "{self}.receive_to_warehouse" first')
            return
        Warehouse.__inventory[self.dep_name][self.hardware_type]['id'].remove(self.item_id)
        Warehouse.__inventory[self.dep_name][self.hardware_type]['qty'] -= 1
        Warehouse.__inventory[destination_dep][self.hardware_type]['id'].append(self.item_id)
        Warehouse.__inventory[destination_dep][self.hardware_type]['qty'] += 1


class Hardware(Warehouse):

    def __init__(self, item_id: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 hardware_type='new_type'):
        self.item_id = item_id
        self.connection_type = connection_type
        self.max_paper_size = max_paper_size
        self.wi_fi_support = wi_fi_support
        self.hardware_type = hardware_type
        super().__init__(hardware_type, item_id)


class Printer(Hardware):
    def __init__(self, item_id: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 colorful: bool, print_type: str, print_dpi: int):
        self.colorful = colorful
        self.print_type = print_type
        self.print_dpi = print_dpi
        hardware_type = 'printer'
        super().__init__(item_id, connection_type, max_paper_size, wi_fi_support, hardware_type)


class Scanner(Hardware):
    def __init__(self, item_id: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 scan_dpi: int, auto_feed: bool):
        self.scan_dpi = scan_dpi
        self.auto_feed = auto_feed
        hardware_type = 'scanner'
        super().__init__(item_id, connection_type, max_paper_size, wi_fi_support, hardware_type)


class CopyMachine(Hardware):
    def __init__(self, item_id: str, connection_type: str, max_paper_size: str, wi_fi_support: bool,
                 scan_dpi: int, auto_feed: bool, colorful: bool, print_type: str, print_dpi: int):
        self.scan_dpi = scan_dpi
        self.auto_feed = auto_feed
        self.colorful = colorful
        self.print_type = print_type
        self.print_dpi = print_dpi
        hardware_type = 'copy_machine'
        super().__init__(item_id, connection_type, max_paper_size, wi_fi_support, hardware_type)


printer1 = Printer('HP2600', 'USB', 'A4', True, True, 'laser', 1200)
scanner1 = Scanner('BearPaw', 'USB', 'A4', False, 1200, False)
xerox1 = CopyMachine('Xerox', 'Ethernet', 'A3', True, 1200, True, True, 'laser', 1200)
printer2 = Printer('Versalink C7025', 'parallel', 'A4', False, False, 'ink jet', 800)
scanner2 = Scanner('HewlettPackard', 'USB', 'A4', True, 1200, True)
xerox2 = CopyMachine('HP', 'Ethernet', 'A3', True, 1200, True, True, 'laser', 1200)
# noinspection PyStatementEffect
printer1.receive_to_warehouse
# noinspection PyStatementEffect
scanner1.receive_to_warehouse
# noinspection PyStatementEffect
xerox1.receive_to_warehouse
# noinspection PyStatementEffect
printer2.receive_to_warehouse
# noinspection PyStatementEffect
xerox2.receive_to_warehouse

printer1.move('production')
xerox2.move('finance')
printer2.move('reception')
scanner2.move('HR')
Warehouse.show_inventory()
print('\n\n===\nFIN\n===')
