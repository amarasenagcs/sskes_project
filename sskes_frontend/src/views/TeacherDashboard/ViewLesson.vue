<template>
    <div class="wrapper">
        <!-- top row start -->
        <div class="row bg-light">
            <div class="col-md-12 justify-content-center align-items-center shadow">
                    <router-link to="/AllCourse"><li class="list-item text-danger fw-4 list-unstyled float-start ms-4 fs-4 p-3 mx-auto"><i class="bi bi-arrow-left-short fw-bold"></i>Back</li></router-link>
<!--                    <li class="list-item list-unstyled float-end me-2 fs-4 p-3 mx-auto">{ Subject Name }</li>-->
            </div>
        </div>
        <!-- top row end -->
        <div class="row" style="height: 100vh;">
            <div class="col-lg-8 col-md-6 p-4" id="secOne">                
                <div class="tab-content px-4 py-3" id="v-pills-tabContent">

<!--                    <div class="tab-pane fade show active" id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab" tabindex="0">Tab 01 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iste beatae, minus eius nesciunt ut ullam consequuntur voluptatum dolor, nemo eaque aliquid exercitationem enim numquam placeat tempore laudantium natus labore non.</div>-->

<!--                    <div class="tab-pane fade" id="v-pills-profile" role="tabpanel" aria-labelledby="v-pills-profile-tab" tabindex="0">Tab 02 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iste beatae, minus eius nesciunt ut ullam consequuntur voluptatum dolor, nemo eaque aliquid exercitationem enim numquam placeat tempore laudantium natus labore non.</div>-->

<!--                    <div class="tab-pane fade" id="v-pills-disabled" role="tabpanel" aria-labelledby="v-pills-disabled-tab" tabindex="0">Tab 03 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iste beatae, minus eius nesciunt ut ullam consequuntur voluptatum dolor, nemo eaque aliquid exercitationem enim numquam placeat tempore laudantium natus labore non.</div>-->

                    <div v-for="lesson in lessons" v-bind:key="lesson.id" class="tab-pane fade" v-bind:id="'lesson'+lesson.id" role="tabpanel" aria-labelledby="v-pills-messages-tab" tabindex="0">
                      <p class="sinhala-font mb-4" style="text-decoration:underline; text-decoration-color: #FF6700; text-underline-offset: 4px; font-weight:600; text-decoration-thickness: 3px;">{{ lesson.lesson_name }}</p>
                      <p class="sinhala-font"> {{lesson.content_description}}</p>
                      <video width="850" height="440" controls class="mt-4">
                            <source :src="lesson.get_content" type="video/mp4">
<!--                            <source src="./sample.mp4" type="video/mp4">-->
                        </video>
                    </div>

<!--                    <div class="tab-pane fade" id="v-pills-settings" role="tabpanel" aria-labelledby="v-pills-settings-tab" tabindex="0">Tab 05 Lorem ipsum dolor sit amet consectetur, adipisicing elit. Iste beatae, minus eius nesciunt ut ullam consequuntur voluptatum dolor, nemo eaque aliquid exercitationem enim numquam placeat tempore laudantium natus labore non.</div>-->
                </div>
            </div>
            <div class="col-lg-4 col-md-6 p-4 border scrolBar overflow-scroll" id="secTwo">
                <div class="nav flex-column nav-pills mx-auto justify-content-center" id="v-pills-tab" role="tablist" aria-orientation="vertical">
<!--                    <h3 class="navbar-header sinhala-font">පාඩම</h3>-->
                        <div class="row">
                              <div class="col-8">
                                  <h3 class="navbar-header sinhala-font me-5">පාඩම</h3>
                              </div>
                              <div class="col-4">
                                  <buttotn type="button" @click="publish" class="btn btn-primary p-2 float-end">PUBLISH</buttotn>
                              </div>
                          </div>
                    <button v-for="lesson in lessons"
                    v-bind:key="lesson.id" class="sinhala-font" id="v-pills-home-tab" data-bs-toggle="pill" v-bind:data-bs-target="'#lesson'+lesson.id" type="button" role="tab" aria-controls="v-pills-home" aria-selected="true">
                      {{ lesson.lesson_name }}</button>

<!--                    <button class="sinhala-font" id="v-pills-profile-tab" data-bs-toggle="pill" data-bs-target="#v-pills-profile" type="button" role="tab" aria-controls="v-pills-profile" aria-selected="false">Profile</button>-->

<!--                    <button class="sinhala-font" id="v-pills-disabled-tab" data-bs-toggle="pill" data-bs-target="#v-pills-disabled" type="button" role="tab" aria-controls="v-pills-disabled" aria-selected="false">About</button>-->

<!--                    <button class="sinhala-font" id="v-pills-messages-tab" data-bs-toggle="pill" data-bs-target="#v-pills-messages" type="button" role="tab" aria-controls="v-pills-messages" aria-selected="false">Messages</button>-->

<!--                    <button class="sinhala-font" id="v-pills-settings-tab" data-bs-toggle="pill" data-bs-target="#v-pills-settings" type="button" role="tab" aria-controls="v-pills-settings" aria-selected="false">Settings</button>-->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name : 'LessonView',
        data(){
        return{
          lessons:[]
        }
      },
      methods:{
          publish(){
            // let coursId = this.$route.query.courseId
            let url = 'api/v1/pubCourse/?courseId='+this.$route.query.courseId;
            let accessToken = localStorage.getItem('accessToken')
            axios
            .get(url, { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              // this.lessons = response.data
               if (response.data.status == 'publish successfully'){
                        Swal.fire(
                          'successfully!',
                          'publish successfully!',
                          'success'
                        )
                      }else{
                      Swal.fire(
                          'Some thing when wrong!',
                          'ඔබ දැනටමත් මෙම පාඨමාලාව ප්‍රකාශ කර ඇත!',
                          'error'
                        )
                   }
            })
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
      }
    }
</script>

<style lang="scss" scoped>
.wrapper {    
    align-items: stretch;
    background-color: rgba(234,238,240,0.4);
}

a{
    text-decoration: none;
}

#secOne{
    height: 100%;
}

#secTwo{
    background-color: rgba(234,238,240,0.9);
}

.scrolBar{
    height: 100%;
    border: 1px solid gray;
    // overflow: scroll;
}

button{
    color: black;
    font-weight: 600;
    background: rgba(255, 255, 255, 0.8);
    padding: 10px;
    margin-top: 10px;
    border: 0;
    border-radius: 7px;
}

button:hover{
    color: #ffffff;
    font-weight: 600;
    background: #FF6700;
    padding: 10px;
    margin-bottom: 12px;
    border: 0;
    border-radius: 7px;
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.4);
}

video{
    margin-top: 10px;
    width: 920px;
    height: 440px;
}

@media (max-width: 768px) {

    #secOne{
        height: fit-content;
    }

    video{
        width: 450px;
        height: 350px;
    }
}
</style>