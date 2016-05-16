from django.shortcuts import render_to_response
from app.models import Client
from app.models import Contract
from app.models import Worth

def index(request):
    clients_list = Client.objects.all().order_by('id')
    return render_to_response('app/index.html', {'clients_list': clients_list,
                                                 'cells_list':cells_list,
                                                 'profit':profit,
                                                 'max_payment':max_payment})

class Cell_infomation(object):
    def __init__(self,cell_number,contract_number,holder,worths):
        self.cell_infomation = {}
        self.cell_infomation['contract_number'] = contract_number
        self.cell_infomation['cell_number'] = cell_number
        self.cell_infomation['holder'] = holder
        self.cell_infomation['worths'] = ', '.join(worths)

    def get_sell_information(self):
        return self.cell_infomation

class Statistics(object):
    def __init__(self,contracts):
        self.contracs = contracts
        self.contracts_list = []
        for self.contract in self.contracs:
            self.contracts_list.append(self.contract.payment)
    def profit(self):
        return sum(self.contracts_list)
    def max_payment(self):
        return max(self.contracts_list)

contracts = Contract.objects.all()
cells_list = []

for contract in contracts:
    worths = Worth.objects.filter(contract = contract.id)
    worths_list = []
    for worth in worths:
        worths_list.append(worth.evidence)
    new_cells_information = Cell_infomation(contract.cell_number,contract.contract_number,contract.client,worths_list)
    cells_list.append(new_cells_information.get_sell_information())

statistic = Statistics(contracts)
profit = statistic.profit()
max_payment = statistic.max_payment()


