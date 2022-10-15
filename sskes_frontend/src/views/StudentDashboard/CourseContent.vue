<template>
    <div class="wrapper">
        <sidebar/>
        <!-- Page Content  -->
        <div id="content">

            <nav class="navbar navbar-expand-lg navbar-light bg-light shadow">
                <div class="container-fluid">

                    <button type="button" id="sidebarCollapse" class="btn btn-info">
                        <i class="bi bi-text-left"></i>
<!--                        <span>Toggle Sidebar</span>-->
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

            <!-- Subject lerning details card start -->            
            <div class="row p-4 col-10 mx-auto">
                <div class="card border">
                    <div class="card-body">
                        <div class="row">
<!--                          <div class="row col-md-6">-->
<!--                            <h4 class="sinhala-font fs-5 mb-5 pt-4 fw-bold">ඔබ ඉගෙනුම ලබන දෑ</h4>-->
<!--                          </div>-->
<!--                          <div class="row col-md-6 text-right">-->
<!--                            <div class="col-md-6 mt-3 sinhala-font text-right">-->
<!--                                <button type="button" class="btn btn-primary float-end pull-right" id="enroll" @click="courseReg">ලියාපදිංචි කරන්න</button>-->
<!--&lt;!&ndash;                                <router-link :to="'/content-view?'+'courseId='+course.id">ලියාපදිංචි කරන්න</router-link>&ndash;&gt;-->
<!--                            </div>-->
<!--                          </div>-->

                          <div class="row">
                                <div class="col-8">
                                    <h4 class="sinhala-font fs-5 mb-3 pt-4 fw-bold">ඔබ ඉගෙනුම ලබන දෑ</h4>
                                </div>
                                <div class="col-4 pt-3 sinhala-font">
                                    <button @click="courseReg" class="btn btn-warning float-end mb-5">ලියාපදිංචිවන්න</button>
                                </div>
                            </div>



                            <div class="col-md-12">
                                <ul>
                                    <li class=" d-flex" v-for="lesson in lessons"
                                    v-bind:key="lesson.id">
                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                        <p class="sinhala-font text-dark">{{lesson.content_description}}</p>
                                    </li>
<!--                                    <li class=" d-flex">-->
<!--                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>-->
<!--                                        <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>-->
<!--                                    </li>-->
<!--                                    <li class=" d-flex">-->
<!--                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>-->
<!--                                        <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>-->
<!--                                    </li>-->
<!--                                    <li class=" d-flex">-->
<!--                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>-->
<!--                                        <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>-->
<!--                                    </li>-->
<!--                                    <li class=" d-flex">-->
<!--                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>-->
<!--                                        <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>-->
<!--                                    </li>-->
<!--                                    <li class=" d-flex">-->
<!--                                        <span class="bi bi-check-circle-fill me-4 text-success"></span>-->
<!--                                        <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>-->
<!--                                    </li>-->
                                </ul>                              
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Subject lerning details card end -->            

            <!-- subject contents list start -->
            <div class="row col-10 p-2 mx-auto mb-5">
                <div class="accordion sinhala-font" id="accordionExample">
                    <div class="accordion-item border border-2" v-for="lesson in lessons"
                    v-bind:key="lesson.id">
                        <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" id="accordian-button-color">
                            {{lesson.lesson_name}}
                        </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
<!--                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odio pariatur doloribus sunt eaque officia eveniet corporis eos sed quo, minima incidunt, laboriosam laudantium modi placeat odit dolorem magni totam commodi!ඔබ කරමින් පවතින පාඨමාළාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න.-->
                            {{lesson.content_description}}
                        </div>
                        </div>
                    </div>
<!--                    <div class="accordion-item border border-2">-->
<!--                        <h2 class="accordion-header" id="headingTwo">-->
<!--                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" id="accordian-button-color">-->
<!--                            පාඩම් අංක #2-->
<!--                        </button>-->
<!--                        </h2>-->
<!--                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">-->
<!--                        <div class="accordion-body">-->
<!--                            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.-->
<!--                        </div>-->
<!--                        </div>-->
<!--                    </div>-->
<!--                    <div class="accordion-item border border-2">-->
<!--                        <h2 class="accordion-header" id="headingThree">-->
<!--                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree" id="accordian-button-color">-->
<!--                            පාඩම් අංක #3-->
<!--                        </button>-->
<!--                        </h2>-->
<!--                        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">-->
<!--                        <div class="accordion-body">-->
<!--                            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.-->
<!--                        </div>-->
<!--                        </div>-->
<!--                    </div>-->
                </div>
            </div>
            <!-- subject contents list end -->

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    import axios from "axios";

    export default {
        name : 'courseContent',
        components : {
            sidebar,
        },
        data(){
        return{
          lessons:[],
          errors:[]
        }
      },
      mounted(){
        console.log('mounted')
        console.log(this.$route.query.courseId)
        let url = 'api/v1/getLessons/?courseId='+this.$route.query.courseId;
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get(url, { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.lessons = response.data
            })
      },
      methods:{
          courseReg(){
           // const fd = new FormData()
            // fd.append("course", this.$route.query.courseId)
            let accessToken = localStorage.getItem('accessToken')
            let url = 'api/v1/createEnrollments/?course='+this.$route.query.courseId;
            axios
                .get(url, { headers: { "Content-Type": "multipart/form-data", Authorization: `Bearer ${accessToken}` } })
                .then(response =>{
                    console.log(response.data)
                   // this.response = response.data
                   //  alert('Course Register successfully!')
                   if (response.data.status == 'success'){
                        Swal.fire(
                          'successfully!',
                          'Enroll successfully!',
                          'success'
                        )
                      }else{
                      Swal.fire(
                          'Some thing when wrong!',
                          'ඔබ දැනටමත් ලියාපදිංචි වී ඇත!',
                          'error'
                        )
                   }
                    //window.location.href ='./index.php';
                })
                .catch(error =>{
                    if(error.response){
                        for(const property in error.response.data){
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }else if(error.message){
                        this.errors.push('Something went wrong. Please try again!')
                    }
                })
          }
      }
    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>