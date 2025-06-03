import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: '/favicon.png' }]
  ],

  lang: 'zh-CN',
  title: "六楼实验室",
  description: "Sixlab",
  srcDir: './src',

  sitemap: {
    hostname: 'https://sixlab.cn'
  },
  
  lastUpdated: true,

  themeConfig: {
    logo: '/logo.png',
    siteTitle: '六楼实验室',

    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/archives/' },
      {
        text: '测试', items: [
          { text: '测试1', link: '/test1' },
          { text: '测试2', link: '/test2' }
        ]
      },
      { text: '关于', link: '/about' }
    ],

    sidebar: {
      "/archives/": [
        {
          text: 'Examples',
          items: [
            { text: 'Markdown Examples', link: '/examples/' },
            { text: 'Runtime API Examples', link: '/examples/api-examples' },
            { text: 'Demo Examples', link: '/examples/demo' },
          ]
        }
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/nianqinianyi' },
      {
        icon: {
          svg:'<?xml version="1.0" encoding="utf-8"?><svg fill="#000000" width="800px" height="800px" viewBox="0 0 24 24" role="img" xmlns="http://www.w3.org/2000/svg"><path d="M11.984 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.016 0zm6.09 5.333c.328 0 .593.266.592.593v1.482a.594.594 0 0 1-.593.592H9.777c-.982 0-1.778.796-1.778 1.778v5.63c0 .327.266.592.593.592h5.63c.982 0 1.778-.796 1.778-1.778v-.296a.593.593 0 0 0-.592-.593h-4.15a.592.592 0 0 1-.592-.592v-1.482a.593.593 0 0 1 .593-.592h6.815c.327 0 .593.265.593.592v3.408a4 4 0 0 1-4 4H5.926a.593.593 0 0 1-.593-.593V9.778a4.444 4.444 0 0 1 4.445-4.444h8.296z"/></svg>'
        },
        link: '...',
        // 也可以为无障碍添加一个自定义标签 (可选但推荐):
        ariaLabel: 'cool link'
      }
    ],

    footer: {
      message: '欢迎来到六楼实验室',
      copyright: 'Copyright © 2025 Sixlab'
    },

    lastUpdated: {
      text: 'Updated at',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'medium'
      }
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    }
  
  }
})
