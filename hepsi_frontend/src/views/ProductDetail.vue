<template>
  <div >
    <h2>{{ product.title}}</h2>

    <img :src="product.image">

    <h4>Price: {{product.price}} </h4>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "ProductDetail",
  data(){
      return {
          product: null
      }
  },
  components: {
    
  },
  created(){
      const axios = require('axios');
        var param = this.$route.params.productId
    axios
      .get('http://127.0.0.1:8000/products/'+param+'/')
      .then(response => (this.product= response.data))
  }
};
</script>
