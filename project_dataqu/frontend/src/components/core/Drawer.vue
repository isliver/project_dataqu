<template>
    <div>
        <v-navigation-drawer
            permanent
            app
            dark
        >
            <v-list>
                <v-list-item link>
                    <v-list-item-content>
                    <v-list-item-title class="text-h6">
                        Prueba DataQu
                    </v-list-item-title>
                    <v-list-item-subtitle>Esteban Troncoso</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>
            </v-list>

            <v-divider></v-divider>

            <v-list
                nav
                dense
            >
                <v-list-item
                    v-for="item in items"
                    :key="item.title"
                    link
                    :to="item.link"
                >
                <v-list-item-icon>
                    <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </div>
</template>

<script>
     export default {
        data: () => ({
            items: [
                { title: 'Mantenedor', icon: 'mdi-google-maps', link: '/maintainer'},
                { title: 'Indicadores', icon: 'mdi-home-analytics', link: '/indicators'},
                { title: 'Graficos', icon: 'mdi-account-clock', link: '/charts'},
                { title: 'Funciones', icon: 'mdi-compare', link: '/functions'},
            ],
            drawer: true
        }),
    }
</script>