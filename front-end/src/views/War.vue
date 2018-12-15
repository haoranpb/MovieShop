<template>
  <div class="war">
    <div class="image">
      <img src="@/assets/war-small.png" />
    </div>
  <search genre="War"/>
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
