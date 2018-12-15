<template>
  <div class="documentary">
    <div class="image">
      <img src="@/assets/documentary-small.png" />
    </div>
  <search genre="documentary"/>
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
