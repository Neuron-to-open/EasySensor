<template>
    <div class="home">
      <el-row display="margin-top:10px">
          <el-button type="primary" @click="add()" style="float:left; margin: 2px;">传感器</el-button>
      </el-row>
      <el-row>
          <el-table :data="datalist" style="width: 100%" border>
            <el-table-column prop="id" label="记录数" min-width="100">
              <template scope="scope"> {{ scope.row.pk }} </template>
            </el-table-column>
            <el-table-column prop="airhum" label="空气湿度" min-width="100">
              <template scope="scope"> {{ scope.row.fields.airhum }} </template>
            </el-table-column>
            <el-table-column prop="sun" label="太阳光强度" min-width="100">
              <template scope="scope"> {{ scope.row.fields.sun }} </template>
            </el-table-column>
            <el-table-column prop="soilhum" label="土壤湿度" min-width="100">
              <template scope="scope"> {{ scope.row.fields.soilhum}} </template>
            </el-table-column>
            <el-table-column prop="temp" label="温度" min-width="100">
              <template scope="scope"> {{ scope.row.fields.temp }} </template>
            </el-table-column>
          </el-table>
      </el-row>
      <el-row display="margin-top:10px">
          <el-button type="success" @click="handle()" style="float:left; margin: 2px;">可视化</el-button>
      </el-row>

      
    </div>
  </template>
  
  <script>

  export default {
    name: 'home',
    data () {
      return {
        datalist :[],
      }
    },
    mounted: function() {
        this.show() 
    },
    methods: {
      add(){
        /**
         * 生成四个随机数
         */
        this.$http.get('add/', {
          params: {
            airhum :  (Math.random()*(60-40)+40).toFixed(2) ,
            sun :     Math.floor(Math.random()*10),
            soilhum : (Math.random()*(80-20)+20).toFixed(2),
            temp :    (Math.random()*(40-0)+0).toFixed(2) 
          }
        })
          .then((response) => {
            
              console.log(response)
              if (response.data.error_num == 0) {
                this.$message({showClose: true, message: '增加成功！',type: 'success'})
              } else {
                this.$message.error('新增失败，请重试')
                console.log(response['msg'])
              }
          })
      },
      show(){
        this.$http.get('show/')
          .then((response) => {
            this.datalist = response.data.all
            localStorage.setItem("temp", JSON.stringify(response.data.all))
            console.log(response.data.all)
          })
      },
      handle(){
        this.$router.push('/pic')
      },
    }
  }
  
        
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  </style>