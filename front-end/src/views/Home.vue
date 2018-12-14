<template>
  <div class="multi-pic">
    <el-carousel arrow="always" height="730px">
      <el-carousel-item :key="action">
        <img src='@/assets/action.png' alt="action" />
      </el-carousel-item>
      <el-carousel-item :key="comedy">
        <img src='@/assets/comedy.png' alt="comedy" />
      </el-carousel-item>
      <el-carousel-item :key="diaster">
        <img src='@/assets/diaster.png' alt="diaster" />
      </el-carousel-item>
      <el-carousel-item :key="documentary">
        <img src='@/assets/documentary.png' alt="documentary" />
      </el-carousel-item>
      <el-carousel-item :key="fiction">
        <img src='@/assets/fiction.png' alt="fiction" />
      </el-carousel-item>
      <el-carousel-item :key="war">
        <img src='@/assets/war.png' alt="war" />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<style scoped>
img{
  width: 100%;
}
</style>


