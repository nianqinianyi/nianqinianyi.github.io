---
aside: false
padding: false
---

<script setup>
import { onMounted } from "vue";
import { useData } from "vitepress"
import Broadcast from "@/views/Broadcast.vue"
</script>

<Broadcast :page="Number(1)" />
