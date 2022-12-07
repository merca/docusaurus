---
slug: day-3
title: Day 3
authors: [merca]
tags: [100daysofcode, docusaurus]
---


For the third day of my hundred days of coding journey, I decided to customize my docusaurus setup and use codespaces in GitHub for that.

Docusaurus is a static site generator that allows you to create documentation websites quickly and easily. It enables you to write content with markdown or React components while providing an intuitive user interface for customizing your website's look and feel.

Before getting started, I needed to configure Codespaces in GitHub so that it could be used as an integrated development environment (IDE) for writing code.

Simplest codespace configuration for site that is built with React:

```json title=".devcontainer/devcontainer.json"
{
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "hostRequirements": {
    "cpus": 4
  },
  "waitFor": "onCreateCommand",
  "updateContentCommand": "npm install",
  "postCreateCommand": "",
  "postAttachCommand": {
    "server": "npm run start"
  },
  "customizations": {

  },
  "portsAttributes": {
    "3000": {
      "label": "Application",
      "onAutoForward": "openPreview"
    }
  },
  "forwardPorts": [3000]
}
```
