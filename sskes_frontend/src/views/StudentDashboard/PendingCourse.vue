<template>
    <div class="wrapper">
        <sidebar/>
        <!-- Page Content  -->
        <div id="content">

            <nav class="navbar navbar-expand-lg navbar-light bg-light shadow">
                <div class="container-fluid">

                    <button type="button" id="sidebarCollapse" class="btn btn-info">
                        <i class="bi bi-text-left"></i>
                        <span>Toggle Sidebar</span>
                    </button>
                    <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="fas fa-align-justify"></i>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-2 mx-auto mb-2 mb-lg-0">
                            <li class="nav-item active">
<!--                                <a class="nav-link" href="#">{UserName}</a>-->
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="row align-items-center justify-content-center">
                <div class="col-md-6 my-4" v-for="course in courses"
                    v-bind:key="course.id">
                    <router-link :to="'/study-mode?'+'courseId='+course.course.id">
                        <div class="card d-flex">
                                <div class="card-body">
                                    <h4 class="card-title sinhala-font fw-bold">{{course.course.title}}</h4>
                                    <p class="card-text sinhala-font text-dark fw-bold">{{ course.course.short_description }}</p>
                                </div>
                            </div>
                    </router-link>
                </div>
<!--                <div class="col-md-6 my-4">-->
<!--                    <router-link to="/my-subject"><PendingCourses class="completeCard" subject="ගණිතය" text="ඔබගේ සම්පූර්න කරන ලද ගණිතය පාඨමාළාව බලාගැනීම මෙයින් පිවිසෙන්න"/></router-link>-->
<!--                </div>-->
            </div>

            <div class="line"></div>

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    // import PendingCourses from '@/components/StudentDashboard/PendingCoursesCard'
    import axios from "axios";

    export default {
        name : 'PendingCourse',
        components : {
            sidebar,
            // PendingCourses,
        },
      data(){
        return{
          courses:[]
        }
      },
        mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('api/v1/notcompleteCourse/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.courses = response.data.notCompleteCourse
            })
      }
    }
</script>

<style scoped src="../../assets/css/student/main.css">
    
</style>