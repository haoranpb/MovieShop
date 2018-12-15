<template>
  <div class="action">
    <div class="image">
      <img src="@/assets/action-small.png" />
    </div>
  <search genre="Action"/>
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
