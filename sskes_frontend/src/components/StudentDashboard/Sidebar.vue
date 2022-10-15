<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <!-- <h3>SSKES</h3> -->
            <img src="../../assets/images/logo/logo.png" alt="" class="img-fluid">
        </div>

        <ul class="list-unstyled components">
            <li class="active sinhala-font">
                <router-link to="/student-dashboard"><i class="bi bi-house-door-fill pe-1 text-primary"></i>පුවරුව</router-link>
            </li>
            <li class=" sinhala-font pt-3">
                <router-link to="/my-courses"><i class="bi bi-bookmark-star-fill pe-1" style="color:#FF6700"></i>පාඨමාළාවන්</router-link>
            </li>
            <li class=" sinhala-font pt-3">
                <router-link to="/my-progress"><i class="bi bi-pie-chart-fill pe-1 text-success"></i>මාගේ ප්‍රගතිය</router-link>
            </li>
            <li class=" sinhala-font pt-3">
                <router-link to="/student-profile"><i class="bi bi-person-circle pe-1 text-danger"></i>මාගේ ගිණුම</router-link>
            </li>
        </ul>

        <ul class="list-unstyled second">
            <li class=" sinhala-font">
                <button @click="logout" class="signout text-center fw-bold btn"><i class="bi bi-box-arrow-left"></i> ඉවත්වන්න</button>
            </li>
        </ul>
    </nav>
</template>

<script>
    export default {
        name : 'StuSiidebar',
        methods:{
          logout(){
            localStorage.clear();
            this.$router.push('/login')
          }
      }
    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>