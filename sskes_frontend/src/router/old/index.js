import { createRouter, createWebHistory } from 'vue-router'
import login from '../views/login.vue'
// import Home from '../views/Home.vue'
// import HomeDashboard from '../views/Home/Home.vue'
import About from '../views/About.vue'
import signUp from '../views/signUp.vue'
import ForgetPassword from '../views/forgetPassword'
import NewPassword from '../views/NewPassword'
import ParentDashboard from '../views/ParentDashboard/Dashboard'
// import TeacherDashboard from '../views/teacher/teacher-dashboard.vue'
import teacherCourceManage from '../views/teacher/teacher-cource-manage.vue'
import teacherAddCource from '../views/teacher/teacher-add-course.vue'
import teacherViewCource from '../views/teacher/teacher-view-cources.vue'
import teacherRegistration from '../views/auth-register-as-teacher.vue'
import studentDashboard from '../views/student/student-dashboard.vue'
import otpValidate from "../views/otp-validate.vue";
//import TeacherDashboard from '../components/Sidebar.vue'
import store from '../store'
import TeacherDashboard from '../views/TeacherDashboard/Dashboard'
import TeacherAddCourse from '../views/TeacherDashboard/AddCourse'
import AllCourse from '../views/TeacherDashboard/AllCourses'
import AllStudents from '../views/TeacherDashboard/AllStudents'
import StuProgress from '../views/TeacherDashboard/StuProgress'
import CourProgress from '../views/TeacherDashboard/CourProgress'
import TeacherProfile from '../views/TeacherDashboard/Profile'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: login
  },
  // {
  //   path: '/',
  //   name: 'HomeDashboard',
  //   component: HomeDashboard
  // },
  {
    path: '/signUp',
    name: 'signUp',
    component: signUp
  },
  {
    path: '/forgetPassword',
    name: 'ForgetPassword',
    component: ForgetPassword
  },
  {
    path: '/NewPassword',
    name: 'NewPassword',
    component: NewPassword
  },
  {
    path: '/parent-dashboard',
    name: 'parent-dashboard',
    component: ParentDashboard
  },
  // {
  //   path: '/teacher-dashboard',
  //   name: 'teacher-dashboard',
  //   component: TeacherDashboard
  // },
  
  {
    path: '/TeacherDashboard',
    name: 'TeacherDashboard',
    component: TeacherDashboard
  },
  {
    path: '/AllCourse',
    name: 'AllCourse',
    component: AllCourse
  },
  {
    path: '/TeacherAddCourse',
    name: 'TeacherAddCourse',
    component: TeacherAddCourse
  },
  {
    path: '/AllStudents',
    name: 'AllStudents',
    component: AllStudents
  },
  {
    path: '/Student-Progress',
    name: 'StuProgress',
    component: StuProgress
  },
  {
    path: '/Course-Progress',
    name: 'CourProgress',
    component: CourProgress
  },
  {
    path: '/Teacher-Profile',
    name: 'Profile',
    component: TeacherProfile
  },
  {
    path: '/otp-validate',
    name: 'otp-validate',
    component: otpValidate
  },
  {
    path: '/teacher-course-manage',
    name: 'teacherCourseManage',
    component: teacherCourceManage
  },
  {
    path: '/teacher-add-course',
    name: 'teacherAddCourse',
    component: teacherAddCource
  },
  {
    path: '/teacher-view-courses',
    name: 'teacherViewCourse',
    component: teacherViewCource
  },
  {
    path: '/auth-register-as-teacher',
    name: 'teacherRegistration',
    component: teacherRegistration
  },
  {
    path: '/student-dashboard',
    name: 'student-dashboard',
    component: studentDashboard
  },
  {
    path: '/about',
    name: 'About',
    component: About,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) =>{
  if(to.matched.some(record=>record.meta.requireLogin) && !store.state.isAuthenticated){
    next('/login')
  }else{
    next()
  }
})

export default router
