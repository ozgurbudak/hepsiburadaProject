<template>
  <div>

    <form>
  <div class="form-group">
    <label >URL</label>
    <input v-model="url" type="text" class="form-control" placeholder="Enter hepsiburada url">
  </div>
  <button @click="postProduct($event)" type="submit" class="btn btn-primary">Submit</button>
</form>

<div v-if="isValidVisible" class="alert alert-success" role="alert">
  product is created! :)
</div>
<div v-if="isInvalidVisible" class="alert alert-danger" role="alert">
  Invalid url :(
</div>
    

  </div>
</template>

<script>
export default {
  name: "AddProduct",
 data() {
            return {
                url: null,
                isValidVisible: false,
                isInvalidVisible: false

            }
        },
  props: {
    
  },
  methods: {
    
    async postProduct(e){
         const axios = require('axios');
        e.preventDefault()

        var valid = this.url.startsWith("https://www.hepsiburada.com/")
        
        if (valid) {
             var params = {
                url: this.url
            }

            let res = await axios.post('http://127.0.0.1:8000/product/', params);
            this.isValidVisible= true
            console.log(res.data)
            this.url = ""
            setTimeout(() => this.isValidVisible = false, 3000)

        } else {
            this.isInvalidVisible= true
            this.url = ""
            setTimeout(() => this.isInvalidVisible = false, 3000)
         console.log("invalid url")   
        }


    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
