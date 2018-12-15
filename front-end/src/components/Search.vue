<template>
  <div>
    <div class="search">
      <el-form :inline="true" :model="form" @submit.native.prevent>
        <el-form-item label="请输入电影名称">
          <el-input v-model="form.name" placeholder="对名称进行正则匹配"></el-input>
        </el-form-item>
        <el-form-item
          label="请输入最低价格"
          prop="low"
          :rules="[
          { type: 'number', message: '年龄必须为数字值'}
          ]">
          <el-input v-model.number="form.low" placeholder="请输入整数"></el-input>
        </el-form-item>
        <el-form-item
        label="请输入最高价格"
        prop="high"
        :rules="[
        { type: 'number', message: '年龄必须为数字值'}
        ]">
          <el-input v-model.number="form.high" placeholder="请输入整数"></el-input>
        </el-form-item>
        <el-form-item label="请选择年份">
          <el-time-picker
            v-model="form.year"
            type="year"
            placeholder="选择年">
          </el-time-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="search">查询</el-button>
        </el-form-item>
      </el-form>
    </div>

    <div class="result">
      <el-table :data="movieData" stripe height="400" style="width: 100%">
        <el-table-column prop="id" label="ID" width="140" sortable="">
        </el-table-column>
        <el-table-column prop="title" label="电影名" width="140">
        </el-table-column>
        <el-table-column prop="actor" label="演员" width="140">
        </el-table-column>
        <el-table-column prop="director" label="导演" width="140">
        </el-table-column>
        <el-table-column prop="genre" label="分类" width="140">
        </el-table-column>
        <el-table-column prop="review" label=" 评论数目" width="140" sortable>
        </el-table-column>
        <el-table-column prop="price" label="价格" width="140" sortable>
        </el-table-column>
        <el-table-column prop="time" label="上映时间" width="140" sortable>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button @click.native.prevent="addCart(scope.row)" type="text" size="medium">
              加入购物车
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['genre'],
  data(){
    return {
      form:{
        name: '',
        low: '',
        high: '',
        year: ''
      },
      movieData: [{
          id: '1123',
          title: 'HP',
          actor: 'ludanxer',
          director: 'ludan',
          genre: 'Action',
          review: '20',
          price: '1.99',
          time: '2018'
        },
        {
          id: '123',
          title: 'HP',
          actor: 'ludanxer',
          director: 'ludan',
          genre: 'Action',
          review: '2',
          price: '12.99',
          time: '2017'
        }]
    }
  },
  methods: {
    search(){
      let movie_name = this.form.name;
      let low_price = this.form.low;
      let high_price = this.form.high;
      let time = this.year;

      axios.get('http://127.0.0.1:5000/search', {
        params: {
          genre: this.genre,
          name: movie_name,
          low: low_price,
          high: high_price,
          year: time
        }
      })
      .then(function (response) {
        console.log(response); // 将获取的数据，解析到movieData中即可
      })
      .catch(function (error) {
        alert(error);
      });
    },
    addCart(row){
      console.log(row);
    }
  }
}
</script>

<style scoped>
.search{
  margin: 40px;
}
.result{
  margin-left: 80px;
  margin-right: 80px;
  display: block;
}
</style>
