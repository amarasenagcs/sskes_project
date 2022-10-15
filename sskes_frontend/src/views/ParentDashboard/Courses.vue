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

            <!-- Course search bar start -->
            <div class="row justify-content-center align-items-center">                
                <form method="post">
                    <legend class="text-center sinhala-font fw-bold py-3">ඔබගේ දරුවාට සුදුසු පාඨමාළාව සොයන්න</legend>
                    <div class="row d-flex my-5 justify-content-center align-items-center">
                        <div class="col-md-10 d-flex">
                            <input type="text" class="form-control ms-4 me-3 p-2 shadow" name="searchCourse" id="courseSearchBar" placeholder="පාඨමාළාවේ නම...">
                            <!-- <button class="btn btn-primary shadow">සොයන්න</button> -->
                        </div>
                    </div>
                </form>
            </div>
            <!-- Course search bar end -->

            <div class="row p-3">
                <!-- courses list cards start -->
                <div class="col-md-3 my-3">
                    <!-- <CoursesList/> -->
                    <div class="card coursesCard">
                        <img src="../../assets/images/course/science.jpg" class="img-fluid" >
                        <div class="card-body border border-3">
                            <div class="h5 text-center sinhala-font fs-5 pt-1 fw-bold">පාඨමාළා නම</div>
                            <div class="h6 sinhala-font fs-6 pt-1 fw-bold">වසර : <span class="ms-2">5</span></div>
                            <p class="sinhala-font  pt-2 mb-3" id="courseList">මෙහි පාඨමාළා පිළිබද කෙටි විස්තරයක් ඇතුලත් වේ. සංහල පාඨමාළාව මෙම වයෛ සිසුන් සදහා.</p>
                            <router-link to="/course-content-view" class="sinhala-font px-2 mb-1 float-end next">පිවිසෙන්න</router-link>
                        </div>
                    </div>
                </div>
                <!-- courses list cards end -->
            </div>

            <h2 style="color: #FFFFFF">fdasjnbfjladnbfva</h2>
            <p style="color: #FFFFFF">Lorem ipsum, dolor sit amet consectetur adipisicing elit. In optio quis consequatur et quos? Consectetur magnam dolor corrupti explicabo non officiis nihil voluptatum veniam, voluptate harum repellendus saepe id veritatis?</p>
        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import Sidebar from "@/components/ParentDashboard/Sidebar"
    // import CoursesList from "@/components/ParentDashboard/Courses"

    export default {
        name : 'MyCourses',
        components : {
            Sidebar,
            // CoursesList,

        }
    }
</script>

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>