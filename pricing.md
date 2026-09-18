# QuickDictate - Pricing

**QuickDictate is free for personal and any other noncommercial use (PolyForm
Noncommercial License 1.0.0, source available).** There is no subscription, no paid tier,
no QuickDictate account, and no purchase required to use any feature of the app itself.
Commercial use needs a license from LunarWerx Studios, one per installation; see
"Commercial / business use" below.

## Commercial / business use

Two plans, the same unit and the same app; they differ only in how you pay. Tax is added
at checkout where it applies. Card payment via Stripe on Connections' hosted checkout.

- Licence unit: installation. Buy one per PC and set the quantity at checkout. A licence
  key per installation is emailed on payment. QuickDictate needs no activation: the key is
  your proof of a commercial license.
- One-time: US$19.99 per installation, a perpetual license covering every release.
  Buy: https://checkout.connections.icu/licence/a0aab7bb-ba43-4d7f-8772-3c93659bad68
- Monthly: US$1.99 per installation per month, for as long as the subscription runs.
  Buy: https://checkout.connections.icu/licence/41b7e7f1-67b8-40ba-9d49-7ced20358da7
  Cancel any time, self-serve, at https://checkout.connections.icu/manage (sign in with the email
  used to pay).
- Break-even between the two: about 10 months.
- Volume, purchase orders, or anything else: open a GitHub issue.

## What you actually pay for

QuickDictate is bring-your-own-key: it is a client for speech-to-text services you already
have, not a service it resells. It never bills you and never sees a payment method.

| Component | Cost from QuickDictate | Who actually bills you |
|---|---|---|
| The QuickDictate app | $0 for noncommercial use (PolyForm Noncommercial license); commercial US$19.99 once or US$1.99/month per installation | nobody for noncommercial use; LunarWerx Studios for a commercial license |
| Local mode: Cohere Transcribe Q5 (1.65 GiB) | $0 | nobody, runs on your PC, no key, no account |
| Local mode: Whisper Large v3 Turbo Q5 (591 MiB) | $0 | nobody, runs on your PC, no key, no account |
| Cloud: ElevenLabs | $0 | ElevenLabs, via the API key you supply |
| Cloud: Deepgram | $0 | Deepgram, via the API key you supply |
| Cloud: OpenAI | $0 | OpenAI, via the API key you supply |
| Cloud: AssemblyAI | $0 | AssemblyAI, via the API key you supply |
| Cloud: DashScope | $0 | Alibaba Cloud / DashScope, via the API key you supply |
| Cloud: Google Cloud | $0 | Google Cloud, via the API key you supply |

"$0 from QuickDictate" means QuickDictate charges nothing and adds no markup on any cloud
provider's own rates. Check each provider's own pricing page for current cloud API rates.
QuickDictate does not set, cap, or mark those up.

## License

PolyForm Noncommercial 1.0.0, starting with v0.9.0 (releases through v0.8.0 were MIT, and
that grant stays in effect for those copies). Full text:
https://github.com/LunarWerxs/QuickDictate/blob/main/LICENSE

## Notes for procurement / buying agents

- The app never collects a card and has no account to create. A commercial license is
  bought on Connections' hosted checkout (Stripe), not inside the app.
- Local mode has zero ongoing or one-time cost beyond the model download itself (591 MiB
  to 1.65 GiB of disk space, fetched once from inside the app).
- Cloud provider costs are entirely optional and entirely the user's choice. QuickDictate
  works with zero cloud spend if Local mode is selected.
- No enterprise tier and no team plan; commercial licensing is per installation (above).
- Source is public on GitHub, so total cost of ownership can be verified directly:
  https://github.com/LunarWerxs/QuickDictate

Last updated: 2026-09-18
