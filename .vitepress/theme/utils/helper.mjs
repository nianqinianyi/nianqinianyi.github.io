import { mainStore } from "@/store";
import { throttle } from "lodash-es";

/**
 * 计算滚动高度和滚动百分比
 */
export const calculateScroll = throttle(
  () => {
    try {
      if (typeof window === "undefined" || typeof document === "undefined") return false;
      const store = mainStore();
      const scrollY = window.scrollY || window.pageYOffset;
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercentage = ((scrollY / totalHeight) * 100).toFixed(0);
      // 判断滚动方向
      const scrollDirection = scrollY > store.scrollData.height ? "down" : "up";
      // 储存计算结果
      store.scrollData = {
        height: Number(scrollY.toFixed(0)),
        percentage: Number(scrollPercentage),
        direction: scrollDirection,
      };
    } catch (error) {
      console.error("计算滚动时出现错误：", error);
    }
  },
  300,
  true,
);

/**
 * 平滑滚动至目标高度或元素
 * @param {number|HTMLElement} target - 目标高度或元素
 */
export const smoothScrolling = (target = 0) => {
  try {
    if (typeof window === "undefined") return false;
    if (typeof target === "number") {
      // 滚动至指定高度
      window.scrollTo({ top: target, behavior: "smooth" });
    } else if (target instanceof HTMLElement) {
      // 滚动至元素
      const top = target.getBoundingClientRect().top - 80;
      window.scrollTo({ top, behavior: "smooth" });
    } else if (typeof target === "string" && target.startsWith("#")) {
      // 滚动至 ID
      const element = document.querySelector(target);
      if (element) {
        const top = element.getBoundingClientRect().top - 80;
        window.scrollTo({ top, behavior: "smooth" });
      }
    } else {
      // 滚动至顶部
      window.scrollTo({ top: 0, behavior: "smooth" });
    }
  } catch (error) {
    console.error("平滑滚动出错：", error);
  }
};

export const formatNumber = (n) =>{
  return String(n).padStart(2, '0')
}

/**
 * 格式化时间戳为相应的日期格式
 * 如果时间戳表示的时间为7天内，则返回 'n天内'
 * 如果时间戳表示的时间为7天之后但在当年，则返回 '月/日'
 * 如果时间戳表示的时间在当年之前，则返回 '年/月/日'
 * @param {number} timestamp - 时间戳（以毫秒为单位）
 * @return {string} 返回日期格式的字符串
 */
export const formatTimestamp = (timestamp) => {
  let now = new Date();
  // 获取今天0点
  let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  // 获取昨天0点
  let yesterday = new Date(today.getTime() - 1000 * 60 * 60 * 24);
  let targetDate = new Date(timestamp);
  // 是否为昨天
  if (targetDate >= yesterday && targetDate < today) {
    return "1天前";
  } else {
    let difference = Math.floor((today - targetDate) / (1000 * 60 * 60 * 24));
    if (difference <= 0) {
      return "今日内";
    } else if (difference < 7) {
      return `${difference}日内`;
    } else {
      const year = targetDate.getFullYear();
      const month = formatNumber(targetDate.getMonth() + 1);
      const day = formatNumber(targetDate.getDate());
      const hours = formatNumber(targetDate.getHours());
      const minutes = formatNumber(targetDate.getMinutes());
      const seconds = formatNumber(targetDate.getSeconds());
      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    }
  }
};

/**
 * 格式化时间戳为相应的日期格式
 * 如果时间戳表示的时间为7天内，则返回 'n天内'
 * 如果时间戳表示的时间为7天之后但在当年，则返回 '月/日'
 * 如果时间戳表示的时间在当年之前，则返回 '年/月/日'
 * @param {number} timestamp - 时间戳（以毫秒为单位）
 * @return {string} 返回日期格式的字符串
 */
export const formatTimestampWithTime = (timestamp) => {
  const targetDate = new Date(timestamp);

  const year = targetDate.getFullYear();
  const month = formatNumber(targetDate.getMonth() + 1);
  const day = formatNumber(targetDate.getDate());
  const hours = formatNumber(targetDate.getHours());
  const minutes = formatNumber(targetDate.getMinutes());
  const seconds = formatNumber(targetDate.getSeconds());

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
};

/**
 * 计算给定日期与当前日期相差的天数
 * @param {string} dateStr - 要计算差值的日期，为字符串形式
 * @returns {number} 天数差值
 */
export const daysFromNow = (dateStr) => {
  const currentDate = new Date();
  const inputDate = new Date(dateStr);
  const timeDiff = currentDate - inputDate;
  const dayDiff = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
  return dayDiff;
};

/**
 * 计算给定日期与当前日期相差的天数
 * @param {string} dateStr - 要计算差值的日期，为字符串形式
 * @returns {number} 天数差值
 */
export const yearDaysFromNow = (dateStr) => {
  // 1. 创建起始日期和今天的日期对象
  // 为避免时区问题，我们最好将时间都设置为0点
  const startDate = new Date(dateStr);
  startDate.setHours(0, 0, 0, 0);

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // 2. 计算基础的年份差
  let years = today.getFullYear() - startDate.getFullYear();

  // 3. 创建一个“今年”的周年纪念日，用于判断今年的生日/纪念日是否已过
  const anniversaryThisYear = new Date(startDate);
  anniversaryThisYear.setFullYear(today.getFullYear());

  // 4. 如果今天的日期小于今年的周年纪念日，说明还没满整年，年份减一
  if (today < anniversaryThisYear) {
    years--;
  }

  // 5. 计算上一个周年纪念日
  const lastAnniversary = new Date(startDate);
  lastAnniversary.setFullYear(startDate.getFullYear() + years);

  // 6. 计算上一个周年纪念日到今天的天数差
  const diffTime = today.getTime() - lastAnniversary.getTime();
  const days = Math.floor(diffTime / (1000 * 60 * 60 * 24));

  return `${years} 年 ${days} 天`;
};

/**
 * 随机前往一篇文章
 * @param {Object} postData - 文章数据
 * @returns {number} 天数差值
 */
let lastIndex = -1;
export const shufflePost = (postData) => {
  let randomIndex;
  do {
    // 随机生成一个索引值
    randomIndex = Math.floor(Math.random() * postData.length);
  } while (randomIndex === lastIndex && postData.length > 1);
  // 更新上一次的索引值
  lastIndex = randomIndex;
  // 随机文章
  const randomPost = postData[randomIndex];
  console.log(randomPost);
  // 跳转到随机文章
  return randomPost.regularPath;
};

/**
 * 复制文本到剪贴板
 * @param {string} data 要复制到剪贴板的文本
 */
export const copyText = async (data) => {
  if (navigator.clipboard) {
    try {
      await navigator.clipboard.writeText(data);
      $message.success("复制成功，在转载时请标注本文地址");
    } catch (error) {
      console.error("复制出错：", error);
      $message.error("复制出现错误，请重试");
    }
  } else {
    // 如果浏览器不支持 navigator.clipboard
    const textArea = document.createElement("textarea");
    textArea.value = data;
    document.body.appendChild(textArea);
    textArea.select();
    try {
      document.execCommand("copy");
      $message.success("复制成功，在转载时请标注本文地址");
    } catch (err) {
      console.error("复制出错：", err);
      $message.error("复制出现错误，请重试");
    } finally {
      document.body.removeChild(textArea);
    }
  }
};

/**
 * 图片 URL 复制到剪贴板
 * @param {string} imageURL 要复制到剪贴板的图片的URL
 */
export const copyImage = async (imageURL) => {
  if (!navigator.clipboard) {
    console.error("浏览器不支持 Clipboard API");
    return;
  }
  try {
    const response = await fetch(imageURL);
    const blob = await response.blob();
    await navigator.clipboard.write([
      new ClipboardItem({
        [blob.type]: blob,
      }),
    ]);
    console.log("图片已复制到剪贴板");
    $message.success("图片已复制到剪贴板");
  } catch (error) {
    console.error("复制图片出错：", error);
    $message.error("复制图片错误，请重试");
  }
};

/**
 * 下载图片
 * @param {string} imageUrl 要下载的图片的URL地址
 */
export const downloadImage = (imageUrl) => {
  try {
    // 获取当前日期并转换为字符串形式，作为文件名
    const date = new Date();
    const timestamp = date.toISOString().replace(/[:.]/g, "-");
    const imageName = `image-${timestamp}.jpg`;
    const anchor = document.createElement("a");
    anchor.download = imageName;
    anchor.href = imageUrl;
    anchor.target = "_blank";
    anchor.style.display = "none";
    document.body.appendChild(anchor);
    anchor.click();
    document.body.removeChild(anchor);
  } catch (error) {
    console.error("下载图片出错：", error);
    $message.error("下载图片错误，请重试");
  }
};

/**
 * 获取根据当前时间的问候语
 * @returns {string} 当前时间对应的问候语
 */
export const getGreetings = () => {
  const hour = new Date().getHours();
  let hello;
  if (hour < 6) {
    hello = "凌晨好，昨晚睡得怎么样？";
  } else if (hour < 9) {
    hello = "早上好，今天也要开心哦！";
  } else if (hour < 12) {
    hello = "上午好，今天也要加油哦！";
  } else if (hour < 14) {
    hello = "中午好，吃饱了精神好！";
  } else if (hour < 17) {
    hello = "下午好，继续加油！";
  } else if (hour < 19) {
    hello = "傍晚好，是时候放松一下了！";
  } else if (hour < 22) {
    hello = "晚上好，是时候休息了！";
  } else {
    hello = "夜深了，明天继续加油！";
  }
  return hello;
};

// 打乱数组 - Fisher-Yates 洗牌算法
export const shuffleArray = (array) => {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    // 解构赋值进行元素互换
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
};

// 特殊纪念日置灰
export const specialDayGray = () => {
  const specialDays = [
    { date: "4-4", name: "清明节" },
    { date: "5-12", name: "汶川大地震纪念日" },
    { date: "7-7", name: "中国人民抗日战争纪念日" },
    { date: "9-18", name: "九·一八事变纪念日" },
    { date: "12-13", name: "南京大屠杀死难者国家公祭日" },
  ];
  // 获取当天日期
  const today = new Date();
  const month = today.getMonth() + 1;
  const day = today.getDate();
  const currentDate = `${month}-${day}`;
  // 查找纪念日
  const specialDay = specialDays.find((day) => day.date === currentDate);
  if (specialDay) {
    document.documentElement.classList.add("gray");
    if (typeof $message !== "undefined") {
      $message.info(`今天是${specialDay.name}，特此默哀`, {
        duration: 8000,
        close: true,
      });
    }
  }
};
