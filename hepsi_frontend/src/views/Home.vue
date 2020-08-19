<template>
  <div class="home">
    <AddProduct></AddProduct>
  </div>
</template>

<script>
// @ is an alias to /src
import AddProduct from "@/components/AddProduct.vue";

export default {
  name: "Home",
  components: {
    AddProduct
  }
};
</script>
