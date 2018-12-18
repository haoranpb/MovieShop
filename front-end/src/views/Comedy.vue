<template>
  <div class="comedy">
    <div class="image">
      <img src="@/assets/comedy-small.jpg" />
    </div>
  <search genre="Comedy"/>
  </div>
</template>

<script>
import Search from '@/components/Search.vue'

export default {
  components: {
    Search
  }
}
</script>


<style scoped>
img{
  height: 300px;
  width: 100%;
}
</style>
