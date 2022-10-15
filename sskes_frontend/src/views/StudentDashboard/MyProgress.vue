<template>
    <div class="wrapper">
        <sidebar/>
        
        <!-- <nav id="sidebar">
        <div class="sidebar-header">
            <img src="../../assets/images/logo/logo.png" alt="" class="img-fluid">
        </div>

        <ul class="list-unstyled components">
            <li class="active sinhala-font">
                <a href="#homeSubmenu" data-bs-toggle="collapse" aria-expanded="false" class="dropdown-toggle"><i class="bi bi-house-door-fill pe-2"></i>මාගේ විෂයන්</a>
                <ul class="collapse list-unstyled" id="homeSubmenu">
                    <li class="pt-3">
                        <a href="#">Home 1</a>
                    </li>
                    <li class="pt-3">
                        <a href="#">Home 2</a>
                    </li>
                    <li class="pt-3">
                        <a href="#">Home 3</a>
                    </li>
                </ul>
            </li>
            <li class=" sinhala-font pt-3">
                <a href="#"><i class="bi bi-gear-fill"></i>මාගේ තොරතුරු</a>
            </li>
            <li class=" sinhala-font pt-3">
                    <a class="dropdown-toggle" data-bs-toggle="collapse" href="#pageSubmenu" role="button" aria-expanded="false" aria-controls="collapseExample">Page</a>

                <ul class="collapse list-unstyled" id="pageSubmenu">
                    <li class=" pt-3">
                        <a href="#">Page 1</a>
                    </li>
                    <li class=" pt-3">
                        <a href="#">Page 2</a>
                    </li>
                    <li class=" pt-3">
                        <a href="#">Page 3</a>
                    </li>
                </ul>
            </li>
            <li class=" sinhala-font pt-3">
                <a href="#"><i class="bi bi-graph-up"></i>මාගේ ප්‍රගතිය</a>
            </li>
            <li class=" sinhala-font pt-3">
                <a href="#"><i class="bi bi-person-circle"></i>මාගේ ගිණුම</a>
            </li>
        </ul>

        <ul class="list-unstyled second">
            <li class=" sinhala-font">
                <a href="#signout" class="signout text-center"><i class="bi bi-box-arrow-left"></i>ඉවත්වන්න</a>
            </li>
        </ul>
    </nav> -->

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

            <h1 class="text-center sinhala-font fw-bold mb-5">මාගේ ප්‍රගතිය</h1>

            <div class="row align-items-center mb-4">
                <h4 class="sinhala-font fw-bold ms-4">පාඨමාළා ප්‍රගතිය</h4>
                <div class="col-md-6 mb-3">
                    <ProgressPrecentageCard/>
                </div>
            </div>

            <div class="row align-items-center mt-5">
                <h4 class="sinhala-font fw-bold ms-4">සම්මාණ</h4>
                <div class="col-md-6 mb-3">
                    <GoldCard/>
                </div>
                <div class="col-md-6 mb-3">
                    <SilverCard/>
                </div>
                <div class="col-md-6 mb-3">
                    <BronzeCard/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/StudentDashboard/Sidebar'
    import ProgressPrecentageCard from '@/components/StudentDashboard/Progress/ProgressPrecentage'
    import GoldCard from '@/components/StudentDashboard/Progress/GoldCard'
    import SilverCard from '@/components/StudentDashboard/Progress/SilverCard'
    import BronzeCard from '@/components/StudentDashboard/Progress/BronzeCard'
    // import quiz from '@/components/TeacherDashboard/AddQuiz'


    export default {
        name : 'StuDashboard',
        components : {
            sidebar,
            ProgressPrecentageCard,
            GoldCard,
            SilverCard,
            BronzeCard,
            // quiz,
        }
    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>