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
                            <li class="nav-item fs-5 px-3">{{ user.first_name }}</li>
                        </ul>
                    </div>
                </div>
            </nav>
            
            <div class="row">
                <div class="col-md-6 my-4">
                    <router-link to="/students-list"><DashboardCard header="මාගේ දරුවන්" text="ඔබගේ දරුවන් පිළිබද තොරතුරු මෙහි පිවිසීමෙන් දැකගත හැකිය. ඇතුල්වන්න" class="cardPic pic1"/></router-link>
                </div>
                <div class="col-md-6 my-4">
                    <router-link to="/my-child-courses"><DashboardCard header="දරුවන්ගේ පාඨමාළා" text="ඔබගේ දරුවන්ගේ පාඨමාළා පිළිබද තොරතුරු පිවිසීමෙන් දැකගත හැකිය." class="cardPic pic2"/></router-link>
                </div>
                <!-- <div class="col-md-6 my-4">
                    <router-link ><DashboardCard header="" text=""/></router-link>
                </div> -->
            </div>

            <h2 style="color: #FFFFFF">fdasjnbfjladnbfva</h2>
            <p style="color: #FFFFFF">Lorem ipsum, dolor sit amet consectetur adipisicing elit. In optio quis consequatur et quos? Consectetur magnam dolor corrupti explicabo non officiis nihil voluptatum veniam, voluptate harum repellendus saepe id veritatis?</p>
        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import Sidebar from "@/components/ParentDashboard/Sidebar"
    import DashboardCard from '@/components/ParentDashboard/DashCard'
    import axios from "axios";

    export default {
        name : 'ParentDashboard',
        components : {
            Sidebar,
            DashboardCard
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
      }
    }
</script>

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>