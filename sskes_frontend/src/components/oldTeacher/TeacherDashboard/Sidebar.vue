<template>
    <nav id="sidebar">
        <div class="sidebar-header">
            <h3>SSKES</h3>
            <strong>SSKES</strong>
        </div>

        <ul class="list-unstyled components">
            <li class="active">
                <!-- <a href="#homesubmenu" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-house-door-fill"></i>
                    Home
                </a> -->
                <router-link to="/TeacherDashboard" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-house-door-fill"></i>
                    Home
                </router-link>
            </li>
            <li class="active">
                <!-- <a href="#homesubmenu" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-bookmark-fill"></i>
                    Courses
                </a> -->
                <router-link to="/AllCourse" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-bookmark-fill"></i>
                    Courses
                </router-link>
            </li>
            <li class="active">
                <!-- <a href="#homesubmenu" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-plus-fill"></i>
                    Add Student
                </a> -->
                <router-link to="/TeacherAddCourse" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-plus-fill"></i>
                    Add Course
                </router-link>
            </li>
            <li class="active">
                <!-- <a href="#homesubmenu" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-clipboard-data-fill"></i>
                    Progress
                </a> -->
                <router-link to="/Course-Progress" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-clipboard-data-fill"></i>
                    Progress
                </router-link>
            </li>
            <li class="active">
                <!-- <a href="#homesubmenu" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-square"></i>
                    Account
                </a> -->
                <router-link to="/Teacher-Profile" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-person-square"></i>
                    Account
                </router-link>
            </li>
        </ul>

        <ul class="list-unstyled CTAs">
            <li>
                <a @click="logout" data-toggle="collapse" aria-expanded="false">
                    <i class="bi bi-box-arrow-right ms-2"></i>
                    Sign Out
                </a>
<!--                <router-link to="/login" class="active text-center">Sign Out<i class="bi bi-box-arrow-right ms-2"></i></router-link>-->
            </li>
        </ul>
    </nav>
</template>

<script>

    export default {
        name : 'TeacherSidebar',

      methods:{
      logout(){
      window.localStorage.clear();
      this.$router.push('/login')
    }
}
        
    };

    
</script>

<style lang="scss" scoped>
p {
    font-family: 'Poppins', sans-serif;
    font-size: 1.1em;
    font-weight: 300;
    line-height: 1.7em;
    color: #999;
}

a, a:hover, a:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}
router-link, router-link:hover, router-link:focus {
    color: inherit;
    text-decoration: none;
    transition: all 0.3s;
}

.navbar {
    padding: 15px 10px;
    background: #fff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    border: none;
    border-radius: 0;
    margin-bottom: 40px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}

.navbar-btn {
    box-shadow: none;
    outline: none !important;
    border: none;
}

.line {
    width: 100%;
    height: 1px;
    border-bottom: 1px dashed #ddd;
    margin: 40px 0;
}

i, span {
    display: inline-block;
}

/* ---------------------------------------------------
    SIDEBAR STYLE
----------------------------------------------------- */
.wrapper {
    display: flex;
    align-items: stretch;
}

#sidebar {
    min-width: 250px;
    max-width: 250px;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #fff;
    transition: all 0.3s;
}

#sidebar.active {
    min-width: 80px;
    max-width: 80px;
    text-align: center;
}

#sidebar.active .sidebar-header h3{
    display: none;
}

#sidebar.active .sidebar-header strong {
    display: block;
}

#sidebar ul li a {
    text-align: left;
}
#sidebar ul li router-link {
    text-align: left;
}

#sidebar.active ul li a {
    padding: 20px 10px;
    text-align: center;
    font-size: 0.85em;
}
#sidebar.active ul li router-link {
    padding: 20px 10px;
    text-align: center;
    font-size: 0.85em;
}

#sidebar.active ul li a i {
    margin-right:  0;
    display: block;
    font-size: 1.8em;
    margin-bottom: 5px;
}

#sidebar.active ul li router-link i {
    margin-right:  0;
    display: block;
    font-size: 1.8em;
    margin-bottom: 5px;
}

#sidebar.active ul ul a {
    padding: 10px !important;
}
#sidebar.active ul ul router-link {
    padding: 10px !important;
}

#sidebar.active a[aria-expanded="false"]::before, #sidebar.active a[aria-expanded="true"]::before {
    top: auto;
    bottom: 5px;
    right: 50%;
    -webkit-transform: translateX(50%);
    -ms-transform: translateX(50%);
    transform: translateX(50%);
}
#sidebar.active router-link[aria-expanded="false"]::before, #sidebar.active router-link[aria-expanded="true"]::before {
    top: auto;
    bottom: 5px;
    right: 50%;
    -webkit-transform: translateX(50%);
    -ms-transform: translateX(50%);
    transform: translateX(50%);
}

#sidebar .sidebar-header {
    padding: 20px;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

#sidebar .sidebar-header strong {
    display: none;
    font-size: 1.8em;
}

#sidebar ul.components {
    padding: 20px 0;
    border-bottom: 1px solid #00d2ff;
}

#sidebar ul li a {
    padding: 20px;
    font-size: 1.2em;
    display: block;
}
#sidebar ul li router-link {
    padding: 20px;
    font-size: 1.2em;
    display: block;
}

#sidebar ul li a:hover {
    color: #00d2ff;
    background: #ffffff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
#sidebar ul li router-link:hover {
    color: #00d2ff;
    background: #ffffff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

#sidebar ul li a i {
    margin-right: 10px;
}
#sidebar ul li router-link i {
    margin-right: 10px;
}

#sidebar ul li.active > a, a[aria-expanded="true"] {
    color: #fff;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
#sidebar ul li.active > router-link, router-link[aria-expanded="true"] {
    color: #fff;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}


a[data-toggle="collapse"] {
    position: relative;
}

/* a[aria-expanded="false"]::before, a[aria-expanded="true"]::before {
    content: '\e259';
    display: block;
    position: absolute;
    right: 20px;
    font-family: 'Glyphicons Halflings';
    font-size: 0.6em;
}
a[aria-expanded="true"]::before {
    content: '\e260';
} */


ul ul a {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
ul ul router-link {
    font-size: 0.9em !important;
    padding-left: 30px !important;
    background: #00d2ff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

ul.CTAs {
    padding: 20px;
}

ul.CTAs a {
    text-align: center;
    font-size: 0.9em !important;
    display: block;
    border-radius: 5px;
    margin-bottom: 5px;
}
ul.CTAs router-link {
    text-align: center;
    font-size: 0.9em !important;
    display: block;
    border-radius: 5px;
    margin-bottom: 5px;
}

a.download {
    background: #fff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #00d2ff;
}
router-link.download {
    background: #fff;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #00d2ff;
}

a.article, a.article:hover {
    background: #00d2ff !important;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #fff !important;
}
router-link.article, a.article:hover {
    background: #00d2ff !important;
    background: -webkit-linear-gradient(to right, #3a7bd5, #00d2ff);  /* Chrome 10-25, Safari 5.1-6 */
background: linear-gradient(to right, #3a7bd5, #00d2ff); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
    color: #fff !important;
}

@media (max-width: 768px) {
    #sidebar {
        min-width: 80px;
        max-width: 80px;
        text-align: center;
        margin-left: -80px !important ;
    }
    a[aria-expanded="false"]::before, a[aria-expanded="true"]::before {
        top: auto;
        bottom: 5px;
        right: 50%;
        -webkit-transform: translateX(50%);
        -ms-transform: translateX(50%);
        transform: translateX(50%);
    }
    #sidebar.active {
        margin-left: 0 !important;
    }

    /* #sidebar .sidebar-header h3 {
        display: none;
    } */

    #sidebar .sidebar-header strong {
        display: block;
    }

    #sidebar ul li a {
        padding: 20px 10px;
    }

    #sidebar ul li a span {
        font-size: 0.85em;
    }
    #sidebar ul li a i {
        margin-right:  0;
        display: block;
    }

    #sidebar ul ul a {
        padding: 10px !important;
    }

    #sidebar ul li a i {
        font-size: 1.3em;
    }
    #sidebar {
        margin-left: 0;
    }
    #sidebarCollapse span {
        display: none;
    }
}
</style>