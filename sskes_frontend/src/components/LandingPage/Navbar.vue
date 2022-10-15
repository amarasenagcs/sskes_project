<template>
    <!-- <div> -->
      <nav class="navbar navbar-expand-lg bg-light p-0">
        <div class="container-fluid">
          <img src="assets/images/logo/logo.png" alt="sskes-logo" class="navbar-brand img-fluid">
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarScroll">
            <ul class="navbar-nav me-2 mx-auto navbar-nav-scroll" style="--bs-scroll-height: 158px;">
              <li class="nav-item fs-5 px-3">
                <router-link class="nav-link" aria-current="page" to="/">Home</router-link>
              </li>
              <li class="nav-item fs-5 px-3">
                <router-link class="nav-link" to="/login">Login</router-link>
              </li>
              <li class="nav-item fs-5 px-3">
                <router-link class="nav-link" to="/signUp">Sign Up</router-link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <!-- </div> -->
</template>

<script>
    export default {
        name : 'Navbar',
    }
</script>

<style scoped>

.nav-link{
  color: #000000;
  font-weight: 600;
}
.active{
  color: #FF6700;
  font-weight: 600;
  text-shadow: 5px 10px 10px rgba(0, 0, 0, 0.2);
}
.nav-link:hover{
  color: #FF6700;
  font-weight: 600;
  text-shadow: 5px 10px 10px rgba(0, 0, 0, 0.2);
}

/* ----------------------Media Query-------------------------- */
@media only screen and (max-width: 767px){
    .navbar-brand{
      width: 150px;
      height: 80px;
    }
  
    /* .nav-item router-link{
      font-size: 90px;
      font-weight: 700;
    } */
}

@media only screen and (min-width: 768px){
    .navbar-brand{
      width: 230px;
      height: 100px;
    }
}
</style>