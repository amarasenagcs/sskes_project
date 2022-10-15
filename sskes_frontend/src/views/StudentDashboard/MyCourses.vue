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

            <div class="row justify-content-center align-items-center">
                <!-- <div class="col-md-3 my-5">
                    <select name="selectGrade" id="" class="form-select form-select-lg sinhala-font bg-light" aria-label=".form-select-lg ">
                        <option selected>ඔබගේ වසර තෝරන්න</option>
                        <option value="grade">පෙර පාසල්</option>
                        <option value="1grade">1 වසර</option>
                        <option value="2grade">2 වසර</option>
                        <option value="3grade">3 වසර</option>
                        <option value="4grade">4 වසර</option>
                        <option value="5grade">5 වසර</option>
                        <option value="6grade">6 වසර</option>
                        <option value="7grade">7 වසර</option>
                        <option value="8grade">8 වසර</option>
                        <option value="9grade">9 වසර</option>
                        <option value="10grade">10 වසර</option>
                        <option value="11grade">11 වසර</option>
                        <option value="12grade">12 වසර</option>
                    </select>
                </div> -->
                <!-- <div class="col-md-10 my-5"> -->
                    <form method="post">
                        <legend class="text-center sinhala-font fw-bold py-3">ඔබට අවශ්‍ය පාඨමාළාව සොයන්න</legend>
                        <div class="row d-flex my-5 justify-content-center align-items-center">
                            <div class="col-md-4 pe-5">
                                <select name="selectGrade" id="CourseGrade" class="form-select form-select-lg sinhala-font bg-light float-start" aria-label=".form-select-lg ">
                                    <option selected>ඔබගේ වසර තෝරන්න</option>
                                    <option value="grade">පෙර පාසල්</option>
                                    <option value="1grade">1 වසර</option>
                                    <option value="2grade">2 වසර</option>
                                    <option value="3grade">3 වසර</option>
                                    <option value="4grade">4 වසර</option>
                                    <option value="5grade">5 වසර</option>
                                    <option value="6grade">6 වසර</option>
                                    <option value="7grade">7 වසර</option>
                                    <option value="8grade">8 වසර</option>
                                    <option value="9grade">9 වසර</option>
                                    <option value="10grade">10 වසර</option>
                                    <option value="11grade">11 වසර</option>
                                    <option value="12grade">12 වසර</option>
                                </select>
                            </div>
                            <div class="col-md-6 d-flex sinhala-font">
                                <input type="text" class="form-control ms-4 me-3 p-2" v-model="search" name="searchCourse" id="courseSearchBar" placeholder="පාඨමාළාවේ නම...">
<!--                                <button class="btn btn-primary sinhala-font shadow ">සොයන්න</button>-->
                            </div>
                        </div>
                    </form>
                <!-- </div> -->
            </div>

            <div class="row justify-content-center align-items-center">
                <div class="col-md-10" v-for="course in filteredList"
                    v-bind:key="course.id">
<!--                    <Course/>-->
<!--                    <div class="card completeCard mt-3">-->
<!--                        <div class="card-body d-flex sinhala-font justify-content-center align-items-center">-->
<!--                            <div class="col-md-9">-->
<!--                                <h4>විෂය : {{course.title}}</h4>-->
<!--                                <h6 id="subject-grade">වසර : {{course.grade}}</h6>-->
<!--                                <p class="fw-bold">විෂයන් පිළිබද කෙටි විස්තරයක් මෙම ස්තානයෙ දැකබලාගත් හැක..එහි ඇත්තේ අදාළ පාඨමාලාව පිළිබද හැදින්වීමකි.. එයින් අදාල ශිෂ්‍යාට සරිලන විෂය පාඨමාලාව සදහා සම්බන්ද විය හැක.</p>-->
<!--                            </div>-->
<!--                            <div class="col-md-3">-->
<!--                                <button type="button" class="btn btn-primary float-end" id="enrollCourse">ලියාපදිංචි කරන්න</button>-->
<!--                                <router-link :to="'/content-view?'+'courseId='+course.id">ලියාපදිංචි කරන්න</router-link>-->
<!--                            </div>-->
<!--                        </div>-->
<!--                    </div>-->

                      <div class="card completeCard mt-3">
                          <div class="card-body d-flex sinhala-font justify-content-center align-items-center">
                              <div class="col-md-2">
                                  <img :src="course.get_image" class="img-fluid" id="course-images">
                              </div>
                              <div class="col-md-7 ps-4">
                                  <h4>විෂය : {{course.title}}</h4>
                                  <h6 id="subject-grade">වසර : {{course.grade}}</h6>
                                  <p class="fw-bold">විෂයන් පිළිබද කෙටි විස්තරයක් මෙම ස්තානයෙ දැකබලාගත් හැක..එහි ඇත්තේ අදාළ පාඨමාලාව පිළිබද හැදින්වීමකි.. එයින් අදාල ශිෂ්‍යාට සරිලන විෂය පාඨමාලාව සදහා සම්බන්ද විය හැක.</p>
                              </div>
                              <div class="col-md-3 text-center">
                                  <router-link :to="'/content-view?'+'courseId='+course.id" class="btn btn-primary" id="enrollCourse">වැඩි විස්තර</router-link>
                                  <!-- <router-link to="/content-view" class="sinhal-font py-4"> විස්තරය</router-link> -->
                              </div>
                          </div>
                      </div>

                </div>
            </div>

            <div class="line"></div>

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    import Course from '@/components/StudentDashboard/MyCoursesCard'
    import axios from "axios";


    export default {
        name : 'MyCourses',
        components : {
            sidebar,
            Course,
        },
        data(){
        return{
          courses:[],
          search: '',
        }
      },
      computed: {
      filteredList() {
          return this.courses.filter(courses => {
            return courses.title.toLowerCase().includes(this.search.toLowerCase())
          })
        }
      },
      mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('/api/v1/get_all_courses/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.courses = response.data
            })
      },

    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>