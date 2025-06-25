---
aside: false
padding: false
---

<script setup>
import { onMounted } from "vue";
import { useData } from "vitepress"
import Broadcast from "@/views/Broadcast.vue"

const { params } = useData();
</script>

<Broadcast :page="Number(params.num)" />
