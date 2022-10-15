<template>
    <div class="card">
            <div class="card-body">
                <h4 class="card-title sinhala-font fw-bold">{{ header }}</h4>
                <p class="card-text sinhala-font text-dark fw-bold">{{ text }}</p>
            </div>
        </div>
</template>

<script>
    export default {
        name : 'ParentDashCard',
        props: {
            header : String,
            text : String,
        }
    }
</script>

<style scoped>

</style>