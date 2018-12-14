<template>
  <div class="shop-header">
    <h1>Shop Movie</h1>
    <router-link to="/cart">
      <el-button type="primary" round size="small">购物车</el-button>
    </router-link>
    <el-dropdown @leger="click">
      <span class="el-dropdown-link">
        全部分类<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <router-link to="/">
          <el-dropdown-item>all</el-dropdown-item>
        </router-link>
        <router-link to="/action">
          <el-dropdown-item>Action</el-dropdown-item>
        </router-link>
        <router-link to="/comedy">
          <el-dropdown-item>Comedy</el-dropdown-item>
        </router-link>
        <router-link to="/diaster">
          <el-dropdown-item>Diaster</el-dropdown-item>
        </router-link>
        <router-link to="/documentary">
        <el-dropdown-item>Documentary</el-dropdown-item>
        </router-link>
        <router-link to="/fiction">
          <el-dropdown-item>Fiction</el-dropdown-item>
        </router-link>
        <router-link to="/war">
          <el-dropdown-item >War</el-dropdown-item>
        </router-link>
      </el-dropdown-menu>
    </el-dropdown>
  </div>
</template>


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



