<template>
    <div class="col-md-4 p-3" v-for="item in products" :key="item.title">
        <div class="card">
            <div class="card-body">
                <div class="card-title text-center sinhala-font">
                    <h3>{{item.title}}hello</h3>
                    <img :src="item.src" class="img-fluid" alt=""/>
                    <!-- <router-link :to="item.path">view</router-link> -->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name : 'Dashboard-Cards',
        // props : ['product']
        data(){
            return{
                products: [
                {
                        title : 'පාඨමාලාවන්',
                        src : require('../../assets//images/teacher/courses2.svg'),
                        // path : '/TeacherAddCourse'
                    },
                    {
                        title : 'පාඨමාලාවන් ඇතුල්කිර්‍රීම',
                        src : require('../../assets//images/teacher/addCourse2.svg')
                    },
                    {
                        title : 'ලියාපදිංචි සිසුන්',
                        src : require('../../assets//images/teacher/changeCourse.svg')
                    },
                    {
                        title : 'සිසුන්ගේ කාර්‍යසාදනය',
                        src : require('../../assets//images/teacher/course_performence.png')
                    },
                    {
                        title : 'පාඨමාලා කාර්‍යසාදනය',
                        src : require('../../assets//images/teacher/performence.png')
                    },
                ]
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>