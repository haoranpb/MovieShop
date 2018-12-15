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
              <el-button @click.native.prevent="deleteRow(scope.$index, cartData)" type="text" size="medium">
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
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      cartData: [{
        id: 'C3',
        title: 'HP',
        actor: 'ludanxer',
        director: 'ludan',
        genre: 'Action',
        review: '2',
        price: '12.99',
        time: '2017'
      },
      {
        id: 'B3',
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
    deleteRow(index, rows) {
      rows.splice(index, 1); // 还需要从数据库中删除
    }
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
.pay{
  margin-top: 10px;
  margin-right: 380px;
  float: right;
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
