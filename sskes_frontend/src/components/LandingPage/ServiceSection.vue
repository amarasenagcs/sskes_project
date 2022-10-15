<template>
    <!-- services section Starts -->
    <section class="services section-padding " id="services">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="section-header text-center pb-5">
                        <h2>Our Services</h2>
                    </div>
                </div>
            </div>
            <div class="row">
            <div class="col-12 col-md-12 col-lg-4">
                <div class="card text-white text-center bg-dark pb-2">
                    <div class="card-body">
                        <i class="bi bi-play-circle"></i>
                        <h3 class="card-title sinhala-font">වීඩියෝ පාඨමාලාවන්</h3>
                        <p class="lead sinhala-font">අපහා සම්බන්දවන සිසුන්ට වීඩියෝ දර්ශන නැරඹීමෙන් තම පාඨමාලාවන් සාර්ථකව අවසන් කරගත හැකිය.</p>
                        <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
                    </div>
                </div>
            </div>
                <div class="col-12 col-md-12 col-lg-4">
                    <div class="card text-white text-center bg-dark pb-2">
                        <div class="card-body">
                            <i class="bi bi-translate"></i>
                            <h3 class="card-title sinhala-font">සිංහල භාෂාව</h3>
                            <p class="lead sinhala-font">අපහා සම්බන්දවන සිසුන්ට තේරෙන සිංහල භාෂාවෙන් තම පාඨමාලාවන් සාර්ථකව හැදෑරියහැකි බැවින් සියලුම සිසුන්ට සාර්ථකව අධ්‍යනයක් ලබාගත හැකිය.</p>
                            <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
                        </div>
                    </div>
                </div>
                <div class="col-12 col-md-12 col-lg-4">
                    <div class="card text-white text-center bg-dark pb-2">
                        <div class="card-body">
                            <i class="bi bi-journal-bookmark-fill"></i>
                            <h3 class="card-title sinhala-font">අභ්‍යාස</h3>
                            <p class="lead sinhala-font">අපහා සම්බන්දවන සිසුන්ව අභ්‍යාස කිරීමෙන් සාර්ථක අධ්‍යාපනයක් ලබාදීමට අප සෑමවිටම බැදී සිටින්නෙමු.</p>
                            <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- services section Ends -->
</template>

<script>
    export default {
        name : 'Features'
    }
</script>

<style scoped src="../../assets/css/LandingPage/style.css">

</style>