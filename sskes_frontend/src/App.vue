<template>
<div id="app">
<router-view/>
</div>
</template>


<script>
import axios from 'axios'
// import Nav from '@/components/Nav';
export default {
  name: 'app',
  components:{
    // Nav,
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    if(this.$store.state.token){
      axios.defaults.headers.common['Authorization'] = "Token" + this.$store.state.token
    }else{
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>


