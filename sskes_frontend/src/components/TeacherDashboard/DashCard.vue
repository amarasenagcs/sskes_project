<template>
    <!-- <div class="col-md-6 p-3"> -->
        <div class="card">
            <div class="card-body">
                <h4 class="card-title sinhala-font fw-bold">{{ title }}</h4>
                <p class="card-text sinhala-font text-dark fw-bold">{{ body }}</p>
            </div>
        </div>
    <!-- </div> -->
</template>

<script>
    export default {
        name : 'DashCards',
        props:{
            title : String,
            body : String,
        }
    }
</script>

<style lang="scss" scoped>

</style>