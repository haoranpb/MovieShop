<template>
  <div id="app">
    <el-container>
      <el-header style="padding: 0;background-color: black;">
        <shop-header />
      </el-header>
      <el-main style="margin: 0;padding: 0;">
        <router-view />
      </el-main>
    </el-container>
  </div>
</template>

<script>
import ShopHeader from './components/ShopHeader'

export default {
  components: {
    ShopHeader
  }
}
</script>


<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
html, body, .el-main, .el-header{
  margin: 0;
  padding: 0;
}
a{
  text-decoration: none;
}
</style>
