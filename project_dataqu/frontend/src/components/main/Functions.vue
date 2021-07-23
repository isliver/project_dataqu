<template>
    <v-container>
        <v-row>
            <v-col
                cols="12"
                md="5"
            >
                <v-card
                    tile
                >
                    <v-list flat>
                    <v-subheader>Funciones</v-subheader>
                    <v-list-item-group
                        v-model="selectedItem"
                        color="primary"
                    >
                        <v-list-item
                            v-for="(item, i) in items"
                            :key="i"
                        >
                        <v-list-item-icon>
                            <v-icon v-text="item.icon"></v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title v-text="item.text"></v-list-item-title>
                        </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                    </v-list>
                </v-card>
            </v-col>
            <v-col
                cols="12"
                md="7"
            >
                
                <v-card
                    tile
                >
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title class="text-h8 mb-1">
                                {{currentFunctionText}}
                            </v-list-item-title>
                            <v-row>
                                <v-col
                                    cols="12"
                                    md="7"
                                >
                                    <v-row v-if="showPayload == 'company'">
                                        <v-col
                                            cols="12"
                                            md="12"
                                        >
                                            <v-select
                                                :items="companies"
                                                item-text="name"
                                                item-value="id"
                                                label="Empresa"
                                                v-model="selectedCompanyRen"
                                            ></v-select>
                                        </v-col>
                                    </v-row>
                                </v-col>
                                <v-col
                                    cols="12"
                                    md="5"
                                >
                                    <div class="text-right">
                                        <v-btn color="green" dark @click="sendRequest">
                                            Enviar
                                        </v-btn>
                                    </div>
                                </v-col>
                            </v-row>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <div class="text-overline mb-4">
                                Respuesta
                            </div>
                            <v-list-item-subtitle>
                                <vue-json-pretty :data="responseJson"> </vue-json-pretty>
                            </v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import VueJsonPretty from 'vue-json-pretty';
    import 'vue-json-pretty/lib/styles.css';
    import axios from 'axios'

    export default {
        components: {
            VueJsonPretty,
        },
        data: () => ({
            selectedItem: 1,
            responseJson: '',
            companies: [],
            selectedCompanyRen: null,
            items: [
                { text: 'def getClientIds():', icon: 'mdi-numeric-1-box-outline', url:'http://127.0.0.1:8000/api/v1.0/clientes/'},
                { text: 'def getClientSortByLastName():', icon: 'mdi-numeric-2-box-outline' , url:'http://localhost:8000/api/v1.0/clientes/?sort=last_name'},
                { text: 'def getClientsSortByRentExpenses():', icon: 'mdi-numeric-3-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/clientes/?sort=rent_expenses'},
                { text: 'def getCompanyClientsSortByName():', icon: 'mdi-numeric-4-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/empresas/clientes/'},
                { text: 'def getClientsSortByAmount(id_empresa):', icon: 'mdi-numeric-5-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/clientes/cantidad/', payload: 'company'},
                { text: 'def getCompaniesSortByProfits():', icon: 'mdi-numeric-6-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/empresas/?sort=profits'},
                { text: 'def getCompaniesWithRentsOver1Week():', icon: 'mdi-numeric-7-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/empresas/rentaunasemana/'},
                { text: 'def getClientsWithLessExpense():', icon: 'mdi-numeric-8-box-outline' , url:'http://127.0.0.1:8000/api/v1.0/empresas/clientesmenorgastos/'},
                { text: 'def newClientRanking():', icon: 'mdi-numeric-9-box-outline' , url:''},
            ],
        }),
        computed: {
            currentFunctionText () {
                return `Funcion: ${this.items[this.selectedItem].text}`
            },
            showPayload () {
                let hasPayload = this.items[this.selectedItem].payload !== undefined
                
                return hasPayload ? this.items[this.selectedItem].payload : 'none'
            }
		},
        methods: {
            sendRequest () {
                let url = this.items[this.selectedItem].url

                if (this.showPayload == 'company')
                    url = `http://127.0.0.1:8000/api/v1.0/clientes2/cantidad/${this.selectedCompanyRen}/`

                axios.get(url)
				.then((response) => {
					this.responseJson = response.data
				})
            },
            loadCompanies () {
				axios.get('http://127.0.0.1:8000/api/v1.0/empresas/')
				.then((response) => {
					this.companies = response.data
				})
			},
        },
        watch: {
            selectedItem () {
                this.responseJson = ""
            }
        },
        created () {
			this.loadCompanies ()
		}
    }
</script>