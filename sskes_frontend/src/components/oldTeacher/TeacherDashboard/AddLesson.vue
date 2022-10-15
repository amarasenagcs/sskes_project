<template>
    <div class="card">
    <div class="card-body">
      <h3 class="card-title text-center sinhala-font pb-3">පාඩම ඇතුලත්කරන්න</h3>
      <div class="alert alert-success sinhala-font alert-dismissible fade show " role="alert">
          <strong>බොහොම ස්තූතියි !..</strong> ඔබ පාඩම සාර්ථකව ඇතුලත්ක්‍රන ලදි.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      <form method="POST">
        <div class="col-md-12">
          <div class="mb-3">
            <label for="lesson" class="form-label sinhala-font">විෂය මතෘකාව</label>
            <input type="text" name="lesson" id="lesson" class="form-control sinhala-font">
          </div>
        </div>
        <!-- <div class="col-md-12">
          <div class="mb-3">
            <label for="name" class="form-label sinhala-font">පාඨමාළාව තෝරන්න</label>
            <select name="selectSubject" id="selectSubject" class="form-select form-select-lg sinhala-font bg-light float-start mb-3" aria-label=".form-select-lg ">
              <option selected>පාඨමාළාව තෝරන්න</option>
              <option value="courseName">සිංහල</option>
              <option value="courseName">ගණිතය</option>
              <option value="courseName">ඉතිහාසය</option>
              <option value="courseName">විද්‍යාව</option>
            </select>
          </div>
        </div> -->
        <div class="col-md-12">
          <div class="mb-3">
            <label for="name" class="form-label sinhala-font">අන්තර්ගතය ඇතුලත්කරන්න</label>
            <input type="text" name="name" id="name" class="form-control sinhala-font">
          </div>
        </div>
        <div class="col-md-12">
          <div class="mb-3">
            <label for="uploadVideo" class="form-label sinhala-font">ඔබගේ වීඩියෝව ඇතුලත් කරන්න</label>
            <input type="file" name="uploadVideo" id="uploadVideo" class="form-control sinhala-font">
          </div>
        </div>        
        <div class="col-md-12">
          <div class="mt-3 text-center sinhala-font">
            <button type="submit" class="btn btn-success my-3">පාඩම පළ කරන්න</button>
          </div>
        </div>
      </form>      
    </div>
  </div>
</template>

<script>
    export default {
        name : 'AddLesson',
    }
</script>

<style lang="scss" scoped>
#selectSubject.sinhala-font{
  font-size: medium;
}
</style>