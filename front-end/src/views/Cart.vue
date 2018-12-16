<template>
  <div id="cart">
    <div class="image">
      <img src="@/assets/movie.jpg" />
    </div>
    <div class="cart-main">
      <div class="table">
        <el-table :data="cartData" style="width: 100%" height="350" show-summary>
          <el-table-column type="expand">
            <template slot-scope="props">
              <el-form label-position="left" inline class="demo-table-expand">
                <el-form-item label="演员">
                  <span>{{ props.row.actor }}</span>
                </el-form-item>
                <el-form-item label="导演">
                  <span>{{ props.row.director }}</span>
                </el-form-item>
                <el-form-item label="分类">
                  <span>{{ props.row.genre }}</span>
                </el-form-item>
                <el-form-item label="评论数目">
                  <span>{{ props.row.review }}</span>
                </el-form-item>
                <el-form-item label="上映时间">
                  <span>{{ props.row.time }}</span>
                </el-form-item>
              </el-form>
            </template>
          </el-table-column>
          <el-table-column label="电影 ID" prop="id">
          </el-table-column>
          <el-table-column label="电影名称" prop="title">
          </el-table-column>
          <el-table-column label="价格" prop="price" sortable="">
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click.native.prevent="deleteRow(scope.row, scope.$index, cartData)" type="text" size="medium">
                移除购物车
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      <div>
        <router-link to="/pay">
          <el-button class="pay" type="primary">立即付款</el-button>
        </router-link>
        <el-button class="refresh" type="primary" @click="refresh()">刷新页面</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return {
      cartData: []
    }
  },
  methods: {
    deleteRow(row, index, rows) {
      let obj = this;
      this.$message('正在删除，请稍后！');

      axios.get('http://127.0.0.1:5000/deletecart', {
        params: { id: row.id }
      })
      .then(function () {
        obj.$message({
          message: '成功删除！',
          type: 'success'
        });
        rows.splice(index, 1);
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    },
    refresh(){
      let obj = this;
      this.$message('正在刷新，请稍后！');

      axios.get('http://127.0.0.1:5000/getcart')
      .then(function (response) {
        obj.$message({
            message: '成功刷新！',
            type: 'success'
          });
        obj.cartData = []
        for(let key of Object.keys(response.data)){
          obj.cartData.push(response.data[key]);
        }
      })
      .catch(function () {
        obj.$message.error('糟糕，哪里出了点问题！');
      });
    }
  },
  mounted: function(){
    let obj = this;
    axios.get('http://127.0.0.1:5000/getcart')
    .then(function (response) {
      obj.cartData = []
      for(let key of Object.keys(response.data)){
        obj.cartData.push(response.data[key]);
      }
    })
    .catch(function () {
      obj.$message.error('糟糕，哪里出了点问题！');
    });
  }
}
</script>

<style scoped>
img{
  height: 100%;
  width: 100%;
}
.image{
  height: 300px;
}
.table{
  margin-top: 5px;
  margin-left: 80px;
  margin-right: 200px;
}
.pay, .refresh{
  margin-top: 10px;
  margin-right: 380px;
  float: right;
}
.refresh{
  margin-right: 80px;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
