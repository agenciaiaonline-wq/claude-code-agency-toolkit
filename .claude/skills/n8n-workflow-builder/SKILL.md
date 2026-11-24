---
name: n8n-workflow-builder
description: Guidelines for designing resilient, deduplicated self-hosted n8n workflows connected to WhatsApp, Redis, and CRM webhooks.
---

# n8n Workflow Engineering Skill

1. Validate webhook signatures or shared secret headers on every public HTTP trigger.
2. Filter self-echo events (`fromMe === true`) and deduplicate message IDs in Redis (`EX 300`).
3. Split sub-workflows into modular triggerable units (`01-intake`, `02-rag-lookup`, `03-handoff`) under version control with sanitized `.example.json` exports.
