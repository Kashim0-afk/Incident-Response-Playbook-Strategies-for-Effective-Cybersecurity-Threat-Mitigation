# Template: internal communication

Internal messages during an incident have two jobs: tell people what to do (and not do), and stop rumours. Keep them short, factual and dated. Do not include technical indicators, names of suspected attackers or guesses about the cause.

If email or Teams may be compromised, send the notice through a channel the attacker cannot read: SMS, a phone tree, a message from a separate tenant, posters at the entrance.

## 1. First notice to staff

```text
Subject: [IT INCIDENT] {Service/system} unavailable – update #{n} – {date} {time}

What is happening
At {time} we detected a security incident affecting {systems or services, in plain words}.
The IT and security teams are working on it.

What this means for you
- {e.g. email and the file server are unavailable}
- {e.g. the ERP is working normally}

What we ask you to do
- Leave your computer switched on and do not restart it, unless IT tells you to.
- Do not connect USB drives or personal devices to the network.
- Do not forward this message outside the company and do not comment on social media.
- Report anything unusual (strange messages, requests for passwords or payments)
  to {phone number / contact}, not by email.

What we will never ask
We will never ask for your password or MFA code by email, chat or phone.

Next update
By {time}, through {channel}.

{Name}, {role} – {phone number}
```

## 2. Update

```text
Subject: [IT INCIDENT] {Service} – update #{n} – {date} {time}

What has changed since the last update
- {e.g. email is available again; the file server is still offline}

What you can do now
- {e.g. you can sign in again; you will be asked to set a new password}

What is still unavailable, and the estimate if we have one
- {system}: {estimate or "no estimate yet"}

Next update by {time}.
```

## 3. Management briefing

One page, read in two minutes. Send it at a fixed interval during SEV1 and SEV2.

```text
Incident {ID} – briefing #{n} – {date} {time UTC}
Severity: {SEV1–SEV4} (changed from {previous} because {reason}) | IR lead: {name}

1. Situation
   {Two or three sentences: what happened, what is affected, whether it is contained.}

2. Business impact
   - Services down: {list} since {time}
   - Customers affected: {who, how many, estimated}
   - Data possibly involved: {categories, or "under investigation"}

3. Actions since last briefing
   - {action} – {owner} – {done / in progress}

4. Decisions needed from management
   - {e.g. approve shutting down the web shop for up to 4 hours}
   - {e.g. approve engaging the external IR retainer}

5. Legal and regulatory clocks
   - GDPR: awareness at {time}; 72h deadline {date time}; DPO assessment {status}
   - NIS2: early warning due {date time} / sent {time} / not applicable because {reason}
   - Insurer notified: {yes/no, time}; law enforcement: {yes/no}

6. Next briefing: {time}
```

## Writing tips

- Say what you know and what you do not know yet. "We don't know yet whether data was copied; we will know more by 18:00" is better than silence or a guess.
- Use the same facts in every channel. Internal notices leak; write them as if they could be read by a customer.
- Name a single contact point so questions do not reach the people doing the technical work.
