<template>
  <div class="fiction">
    <div class="image">
      <img src="@/assets/fiction.jpeg" />
    </div>
  <search />
  <result />
  </div>
</template>

<script>
import Result from '@/components/Result.vue'
import Search from '@/components/Search.vue'

export default {
  components: {
    Result,
    Search
  },
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
.image{
  height: 300px;
  width: 100%;
}
</style>
