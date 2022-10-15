<template>
  <div class="card">
    <div class="card-body">
      <h3 class="card-title text-center pb-3">Add Course</h3>
      <div class="alert alert-success sinhala-font alert-dismissible fade show " role="alert">
          <strong>බොහොම ස්තූතියි !..</strong> ඔබගේ පාඨමාළාව දැන් ප්‍රකාශයට පත්කර ඇත.
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      <form @submit.prevent="submitForm">
        <div class="col-md-12">
          <div class="mb-3">
            <label for="name" class="form-label sinhala-font">පාඨමාළාවේ නම</label>
            <input type="text" name="name" id="name" v-model="title" class="form-control sinhala-font">
          </div>
        </div>
        <div class="col-md-12">
          <div class="mb-3">
            <label for="description" class="form-label sinhala-font">පාඨමාළාවේ අන්තර්ගතය පිළිබද කෙටි විස්තරයක්</label>
            <textarea type="text" name="description" id="description" v-model="short_description" class="form-control sinhala-font"/>
          </div>
        </div>
        <div class="col-md-12">
          <div class="mb-3">
            <label for="name" class="form-label sinhala-font">ඉගෙනුම ලබන වසර සදහා</label>
            <select name="selectGrade" id="CourseGrade" class="form-select form-select-lg sinhala-font bg-light float-start mb-3" v-model="grade" aria-label=".form-select-lg ">
              <option selected>අදාල වසර තෝරන්න</option>
              <option value="grade">පෙර පාසල්</option>
              <option value="1grade">1 වසර</option>
              <option value="2grade">2 වසර</option>
              <option value="3grade">3 වසර</option>
              <option value="4grade">4 වසර</option>
              <option value="5grade">5 වසර</option>
              <option value="6grade">6 වසර</option>
              <option value="7grade">7 වසර</option>
              <option value="8grade">8 වසර</option>
              <option value="9grade">9 වසර</option>
              <option value="10grade">10 වසර</option>
              <option value="11grade">11 වසර</option>
              <option value="12grade">12 වසර</option>
            </select>
          </div>
        </div>
        <div class="col-md-12">
          <div class="col-md-12">
<!--            <div class="mb-3">-->
                <label for="Image" ref="file" class="form-label sinhala-font">image Upload</label>
                <input class="form-control" type="file" id="formFile"   @change="preview">
                <button v-on:click="clearImage()" class="btn btn-danger mt-3">Clear Image</button>
<!--            </div>-->
            <img id="frame" src="" alt="" class="img-fluid" />
        </div>
        </div>
        <div class="col-md-12">
          <div class="mt-3 text-center sinhala-font">
            <button type="submit" class="btn btn-primary my-3">පාඨමාළාව පළ කරන්න</button>
          </div>
        </div>
      </form>      
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name : 'AddCourse',
  data(){
      return{
          title:'',
          grade:'',
          // image:'',
          short_description:'',
          errors:[]
      }
  },
  methods:{
    preview(event) {

                // this.image = this.$refs.file.files.item(0);
                console.log(event.target.files[0].name)
                this.selectedFile = event.target.files[0]

            },
        clearImage() {
                document.getElementById('formFile').value = null;
                //frame.src = "";
            },

    submitForm(){

      console.log('submit testing form')
      this.errors = []
        //console.log(this.username)
        if(!this.errors.length){
            const formData = {
                title: this.title,
                grade: this.grade,
                // image: this.image,
                // teacher: localStorage.getItem('userId'),
                short_description: this.short_description,
                // is_teacher: this.is_teacher,
                // is_parent: this.is_parent,
                // is_student: this.is_student,
            }
           // const form = new formData;
          //  console.log(formData)
          //  formData.is_student = this.is_student;
            ///form.set('is_student',true)
           let accessToken = localStorage.getItem('accessToken')
            axios
                .post('api/v1/courseRegister/', formData, { headers: { Authorization: `Bearer ${accessToken}` } })
                .then(response =>{
                    console.log(response.data)
                   // this.response = response.data
                   // this.response = response.data



                    alert('Course Register successfully!')


                    //window.location.href ='./index.php';

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
        },

  }
}
</script>

<style scoped>
#CourseGrade.sinhala-font{
  font-size: medium;
}
</style>

