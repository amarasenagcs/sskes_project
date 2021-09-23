<template>
  <nav class="navbar" role="navigation" aria-label="main naviagation" style="min-height:5rem;">
    <div class="navbar-brand">
      <router-link class="navbar-item is-size-4" to="/">sskes</router-link>
      </div>

      <div id="navbar-item" class="navbar-menu">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">මුල්පිටුව</router-link>
          <router-link to="/about" class="navbar-item">අපි ගැන</router-link>
          <router-link to="/courses" class="navbar-item">Courses</router-link>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.user.isAuthenticated">
                  <router-link to="/dashboard/my-account" class="button is-info">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/sign-up" class="button is-primary"><strong>Sign up</strong></router-link>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
              </template>

            </div>
          </div>
        </div>
      </div>        
  </nav>
</template>

<script>
</script>

<style>

</style>