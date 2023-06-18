<template>
    <div class="echart" id="mychart" :style="myChartStyle"></div>
  </template>
  
  <script>
  import * as echarts from "echarts";
  
  export default {
    data() {
      return {
        myChart: {},
        xData: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], //横坐标
        yData: [23, 24, 18, 25, 27, 28, 25], //人数数据
        myChartStyle: { float: "left", width: "100%", height: "400px" } //图表样式
      };
    },
    mounted() {
      this.initEcharts();
    },
    methods: {
      initEcharts() {
        var tempdate = JSON.parse(localStorage.getItem('temp'))
        console.log(tempdate)
        var i 
        for (i = 0 ; i < 7 ; i ++){
            this.yData[i] = tempdate[i].fields.temp
        }
        const option = {
          xAxis: {
            data: this.xData
          },
          yAxis: {},
          series: [
            {
              data: this.yData,
              type: "line" // 类型设置为折线图
            }
          ]
        };
        this.myChart = echarts.init(document.getElementById("mychart"));
        this.myChart.setOption(option);
        //随着屏幕大小调节图表
        window.addEventListener("resize", () => {
          this.myChart.resize();
        });
      }
    }
  };
  </script>
  
  