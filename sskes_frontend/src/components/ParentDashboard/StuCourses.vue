<template>
    <div class="card">
            <div class="card-body">
                <h4 class="card-title sinhala-font fw-bold">{{ header }}</h4>
                <p class="card-text sinhala-font text-dark fw-bold">{{ text }}</p>
                <span class="card-text text-dark text-muted float-end">{{ stuEmail }}</span>
            </div>
        </div>
</template>

<script>
    export default {
        name : 'StuCourses',
        props: {
            header : String,
            text : String,
            stuEmail : String,
        }
    }
</script>

<style scoped>

</style>