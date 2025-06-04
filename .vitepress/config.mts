import { defineConfig } from "vitepress"
import socialLinks from './socialLinks'
import nav from './nav'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }]
  ],

  lang: 'zh-CN',
  title: "六楼实验室",
  description: "Sixlab",
  srcDir: './posts',

  sitemap: {
    hostname: 'https://sixlab.cn'
  },
  
  themeConfig: {
    logo: '/logo.png',
    siteTitle: '六楼实验室',

    // https://vitepress.dev/reference/default-theme-config
    footer: {
      message: '欢迎来到六楼实验室',
      copyright: 'Copyright © 2025 Sixlab'
    },

    lastUpdated: {
      text: 'Updated at',
      formatOptions: {
        dateStyle: 'medium',
        timeStyle: 'medium'
      }
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    }
  
  }
})
