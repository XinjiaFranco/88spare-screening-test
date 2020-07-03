<template>
    <div class="row">
      <div class="col-lg-6">
        <h1>Currency Rate</h1>
      </div>
      <div class="col-lg-6">
        <table class = "table">
          <thead>
            <th>No</th>
            <th>Currency Name</th>
            
          </thead>
          <tbody>
            <tr v-for="c in currencyrate" v-bind:key="c.id">
              <td>{{c.id}}</td>
              <button @click="getOne(c)">{{c.currency}}</button>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <h1>Select Currency</h1>      
      <p>Currency name: {{this.currency}}</p>
      <p>Curreny value: {{this.value}}</p>
      <p>Currency rate: {{this.rate}}</p>
    </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Container',
  props: {
    msg: String
  },
  data(){
    return{
      currencyrate:null,
      id: 0,
      currency:'',
      value: 0,
      rate: 0,
    }
  },
  mounted(){
    this.getAll();
  },
  methods:{
    getAll(){
      axios.get('http://localhost:8000/currency')
      .then((res)=>{
        this.currencyrate = res.data
      })
    },
    getOne(c){
      this.id = c.id;
      this.currency = c.currency;
      this.value = c.value;
      this.rate = c.rate;
    }
  }
}

export function authHeader(){
  let user = JSON.parse(localStorage.getItem('item'));
  if(user && user.token){
    return {'Authorization' : 'Bearer' + user.token};
  }else{
    return{};
  }
}
</script>

<style scoped>

</style>
