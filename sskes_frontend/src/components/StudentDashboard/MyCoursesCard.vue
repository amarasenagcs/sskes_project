<template>  
    <div class="card completeCard">
        <div class="card-body d-flex sinhala-font justify-content-center align-items-center">
            <div class="col-md-9">
                <h4>විෂය : {{subject}}</h4>
                <h6 id="subject-grade">වසර : {{grade}}</h6>
                <p class="fw-bold">විෂයන් පිළිබද කෙටි විස්තරයක් මෙම ස්තානයෙ දැකබලාගත් හැක..එහි ඇත්තේ අදාළ පාඨමාලාව පිළිබද හැදින්වීමකි.. එයින් අදාල ශිෂ්‍යාට සරිලන විෂය පාඨමාලාව සදහා සම්බන්ද විය හැක.</p>
            </div>
            <div class="col-md-3">
                <button type="button" class="btn btn-primary float-end" id="enrollCourse">ලියාපදිංචි කරන්න</button>
                <router-link to="/content-view">ලියාපදිංචි කරන්න</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name : 'MyCoursesCard',
        props:{
            grade : String,
            subject : String,
        }
        
    }
</script>

<style scoped src="../../assets/css/student/main.css">

</style>