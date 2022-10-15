<template>
    <div class="wrapper">
        <TeacherSidebar/>
        <!-- Page content start -->
        <div id="content">
            <nav class="navbar navbar-expand-lg bg-light">
                <div class="container-fluid">
                    <button type="button" id="sidebarCollapse" class="btn btn-success navbar-btn">
                        <i class="bi bi-list"></i>
                        <span>Toggle Sidebar</span>
                    </button>
                    <div class="collapse navbar-collapse p-3" id="navbarSupportedContent">
                        <ul class="navbar-nav me-2 mx-auto mb-2 mb-lg-0">
<!--                            <li class="nav-item fs-5 px-3"><a href="#">Username</a></li>-->
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="line"></div>

            <h2 class="sinhala-font">ඔබගේ පාඨමාලාවන් මෙහි ඇතුලත්වේ</h2>
            <p>පටමලාවන් ප්‍රකාශ කිරීමට පෙර එය නැවැත සොයාබලන්න</p>

        <!--    Teacher course cards      -->
            <div class="album py-5 bg-light">
                <div class="container">

                  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
                    <div class="col" v-for="course in courses"
                    v-bind:key="course.id">
                      <div class="card shadow-sm">
                        <img class="bd-placeholder-img card-img-top" width="100%" height="225" :src="course.get_image" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false">

                        <div class="card-body">
                          <p class="card-text">{{course.short_description}}</p>
                          <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group">
<!--                              <button  type="button" class="btn btn-sm btn-outline-primary">View</button>-->
                              <router-link  :to="'/View-Lessons?'+'courseId='+course.id" class="btn btn-sm btn-outline-primary">View</router-link>
<!--                              <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>-->
                            </div>
                            <small class="text-muted">9 mins</small>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
<!--              <div class="row p-4"  v-for="course in courses"-->
<!--                    v-bind:key="course.id">-->
<!--                    <div class="col-md-3 my-3">-->
<!--                        &lt;!&ndash; <CoursesList/> &ndash;&gt;-->
<!--                        <div class="card coursesCard">-->
<!--                            <img :src="course.get_image" class="img-fluid" >-->
<!--                            <div class="card-body border border-3">-->
<!--                                <div class="h5 text-center sinhala-font fs-5 pt-1 fw-bold">{{ course.title }}</div>-->
<!--                                <div class="h6 sinhala-font fs-6 pt-1 fw-bold">වසර : <span class="ms-2">5</span></div>-->
<!--                                <p class="sinhala-font  pt-2 mb-3" id="courseList">{{course.short_description}}</p>-->
<!--                                <router-link :to="'/View-Lessons?'+'courseId='+course.id" class="sinhala-font px-2 mb-1 float-end next">පිවිසෙන්න</router-link>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
          <!--  end  of Teacher course cards      -->
        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import TeacherSidebar from "@/components/TeacherDashboard/Sidebar"
    import axios from 'axios';
    export default {
        name : 'AllCourses',
        components : {
            TeacherSidebar,
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
            .get('/api/v1/getCourses/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.courses = response.data
            })
      }
    }
</script>

<style scoped src="../../assets/css/TeacherDashboard/main.css">

</style>