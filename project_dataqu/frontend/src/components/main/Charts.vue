<template>
    <v-container>
        <v-item-group mandatory v-model="select">
			<v-row>
				<v-col
					v-for="item in items"
					:key="item"
					cols="12"
					md="4"
				>
					<v-item v-slot="{ active, toggle }">
						<v-card
							:color="active ? 'primary' : ''"
							class="d-flex align-center"
							dark
							height="70"
							@click="toggle"
						>
						<v-scroll-y-transition>
							<div
								v-if="active"
								class="flex-grow-1 text-center"
							>
								{{item}}
							</div>
							<div
								v-else
								class="flex-grow-1 text-center"
							>
								{{item}}
							</div>
						</v-scroll-y-transition>
						</v-card>
					</v-item>
				</v-col>
			</v-row>
		</v-item-group>
        <v-row>
            <v-col cols="12" v-if="select == 0">
				<apexchart ref="chart" :options="chartOptions" :series="series"></apexchart>
			</v-col>
            <v-col cols="12" v-if="select == 1">
				<apexchart ref="chart2" :options="chartOptions2" :series="series2"></apexchart>
			</v-col>
        </v-row>
    </v-container>
</template>

<script>
    import axios from 'axios'
    import VueApexCharts from 'vue-apexcharts'

    export default {
        components: {
			apexchart: VueApexCharts
		},
        data: () => ({
            select: null,
			items: [
				'Arriendos',
				'Costos'
			],
            companies: [],
            rents: [],
            clients: [],
            series: [],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                            borderRadius: 10,
                            dataLabels: {
                            position: 'top',
                        },
                    }
                },
                dataLabels: {
                    enabled: false,
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#304758"]
                    }
                },
                
                xaxis: {
                    categories: [],
                    crosshairs: {
                        fill: {
                        type: 'gradient',
                        gradient: {
                                colorFrom: '#D8E3F0',
                                colorTo: '#BED1E6',
                                stops: [0, 100],
                                opacityFrom: 0.4,
                                opacityTo: 0.5,
                            }
                        }
                    },
                    tooltip: {
                        enabled: true,
                    }
                },
                yaxis: {
                    axisBorder: {
                        show: false
                    },
                    axisTicks: {
                        show: false,
                    }
                },
                title: {
                    text: 'Cantidad arriendos por empresa',
                    offsetY: 330,
                    align: 'center',
                    style: {
                        color: '#444'
                    }
                }
            },
            series2: [],
            chartOptions2: {
                chart: {
                    height: 350,
                    type: 'bar',
                },
                plotOptions: {
                    bar: {
                            borderRadius: 10,
                            dataLabels: {
                            position: 'top',
                        },
                    }
                },
                dataLabels: {
                    enabled: false,
                    offsetY: -20,
                    style: {
                        fontSize: '12px',
                        colors: ["#304758"]
                    }
                },
                
                xaxis: {
                    categories: [],
                    crosshairs: {
                        fill: {
                        type: 'gradient',
                        gradient: {
                                colorFrom: '#D8E3F0',
                                colorTo: '#BED1E6',
                                stops: [0, 100],
                                opacityFrom: 0.4,
                                opacityTo: 0.5,
                            }
                        }
                    },
                    tooltip: {
                        enabled: true,
                    }
                },
                yaxis: {
                    axisBorder: {
                        show: false
                    },
                    axisTicks: {
                        show: false,
                    }
                },
                title: {
                    text: 'Cantidad costo por empresa',
                    offsetY: 330,
                    align: 'center',
                    style: {
                        color: '#444'
                    }
                }
            },
          }),
        computed: {

		},
        methods: {
            loadCompanies () {
				axios.get('http://127.0.0.1:8000/api/v1.0/empresas/')
				.then((response) => {
					this.companies = response.data
                    this.loadClients()
				})
			},
			loadClients () {
				axios.get('http://127.0.0.1:8000/api/v1.0/clientes/')
				.then((response) => {
					this.clients = response.data
                    this.loadRents ()
				})
			},
			loadRents () {
				axios.get('http://127.0.0.1:8000/api/v1.0/arriendos/')
				.then((response) => {
					this.rents = response.data
                    this.setChartTotalSeld()
                    this.setChartTotalCost()
				})
			},
            setChartTotalSeld () {
                let companyTotalRents = {}
                this.rents.forEach(e => {
                    if (!Object.hasOwnProperty.call(companyTotalRents, e.id_empresa))
                        companyTotalRents[e.id_empresa] = 0

                    companyTotalRents[e.id_empresa] += 1
                })

                let categories = []
                let data = []

                this.companies.forEach(e => {
                    categories.push(e.name)
                    data.push(companyTotalRents[e.id])
                })
                
                this.series.push({
                    name: 'Arriendos',
                    data: data
                })

                this.chartOptions.xaxis.categories = categories
                this.$refs.chart.updateOptions({ 
					xaxis: {
                        categories: categories
                    }
				})
            },
            setChartTotalCost () {
                let companyTotalRents = {}
                this.rents.forEach(e => {
                    if (!Object.hasOwnProperty.call(companyTotalRents, e.id_empresa))
                        companyTotalRents[e.id_empresa] = 0

                    companyTotalRents[e.id_empresa] += e.costo_diario
                })

                let categories = []
                let data = []

                this.companies.forEach(e => {
                    categories.push(e.name)
                    data.push(companyTotalRents[e.id])
                })
                
                this.series2.push({
                    name: 'Costos',
                    data: data
                })

                this.chartOptions2.xaxis.categories = categories
                this.$refs.chart2.updateOptions({ 
					xaxis: {
                        categories: categories
                    }
				})
            }
        },
        watch: {
            
        },
        created () {
			this.loadCompanies()
		}
    }
</script>