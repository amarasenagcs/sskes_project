<template>
    <div id="auth">
        <div class="container-fluid">
            <div class="row d-flex justify-content-center align-items-center h-100" style="margin-top: 10%;">
                <div class="col-md-6 pt-2">
                    <img src="../assets/images/bg/forget-password.png" class="img-fluid" alt="login-image">
                </div>
                <div class="col-md-6 pt-2">
                    <div class="card shadow mt-5">
                        <div class="card-body">
                            <h2 class="text-center mb-4" style="color: #FF6700;">
                                Forget Password
                            </h2>
                            <div class="alert alert-success alert-dismissible fade show" role="alert">
                                <strong>Success sharing!</strong> Check your email address to reset link
                                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                            </div>
                            <form @submit.prevent="submitForm">
                                <label class="form-label py-2" for="email">Email Address</label>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1"><i class="bi bi-envelope fw-bolder"></i></span>
                                    <input type="email" class="form-control p-2" placeholder="Type your Email." aria-label="email" v-model="email" aria-describedby="basic-addon1">
                                </div>
                                                            
                                <button class="btn btn-secondary opacity-50 btn-block btn-lg shadow-lg mt-3">Send reset link</button>
                            </form>
                            
                            <p class="mt-4 fs-5 text-center"><router-link to="/login" class="text-primary fw-semibold">SignIn</router-link></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer class="mt-2 mb-0"/>
    </div>
</template>

<script>
// import Nav from '@/components/Nav';
// import Navbar from "@/components/Home/Navbar"
// import Footer from "@/components/Home/Footer"
import axios from 'axios';


export default {
    name: 'ForgetPassword',
    components : {
        // Navbar,
        // Footer,
    },
    data(){
        return{
            email:'',
            //   is_teacher: false,
            //   is_parent: false,
            //   is_student: false,
            errors:[],
        }
    },
  methods: {

    submitForm(){


      console.log('submit testing form')



        if(this.email==='') {
          this.errors.push('The email is missing')
        }

        if(!this.errors.length){
            const formData = {
                email: this.email
            }
           // const form = new formData;
            console.log(formData)

              axios
                .post('api/password_reset/', formData)
                .then(response =>{
                    // var toastTrigger = document.getElementById('liveToastBtn')
                    // var toastLiveExample = document.getElementById('liveToast')
                    // if (toastTrigger) {
                    // toastTrigger.addEventListener('click', function () {
                    //     var toast = new bootstrap.Toast(toastLiveExample)
                    //     toast.show()
                    // })
                    // }
                    alert('Check your email address')
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
    /* h2{
        color: #FF6700;
    } */
    .btn {
        border-radius: 2px;
        text-transform: capitalize;
        font-size: 15px;
        padding: 10px 19px;
        cursor: pointer
    }
    .btn-google {
        color: #545454;
        background-color: #ffffff;
        box-shadow: 0 1px 2px 1px #ddd;
    }
</style>