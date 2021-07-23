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
			<v-col cols="12" md="12">
				<v-btn color="green" dark @click="addItem">
					Agregar
				</v-btn>
			</v-col>
		</v-row>

		<v-row v-if="select == 0">
			<v-col cols="12" md="12">
				<v-simple-table>
					<template v-slot:default>
						<thead>
							<tr>
								<th class="text-left">
									id
								</th>
								<th class="text-left">
									Nombre
								</th>
								<th></th>
							</tr>
						</thead>
						<tbody>
							<tr
								v-for="item in companies"
								:key="item.name"
							>
								<td>{{ item.id }}</td>
								<td>{{ item.name }}</td>
								<td style="width: 120px"> 
									<v-btn
										icon
										color="primary"
										@click="editCompany(item)"
									>
										<v-icon dark>
											mdi-pencil
										</v-icon>
									</v-btn>
									<v-btn
										icon
										color="red"
										@click="deleteItem ('empresas',item.id)"
									>
										<v-icon dark>
											mdi-delete
										</v-icon>
									</v-btn>
								</td>
							</tr>
						</tbody>mdi-minus
					</template>
				</v-simple-table>				
			</v-col>
		</v-row>

		<v-row v-if="select == 1">
			<v-col cols="12" md="12">
				<v-simple-table>
					<template v-slot:default>
						<thead>
							<tr>
								<th class="text-left">
									id
								</th>
								<th class="text-left">
									Nombre
								</th>
								<th class="text-left">
									RUT
								</th>
								<th></th>
							</tr>
						</thead>
						<tbody>
							<tr
								v-for="item in clients"
								:key="item.name"
							>
								<td>{{ item.id }}</td>
								<td>{{ item.name }}</td>
								<td>{{ item.rut }}</td>
								<td style="width: 120px"> 
									<v-btn
										icon
										color="primary"
										@click="editClient(item)"
									>
										<v-icon dark>
											mdi-pencil
										</v-icon>
									</v-btn>
									<v-btn
										icon
										color="red"
										@click="deleteItem ('clientes', item.id)"
									>
										<v-icon dark>
											mdi-delete
										</v-icon>
									</v-btn>
								</td>
							</tr>
						</tbody>
					</template>
				</v-simple-table>				
			</v-col>
		</v-row>

		<v-row v-if="select == 2">
			<v-col cols="12" md="12">
				<v-simple-table>
					<template v-slot:default>
						<thead>
							<tr>
								<th class="text-left">
									id
								</th>
								<th class="text-left">
									Empresa
								</th>
								<th class="text-left">
									Cliente
								</th>
								<th class="text-left">
									Costo diario
								</th>
								<th class="text-left">
									Dias
								</th>
								<th></th>
							</tr>mdi-minus
						</thead>
						<tbody>
							<tr
								v-for="item in rents"
								:key="item.name"
							>
								<td>{{ item.id }}</td>
								<td>{{ showCompany(item.id_empresa) }}</td>
								<td>{{ showClient(item.id_cliente) }}</td>
								<td>$ {{ item.costo_diario }}</td>
								<td>{{ item.dias }}</td>
								<td style="width: 120px"> 
									<v-btn
										icon
										color="primary"
										@click="editRent(item)"
									>
										<v-icon dark>
											mdi-pencil
										</v-icon>
									</v-btn>
									<v-btn
										icon
										color="red"
										@click="deleteItem ('arriendos', item.id)"
									>
										<v-icon dark>
											mdi-delete
										</v-icon>
									</v-btn>
								</td>
							</tr>
						</tbody>
					</template>
				</v-simple-table>				
			</v-col>
		</v-row>

		<v-dialog v-model="dialogDelete" max-width="530px">
			<v-card>
				<v-card-title class="text-h6">¿Está seguro de que quiere eliminar este elemento?</v-card-title>
					<v-card-actions>
					<v-spacer></v-spacer>
						<v-btn color="blue darken-1" text @click="closeDelete">Cancelar</v-btn>
						<v-btn color="blue darken-1" text @click="deleteItemConfirm">Eliminar</v-btn>
				</v-card-actions>
			</v-card>
        </v-dialog>


		<v-dialog
			v-model="dialogCompany"
			persistent
			max-width="600px"
		>
			<v-card>
				<v-card-title>
					<span class="text-h5">{{titleCompany}} Empresa</span>
				</v-card-title>
				<v-card-text>
					<v-container>
						<v-row>
							<v-col
								cols="12"
								sm="6"
								md="12"
							>
								<v-text-field
									label="Nombre"
									v-model="nameCompany"
									required
								></v-text-field>
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="blue darken-1"
						text
						@click="dialogCompany = false"
					>
						Cerrar
					</v-btn>
					<v-btn
						color="blue darken-1"
						text
						@click="saveCompany"
					>
						Guardar
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>


		<v-dialog
			v-model="dialogClient"
			persistent
			max-width="600px"
		>
			<v-card>
				<v-card-title>
					<span class="text-h5">{{titleCompany}} Cliente</span>
				</v-card-title>
				<v-card-text>
					<v-container>
						<v-row>
							<v-col
								cols="12"
								sm="6"
								md="12"
							>
								<v-text-field
									label="Nombre"
									v-model="nameClient"
									required
								></v-text-field>
								<v-text-field
									label="Rut"
									v-model="rutClient"
									required
								></v-text-field>
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="blue darken-1"
						text
						@click="dialogClient = false"
					>
						Cerrar
					</v-btn>
					<v-btn
						color="blue darken-1"
						text
						@click="saveClient"
					>
						Guardar
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<v-dialog
			v-model="dialogRent"
			persistent
			max-width="600px"
		>
			<v-card>
				<v-card-title>
					<span class="text-h5">{{titleCompany}} Arriendo</span>
				</v-card-title>
				<v-card-text>
					<v-container>
						<v-row>
							<v-col
								cols="12"
								sm="6"
								md="12"
							>
								<v-select
									:items="companies"
									item-text="name"
									item-value="id"
									label="Empresa"
									v-model="companyRent"
								></v-select>
								<v-select
									:items="clients"
									item-text="name"
									item-value="id"
									label="Clientes"
									v-model="clientRent"
								></v-select>
								<v-text-field
									label="Costo Diario"
									v-model="costRent"
									required
								></v-text-field>
								<v-text-field
									label="Dias"
									v-model="daysRent"
									required
								></v-text-field>
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="blue darken-1"
						text
						@click="dialogRent = false"
					>
						Cerrar
					</v-btn>
					<v-btn
						color="blue darken-1"
						text
						@click="saveRent"
					>
						Guardar
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<v-snackbar
			v-model="snackbar"
		>
			{{ notificationText }}

			<template v-slot:action="{ attrs }">
				<v-btn
				color="pink"
				text
				v-bind="attrs"
				@click="snackbar = false"
				>
				Close
				</v-btn>
			</template>
		</v-snackbar>

	</v-container>
</template>

<script>
	import axios from 'axios'

	export default {
        name: 'Maintainer',
        
		data: () => ({
            dialogDelete: false,
			dialogCompany: false,
			dialogClient: false,
			dialogRent: false,
			snackbar: false,
			notificationText: '',
			select: null,
			items: [
				'Empresas',
				'Clientes',
				'Arriendos'
			],
			companies: [],
			clients: [],
			rents: [],
			editItem: null,
			typeItem: null,
			modeCompany: '',
			modeClient: '',
			modeRent: '',
			nameCompany: null,
			idCompany: null,
			nameClient: null,
			rutClient: null,
			idClient: null,
			companyRent: null,
			clientRent: null,
			daysRent: null,
			costRent: null,
			idRent: null,
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
			showCompany (id) {
				return this.companies.find( e => {
					return e.id == id
				}).name
			},
			showClient (id) {
				return this.clients.find( e => {
					return e.id == id
				}).name
			},
			deleteItem (type, item) {
				this.dialogDelete = true
				this.editItem = item
				this.typeItem = type
			},
			deleteItemConfirm () {
				this.dialogDelete = false

				axios.delete(`http://127.0.0.1:8000/api/v1.0/${this.typeItem}/${this.editItem}/`)
				.then(() => {
					this.snackbar = true
					this.notificationText = 'Elemento eliminado'

					if (this.typeItem === 'empresas')
						this.loadCompanies ()
					else if (this.typeItem === 'clientes')
						this.loadClients()
					else if (this.typeItem === 'arriendos')
						this.loadRents()
				})

				this.editItem = null
			},
			closeDelete () {
				this.dialogDelete = false
			},
			addItem () {
				if (this.select === 0) {
					this.nameCompany = null
					this.dialogCompany = true
					this.modeCompany = 'add'
				} else if (this.select === 1) {
					this.nameClient = null
					this.rutClient = null
					this.dialogClient = true
					this.modeClient = 'add'
				} else if (this.select === 2) {
					this.companyRent = null
					this.clientRent = null
					this.daysRent = null
					this.costRent = null
					this.dialogRent = true
					this.modeRent = 'add'
				}
			},
			editCompany (item) {
				this.dialogCompany = true
				this.modeCompany = 'edit'
				this.nameCompany = item.name
				this.idCompany = item.id
			},
			saveCompany () {
				const payload = {
					name: this.nameCompany
				}

				if (this.modeCompany === 'add') {
					axios.post('http://127.0.0.1:8000/api/v1.0/empresas/', payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Nueva empresa agregada'
						this.loadCompanies ()
					})
				} else if (this.modeCompany === 'edit') {
					axios.put(`http://127.0.0.1:8000/api/v1.0/empresas/${this.idCompany}/`, payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Empresa modificada'
						this.loadCompanies ()
					})
				}

				this.dialogCompany = false
			},
			editClient (item) {
				this.dialogClient = true
				this.modeClient = 'edit'
				this.nameClient = item.name
				this.rutClient = item.rut
				this.idClient = item.id
			},
			saveClient () {
				const payload = {
					name: this.nameClient,
					rut: this.rutClient
				}

				if (this.modeClient === 'add') {
					axios.post('http://127.0.0.1:8000/api/v1.0/clientes/', payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Nuevo cliente agregado'
						this.loadClients()
					})
				} else if (this.modeClient === 'edit') {
					axios.put(`http://127.0.0.1:8000/api/v1.0/clientes/${this.idClient}/`, payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Cliente modificado'
						this.loadClients()
					})
				}

				this.dialogClient = false
			},
			editRent (item) {
				this.dialogRent = true
				this.modeRent = 'edit'
				this.companyRent = item.id_empresa
				this.clientRent = item.id_cliente
				this.daysRent = item.dias
				this.costRent = item.costo_diario
				this.idRent = item.id
			},
			saveRent () {
				const payload = {
					id_empresa: this.companyRent,
					id_cliente: this.clientRent,
					dias: this.daysRent,
					costo_diario: this.costRent,
				}

				if (this.modeRent === 'add') {
					axios.post('http://127.0.0.1:8000/api/v1.0/arriendos/', payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Nuevo arriendo agregado'
						this.loadRents ()
					})
				} else if (this.modeRent === 'edit') {
					axios.put(`http://127.0.0.1:8000/api/v1.0/arriendos/${this.idRent}/`, payload)
					.then(() => {
						this.snackbar = true
						this.notificationText = 'Arriendo modificado'
						this.loadRents ()
					})
				}

				this.dialogRent = false
			},

		},
		computed: {
            titleCompany () {
				return this.modeCompany == 'add' ? 'Agregar' : 'Editar'
			},
            titleClient () {
				return this.modeClient == 'add' ? 'Agregar' : 'Editar'
			},
            titleRent () {
				return this.modeRent == 'add' ? 'Agregar' : 'Editar'
			},
		},
        watch: {
            select (val) {
				console.log(val)
				if (val === 0)
					this.loadCompanies()
				else if (val === 1)
					this.loadClients ()
				else if (val === 2)
					this.loadRents ()
			}
        },
		created () {
			this.loadCompanies()
			this.loadClients ()
			this.loadRents ()
		}
	}
</script>