<template>
  <div>
    <div class="search">
      <el-form :inline="true" :model="form" @submit.native.prevent>
        <el-form-item label="电影名称">
          <el-input v-model="form.name" placeholder="正则匹配名称"></el-input>
        </el-form-item>
        <el-form-item label="最低价格" prop="low"
          :rules="[{ type: 'number', message: '价格必须为数字值'}]">
          <el-input v-model.number="form.low" placeholder="整数"></el-input>
        </el-form-item>
        <el-form-item label="最高价格" prop="high"
        :rules="[{ type: 'number', message: '价格必须为数字值'}]">
          <el-input v-model.number="form.high" placeholder="整数"></el-input>
        </el-form-item>
        <el-form-item label="获取条数" prop="num"
        :rules="[{ type: 'number', message: '条数必须为数字值'}]">
          <el-input v-model.number="form.num" placeholder="LIMIT 10"></el-input>
        </el-form-item>
        <el-form-item label="年份">
          <el-date-picker v-model="form.year" type="year" value-format="yyyy" placeholder="选择年">
          </el-date-picker>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="search">查询</el-button>
        </el-form-item>
      </el-form>
    </div>
    <el-tag type="warning">程序查询时间：{{ time }}S</el-tag>
    <el-tag type="success">数据库返回条目数量：{{ number }}</el-tag>
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
        year: '',
        num: ''
      },
      movieData: [],
      time: '0',
      number: '0'
    }
  },
  methods: {
    search(){
      let low_price = this.form.low;
      let high_price = this.form.high;
      let num = this.form.num;
      if(!low_price){ low_price='0' }
      if(!high_price){ high_price='40' }
      if(!num){ num='10' }
      let obj = this;
      this.$message('开始发送请求，请稍后！');

      axios.get('http://127.0.0.1:5000/search', {
        params: {
          genre: this.genre,
          name: this.form.name,
          low: low_price,
          high: high_price,
          year: this.form.year,
          number: num
        }
      })
      .then(function (response) {
        obj.time = response.data.time;
        obj.number = response.data.number;
        obj.movieData = [];
        obj.$message({
          message: '恭喜你，成功了！',
          type: 'success'
        });
        for(let key of Object.keys(response.data)){
          if(key!='time'&&key!='number'){
            obj.movieData.push(response.data[key]);
          }
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    addCart(row){
      let obj = this;
      this.$message('正在加购，请稍后！');
      console.log(row);

      axios.get('http://127.0.0.1:5000/addcart', {
        params: { 
          id: row.id,
          actor: row.actor,
          director: row.director,
          price: row.price,
          title: row.title,
          time: row.time,
          review: row.review,
          genre: row.genre
        }
      })
      .then(function (response) {
        if(response.status==200){
          obj.$message({
            message: '成功加购！',
            type: 'success'
          });
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  }
}
</script>

<style scoped>
.search{
  margin: 15px;
  margin-bottom: 0;
}
.el-tag{
  margin-left: 60px;
  margin-right: 60px;
  margin-bottom: 10px;
}
.result{
  margin-left: 80px;
  margin-right: 80px;
  display: block;
}
.el-input{
  width: 140px;
}
</style>
