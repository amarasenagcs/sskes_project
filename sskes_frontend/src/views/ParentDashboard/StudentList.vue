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
                            <li class="nav-item fs-5 px-3">{UserName}</li>
                        </ul>
                    </div>
                </div>
            </nav>
            
            <div class="row p-5">
                <h3 class="text-center sinhala-font fw-bold mb-4">මාගේ සිසුන්</h3>
                <div class="card completeCard border border-3 mt-3" v-for="student in students"
                    v-bind:key="student.id">
                    <div class="card-body sinhala-font">
                        <div class="row">
                            <div class="col-md-6 mb-3">
                                <label for="fName" class="form-label">මුල් නම</label>
                                <input type="text" class="form-control" :value="student.student.first_name"  name="fName" id="fName" readonly disabled>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="lName" class="form-label">අග නම</label>
                                <input type="text" class="form-control" :value="student.student.last_name"  name="lName" id="lName" disabled>
                            </div>
                            <div class="col-md-6 mb-3">
                                <label for="fName" class="form-label">ඊමේල් ලිපිනය</label>
                                <input type="email" class="form-control" name="email" :value="student.student.email" id="email" disabled>
                            </div>
                            <div>
                                <button class="text-center btn btn-danger float-end" v-bind:id="student.id"  @click="removeChild">ඉවත් කරන්න</button>
                            </div>
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
        name : 'studentList',
        components : {
            Sidebar,
        },
        data(){
        return{
          students:[],
        }
      },
      methods:{
          removeChild(){

            const fd = new FormData();
            fd.append('parntConId', event.target.id)
            let accessToken = localStorage.getItem('accessToken')
            axios
                .post('api/v1/remParentChildren/', fd, { headers: { "Content-Type": "multipart/form-data", Authorization: `Bearer ${accessToken}` } })
                .then(response =>{

                    console.log(response.data)
                    // alert('Remove successfully!')
                    Swal.fire(
                          'successfully!',
                          'successfully removed!',
                          'success'
                        )
                    location.reload()
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
      },
      mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('api/v1/getParentChildren/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.students = response.data
            })
      },
    }
</script>

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>