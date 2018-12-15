<template>
  <div class="disaster">
    <div class="image">
      <img src="@/assets/disaster-small.png" />
    </div>
  <search genre="disaster"/>
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
