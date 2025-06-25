<!-- AI 摘要（假） -->
<template>
  <div v-if="frontmatter.articleGPT" class="article-gpt s-card">
    <div class="title">
      <span class="name">
        <i class="iconfont icon-robot"></i>
        Ai摘要
        <!-- <i class="iconfont icon-up"></i> -->
      </span>
      <span v-if="showBroadcast" :class="['logo', { loading }]" @click="playBroadcast"> 播放 Ai Broadcast </span>
    </div>
    <div class="content s-card">
      <span class="text">{{ abstractData === "" ? "加载中..." : abstractData }}</span>
      <span v-if="loading" class="point">|</span>
    </div>
    <div class="meta">
      <span class="tip">此摘要由AI根据文章内容生成，并经过人工审核，仅用于文章内容的解释与总结</span>
      <span>
        <a href="/pages/message" class="logo report" target="_blank">投诉</a>
        <span class="logo report" @click="showOther"> Ai 说明 </span>
      </span>
    </div>
  </div>
</template>

<script setup>
const { page, frontmatter } = useData();
const router = useRouter();

// 摘要数据
const loading = ref(true);
const waitTimeOut = ref(null);
const abstractData = ref("");
const showIndex = ref(0);
const showType = ref(false);
const showBroadcast = ref(false);

// 输出摘要
const typeWriter = (text = null) => {
  try {
    const data = text || frontmatter.value.articleGPT;
    if (!data) return false;
    if (showIndex.value < data.length) {
      abstractData.value += data.charAt(showIndex.value++);
      // 生成字符延迟
      const delay = Math.random() * (30 - 10) + 10;
      setTimeout(() => {
        typeWriter(text);
      }, delay);
    } else {
      loading.value = false;
    }
  } catch (error) {
    loading.value = false;
    abstractData.value = "摘要生成失败";
    $message.error("摘要生成失败，请重试");
    console.error("摘要生成失败：", error);
  }
};

// 初始化摘要
const initAbstract = () => {
  waitTimeOut.value = setTimeout(
    () => {
      typeWriter();
    },
    Math.random() * (1200 - 800) + 800,
  );
};

// 输出摘要介绍
const showOther = () => {
  if (loading.value) return false;
  const text =
    "文章内容中，有两块 Ai 相关功能。\n"+
    "  1. 摘要助理「Ai 摘要」，由AI读取当前文章内容，并生成的摘要，仿照 GPT 的形式输出。\n" +
    "  2. 播客助理「Ai 播客」，由AI读取当前文章内容，并生成播客内容，可点击“播放 Ai Broadcast”按钮收听。";
  showIndex.value = 0;
  loading.value = true;
  abstractData.value = "";
  if (!showType.value) {
    showType.value = true;
    typeWriter(text);
  } else {
    typeWriter();
    showType.value = false;
  }
};

const playBroadcast = () => {
  const broadcast = "" || frontmatter.value.broadcast;
  if (!!broadcast) {
    let url = broadcast;
    if(typeof broadcast === "boolean"){
      url = page.value.filePath.replace(/^posts/,"/audios").replace(/md$/, "mp3");
    }

    window.$player.list.clear()
    window.$player.list.add([{
      name: frontmatter.value.title,
      title: frontmatter.value.title,
      artist: "六楼的雨",
      author: "六楼的雨",
      url: url,
      cover: "/images/post_cover/005.jpg",
    }]);
    window.$player.play();
  }
}

onMounted(() => {
  if (frontmatter.value.articleGPT) initAbstract();
  if (!!frontmatter.value.broadcast) showBroadcast.value = true;
});

onBeforeUnmount(() => {
  clearTimeout(waitTimeOut.value);
});
</script>

<style lang="scss" scoped>
.article-gpt {
  margin-top: 1.2rem;
  background-color: var(--main-card-second-background);
  user-select: none;
  cursor: auto;

  .title {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.8rem;
    padding: 0 8px;

    .name {
      display: flex;
      align-items: center;
      color: var(--main-color);
      font-weight: bold;
      cursor: pointer;

      .icon-robot {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
        font-weight: normal;
        width: 26px;
        height: 26px;
        color: var(--main-card-background);
        background-color: var(--main-color);
        border-radius: 50%;
        margin-right: 8px;
      }

      .icon-up {
        font-weight: normal;
        font-size: 12px;
        margin-left: 6px;
        opacity: 0.6;
        color: var(--main-color);
        transform: rotate(90deg);
      }
    }
  }

  .content {
    cursor: auto;
    white-space: pre-wrap;

    .point {
      color: var(--main-color);
      font-weight: bold;
      margin-left: 4px;
      animation: loading 0.8s infinite;
    }
  }

  .meta {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    margin-top: 1rem;
    padding: 0 8px;
    font-size: 12px;

    .tip {
      opacity: 0.6;
    }

    .report {
      white-space: nowrap;
      margin-left: 12px;
      opacity: 0.6;
    }
  }

  .logo {
    padding: 4px 10px;
    font-size: 12px;
    color: var(--main-card-background);
    background-color: var(--main-color);
    border-radius: 25px;
    font-weight: bold;
    cursor: pointer;

    &.loading {
      animation: loading 1s infinite;
      cursor: not-allowed;
    }
  }
}
</style>
