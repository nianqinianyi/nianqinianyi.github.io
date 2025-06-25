<!-- 首页 -->
<template>
  <div class="home">
    <div class="home-content">
      <div class="posts-content">
        <!-- 文章列表 -->
        <BroadcastList :listData="postData" />
        <!-- 分页 -->
        <Pagination
          :total="allListTotal"
          :page="Number(page)"
          :limit="postSize"
          :useParams="false"
          routePath="/broadcast"
        />
      </div>
      <!-- 侧边栏 -->
      <Aside />
    </div>
  </div>
</template>

<script setup>
import { mainStore } from "@/store";

const { theme } = useData();
const store = mainStore();
const props = defineProps({
  // 当前页数
  page: {
    type: Number,
    default: 1,
  },
});

// 每页文章数
const postSize = theme.value.postSize;

// 列表总数量
const allListTotal = computed(() => {
  const data = theme.value.boardcastData;
  // 返回数量
  return data ? data.length : 0;
});

// 获得当前页数
const getCurrentPage = () => {
  return props.page ? props.page - 1 : 0;
};

// 根据页数计算列表数据
const postData = computed(() => {
  const page = getCurrentPage();
  console.log("当前页数：", page);
  let data = theme.value.boardcastData;
  // 返回列表
  return data ? data.slice(page * postSize, page * postSize + postSize) : [];
});

// 恢复滚动位置
const restoreScrollY = (val) => {
  if (typeof window === "undefined" || val) return false;
  const scrollY = store.lastScrollY;
  nextTick().then(() => {
    console.log("滚动位置：", scrollY);
    // 平滑滚动
    window.scrollTo({
      top: scrollY,
      behavior: "smooth",
    });
    // 清除滚动位置
    store.lastScrollY = 0;
  });
};

// 监听加载结束
watch(
  () => store.loadingStatus,
  (val) => restoreScrollY(val),
);
</script>

<style lang="scss" scoped>
.home {
  .home-content {
    width: 100%;
    display: flex;
    flex-direction: row;
    .posts-content {
      width: calc(100% - 300px);
      transition: width 0.3s;
    }
    .main-aside {
      width: 300px;
      padding-left: 1rem;
    }
    @media (max-width: 1200px) {
      .posts-content {
        width: 100%;
      }
      .main-aside {
        display: none;
      }
    }
  }
}
</style>
