<template>
	<v-app style="background: #f7f7f8;">
		<dashboard-core-app-bar/>
		<dashboard-core-drawer/>
		<dashboard-core-view />
	</v-app>
</template>

<script>
export default {
	name: 'App',
	components: {
		DashboardCoreAppBar: () => import('./components/core/BarApp'),
		DashboardCoreDrawer: () => import('./components/core/Drawer'),
		DashboardCoreView: () => import('./components/core/View'),
	},
}
</script>