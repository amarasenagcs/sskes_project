import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

//   -------------------------  Home Routers  ---------------------------
import HomeDashboard from '../views/LandingPage/Home.vue'
import login from '../views/login.vue'
import signUp from '../views/signUp.vue'
import ForgetPassword from '../views/forgetPassword'
import NewPassword from '../views/NewPassword'

//     Parent Routers
import ParentDashboard from '../views/ParentDashboard/Dashboard'
import Courses from '../views/ParentDashboard/Courses'
import AddStudent from '../views/ParentDashboard/AddStudent'
import StudentList from '../views/ParentDashboard/StudentList'
import ParentCourseContentView from '../views/ParentDashboard/CourseContent'
import StudentCourses from '../views/ParentDashboard/StudentCourses'
import ParentProfile from '../views/ParentDashboard/Profile'

//     Teacher Routers
import TeacherDashboard from '../views/TeacherDashboard/Dashboard'
import TeacherAddCourse from '../views/TeacherDashboard/AddCourse'
import AllCourse from '../views/TeacherDashboard/AllCourses'
import AllStudents from '../views/TeacherDashboard/AllStudents'
import StuProgress from '../views/TeacherDashboard/StuProgress'
import CourProgress from '../views/TeacherDashboard/CourProgress'
import TeacherProfile from '../views/TeacherDashboard/Profile'
import AddLessons from '../views/TeacherDashboard/AddLesson'
import ViewLessons from '../views/TeacherDashboard/ViewLesson'
import PublishAssesmentGrades from '../views/TeacherDashboard/Assignments/PublishGrade'
import AssignmentStudents from '../views/TeacherDashboard/Assignments/AssStudents'

//     Student Routers
import StudentDashboard from '../views/StudentDashboard/Dashboard'
import MyCourses from '../views/StudentDashboard/MyCourses'
import MyProgress from '../views/StudentDashboard/MyProgress'
import StudentProfile from '../views/StudentDashboard/Profile'
import CompletedCourse from '../views/StudentDashboard/CompletedCourse'
import PendingCourses from '../views/StudentDashboard/PendingCourse'
import SubjectView from '../views/StudentDashboard/SubjectView'
import StudyMode from '../views/StudentDashboard/StudyMode'
import CourseContentView from '../views/StudentDashboard/CourseContent'


const routes = [
  
  {
    path: '/',
    name: 'HomeDashboard',
    component: HomeDashboard
  },
  {
    path: '/login',
    name: 'login',
    component: login
  },  
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
    path: '/api/password_reset/',
    name: 'NewPassword',
    component: NewPassword
  },

  //   -------------------------  Parent Routers  ---------------------------
  {
    path: '/parent-dashboard',
    name: 'parent-dashboard',
    component: ParentDashboard
  },
  {
    path: '/courses-section',
    name: 'courses-section',
    component: Courses
  },
  {
    path: '/add-students',
    name: 'add-students',
    component: AddStudent
  },
  {
    path: '/students-list',
    name: 'Student-List',
    component: StudentList
  },
  {
    path: '/course-content-view',
    name: 'Course-Content-View',
    component: ParentCourseContentView
  },
  {
    path: '/my-child-courses',
    name: 'My-Child-Courses',
    component: StudentCourses
  },
  {
    path: '/parent-profile',
    name: 'My-Profile',
    component: ParentProfile
  },

  //   -------------------------  Teacher Routers  ---------------------------
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
    path: '/Add-Lesson',
    name: 'AddLesson',
    component: AddLessons
  },
  {
    path: '/View-Lessons',
    name: 'ViewLessonDetails',
    component: ViewLessons
  },
  {
    path: '/publish-grade',
    name: 'Publish-Assesment-Grade',
    component: PublishAssesmentGrades
  },
  {
    path: '/assignment-complete-student',
    name: 'Assignment-Complete-Student',
    component: AssignmentStudents
  },

  //   -------------------------  Student Routers  ---------------------------
  {
    path: '/student-dashboard',
    name: 'student-dashboard',
    component: StudentDashboard
  },
  {
    path: '/content-view',
    name: 'Course Content View',
    component: CourseContentView
  },
  {
    path: '/my-courses',
    name: 'My-Courses',
    component: MyCourses
  },
  {
    path: '/student-profile',
    name: 'student-profile',
    component: StudentProfile
  },
  {
    path: '/my-progress',
    name: 'My-Progress',
    component: MyProgress
  },
  {
    path: '/completed-course',
    name: 'Completed-Course',
    component: CompletedCourse
  },
  {
    path: '/pending-course',
    name: 'pending-Course',
    component: PendingCourses
  },
  {
    path: '/my-subject',
    name: 'my-subject',
    component: SubjectView
  },
  {
    path: '/study-mode',
    name: 'StudyMode',
    component: StudyMode
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
