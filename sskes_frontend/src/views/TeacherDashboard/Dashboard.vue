<template>
    <div class="wrapper">
        <TeacherSidebar/>
        <!-- Page content start -->
        <div id="content">
            <nav class="navbar navbar-expand-lg bg-light shadow p-3 mb-5 bg-body">
                <div class="container-fluid">
                    <button type="button" id="sidebarCollapse" class="btn btn-success navbar-btn">
                        <i class="bi bi-list fs-4"></i>
                    </button>
                    <div class="collapse navbar-collapse p-3" id="navbarSupportedContent">
                        <ul class="navbar-nav me-2 mx-auto mb-2 mb-lg-0">
                            <li class="nav-item fs-5 px-3"><a href="#">{{ user.first_name}}</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
            <div class="row">
                <div class="col-md-6 p-3">
                    <router-link to="/AllCourse">
                        <DashCards 
                            title = "පාඨමාලාවන්"
                            body = "ඔබගේ සියලූම පාඨමාලාවන් මෙයින් දැකගත හැක"
                            class="border image-style img border-primary border-4 shadow p-3 mb-5 bg-body rounded"
                        />
                    </router-link>
                </div>
                <div class="col-md-6 p-3">
                    <router-link to="/TeacherAddCourse">
                        <DashCards
                            title = "පාඨමාලාවන් ඇතුලත් කීරීම"
                            body = "නව පාඨමාලාවන් ඇතුලත්කිරීම සදහා ඇතුල්වන්න"
                            class="border image-style img1 border-success border-4 shadow p-3 mb-5 bg-body rounded"
                        />
                    </router-link>
                </div>
                <div class="col-md-6 p-3">
                    <router-link to="/AllStudents">
                        <DashCards
                            title = "ලියාපදිංචි සිසුන්"
                            body = "ඔබ සමග ලියාපදිංචි සිසුන්ගේ විස්තර දැනගැනීමට ඇතුල්වන්න"
                            class="border image-style img2 border-warning border-4 shadow p-3 mb-5 bg-body rounded"
                        />
                    </router-link>
                </div>
                <div class="col-md-6 p-3">
                    <router-link to="/Student-Progress">
                        <DashCards
                            title = "සිසුන්ගේ කාර්ය සාධනය"
                            body = "ඔබගේ සිසුන්ගේ කාර්ය සාධනය අධ්‍යනය කිරීම"
                            class="border image-style img3 border-danger border-4 shadow p-3 mb-5 bg-body rounded"
                        />
                    </router-link>
                </div>
                <div class="col-md-6 p-3">
                    <router-link to="/Course-Progress">
                        <DashCards
                            title = "පාඨමාලා කාර්ය සාධනය"
                            body = "ඔබගේ පාඨමාලා කාර්ය සාධනය අධ්‍යනය කිරීම"
                            class="border image-style img4 border-secondary border-4 shadow p-3 mb-5 bg-body rounded"
                        />
                    </router-link>
                </div>

            </div>
<!-- 
            <div class="line"></div>
            
            <h2>contentfafaa</h2>
            <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Impedit in quod ducimus, nulla commodi tenetur officiis delectus veritatis, illo vitae sed quisquam omnis eaque nemo deleniti quasi, sunt ipsa doloremque.</p> -->

        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import TeacherSidebar from "@/components/TeacherDashboard/Sidebar"
    import DashCards from "@/components/TeacherDashboard/DashCard"
    import axios from "axios";

    export default {
        name : 'TeacherDashboard',
        components : {
            TeacherSidebar,
            DashCards
        },
      data(){
        return{
          user:[]
        }
      },
      mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('/api/v1/getCurrentUser/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.user = response.data.userInfo
            })
      },
    }
</script>

<style scoped src="../../assets/css/TeacherDashboard/main.css">

</style>