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
<!--                                <a class="nav-link" href="#">{UserName}</a>-->
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <div class="row justify-content-center align-items-center">
                <div class="col-md-10">
                    <profileForm/>
                </div>
            </div>

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    import profileForm from '@/components/StudentDashboard/ProfileForm'
    import axios from "axios";

    export default {
        name : 'StuProfile',
        components : {
            sidebar,
            profileForm
        }
    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>