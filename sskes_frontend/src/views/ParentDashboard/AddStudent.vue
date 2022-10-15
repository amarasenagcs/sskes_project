<template>
    <div class="wrapper">        
        <Sidebar/>
        <!-- Page content start -->
        <div id="content">
            <nav class="navbar navbar-expand-lg bg-light shadow p-3 mb-5 bg-body">
                <div class="container-fluid">
                    <button type="button" id="sidebarCollapse" class="btn btn-info navbar-btn">
                        <i class="bi bi-list fs-4"></i>
                    </button>
                    <div class="collapse navbar-collapse p-3" id="navbarSupportedContent">
                        <ul class="navbar-nav me-2 mx-auto mb-2 mb-lg-0">
<!--                            <li class="nav-item fs-5 px-3">{UserName}</li>-->
                        </ul>
                    </div>
                </div>
            </nav>
            
            <div class="row d-flex">
            <div class="col-md-6 pt-2">
                <img src="../../assets/images/bg/addStudent.svg" class="img-fluid" alt="login-image">
            </div>
            <div class="col-md-6 pt-2">
                <div class="card shadow mt-5">
                    <div class="card-body">
                        <h2 class="form-header text-center" style="color: #FF6700;">
                            ඔබගේ දරුවා සමග සම්බන්ද වෙන්න
                        </h2>

                        <form @submit.prevent="submitForm">
                            <div class="form-group position-relative has-icon-left mt-4 mb-4">
                                <input type="email" v-model="email" class="form-control form-control-xl"  placeholder="සිසුවාගේ ඊමේල් ලිපිනය" pattern=".+.com" title="කරුණාකර වලංගු විද්‍යුත් තැපැල් ලිපිනයක් භාවිතා කරන්න" style="text-transform: lowercase;" required>
                            </div>
                            <button class="btn btn-primary float-end btn-block btn-lg shadow-lg mt-3">Sign Up</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

            <h2 style="color: #FFFFFF">fdasjnbfjladnbfva</h2>
            <p style="color: #FFFFFF">Lorem ipsum, dolor sit amet consectetur adipisicing elit. In optio quis consequatur et quos? Consectetur magnam dolor corrupti explicabo non officiis nihil voluptatum veniam, voluptate harum repellendus saepe id veritatis?</p>
        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import Sidebar from "@/components/ParentDashboard/Sidebar"
    import axios from "axios";
    export default {
        name : 'addStudent',
        components : {
            Sidebar,
        },
        data(){
        return{
          email:''
        }
      },
      methods:{
          submitForm(){
            console.log("submitform");
           const fd = new FormData()
           fd.append('email', this.email)
            let accessToken = localStorage.getItem('accessToken')
            axios
                .post('api/v1/sendInvitationParent/', fd, { headers: { "Content-Type": "multipart/form-data", Authorization: `Bearer ${accessToken}` } })
                .then(response =>{
                    console.log(response.data)
                   // this.response = response.data
                   //  alert('Course Register successfully!')
                    //window.location.href ='./index.php';
                  if (response.data.success == 'successfully invite!'){
                        Swal.fire(
                          'successfully!',
                          'Invitation send successfully!',
                          'success'
                        )
                      }
                  else if (response.data.error=='already requested!') {
                        Swal.fire(
                          'Request already Send!',
                          'ඔබ දැනටමත් ඇරයුම යවා ඇත!',
                          'info'
                        )
                      }
                  else {
                       Swal.fire(
                          'Some thing when wrong!',
                          'ඔබ ලබා දී ඇති පරිසීලකනාමය ලියාපදිංචි වී නොමැත!',
                          'error'
                        )
                      }



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

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>