<template>
    <div class="card shadow p-3 mb-5 border-0">
        <div class="card-body">
            <h3 class="card-title text-center pb-3">
                මාගේ ගිණුම
            </h3>
<!--            <div class="alert alert-success alert-dismissible fade show" role="alert">-->
<!--                <strong>Nice activity!</strong> You have successfully update account.-->
<!--                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>-->
<!--            </div>-->
            <form method="post">
                <div class="col-md-12">
                    <div class="mb-3">
                        <label for="fname" class="form-label">මුල් නම</label>
                        <input type="text" name="fname" id="fname" class="form-control" :value="userDetails.first_name" readonly/>
                    </div>
                </div>
                <div class="col-md-12">
                    <div class="mb-3">
                        <label for="lname" class="form-label">අවසාන නම</label>
                        <input type="text" name="lname" id="lname" :value="userDetails.last_name" readonly class="form-control"/>
                    </div>
                </div>
                <div class="col-md-12">
                    <div class="mb-3">
                        <label for="email" class="form-label">විද්‍යුත් තැපැල් ලිපිනය</label>
                        <input type="text" name="email" id="email" :value="userDetails.email" readonly class="form-control"/>
                    </div>
                </div>
<!--                <div class="col-md-12">-->
<!--                    <div class="mb-3">-->
<!--                        <label for="courses" class="form-label">Courses</label>-->
<!--                        <textarea name="course" id="course" cols="30" rows="4" class="form-control" ></textarea>-->
<!--                    </div>-->
<!--                </div>-->
                <div class="col-md-12">
                    <div class="mb-3 pt-3">
                        <button type="submit" name="update" id="update" class="btn btn-primary float-end">exit</button>
                    </div>
                </div> 
            </form>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name : 'ProfileForm',
        data(){
        return{
          userDetails:[]
        }
      },
        mounted(){
        console.log('mounted')
        // console.log(this.$route.query.courseId)
        let url = 'api/v1/getCurrentUser/';
        let accessToken = localStorage.getItem('accessToken')
        axios
            .get(url, { headers: { Authorization: `Bearer ${accessToken}` } })
            .then(response => {
              console.log(response.data)
              this.userDetails = response.data.userInfo
            })
      }
    }
</script>

<style lang="scss" scoped>

</style>