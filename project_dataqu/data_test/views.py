from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# from django.db.models import Sum

from data_test import serializer, models

class getClientsSortByAmountView(APIView):
    serializer_class = serializer.ClientesSerializer

    def get(self, request, *args, **kwargs):
        _valor_id_pram_ = 2
        company = kwargs.get('company', '')
        filterClientAmount = getClientsSortByAmount(company)
  
        return Response(filterClientAmount)

class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'ping'})

# 9.- newClientRanking
class newClientRankingiewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer_ = self.get_serializer(data=request.data)
        serializer_.is_valid(raise_exception=True)
        self.perform_create(serializer_)
        headers = self.get_success_headers(serializer_.data)
        return Response(serializer_.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

# 8.- getClientsWithLessExpense
class getClientsWithLessExpenseViewSet(viewsets.ViewSet):
     def list(self, request):
        querysetCompany = list(models.Empresas.objects.all().values())
        companyClientsRut = {}
        for company in querysetCompany:
            companyRents = list(models.Arriendos.objects.filter(id_empresa__id=company['id']).values())

            clientExpense = {}
            for rent in companyRents:
                clientID = rent['id_cliente_id']
                if not clientID in clientExpense:
                    clientExpense[clientID] = 0

                clientExpense[clientID] += rent['costo_diario']

            companyClientsRut[company['name']] = min(clientExpense, key=clientExpense.get)

        return Response(companyClientsRut)

# 7.- getCompaniesWithRentsOver1Week
class getCompaniesWithRentsOver1WeekViewSet(viewsets.ViewSet):
    def list(self, request):
        querysetCompany = list(models.Empresas.objects.all().values())

        companyClientsRut = {}
        for company in querysetCompany:
            companyRents = models.Arriendos.objects.filter(id_empresa__id=company['id'], dias__gte=7).values()
            companyClientsRut[company['name']] = len(list(companyRents))

        return Response(companyClientsRut)

# 5.- getClientsSortByAmount
class getClientsSortByAmountViewSet(viewsets.ViewSet):
    # def get(self, request, *args, **kwargs):
    def list(self, request, *args, **kwargs):
        _valor_id_pram_ = 2
        company = kwargs.get('company', '')
        filterClientAmount = getClientsSortByAmount(_valor_id_pram_)
  
        return Response(filterClientAmount)

# 4.- def getCompanyClientsSortByName():
class CompanyClientsViewSet(viewsets.ViewSet):
    def list(self, request):
        def sortList(e):
            return e['name']

        querysetCompany = models.Empresas.objects.all().values()

        companyClientsRut = {}
        for company in querysetCompany:
            companyClientsRut[company['name']] = []
            companyRents = models.Arriendos.objects.filter(id_empresa__id=company['id']).values()
            clientRut = []

            for rent in companyRents:
                countRut = sum(x.get('id') == rent['id_cliente_id'] for x in clientRut)
                
                if countRut == 0:
                    client = list(models.Clientes.objects.filter(id=rent['id_cliente_id']).values())
                    clientRut.append(client[0])
            
            sortClientRut = sorted(clientRut, key=sortList)

            onlyRut = []
            for sortClient in sortClientRut:
                onlyRut.append(sortClient['rut'])

            companyClientsRut[company['name']] = onlyRut

        return Response(companyClientsRut)

class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ClientesSerializer
    queryset = models.Clientes.objects.all()

    def get_queryset(self):
        queryset = models.Clientes.objects.all()
        sort = self.request.query_params.get('sort')

        #2.- def getClientSortByLastName():
        if sort == 'last_name':
            def sortList(e):
                lastName = e['name'].split()
                return lastName[1]
            
            unsortedQuery = queryset.values()
            sortedQuery = sorted(unsortedQuery, key=sortList)
            return sortedQuery

        #3.- def getClientsSortByRentExpenses():
        if sort == 'rent_expenses':
            def sortList(e):
                return e['rent']

            clientList = queryset.values()
            querysetRent = models.Arriendos.objects.all()
            rentList = querysetRent.values()
            
            for rent in rentList:
                for client in clientList:
                    if not 'rent' in client:
                        client['rent'] = 0

                    if 'id' in client and 'id_empresa_id' in rent and client['id'] == rent['id_empresa_id']:
                        client['rent'] += rent['costo_diario']

            sortedQuery = sorted(clientList, key=sortList, reverse=True)
            
            return sortedQuery

        return queryset
    
class EmpresasViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.EmpresasSerializer
    queryset = models.Empresas.objects.all()

    def get_queryset(self):
        queryset = models.Empresas.objects.all()
        sort = self.request.query_params.get('sort')

        if sort == 'profits':
            def sortList(e):
                return e['amount']

            companyList = queryset.values()

            for company in companyList:
                companyRents = models.Arriendos.objects.filter(id_empresa__id=company['id']).values()

                for rent in companyRents:
                    if not 'amount' in company:
                        company['amount'] = 0
                    
                    company['amount'] += rent['costo_diario']

            sortedQuery = sorted(companyList, key=sortList)
            
            return sortedQuery

        return queryset

class ArriendosViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.ArriendosSerializer
    queryset = models.Arriendos.objects.all()
    

def getClientsSortByAmount (_valor_id_pram_):
    def sortList(e):
            return e[1]
        
    minLimitAmount = 1
    querysetCompany = list(models.Arriendos.objects.filter(id_empresa_id=_valor_id_pram_).values())

    companyClientAmount = {}

    for rent in querysetCompany:
        if not rent['id_cliente_id'] in companyClientAmount:
            companyClientAmount[rent['id_cliente_id']] = 0

        companyClientAmount[rent['id_cliente_id']] += rent['costo_diario']

    sortedCompanyClientAmount = dict(sorted(companyClientAmount.items(), key=sortList, reverse=True))

    filterClientAmount = {}
    for clientId in sortedCompanyClientAmount:
        client = list(models.Clientes.objects.filter(id=clientId).values())

        if (sortedCompanyClientAmount[clientId] >= minLimitAmount):
            filterClientAmount[client[0]['rut']] = sortedCompanyClientAmount[clientId]
    
    return filterClientAmount