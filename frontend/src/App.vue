<script setup>
import { ref, onMounted } from "vue";
import api from "./services/api";

const transactions = ref([]);

onMounted(async () => {
  try {
    const res = await api.get("/api/transactions");
    transactions.value = res.data;
  } catch (err) {
    console.log("Greška:", err);
  }
});
</script>

<template>
  <div>
    <h1>Transactions</h1>

    <ul>
      <li v-for="t in transactions" :key="t.id">
        {{ t.title }} - {{ t.amount }}
      </li>
    </ul>
  </div>
</template>