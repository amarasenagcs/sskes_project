<template>
    <div class="wrapper">
        <sidebar/>
        <!-- Page Content  -->
        <div id="content">

            <nav class="navbar navbar-expand-lg navbar-light bg-light shadow">
                <div class="container-fluid">

                    <button type="button" id="sidebarCollapse" class="btn btn-info">
                        <i class="bi bi-text-left"></i>
                        <span>Toggle Sidebar</span>
                    </button>
                    <button class="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <i class="fas fa-align-justify"></i>
                    </button>

                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav me-2 mx-auto mb-2 mb-lg-0">
                            <li class="nav-item active">
                                <a class="nav-link" href="#">{UserName}</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <router-link to="/courses-section" class="btn btn-danger mb-2 text-light"><i class="bi bi-arrow-left-short"></i>Back</router-link>

            <!-- Subject lerning details card start -->            
            <div class="row p-4 col-12 mx-auto">
                <div class="col-4">                    
                    <div class="card border border-dark">
                        <div class="card-body">
                            <h4 class="sinhala-font fs-5 mb-5 pt-4 fw-bold">දරුවාව ලියාපදිංචි කරන්න</h4>
                            <div class="form-check">
                                <input class="form-check-input fs-5 me-4" type="checkbox" name="flexRadioDefault" id="flexRadioDefault1">
                                <label class="form-check-label fs-5" for="flexRadioDefault1">
                                    sandaru-aiya@gmail.com
                                </label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input fs-5 me-4" type="checkbox" name="flexRadioDefault" id="flexRadioDefault2">
                                <label class="form-check-label fs-5" for="flexRadioDefault2">
                                    sathsara@gmail.com
                                </label>
                            </div>
                            <button  class="btn btn-warning fw-bold sinhala-font mt-4 float-end" id="liveToast">ලියාපදිංචි කරන්න</button>
                        </div>
                    </div>
                </div>
                <div class="col-8">
                    <div class="card border">
                        <div class="card-body">
                            <div class="row">
                                <h4 class="sinhala-font fs-5 mb-5 pt-4 fw-bold">ඔබ ඉගෙනුම ලබන දෑ</h4>
                                <div class="col-md-12">
                                    <ul>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                        <li class=" d-flex">
                                            <span class="bi bi-check-circle-fill me-4 text-success"></span>
                                            <p class="sinhala-font text-dark">පාඩමට අදාල කරුණු කිහිපයක්</p>
                                        </li>
                                    </ul>                              
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
            <!-- Subject lerning details card end -->            

            <!-- subject contents list start -->
            <div class="row col-10 p-2 mx-auto mb-5">
                <div class="accordion sinhala-font" id="accordionExample">
                    <div class="accordion-item border border-2">
                        <h2 class="accordion-header" id="headingOne">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" id="accordian-button-color">
                            පාඩම් අංක #1
                        </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odio pariatur doloribus sunt eaque officia eveniet corporis eos sed quo, minima incidunt, laboriosam laudantium modi placeat odit dolorem magni totam commodi!ඔබ කරමින් පවතින පාඨමාළාවන් බලාගැනීම සදහා මෙතැනින් පිවිසෙන්න.
                        </div>
                        </div>
                    </div>
                    <div class="accordion-item border border-2">
                        <h2 class="accordion-header" id="headingTwo">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo" id="accordian-button-color">
                            පාඩම් අංක #2
                        </button>
                        </h2>
                        <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                        </div>
                    </div>
                    <div class="accordion-item border border-2">
                        <h2 class="accordion-header" id="headingThree">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree" id="accordian-button-color">
                            පාඩම් අංක #3
                        </button>
                        </h2>
                        <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                        </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- subject contents list end -->
        </div>
    </div>
</template>

<script>

    import sidebar from '@/components/ParentDashboard/Sidebar'

    export default {
        name : 'courseContentView',
        components : {
            sidebar,
        }
    }
</script>

<style scoped src="../../assets/css/ParentDashboard/main.css">

</style>