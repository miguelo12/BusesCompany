<template>
    <div>
        <b-navbar toggleable="md" type="dark" variant="info">
            <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
            <b-navbar-brand href="#">Agencia</b-navbar-brand>
            <b-collapse is-nav id="nav_collapse">
                <b-navbar-nav>
                    <b-nav-item :to="{ name: 'Home'}">Home</b-nav-item>
                    <b-nav-item :to="{ name: 'Dashboard'}">Dashboard</b-nav-item>
                    <b-nav-item :to="{ name: 'About'}">About</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>
</template>
<script>
export default {
}
</script>
<style lang="">
</style>
