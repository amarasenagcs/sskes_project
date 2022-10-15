<template>
    <Navbar/>
    <SectionOne/>
    <AboutSection/>
    <ServiceSection/>
    <TeacherTeam/>
    <Footer/>
</template>

<script>

    import Navbar from '@/components/LandingPage/Navbar'
    import SectionOne from '@/components/LandingPage/SectionOne'
    import AboutSection from '@/components/LandingPage/AboutSection'
    import ServiceSection from '@/components/LandingPage/ServiceSection'
    import TeacherTeam from '@/components/LandingPage/TeacherTeam'
    import Footer from '@/components/LandingPage/Footer'

    export default {
        name : 'HomeTwo',
        components : {
            Navbar,
            SectionOne,
            AboutSection,
            ServiceSection,
            TeacherTeam,
            Footer,
        }
    }
</script>

<style scoped src="../../assets/css/LandingPage/style.css">

</style>