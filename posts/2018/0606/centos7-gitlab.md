---
title: Centos 7 开发环境之 Gitlab 的安装及配置
tags: ["CentOS", "Git", "Gitlab", "运维"]
categories: ["运维"]
date: 2018-06-06 00:50:00 +08:00
description: 本安装指南详述了在服务器上部署GitLab CE的步骤，并提供了实践指导，以规避版本选择、防火墙及邮件服务配置等常见问题。
articleGPT: 这篇文章记录了在服务器上安装GitLab社区版（CE）的详细步骤，包括必要依赖的配置、添加正确的CE版本源、执行安装，以及SMTP邮件服务的设置。
---

最近需要在服务器上安装了 Gitlab，记录一下过程，防止下次继续踩坑。

注意：官网的教程的是 gitlab-ee 版本（企业版），需要安装的是 gitlab-ce（社区版）  

# 一、安装并配置必要的依赖关系

  1. 这部分可能系统已经安装的有了：`sudo yum install -y curl policycoreutils-python openssh-server sudo systemctl enable sshd sudo systemctl start sshd`
  2. 配置防火墙，因为Centos 7的防火墙已经不是 iptables 了，如果关闭了防火墙，可以不设置：` sudo firewall-cmd --permanent --add-service=http sudo systemctl reload firewalld `
  3. 配置邮箱服务，如果使用SMTP可以不安装，等启动gitlab的时候再设置：` sudo yum install postfix sudo systemctl enable postfix sudo systemctl start postfix `

# 二、添加Gitlab源并安装

  1. 添加Gitlab源，注意，`官网的是ee版本，需要将ee修改为ce`:` curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash `
  2. yum安装 Gitlab` yum install -y gitlab-ce `

# 三、修改配置

  1. 修改 SMTP 设置，文件为`/etc/gitlab/gitlab.rb`，不同邮箱设置相见[官网](https://docs.gitlab.com/omnibus/settings/smtp.html)：` ### Email Settings 取消注释并修改 gitlab_rails['gitlab_email_enabled'] = true gitlab_rails['gitlab_email_from'] = 'root@sixlab.cn' gitlab_rails['gitlab_email_display_name'] = 'admin' gitlab_rails['gitlab_email_reply_to'] = 'noreplay@sixlab.cn' gitlab_rails['gitlab_email_subject_suffix'] = '' ## smtp的设置，在另一处 gitlab_rails['smtp_enable'] = true gitlab_rails['smtp_address'] = "smtp.exmail.qq.com" gitlab_rails['smtp_port'] = 587 gitlab_rails['smtp_user_name'] = "root@sixlab.cn" gitlab_rails['smtp_password'] = "******" gitlab_rails['smtp_authentication'] = "login" gitlab_rails['smtp_enable_starttls_auto'] = true gitlab_rails['smtp_tls'] = true gitlab_rails['smtp_domain'] = "exmail.qq.com" `
  2. 重启gitlab：` gitlab-ctl restart;`
