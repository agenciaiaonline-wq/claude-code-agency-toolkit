---
name: saas-mvp-delivery
description: Standard 14-day Next.js + Supabase + Stripe delivery workflow with strict multi-tenant RLS and automated CI verification.
---

# SaaS MVP Delivery Skill

## Phase 1: Schema & Tenant Boundary
- Create `organizations` and `memberships` tables first with `ENABLE ROW LEVEL SECURITY`.
- Enforce billing entitlement updates exclusively inside verified Stripe webhooks using an event idempotency table.

## Phase 2: App Router & Verification
- Isolate cookie-aware Supabase SSR clients on the server; never ship service role keys to client code.
- Validate health routes, TypeScript strictness, and webhook replay protection in CI before launch.
