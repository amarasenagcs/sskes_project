<template>
    <div class="card">
    <div class="card-body">
      <h3 class="card-title text-center sinhala-font pb-3">පාඩම ඇතුලත්කරන්න</h3>
      <div v-if="success.length" class="alert alert-success sinhala-font alert-dismissible fade show " role="alert">
          <strong>බොහොම ස්තූතියි !..</strong> ඔබ පාඩම සාර්ථකව ඇතුලත් කරන ලදී.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      <form @submit.prevent="submitForm" enctype=“multipart/form-data”>
<!--        <div class="col-md-12">-->
<!--          <div class="mb-4">-->
<!--            <label for="name" class="form-label sinhala-font">ඉගෙනුම ලබන වසර සදහා</label>-->
<!--            <select name="selectGrade" id="CourseGrade" class="form-select form-select-lg sinhala-font bg-light float-start mb-4" aria-label=".form-select-lg ">-->
<!--              <option selected>අදාල වසර තෝරන්න</option>-->
<!--              <option value="grade">පෙර පාසල්</option>-->
<!--              <option value="1grade">  1 වසර</option>-->
<!--              <option value="2grade">  2 වසර</option>-->
<!--              <option value="3grade">  3 වසර</option>-->
<!--              <option value="4grade">  4 වසර</option>-->
<!--              <option value="5grade">  5 වසර</option>-->
<!--              <option value="6grade">  6 වසර</option>-->
<!--              <option value="7grade">  7 වසර</option>-->
<!--              <option value="8grade">  8 වසර</option>-->
<!--              <option value="9grade">  9 වසර</option>-->
<!--              <option value="10grade">10 වසර</option>-->
<!--              <option value="11grade">11 වසර</option>-->
<!--              <option value="12grade">12 වසර</option>-->
<!--            </select>-->
<!--          </div>-->
<!--        </div>-->
        <div class="col-md-12">
          <div class="mb-4">
            <label for="name" class="form-label sinhala-font">පාඨමාළාව තෝරන්න</label>
            <select v-model="course" name="selectSubject" id="selectSubject" class="form-select form-select-lg sinhala-font bg-light float-start mb-4" aria-label=".form-select-lg " required>
              <option disabled value="">පාඨමාළාව තෝරන්න</option>
              <option  v-for="course in courses"
                    v-bind:key="course.id" v-bind:value="course.id" >{{ course.title }}</option>
<!--              <option value="courseName">ගණිතය</option>-->
<!--              <option value="courseName">ඉතිහාසය</option>-->
<!--              <option value="courseName">විද්‍යාව</option>-->
            </select>
          </div>
        </div>
        <div class="col-md-12">
          <div class="mb-4">
            <label for="lesson" class="form-label sinhala-font">විෂය මතෘකාව</label>
            <input type="text" name="lesson" v-model="lesson_name" id="lesson" class="form-control sinhala-font" required>
          </div>
        </div>        
        <div class="col-md-12">
          <div class="mb-4">
            <label for="name" class="form-label sinhala-font">අන්තර්ගතය ඇතුලත්කරන්න</label>
            <textarea type="text" name="name" id="name" v-model="content_description" class="form-control sinhala-font" required> </textarea>
          </div>
        </div>
        <div class="col-md-12">
          <div class="mb-4">
            <label for="name" class="form-label sinhala-font">අන්තර්ගත කරනු ලබන මාධ්‍ය තෝරන්න</label>
            <select  name="selectSubjectType" v-model="content_type" @change="selectOption" id="selectSubjectType" class="form-select form-select-lg sinhala-font bg-light float-start mb-4" aria-label=".form-select-lg " required>
<!--              <option disabled value="" selected>පාඨමාළාව තෝරන්න</option>-->
              <option value="video">වීඩියෝව</option>
              <option value="assignment">අභ්‍යාසය</option>
<!--              <option value="courseName">විද්‍යාව</option>-->
            </select>
          </div>
        </div>
        <div class="col-md-12" v-if="optionSelected=='video'">
          <div class="mb-4">
            <label for="uploadVideo" class="form-label sinhala-font">ඔබගේ වීඩියෝව ඇතුලත් කරන්න</label>
            <input type="file" name="uploadVideo" accept="video/mp4,video/x-m4v,video/video.mkv" id="uploadVideo" @change="preview" class="form-control sinhala-font" required>
          </div>
        </div>
        <div class="col-md-12" v-if="optionSelected=='assignment'">
          <div class="mb-4">
            <label for="uploadVideo" class="form-label sinhala-font">ඔබගේ අභ්‍යාසය ඇතුලත් කරන්න</label>
            <input type="file" name="uploadVideo" accept="application/pdf" id="uploadVideo" @change="preview" class="form-control sinhala-font" required>
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
    import axios from "axios";

    export default {
        name : 'AddLesson',
        data(){
        return{
          courses:[],
          errors: [],
          success: [],
          form:{
            course:'',
            lesson_name:'',
            content_description:'',
            content_type:'',

          },
          selectedFile: '',
          optionSelected:''
        }
      },
      mounted(){
        console.log('mounted')
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get('/api/v1/getCourses/', { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.courses = response.data
            })
      },
      methods:{
          preview(event) {

                // this.image = this.$refs.file.files.item(0);
                console.log(event.target.files[0].name)
                this.selectedFile = event.target.files[0]

            },
            selectOption(event) {
                    // alert(this.content_type)
                // this.image = this.$refs.file.files.item(0);
                // console.log(event.target.files[0].name)
                // this.selectedFile = event.target.files[0]
                    this.optionSelected = this.content_type


            },
        // clearFile() {
        //         document.getElementById('formFile').value = null;
        //         //frame.src = "";
        //     },
        submitForm(){
        console.log('submit testing form')
        this.errors = []
        //console.log(this.username)
        if(!this.errors.length){
             console.log(this.course)
            // let course = options[selectedIndex].id
            const fd = new FormData();
            fd.append('content', this.selectedFile, this.selectedFile.name)
            fd.append('content_description', this.content_description)
            fd.append('course', this.course)
            fd.append('lesson_name', this.lesson_name)
            fd.append('content_type', this.content_type)
            console.log(this.content_type)

            // formData.append('image', this.selectedFile, this.selectedFile.name)
            // console.log(fd)

           let accessToken = localStorage.getItem('accessToken')
            axios
                .post('api/v1/lessonRegister/', fd, { headers: { "Content-Type": "multipart/form-data", Authorization: `Bearer ${accessToken}` } })
                .then(response =>{
                    console.log(response.data)
                    alert('Lesson Register successfully!')
                    this.success.push('Lesson Register successfully!')
                    window.location.href ='/Add-Lesson';

                })
                .catch(error =>{
                    if(error.response){
                        for(const property in error.response.data){
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    }else if(error.message){
                        this.errors.push('Something went wrong. Please try again!')
                    }
                })
        }
        }
      }
    }
</script>

<style lang="scss" scoped>
  #selectSubject.sinhala-font, #CourseGrade.sinhala-font{
    font-size: medium;
  }
</style>