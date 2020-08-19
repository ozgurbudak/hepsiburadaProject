<template>
  <div>
    <h1>Products</h1>

    
<table class="table">
  <thead>
    <tr>
      <th scope="col">Product ID</th>
      <th scope="col">Title</th>
      <th scope="col">Details</th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="(product, index) in this.products" :key="product.id">
      <th scope="row">{{product.id}}</th>
      <td>{{ product.title}}</td>
      <td><router-link :to="'/product/' + product.id">Details</router-link></td>
      <td><button @click="deleteProduct(product.id, index)" class="btn btn-danger">delete</button></td>
    </tr>
    
  </tbody>
</table>

<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item" :class="{ 'disabled' : prevActive == false}">
      <a class="page-link" :href="prevLink" tabindex="-1">Previous</a>
    </li>
    <li class="page-item active">
      <a class="page-link" >{{ currPage }} <span class="sr-only">(current)</span></a>
    </li>
    <li class="page-item" :class="{ 'disabled' : nextActive == false}" >
      <a class="page-link" :href="nextLink">Next</a>
    </li>
  </ul>
</nav>


  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: "Products",
  data: function(){
    return {
          products:[],
          prevActive: false,
          prevLink: "",
          nextActive: false,
          nextLink: "",
          currPage: null
    }
  },

  methods: {
      deleteProduct: function(e, idx) {
        const axios = require('axios');
        axios.delete('http://127.0.0.1:8000/products/'+e+'/')
        .then(res => console.log(res))
        console.log(e)
        this.$delete(this.products, idx)
        this.$router.go()
      }
  },
   created: async function () {
    //fetch all products from api
    const axios = require('axios');

    let pageNumber = this.$route.query.page
    var add = ""
    if (pageNumber != null) {
      add = "?page=" + pageNumber
    }
    
    let response = await axios.get('http://127.0.0.1:8000/product/'+add);
    this.products= response.data.results

  
  //edit pagination numbers 
    let link = "http://localhost:8081/products?page="

    this.currPage = (pageNumber == null)? 1: pageNumber

    if (response.data.previous != null) {
      this.prevActive = true
      this.prevLink =  link + (parseInt(this.currPage)-1)
    }
    
    if (response.data.next != null) {
      this.nextActive = true
      this.nextLink = link + (parseInt(this.currPage)+1)
    }




  }
};
</script>
