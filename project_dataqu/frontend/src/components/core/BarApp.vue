
<template>
    <v-app-bar
        absolute
        app
        color="white"
        elevate-on-scroll
        scroll-target="#scrolling-techniques-7"
    >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-toolbar-title>{{titlePage}}</v-toolbar-title>

        <v-spacer></v-spacer>
    </v-app-bar>
</template>

<script>
    export default {
		name: 'BarApp',
		data: () => ({

		}),
        computed: {
            titlePage () {
                return this.$route.name
            },
        }
    }
</script>