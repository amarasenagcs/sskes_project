<template>
    <div class="card d-flex">
            <div class="card-body">
                <h4 class="card-title sinhala-font fw-bold">{{ subject }}</h4>
                <p class="card-text sinhala-font text-dark fw-bold">{{ text }}</p>
            </div>
        </div>
</template>

<script>
    export default {
        name : 'CompletedCourse',
        props: {
            subject : String,
            text : String,
        }
    }
</script>

<style scoped>

</style>