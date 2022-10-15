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

            <div class="row align-items-center justify-content-center">
                <div class="col-md-10 my-4">
                    <div class="card">
                        <div class="card-body">
                            <h2 class="text-center mt-2 mb-4">My Subject Name</h2>
                            <div class="card mt-2">
                                <div class="card-header subjectViewsCard">
                                    <p data-bs-target="#collapse" data-bs-toggle="collapse" aria-expanded="false" class="text-dark my-auto text-color sinhala-font fw-semibold accordian-button" style="color:#000000">Subject Lesson Name</p>
                                </div>
                                <div class="card-body collapse-show sinhala-font" id="collapse">
                                    <p class="text-color fw-normal">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odio pariatur doloribus sunt eaque officia eveniet corporis eos sed quo, minima incidunt, laboriosam laudantium modi placeat odit dolorem magni totam commodi!ඔබ කරමින් පවතින පාඨමාළාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න.</p>
                                    <router-link to="/study-mode" class="float-end mb-2" id="clickWatchBtn">පිවිසෙන්න</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="line"></div>

        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'

    export default {
        name : 'SubjectView',
        components : {
            sidebar,
        }
    }
</script>

<style scoped src="../../assets/css/student/main.css">
    
</style>