<template>
    <!-- <div class="col-md-10 mx-auto"> -->
        <div class="card shadow p-3 mb-5 border-0">
            <div class="card-body">
                <h3 class="card-title text-center pb-3">
                    Account Information
                </h3>
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    <strong>Nice activity!</strong> You have successfully update account.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
                <form >
                    <div class="col-md-12">
                        <div class="mb-3">
                            <label for="fname" class="form-label">First Name</label>
                            <input type="text" name="fname" id="fname" class="form-control" required/>
<!--                            <div class="invalid-feedback">{{ errors.firstName }}</div>-->
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="mb-3">
                            <label for="lname" class="form-label">Last Name</label>
                            <input type="text" name="lname" id="lname" class="form-control" required/>
<!--                            <div class="invalid-feedback">{{ errors.lastName }}</div>-->
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="mb-3">
                            <label for="email" class="form-label">Email</label>
                            <input type="text" name="email" id="email" class="form-control"/>
<!--                            <div class="invalid-feedback">{{ errors.email }}</div>-->
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="mb-3">
                            <label for="courses" class="form-label">Courses</label>
                            <textarea name="course" id="course" cols="30" rows="4" class="form-control" ></textarea>
<!--                            <div class="invalid-feedback">{{ errors.courses }}</div>-->
                        </div>
                    </div>
                    <div class="col-md-12">
                        <div class="mb-3 pt-3">
                            <button type="submit" name="update" id="update" class="btn btn-primary float-end">Update Account</button>
                        </div>
                    </div> 
                </form>
            </div>
        </div>
    <!-- </div> -->
</template>

<script>
  export default {
        name : 'AccForm',
        // components: {
        //     Form,
        //     Field,
        // },
        // data() {
        //     const schema = Yup.object().shape({
        //         firstName: Yup.string()
        //             .required('Title is required'),
        //         lastName: Yup.string()
        //             .required('Last name is required'),
        //         courses: Yup.string()
        //             .required('Last name is required'),
        //         email: Yup.string()
        //             .required('Email is required')
        //             .email('Email is invalid'),
        //     });
        //
        //     return {
        //         schema
        //     }
        // },
        // methods: {
        //     onSubmit(values) {
        //         // display form values on success
        //         alert('SUCCESS!! :-)\n\n' + JSON.stringify(values, null, 4));
        //     }
        // }
    }
</script>
    