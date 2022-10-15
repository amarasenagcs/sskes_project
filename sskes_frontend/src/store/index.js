import { createStore } from 'vuex'

// export default createStore({
//   state: {
//     user:{
//       token:'',
//       isAuthenticated: false
//     }
//   },
//   mutations: {
//     initializeStore(state){
//       if(localStorage.getItem('token')){
//         state.token = localStorage.getItem('token')
//         state.user.isAuthenticated= true
//       }else{
//         state.user.token=''
//         state.user.isAuthenticated= false
//       }
//     },
//     setToken(state, token){
//       state.user.token =token
//       state.user.isAuthenticated= true
//     },
//     removeToken(state){
//       state.user.token =''
//       state.user.isAuthenticated= false
//     }
//   },
//   actions: {
//   },
//   modules: {
//   }
// })

export default createStore({
  state: {
    user:{
      APIData: '',
      isAuthenticated: false,
      accessToken: null,
      refreshToken: null,
    }
  },
  mutations: {
    initializeStore(state){
      if(localStorage.getItem('accessToken')){
        state.accessToken = localStorage.getItem('accessToken')
        state.user.isAuthenticated= true
      }else{
        state.user.accessToken=''
        state.user.isAuthenticated= false
      }
    },
    setToken(state, accessToken){
      state.user.accessToken =accessToken
      state.user.isAuthenticated= true
    },
    removeToken(state){
      state.user.accessToken =''
      state.user.isAuthenticated= false
    }
  },
  actions: {
  },
  modules: {
  }
})
