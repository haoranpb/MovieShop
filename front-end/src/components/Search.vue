<template>
  <div class="search">
    <el-form :inline="true" :model="formInline">
      <el-form-item>
        <el-input v-model="formInline.name" placeholder="MovieName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data(){
    return {
      formInline:{
        name: ''
      }
    }
  }
}
</script>


<style scoped>
.search{
  margin: 40px;
}
</style>
