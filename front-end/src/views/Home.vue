<template>
  <div class="multi-pic">
    <el-carousel arrow="always" height="700px">
      <el-carousel-item :key="action">
        <img src='@/assets/action.jpg' alt="sorry" />
      </el-carousel-item>
      <el-carousel-item :key="comedy">
        <img src='@/assets/comedy.png' alt="sorry" />
      </el-carousel-item>
      <el-carousel-item :key="fiction">
        <img src='@/assets/fiction.jpeg' alt="sorry" />
      </el-carousel-item>
    </el-carousel>
  </div>
</template>
