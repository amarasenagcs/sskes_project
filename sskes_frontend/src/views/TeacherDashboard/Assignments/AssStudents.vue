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
                            <li class="nav-item fs-5 px-3"><a href="#">Username</a></li>
                        </ul>
                    </div>
                </div>
            </nav>

            <h3 class="sinhala-font text-center fw-bold mb-5">පිළිතුරු ලබාදුන් සිසුන්</h3>

            <div class="row justify-content-center align-items-center">
                <div class="col-9 mb-3">
                    <CompletedStudents/>
                </div>
            </div>

            
            <h2 style="color: #FFFFFF">contentfafaa</h2>
            <p style="color: #FFFFFF">Lorem ipsum dolor sit amet consectetur, adipisicing elit. Impedit in quod ducimus, nulla commodi tenetur officiis delectus veritatis, illo vitae sed quisquam omnis eaque nemo deleniti quasi, sunt ipsa doloremque.</p>

        </div>
        <!-- Page content end -->
    </div>
</template>

<script>
    import TeacherSidebar from "@/components/TeacherDashboard/Sidebar"
    import CompletedStudents from "@/components/TeacherDashboard/Assignment/AssStudents"

    export default {
        name : 'AssStudent',
        components : {
            TeacherSidebar,
            CompletedStudents,
        }
    }
</script>

<style scoped src="../../../assets/css/TeacherDashboard/main.css">

</style>