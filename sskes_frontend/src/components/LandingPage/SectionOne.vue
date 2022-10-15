<template>
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../../assets/images/Home-Dashboard/2.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption">
              <h5 class="sinhala-font">පළපුරුදු ගුරුවරු</h5>
              <p class="fs-4 sinhala-font">අපගේ සිසුන් සෑමවිටම පළපුරුදු ගුරුවරුන් සමග සම්බන්ද වී අධ්‍යන කටයුතු කිරීමට හැකිවේ.</p>
              <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../../assets/images/Home-Dashboard/1.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption">
              <h5 class="sinhala-font">සාර්ථක ප්‍රතිපල</h5>
              <p class="fs-4 sinhala-font">පාඨමාළා අන්තරගතය සිසුන්ට පැහැදිලිවනසේ සකස්කර ඇති බැවින් සිසුන්ට ඉතා ඉක්මනින් අවබෝධකරගත හැකිවේ</p>
              <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
            </div>
          </div>
          <div class="carousel-item">
            <img src="../../assets/images/Home-Dashboard/4.jpg" class="d-block w-100" alt="...">
            <div class="carousel-caption">
              <h5 class="sinhala-font">සාර්ථක පුහුණුව</h5>
              <p class="fs-4 sinhala-font">අප විසින් සිසුන්ව සාර්ථක විෂය පිළිබද අධ්‍යාපනය ලබාදී අමතරව විෂය ගැටලු සදහා සිසුන් පුහුණු කරන ලදි.</p>
              <router-link to="/signUp"><button class="btn bg-warning text-dark">Read More</button></router-link>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
</template>

<script>
    export default {
        name : 'SectionOne',
    }
</script>

<style scoped src="../../assets/css/LandingPage/style.css">

</style>