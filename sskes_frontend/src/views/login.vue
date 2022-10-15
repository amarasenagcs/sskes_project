<template>
    <div id="auth">
        <Navbar/>
        <div class="container-fluid">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-md-6 pt-2">
                    <img src="../assets/images/bg/login.png" class="img-fluid" alt="login-image">
                </div>
                <div class="col-md-6 pt-2">
                    <div class="card shadow mt-5">


                        <div class="card-body">
                            <h2 class="text-center mb-4" style="color: #FF6700;">
                                Login Account
                            </h2>
                          <div v-if="error =='Please activate you account'" class="alert alert-danger" role="alert">
                                Your account not activated , Check your email or sign-up again<a href="#" class="alert-link">here</a>
                          </div>
                            <form @submit.prevent="submitForm">
                                <div class="form-group position-relative has-icon-left mb-4">
                                    <input type="email" class="form-control form-control-xl" placeholder="Email" pattern=".+.com"  v-model="username" required>
                                    <div class="form-control-icon">
                                        <i class="bi bi-envelope"></i>
                                    </div>
                                </div>

                                <div class="form-group position-relative has-icon-left mb-4">
                                    <input type="password" class="form-control form-control-xl" placeholder="Password" v-model="password" required>
                                    <div class="form-control-icon">
                                        <i class="bi bi-shield-lock"></i>
                                    </div>
                                </div>
                               <p class="mt-4 fs-6"><router-link to="/forgetPassword" class="text-primary">Forget Password ?</router-link></p>

                                <button class="btn btn-primary btn-block btn-lg shadow-lg mt-3">Sign In</button>
                            </form>
<!--                            <h6 class="text-center py-4">-->
<!--                                OR-->
<!--                            </h6>-->
<!--                            <button class="btn btn-lg btn-google btn-block text-uppercase btn-outline border shadow-sm align-items-center" href="#"><img src="https://img.icons8.com/color/25/000000/google-logo.png"> SignIn with Google</button>-->
                            
                            <p class="mt-4 fs-5 text-center">Dont't have an already Account? <router-link to="/signUp" class="text-primary fw-semibold">Sign Up</router-link></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
// import Nav from '@/components/Nav';
import Navbar from "@/components/LandingPage/Navbar"
import Footer from "@/components/LandingPage/Footer"
import axios from 'axios';

export default {
    name: 'login',
    components : {
        Navbar,
        Footer,
    },
    data(){
        return{
            username:'',
            password:'', 
            //   is_teacher: false,
            //   is_parent: false,
            //   is_student: false,
            errors:[],
            error:''
        }
    },

    methods: {

                    
        submitForm(){
                

        console.log('submit testing form')

        axios.defaults.headers.common['Authorization'] = ""

        localStorage.removeItem('token')
        localStorage.removeItem('email')
        localStorage.clear();
        this.errors = []
            console.log( this.errors)
            if(this.username===''){
                this.errors.push('The username is missing')
            }
            if(this.password===''){
                this.errors.push('The password is missing')
            }
            
            if(!this.errors.length){
                const formData = {
                    username: this.username,
                    password: this.password,
                    // is_teacher: this.is_teacher,
                    // is_parent: this.is_parent,
                    // is_student: this.is_student,
                }
            // const form = new formData;
              this.errors = []
            //  console.log(formData)
            //  formData.is_student = this.is_student;
                ///form.set('is_student',true)
                axios
                    .post('/api/v1/login/', formData)
                    .then(response =>{
                       // console.log()

                    // this.response = response.data
                    // this.response = response.data

                       // console.log(response.data.userType)
                       //  const x = response.data.userDetails
                       //  console.log(x)
                       // localStorage.setItem('userId', x[0].id)
                     //   localStorage.setItem('username', response.data.username)

                         const accessToken = response.data.accessToken
                      //  const json = JSON.parse(accessToken);
                        console.log(accessToken)
                      //
                        this.$store.commit('setToken', accessToken)
                       // this.$store.state.accessToken
                        axios.defaults.headers.common['Authorization'] = "accessToken" + accessToken
                       //
                        localStorage.setItem('accessToken', accessToken)
                       //
                       //  alert('Login successfully!')

                      /// after delete commnet///
                        if(response.data.userType == 'parent'){
                            alert('Login successfully!')
                            localStorage.setItem('isParentLoggedIn', true);
                            // this.$router.push('/parent-dashboard')
                            window.location.href ='/parent-dashboard';
                        }else if(response.data.userType == 'teacher'){
                            alert('Login successfully!')
                            // this.isTeacherLoggedIn =true
                            localStorage.setItem('isTeacherLoggedIn', true);
                            // this.$router.push('/TeacherDashboard')
                            window.location.href ='/TeacherDashboard';
                        }else if(response.data.userType == 'student'){
                            localStorage.setItem('isStudentLoggedIn', true);
                            alert('Login successfully!')
                            // this.$router.push('/student-dashboard')
                            window.location.href ='/student-dashboard';
                        }else{
                            alert('error login')
                        }

                       //////////////////////////////
                        //window.location.href ='./index.php';

                    })
                    .catch(error =>{
                        if(error.response){
                            for(const property in error.response.data){
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                                console.log(error.response.data)
                                const x = error.response.data
                                console.log(x)
                                if(x.error == "Please activate you account"){
                                  //console.log("condition true"+ x.error)
                                  this.error =  x.error
                                }

                                alert('username or password incorrect')


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