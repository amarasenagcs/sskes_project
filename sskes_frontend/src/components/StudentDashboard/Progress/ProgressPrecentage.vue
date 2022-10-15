<template>
    <div class="card shadow">
        <div class="card-body">
            <h5 class="sinhala-font mb-5">පාඨමාළාවේ නම : {සිංහල}</h5>
            <label for="pendingpresentage" class="form-label sinhala-font">කරමින් පවතින</label>
            <div class="progress mb-3" style="height: 20px;">
                <div class="progress-bar" role="progressbar" aria-label="Example 20px high" style="width: 65%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            
            <label for="finishedpresentage" class="form-label sinhala-font">අවසන් කරනලද</label>
            <div class="progress" style="height: 20px;">
                <div class="progress-bar bg-success" role="progressbar" aria-label="Example 20px high" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name : 'ProgressCard'
    }
</script>

<style lang="scss" scoped>

</style>