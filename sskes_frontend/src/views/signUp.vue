<template>
<div id="auth">
  <!-- <div class="row h-100"> -->
    <Navbar/>
    <div class="container-fluid">
<!--      <div v-if="errors.length" class="alert alert-danger d-flex align-items-center" role="alert">-->
<!--          <svg class="bi flex-shrink-0 me-2" role="img" aria-label="Danger:">-->
<!--            <use xlink:href="#exclamation-triangle-fill"/>-->
<!--          </svg>-->
<!--          <div v-for="error in errors"  v-bind:key="error">-->
<!--           {{error}}-->
<!--          </div>-->
<!--      </div>-->
        <div  v-if="errors.length" class="toastd-flex justify-content-center align-items-center w-100 text-bg-danger border-0 fade show" role="alert" aria-live="assertive" aria-atomic="true">
          <div class="d-flex">
            <div class="toast-body justify-content-center align-items-center" v-for="error in errors"  v-bind:key="error">
              {{error}}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
        </div>
        <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-6 pt-2">
                <img src="../assets/images/bg/signup.png" class="img-fluid" alt="login-image">
            </div>
            <div class="col-md-6 pt-2">
                <div class="card shadow mt-5">
                    <div class="card-body">
                        <h2 class="form-header text-center" style="color: #FF6700;">
                            SignUp Account
                        </h2>

<!--                        <div v-if="errors.length" class="alert alert-danger" role="alert">-->
<!--                          <p-->
<!--                            v-for="error in errors"-->
<!--                            v-bind:key="error">-->
<!--                            {{error}}-->
<!--                          </p>-->
<!--                        </div>-->
                        <div class="userType d-flex justify-content-center align-items-center my-3">
                          <div id = "toolBtns">
                              <div class="btn-group" role="group" id="toolBtns">
                                <button  @click="change_selection" :class="{active: activeBtn === 'student' }" type="button" name="selection_btn" id="student"  class="btn btn-outline-primary btn-lg mx-3">Learner</button>
                                <button @click="change_selection" :class="{active: activeBtn === 'parent' }" type="button" name="selection_btn" id="parent" class="btn btn-outline-primary btn-lg mx-3" >Parent</button>
                                <button @click="change_selection" :class="{active: activeBtn === 'teacher' }" type="button" name="selection_btn" id="teacher" class="btn btn-outline-primary btn-lg mx-3" >Teacher</button>
                              </div>
                            </div>
                        </div>

                        <form @submit.prevent="submitForm">
                            <div class="form-group position-relative has-icon-left mb-4">
                                <input type="text" class="form-control form-control-xl sinhala-font" placeholder="මුල් නම" v-model="first_name" required>
                                <div class="form-control-icon">
                                    <i class="bi bi-person"></i>
                                </div>
                            </div>
                            <div class="form-group position-relative has-icon-left mb-4">
                                <input type="text" class="form-control form-control-xl sinhala-font" placeholder="අවසන් නම" v-model="last_name" required>
                                <div class="form-control-icon">
                                    <i class="bi bi-person"></i>
                                </div>
                            </div>

                            <div class="form-group position-relative has-icon-left mb-4">
                                <input type="email" class="form-control form-control-xl sinhala-font" placeholder="විද්යුත් තැපැල් ලිපිනය" pattern=".+.com" v-model="username" required>
                                <div class="form-control-icon">
                                    <i class="bi bi-envelope"></i>
                                </div>
                            </div>

                            <div class="form-group position-relative has-icon-left mb-4">
                                <input type="password" class="form-control form-control-xl" placeholder="මුරපදය" v-model="password1" required>
                                <div class="form-control-icon">
                                    <i class="bi bi-shield-lock"></i>
                                </div>
                            </div>
                            <div class="form-group position-relative has-icon-left mb-4">
                                <input type="password" class="form-control form-control-xl" placeholder="මුරපදය තහවුරු කරන්න" v-model="password2" required>
                                <div class="form-control-icon">
                                    <i class="bi bi-shield-lock"></i>
                                </div>
                            </div>
                            <button :disabled="!email && !activeBtn" class="btn btn-primary btn-block btn-lg shadow-lg mt-3">Sign Up</button>
                        </form>
<!--                        <h6 class="text-center py-4">-->
<!--                            OR-->
<!--                        </h6>-->

<!--                        <button class="btn btn-lg btn-google btn-block text-uppercase btn-outline border shadow-sm align-items-center" href="#"><img src="https://img.icons8.com/color/25/000000/google-logo.png"> SignUp with Google</button>-->
                        
                        <p class="mt-4 fs-5 text-center">Already have an Account? <router-link to="/login" class="text-primary fw-semibold">LogIn</router-link></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Footer/>
<!-- </div> -->
</div>
</template>

<script>
// import Nav from '@/components/Nav';
import Navbar from "@/components/LandingPage/Navbar"
import Footer from "@/components/LandingPage/Footer"

import axios from 'axios';

export default {
  components: { 
    Navbar,
    Footer
 },
  name: 'signUp',
   el: '#toolBtns',
  data(){

      return{
          username:'',
          email:'',
          password1:'',
          password2:'',
          first_name:'',
          last_name:'',
          is_teacher: false,
          is_parent: false,
          is_student: false,
          errors:[],
          activeBtn:'',
      }
  },

  methods: {

          change_selection: function (event){
            //alert(event.target.id);
            this.activeBtn = event.target.id;
            var id =  event.target.id
            // document.getElementById("selection").innerHTML="You are trying to sign up as a "+ id;
            //
            // document.getElementById("student").classList.remove('btn-primary');
            // document.getElementById("parent").classList.remove('btn-primary');
            // document.getElementById("teacher").classList.remove('btn-primary');
            //
            // document.getElementById(id).classList.add('btn-primary');

            if(id ==="teacher"){
                this.is_student=false;
                this.is_teacher= true;
                this.is_parent= false;

                // Swal.fire({
                //     title: '<strong>Teacher <u>Verification Required</strong>',
                //     icon: 'info',
                //     html:
                //         'You need to <b>Verify your self</b>, ' +
                //         '<a href="auth-register-as-teacher.html">click</a> ' +
                //         'here to continue',
                //     showCloseButton: true,
                //     showCancelButton: true,
                //     focusConfirm: false,
                //     allowOutsideClick: false,
                //     }).then(function (res) {
                //     if (res.isDismissed) {
                //       // alert('Cancel button clicked');
                //       window.location.replace("");
                //     }
                //     else{
                //         //alert('Ok click');
                //         window.location.replace("/auth-register-as-teacher");
                //     }
                //
                // })

            }else if(id==='parent'){
                    this.is_student=false;
                    this.is_teacher= false;
                    this.is_parent= true;
            }
            else if(id==='student'){
            //  alert('hi')
              this.is_student=true;
              this.is_teacher= false;
              this.is_parent= false;
               console.log(this.is_student);
            }else{  
              this.is_student=false;
              this.is_teacher= false;
              this.is_parent= false;
            }

        },

        
    // userType(type){
    //               if(type==='Learner'){
                    
    //                 this.is_student=true;
    //                 this.is_teacher= false;
    //                 this.is_parent= false;
    //                 console.log(type)
                    
    //               }else if(type==='Teacher'){
    //                 this.is_student=false;
    //                 this.is_teacher= true;
    //                 this.is_parent= false;
    //               }
    //               else if(type==='Parent'){
    //                 this.is_student=false;
    //                 this.is_teacher= false;
    //                 this.is_parent= true;
    //               }else{  
    //                 this.is_student=false;
    //                 this.is_teacher= false;
    //                 this.is_parent= false;
    //               }
                  

    //             },
                
    submitForm(){
            

      console.log('submit testing form')
        //console.log(this.username)
        if(this.username===''){
            this.errors.push('The username is missing')
        }
        if(this.password1===''){
            this.errors.push('The password is missing')
        }
        if(this.password2 !== this.password1){
            this.errors.push('The passwords are not matching')
        }
        
        if(!this.errors.length){
            const formData = {
                username: this.username,
                email: this.username,
                password: this.password1,
                is_teacher: this.is_teacher,
                is_parent: this.is_parent,
                is_student: this.is_student,
                first_name:this.first_name,
                last_name:this.last_name
            }
           // const form = new formData;
            console.log(formData)
            localStorage.setItem("formData", JSON.stringify(formData));
          //  formData.is_student = this.is_student;
            ///form.set('is_student',true)
            // axios
            //     .post('/api/v1/registerUser/', formData)
                axios({
                    method: 'post',
                    url: '/api/v1/registerUser/',
                    xstfCookieName: 'csrftoken',
                    xsrfHeaderName: 'X-CSRFToken',
                    data: formData,
                    headers: {
                        'X-CSRFToken': 'csrftoken',
                    }
                })
                .then(response =>{
                    // var toastTrigger = document.getElementById('liveToastBtn')
                    // var toastLiveExample = document.getElementById('liveToast')
                    // if (toastTrigger) {
                    // toastTrigger.addEventListener('click', function () {
                    //     var toast = new bootstrap.Toast(toastLiveExample)
                    //     toast.show()
                    // })
                    // }
                    alert('Acctivation link send successfully!, Check your email')
                    this.$router.push('/login')
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
}
</script>

<style scoped src="../assets/css/main/app.css">
    /* h2 .form-header{
        color: #FFA500;
        padding-bottom: 10px;
        margin-bottom: 10px;
    } */
.active{
  class : btn btn-primary btn-lg mx-3;
}
</style>