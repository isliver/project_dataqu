<template>
    <v-container>

        <v-row align="center">
            <v-col
                class="d-flex"
                cols="12"
                sm="6"
            >
                <v-select
                    v-model="selectCompany"
                    :items="companies"
                    item-text="name"
                    item-value="id"
                    label="Empresas"
                    solo
                ></v-select>
            </v-col>
            </v-row>
        <v-row>
            <v-col
                v-for="item in indicators"
                :key="item.name"
                cols="12"
                md="4"
            >
                <v-card
                    :color="item.color"
                    dark
                >
                    <v-card-title>
                    <v-icon
                        large
                        left
                    >
                        {{item.icon}}
                    </v-icon>
                    <span class="text-h6 font-weight-light">{{item.name}}</span>
                    </v-card-title>

                    <v-card-text class="text-h5 font-weight-bold">
                        {{item.argumentA}}
                    </v-card-text>

                    <v-card-actions>
                        <v-list-item class="grow">
                            <v-list-item-content>
                            <v-list-item-title>{{item.argumentB}}</v-list-item-title>
                            </v-list-item-content>
                        </v-list-item>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
  
</template>

<script>
	import axios from 'axios'

	export default {
        name: 'Maintainer',
        
		data: () => ({
			companies: [],
            clientCompanies: [],
            rents: [],
            clients: [],
            selectCompany: 0,
            indicators: [
                
            ],
		}),
		methods: {
			loadCompanies () {
				axios.get('http://127.0.0.1:8000/api/v1.0/empresas/')
				.then((response) => {
					this.companies = response.data
				})
			},

            loadClients () {
				axios.get('http://127.0.0.1:8000/api/v1.0/clientes/')
				.then((response) => {
					this.clients = response.data
				})
			},

            loadRents () {
				axios.get('http://127.0.0.1:8000/api/v1.0/arriendos/')
				.then((response) => {
					this.rents = response.data
				})
			},

            loadClientCompanie () {
                axios.get('http://127.0.0.1:8000/api/v1.0/empresas/clientes/')
				.then((response) => {
					this.clientCompanies = response.data
				})
            },
            getClientNameByRut (rut) {
                return this.clients.find( e => {
                    return e.rut == rut
                })
            },
            getClientNameById (id) {
                return this.clients.find( e => {
                    return e.id == id
                })
            },
            getSumTotal (rut) {
                const clientId = this.getClientNameByRut(rut).id

                const restCompany = this.rents.filter( e => {
                    return e.id_cliente == clientId && e.id_empresa == this.selectCompany
                })
                
                let sum = 0
                restCompany.forEach(e => {
                    sum += e.costo_diario   
                })

                return sum
            },
            totalsAmount () {
                const restCompany = this.rents.filter( e => {
                    return e.id_empresa == this.selectCompany
                })

                let total = 0

                restCompany.forEach(e => {
                    total += e.costo_diario
                })

                return total
            },

            totalsRent () {
                const restCompany = this.rents.filter( e => {
                    return e.id_empresa == this.selectCompany
                })

                let total = 0

                restCompany.forEach(() => {
                    total += 1
                })

                return total
            },

            daysClient () {
                const restCompany = this.rents.filter( e => {
                    return e.id_empresa == this.selectCompany
                })

                let client = {}

                restCompany.forEach(e => {
                    if (!Object.hasOwnProperty.call(client, e.id_cliente))
                        client[e.id_cliente] = 0

                    client[e.id_cliente] += e.dias
                })

                var sortable = [];
                for (var id in client) {
                    sortable.push([id, client[id]]);
                }

                sortable.sort(function(a, b) {
                    return a[1] - b[1];
                })

                return {
                    less: {
                        name: this.getClientNameById(sortable[0][0]).name,
                        days: sortable[0][1]
                    },
                    most: {
                        name: this.getClientNameById(sortable[sortable.length - 1][0]).name,
                        days: sortable[sortable.length - 1][1]
                    }
                }
            }

		},
		computed: {
            
		},
        watch: {
            selectCompany (val) {
                const selectCompanyName = this.companies.find( e => {
                    return e.id == val
                }).name

                const info = this.clientCompanies[selectCompanyName]
                
                this.indicators = []
                this.indicators.push({
                    name: 'Total arriendos del mes',
                    icon: 'mdi-account-multiple-plus',
                    color: '#8BC8D5',
                    argumentA: `Clientes ${this.totalsRent()}`,
                    argumentB: `Total: ${this.totalsRent ()}`
                })

                this.indicators.push({
                    name: 'Ventas Totales',
                    icon: 'mdi-credit-card-plus',
                    color: '#F94141',
                    argumentA: `$ ${this.totalsAmount()}`,
                    argumentB: `Total: $${this.totalsAmount ()}`
                })

                this.indicators.push({
                    name: 'Cliente mayor monto',
                    icon: 'mdi-bank-plus',
                    color: '#93C66F',
                    argumentA: this.getClientNameByRut(info[0]).name,
                    argumentB: `Total: $${this.getSumTotal (info[0])}`
                })

                this.indicators.push({
                    name: 'Cliente menor monto',
                    icon: 'mdi-bank-minus',
                    color: '#C67F6F',
                    argumentA: this.getClientNameByRut(info[info.length - 1]).name,
                    argumentB: `Total: $${this.getSumTotal (info[info.length - 1])}`
                })

                const limitsDays = this.daysClient()

                this.indicators.push({
                    name: 'Cliente mayor dias',
                    icon: 'mdi-sort-calendar-descending',
                    color: '#6FC6B4',
                    argumentA: limitsDays.most.name,
                    argumentB: `Total: ${limitsDays.most.days} dias`
                })

                this.indicators.push({
                    name: 'Cliente menor dias',
                    icon: 'mdi-sort-calendar-ascending',
                    color: '#6F81C6',
                    argumentA: limitsDays.less.name,
                    argumentB: `Total: ${limitsDays.less.days} dias`
                })
            }
        },
		created () {
			this.loadCompanies ()
            this.loadClients ()
            this.loadRents ()
            this.loadClientCompanie ()
		}
	}
</script>