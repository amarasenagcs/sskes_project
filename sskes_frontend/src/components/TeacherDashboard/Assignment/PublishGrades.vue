<template>
    <div class="card py-2">
        <div class="card-body">
            <h5 class="sinhala-font">සිසුවාගේ නම</h5>
            <p class="sinhala-font mb-5">{ Student Email }</p>

            <p class="sinhala-font">ආදරණීය ගුරුතුමණි, ඔබගේ සිසුවා සම්පූර්ණ කරන ලද පාඨමාළාවේ තිබෙන නිපුණතාවයට අදාළව සිසුවා විසින් සකස්කරනලද පිළිතුර මෙහි තිබෙන බැවින් එය බෑගත කිරීමෙන් පිළිතුරු නිරාවද්‍යතාවය තහවුරු කරගතහැක.</p>
            <a href="my.pdf" class="nav-link text-success" download><p class="sinhala-font fw-bold mb-5 text-center"><i class="bi bi-arrow-down-square-fill me-1"></i>පිළිතුර බාගත කරගන්න </p></a>
            <div class="row">
                <div class="col-6">
                    <div class="mb-3">
                        <label for="result" class="form-label sinhala-font">කරුණාකර සිසුවාගේ පිළිතුරට අදාළ ලකුණු සදහන්කරන්න</label>
                        <input type="text" id="result" class="form-control sinhala-font">
                        <button class="btn btn-primary text-light mt-2">ලකුණු ලබාදෙන්න</button>
                    </div>
                </div>
                <div class="col-6">
                    <label class="form-label float-end sinhala-font">මෙම පාඨමාළාවට අදාළව සිසුවාගේ ලකුණු සාමාර්තය</label>
                    <label class="form-label float-end sinhala-font"><i class="bi bi-patch-check-fill text-success me-2"></i>ප්‍රතිඵලය : <span>65%</span></label>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>
    export default {
        name: 'PlublishingGrades'
    }
</script>

<style lang="scss" scoped>

</style>