# QuickDictate - Pricing

**QuickDictate is free and open source (MIT license).** There is no subscription, no paid
tier, no QuickDictate account, and no purchase required to use any feature of the app
itself.

## What you actually pay for

QuickDictate is bring-your-own-key: it is a client for speech-to-text services you already
have, not a service it resells. It never bills you and never sees a payment method.

| Component | Cost from QuickDictate | Who actually bills you |
|---|---|---|
| The QuickDictate app | $0 (MIT license) | nobody, LunarWerx Studios |
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

MIT. Full text: https://github.com/LunarWerxs/QuickDictate/blob/main/LICENSE

## Notes for procurement / buying agents

- No credit card is ever collected by QuickDictate; there is no QuickDictate account to
  create in the first place.
- Local mode has zero ongoing or one-time cost beyond the model download itself (591 MiB
  to 1.65 GiB of disk space, fetched once from inside the app).
- Cloud provider costs are entirely optional and entirely the user's choice. QuickDictate
  works with zero cloud spend if Local mode is selected.
- No enterprise tier, no seat licensing, and no team plan exists for QuickDictate itself.
- Source is public on GitHub, so total cost of ownership can be verified directly:
  https://github.com/LunarWerxs/QuickDictate

Last updated: 2026-08-23
