<template>
    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-7">
                    <h5 class="sinhala-font">සිසුවාගේ නම</h5>
                    <p class="sinhala-font">{ Student Email }</p>
                    <p class="sinhala-font">පාඨමාළාවේ නම</p>
                </div>
                <div class="col-5">
                    <h5 class="sinhala-font mb-4">සිසුවාට ප්‍රතිඵලය ලබාදෙන්න</h5>
                    <router-link to="/publish-grade" class="sinhala-font nav-link text-danger fw-bold mb-2">පිවිසෙන්න</router-link>
                    <span class="badge text-bg-success p-2">Graded</span>
                    <span class="badge text-bg-warning p-2">Pending Grade</span>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default {
        name : 'completedStudents'
    }
</script>

<style lang="scss" scoped>
.card{
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.2);
}
.card:hover{
    transform: scale(1.07);
    box-shadow: 5px 10px 10px rgba(0, 0, 0, 0.4);
}
</style>