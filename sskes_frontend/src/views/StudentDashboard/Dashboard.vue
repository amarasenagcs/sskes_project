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
                                <a class="nav-link" href="#">{{ user.first_name}}</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="row">
                <div class="col-md-6 my-4">
                    <router-link to="/my-courses"><DashCard header="ආරම්භ කරන්න" text="ඔබගේ සියලුම පාඨමාලාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න" class="cardPic pic1" /></router-link>
                </div>
                <div class="col-md-6 my-4">
                    <router-link to="/completed-course"><DashCard header="සම්පූර්ණ කළ පාඨමාළාවන්" text="ඔබගේ සම්පූර්ණ කරන ලද පාඨමාළාවන් සදහා මෙතැනින් පිවිසෙන්න." class="cardPic pic2" /></router-link>
                </div>
                <div class="col-md-6 my-4">
                    <router-link to="/pending-course"><DashCard header="කරමින් පවතින පාඨමාළාවන්" text="ඔබ කරමින් පවතින පාඨමාළාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න." class="cardPic pic3" /></router-link>
                </div>
                <div class="col-md-6 my-4">
                    <router-link to="/pending-course"><DashCard header="මාගේ පාඨමාළාවන්" text="ඔබ කරමින් පවතින පාඨමාළාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න." class="cardPic pic4" /></router-link>
                </div>
            </div>

            <div class="line"></div>

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    import DashCard from '@/components/StudentDashboard/DashCard'
    import axios from "axios";


    export default {
        name : 'StuDashboard',
        components : {
            sidebar,
            DashCard,
        },data(){
        return{
          user: '',
        }
      },
        mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('/api/v1/getInvitationParent/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              let parentConId = response.data.parentConId
              // this.courses = response.data
              if(response.data.status == 'pending'){

                 Swal.fire({
                     title: '<strong>Parent connect request?</strong>',
                    text:response.data.parent,
                   icon: 'info',
                     showCloseButton: true,
                     showCancelButton: true,
                     focusConfirm: false,
                     allowOutsideClick: false,
                     }).then(function (res) {
                     if (res.isDismissed) {
                       // alert('Cancel button clicked');
                       // window.location.replace("");
                      }
                     else{
                        //alert('Ok click');
                      const fd = new FormData();
                      fd.append('status', 'confirm')
                      fd.append('parentConId', parentConId)

                       let accessToken = localStorage.getItem('accessToken')
                        axios
                            .post('api/v1/resInvitationParent/', fd, { headers: { "Content-Type": "multipart/form-data", Authorization: `Bearer ${accessToken}` } })
                            .then(response =>{
                                console.log(response.data)
                                alert('send successfully!')
                                // this.success.push('Lesson Register successfully!')

                            })
                            .catch(error =>{
                                if(error.response){
                                    for(const property in error.response.data){
                                        this.errors.push(`${property}: ${error.response.data[property]}`)
                                    }
                                }else if(error.message){
                                    // this.errors.push('Something went wrong. Please try again!')
                                }
                            })

                        //  window.location.replace("/auth-register-as-teacher");
                     }

                 })
              }
            })
          ,

        console.log('mounted')
        // let accessToken = localStorage.getItem('accessToken')
        axios
            .get('/api/v1/getCurrentUser/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.user = response.data.userInfo
            })


      },
    }
</script>

<style scoped src="../../assets/css/student/main.css">
    
</style>