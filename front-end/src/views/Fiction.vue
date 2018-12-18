<template>
  <div class="fiction">
    <div class="image">
      <img src="@/assets/fiction-small.jpg" />
    </div>
  <search genre="Fiction"/>
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
