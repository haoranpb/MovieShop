<template>
  <div class="shop-header">
    <h1>Shop Movie</h1>
    <el-button type="primary" round size="small">购物车</el-button>
    <el-dropdown @command="handleCommand" trigger="click">
      <span class="el-dropdown-link">
        全部分类<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="fiction">黄金糕</el-dropdown-item>
        <el-dropdown-item command="action">狮子头</el-dropdown-item>
        <el-dropdown-item command="war">螺蛳粉</el-dropdown-item>
        <el-dropdown-item command="comedy">双皮奶</el-dropdown-item>
        <el-dropdown-item command="e">蚵仔煎</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>

<script>
  export default {
    methods: {
      handleCommand(command) {
        this.$message('click on item ' + command);
      }
    }
  }
</script>

<style scoped>
h1{
  float: left;
  margin: 0;
  padding: 0;
  height: auto;
  color: grey;
  line-height: 60px;
}
.shop-header{
  background-color: black;
  padding-left: 20%;
  padding-right: 20%;
}
.el-dropdown{
  float: right;
  font-size: 1em;
  line-height: 60px;
}
.el-button{
  float: right;
  margin-top: 12px;
  margin-left: 50px;
}
</style>



