<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <img src="../../assets/images/logo/logo.png" class="img-fluid">
        </div>

        <ul class="list-unstyled components">
            <li class="pt-3">
                <router-link to="/parent-dashboard" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-house-door-fill"></i>
                    Home
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/courses-section" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-bookmark-fill"></i>
                    Courses
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/add-students" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-plus-fill"></i>
                    Add Student
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-clipboard-data-fill"></i>
                    Progress
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/parent-profile" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-square"></i>
                    Account
                </router-link>
            </li>
        </ul>

        <ul class="list-unstyled CTAs">
            <li>
                <button @click="logout" class="pt-3 text-center btn signOut">Sign Out<i class="bi bi-box-arrow-right ms-2"></i></button>
            </li>
        </ul>
    </nav>
</template>

<script>

    import $ from 'jquery'

    export default {
        name : 'Sidebar',
        methods:{
          logout(){
            localStorage.clear();
            this.$router.push('/login')
          }
      }
    }
</script>

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>