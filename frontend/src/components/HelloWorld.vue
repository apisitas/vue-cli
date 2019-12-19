<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>first name</th>
          <th>last name</th>
          <th>email</th>
          <th>gender</th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="head" colspan="6">getByuserId</td>
        </tr>
        <tr v-for="item in getByuserId" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
        <tr>
          <td class="head" colspan="6">getByfirstName</td>
        </tr>
        <tr v-for="item in getByfirstName" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
        <tr>
          <td class="head" colspan="6">getBylastName</td>
        </tr>
        <tr v-for="item in getBylastName" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
        <tr>
          <td class="head" colspan="6">getByemail</td>
        </tr>
        <tr v-for="item in getByemail" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
        <tr>
          <td class="head" colspan="6">getBybetween</td>
        </tr>
        <tr v-for="item in getBybetween" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
        <tr>
          <td class="head" colspan="6">getBygender</td>
        </tr>
        <tr v-for="item in getBygender" :key="item">
          <td>{{ item.id }}</td>
          <td>{{ item.first_name }}</td>
          <td>{{ item.last_name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.gender }}</td>
          <td>{{ item.age}}</td>
        </tr>
      </tbody>
    </table>
    <ul>
      
  </ul>
  </div>
</template>

<script>
var host = 'http://127.0.0.1:5000/'
import axios from "axios";
export default {
  name: "HelloWorld",
  props: {
    msg: String
  },
  data() {
    return {
      getByuserId: [],
      getByfirstName: [],
      getBylastName: [],
      getByemail: [],
      getBybetween: [],
      getBygender: [],
    };
  },
  methods: {

    func_getByuserId: function () {
      return axios.get(host+"getByuserId")
        .then(res => {
            this.getByuserId = res.data
            return res
          }
        )
    },

    func_getByfirstName: function () {
      return axios.get(host+"getByfirstName")
        .then(res => {
            this.getByfirstName = res.data
            return res
          }
        )
    },

    func_getBylastName: function () {
      return axios.get(host+"getBylastName")
        .then(res => {
            this.getBylastName = res.data
            return res
          }
        )
    },

    func_getByemail: function () {
      return axios.get(host+"getByemail")
        .then(res => {
            this.getByemail = res.data
            return res
          }
        )
    },
    
    func_getBybetween: function () {
      return axios.get(host+"getBybetween")
        .then(res => {
            this.getBybetween = res.data
            return res
          }
        )
    },

    func_getBygender: function () {
      return axios.get(host+"getBygender")
        .then(res => {
            this.getBygender = res.data
            return res
          }
        )
    },
    func_getByInsert: function () {
      return axios.get(host+"getByInsert")
        .then(res => {
            return res
          }
        )
    },
  },
  mounted() {
    this.func_getByuserId()
    this.func_getByfirstName()
    this.func_getBylastName()
    this.func_getByemail()
    this.func_getBybetween()
    this.func_getBygender()
    this.func_getByInsert()
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table {
  width: 100%;
}
table td {
  border: 1px solid;
}
.head {
  background:green;
  color:white;
}
</style>
