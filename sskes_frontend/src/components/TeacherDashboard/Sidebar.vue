<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <img src="../../assets/images/logo/logo.png" class="img-fluid">
        </div>

        <ul class="list-unstyled components">
            <li class="pt-3">
                <router-link to="/TeacherDashboard" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-house-door-fill"></i>
                    Home
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/AllCourse" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-easel-fill"></i>
                    Courses
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/TeacherAddCourse" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-plus-fill"></i>
                    Add Course
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/Add-Lesson" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-bookmark-plus-fill"></i>
                    Add Lesson
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/Course-Progress" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-clipboard-data-fill"></i>
                    Progress
                </router-link>
            </li>
            <li class="pt-3">
                <router-link to="/Teacher-Profile" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-square"></i>
                    Account
                </router-link>
            </li>
        </ul>

        <ul class="list-unstyled CTAs">
            <li>
                <button @click="logout" class="pt-3 btn text-center">Sign Out<i class="bi bi-box-arrow-right ms-2"></i></button>
            </li>
        </ul>
    </nav>
</template>

<script>

    export default {
        name : 'TeacherSidebar',

      methods:{
          logout(){
            localStorage.clear();
            this.$router.push('/login')
          }
      }
        
    }
    
</script>

<style scoped src="../../assets/css/TeacherDashboard/main.css">

</style>