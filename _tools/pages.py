#!/usr/bin/env python3
"""Page content for davidsonchua.cc — run via build.py"""
import os, shutil, json, html
from build import (BASE, OUT, PERSON_ID, SITE_ID, INFLUENCEES_ID, AUTOSAVE_ID,
                   PERSON, CORE_GRAPH, page, write, breadcrumb, TODAY)

# ===========================================================================
# HOME
# ===========================================================================

HOME_BODY = """
    <section class="hero">
      <div class="shell">
        <div class="portrait">
          <img src="/assets/profile-400.webp" width="132" height="132" fetchpriority="high"
               alt="Portrait of Davidson Chua, Singapore-based founder of Influencees and Autosave">
        </div>

        <h1>Davidson Chua</h1>
        <p class="lead">
          I'm a Singapore-based founder and community builder. I'm the founder and CEO of
          <a href="https://www.influencees.com" rel="noopener">Influencees</a>, the creator
          credibility and discovery platform for Southeast Asia, and the founder of
          <a href="https://www.autosave.club" rel="noopener">Autosave</a>, Singapore's most
          active automotive community.
        </p>

        <ul class="heroFacts">
          <li>Founder &amp; CEO, Influencees</li>
          <li>Founder, Autosave</li>
          <li>NUS Business Analytics</li>
          <li>Singapore</li>
        </ul>

        <div class="ctaRow">
          <a class="btn" href="/about">Read my full story</a>
          <a class="btn ghost" href="https://www.linkedin.com/in/davidsonchua/" rel="me noopener">Connect on LinkedIn</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <p class="eyebrow">By the numbers</p>
        <h2>What I've built</h2>
        <ul class="stats">
          <li><span class="statNum">20,000+</span><span class="statLabel">Autosave community members</span></li>
          <li><span class="statNum">1,200+</span><span class="statLabel">Creators indexed on Influencees</span></li>
          <li><span class="statNum">20M+</span><span class="statLabel">Monthly road-safety impressions via ROADS.sg</span></li>
          <li><span class="statNum">2</span><span class="statLabel">APAC Insider business awards</span></li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <p class="eyebrow">Ventures</p>
        <h2>What I'm working on</h2>
        <div class="cards">

          <a class="card" href="https://www.influencees.com" rel="noopener">
            <div class="cardTop">
              <span class="cardName">Influencees</span>
              <span class="tag">Founder &amp; CEO · 2026</span>
            </div>
            <p>An AI-powered creator credibility and discovery platform for Southeast Asia.
              Influencees syncs data directly from Instagram and TikTok so brands can judge
              creators on verified engagement instead of self-reported follower counts.</p>
            <span class="cardLink">www.influencees.com</span>
          </a>

          <a class="card" href="https://www.autosave.club" rel="noopener">
            <div class="cardTop">
              <span class="cardName">Autosave</span>
              <span class="tag">Founder · 2022</span>
            </div>
            <p>Singapore's most active automotive community — 20,000+ members, owner meets,
              and motoring media. Brand campaigns with Mercedes-Benz, Shell, Porsche and
              Volkswagen Group. Incubated at NUS Enterprise and BLOCK71.</p>
            <span class="cardLink">www.autosave.club</span>
          </a>

        </div>
        <p class="small muted" style="margin-top:16px">
          <a href="/ventures">More on both ventures →</a>
        </p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <p class="eyebrow">Background</p>
        <h2>How I got here</h2>
        <ul class="tl">
          <li>
            <span class="tlWhen">2026 —</span>
            <div class="tlWhat"><strong>Founder &amp; CEO, Influencees</strong>
              <p>Co-founded with Edwin Koh out of the NUS Venture Initiation Programme. Raised a
                six-figure round to build the trust layer for the creator economy.</p></div>
          </li>
          <li>
            <span class="tlWhen">2022 —</span>
            <div class="tlWhat"><strong>Founder, Autosave</strong>
              <p>Grew a Telegram group into Singapore's most active automotive community and
                incorporated it as Autosave Pte. Ltd.</p></div>
          </li>
          <li>
            <span class="tlWhen">2022–2026</span>
            <div class="tlWhat"><strong>BSc (Hons) Business Analytics, National University of Singapore</strong>
              <p>Where the analytics habit that underpins Influencees came from.</p></div>
          </li>
          <li>
            <span class="tlWhen">Earlier</span>
            <div class="tlWhat"><strong>Marine engineering — BP, and Singapore Polytechnic</strong>
              <p>Diploma with Merit in Marine Engineering, then engineering work at BP before
                moving into media and community building.</p></div>
          </li>
        </ul>
        <p class="small muted" style="margin-top:20px">
          <a href="/about">Read the longer version →</a>
        </p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <p class="eyebrow">In the press</p>
        <h2>Selected media</h2>
        <p class="muted">Featured in The Straits Times on Singapore's tech ambitions, and a guest on
          three episodes of the ST <em>Work Talk</em> podcast covering tech careers, hiring and
          generative AI. Speaker at ChargedUp 2026, Singapore's largest EV conference.</p>
        <p class="small"><a href="/media">See all media features →</a></p>
      </div>
    </section>
"""

# ===========================================================================
# ABOUT  — the Entity Home. This is the page Google reads to resolve "who".
# ===========================================================================

ABOUT_BODY = """
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">About</p>
        <h1>About Davidson Chua</h1>
        <p class="lead">
          Davidson Chua is a Singapore-based founder and community builder. He is the founder
          and CEO of Influencees, an AI-powered creator credibility and discovery platform for
          Southeast Asia, and the founder of Autosave, Singapore's most active automotive
          community with more than 20,000 members.
        </p>

        <div class="portrait" style="margin:26px 0">
          <img src="/assets/profile-400.webp" width="132" height="132"
               alt="Davidson Chua, founder and CEO of Influencees">
        </div>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>The short version</h2>
        <p>I started out as a marine engineer. I took a Diploma with Merit in Marine
          Engineering at Singapore Polytechnic and went on to work at <strong>BP</strong>, which is
          about as far from the creator economy as a career can start. What I took from it was a
          bias towards things that actually work under load — systems, not slogans.</p>

        <p>I then read Business Analytics at the <strong>National University of Singapore</strong>,
          graduating with a BSc (Honours). Somewhere in the middle of that I started a Telegram
          group for people who liked cars. That group became
          <a href="https://www.autosave.club" rel="noopener">Autosave</a>.</p>

        <h2>Autosave</h2>
        <p>Autosave grew from a chat group into Singapore's most active automotive community:
          <strong>20,000+ members</strong>, regular owner meets drawing over a thousand attendees,
          and a motoring media arm. Along the way we ran brand campaigns with
          <strong>Mercedes-Benz</strong>, <strong>Shell</strong>, <strong>Porsche</strong>,
          <strong>Volkswagen Group</strong>, Cycle &amp; Carriage, SGCarMart, Carousell Autos,
          Motorist and GetGo.</p>

        <p>The business was incorporated as <strong>Autosave Pte. Ltd.</strong> (UEN 202431449C)
          and incubated at <strong>NUS Enterprise</strong> and <strong>BLOCK71</strong>. It has been
          recognised at the <strong>APAC Insider Singapore Business Awards</strong> in 2025 and 2026.</p>

        <p>I also co-created <a href="https://baycityculture.com/" rel="noopener">Bay City Culture</a>,
          the publication where a lot of Autosave's motoring writing lives, and I contribute to
          <a href="https://roads.sg" rel="noopener">ROADS.sg</a>, which generates more than
          <strong>20 million monthly impressions</strong> on road safety in Singapore, working
          alongside the Traffic Police and the Land Transport Authority.</p>

        <h2>Influencees</h2>
        <p>Running Autosave meant sitting on both sides of a lot of brand deals, and the same
          problem kept surfacing: brands could not tell which creators were actually trusted by
          their audience. Follower count was the only number anyone had, and it is a bad number.
          Some of the most valuable creators I worked with did not have the largest followings.</p>

        <p>That became <a href="https://www.influencees.com" rel="noopener">Influencees</a>, which I
          co-founded with <strong>Edwin Koh</strong> — a relationship that started as a mentorship
          through the NUS Venture Initiation Programme (VIP@SoC). Influencees syncs performance data
          directly from Instagram and TikTok rather than relying on what creators report about
          themselves, and layers credibility signals on top: a verified creator index of
          <strong>1,200+ creators</strong>, a Trust Check, and an AI assistant for campaign work.</p>

        <p>We've raised a six-figure round and the platform is live. The longer-term goal is an
          intelligence layer for the creator economy — the place brands go to find, evaluate and
          work with creators, and the place creators go to be found on more than a vanity metric.</p>

        <blockquote>Influencees is about giving brands a better way to discover creators, while
          giving creators more opportunities to be seen.</blockquote>

        <h2>What I care about</h2>
        <p>Communities, and the infrastructure that makes them trustworthy. Almost everything I've
          built comes back to the same question: how do you know who to believe? In a car community
          that means honest reviews and real owner experience. In the creator economy it means
          verifiable data instead of screenshots. I care about building things that are useful,
          honest, and grounded in something I've actually done.</p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Quick facts</h2>
        <dl class="qa">
          <dt>Who is Davidson Chua?</dt>
          <dd>Davidson Chua is a Singapore-based entrepreneur and community builder, founder and
            CEO of Influencees and founder of Autosave.</dd>

          <dt>What does Davidson Chua do?</dt>
          <dd>He builds credibility and discovery infrastructure for the creator economy at
            Influencees, and runs Autosave, a Singapore automotive community and media business.</dd>

          <dt>Where is Davidson Chua based?</dt>
          <dd>Singapore.</dd>

          <dt>Where did Davidson Chua study?</dt>
          <dd>He holds a BSc (Honours) in Business Analytics from the National University of
            Singapore, and a Diploma with Merit in Marine Engineering from Singapore Polytechnic.</dd>

          <dt>What is Influencees?</dt>
          <dd>Influencees is an AI-powered creator credibility and discovery platform for Southeast
            Asia, co-founded by Davidson Chua and Edwin Koh in 2026. It syncs data directly from
            Instagram and TikTok so brands can evaluate creators on verified engagement.</dd>

          <dt>What is Autosave?</dt>
          <dd>Autosave (Autosave Pte. Ltd., UEN 202431449C) is Singapore's most active automotive
            community, founded by Davidson Chua in 2022, with more than 20,000 members.</dd>

          <dt>How can I contact Davidson Chua?</dt>
          <dd>By <a href="mailto:davidsonchua@outlook.com">email</a>,
            <a href="https://www.linkedin.com/in/davidsonchua/" rel="me noopener">LinkedIn</a> or
            <a href="https://t.me/davidsonchua" rel="me noopener">Telegram</a>. See the
            <a href="/contact">contact page</a>.</dd>
        </dl>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Elsewhere on the web</h2>
        <p class="muted">These are the profiles I actually maintain. If you find a "Davidson Chua"
          somewhere that isn't listed here, it probably isn't me.</p>
        <ul class="contactList">
          <li><span class="k">LinkedIn</span><a href="https://www.linkedin.com/in/davidsonchua/" rel="me noopener">linkedin.com/in/davidsonchua</a></li>
          <li><span class="k">Crunchbase</span><a href="https://www.crunchbase.com/person/davidson-chua-cc" rel="me noopener">crunchbase.com/person/davidson-chua-cc</a></li>
          <li><span class="k">Medium</span><a href="https://davidsonchua.medium.com/" rel="me noopener">davidsonchua.medium.com</a></li>
          <li><span class="k">X</span><a href="https://x.com/davidsonchua" rel="me noopener">x.com/davidsonchua</a></li>
          <li><span class="k">Telegram</span><a href="https://t.me/davidsonchua" rel="me noopener">t.me/davidsonchua</a></li>
          <li><span class="k">Press enquiries</span><a href="https://www.helpareporter.com/journalist/davidsonchua" rel="me noopener">Connectively / HARO</a></li>
        </ul>
      </div>
    </section>
"""

# ===========================================================================
# VENTURES
# ===========================================================================

VENTURES_BODY = """
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">Ventures</p>
        <h1>Companies founded by Davidson Chua</h1>
        <p class="lead">Two businesses, both built around the same idea: communities work when
          people can tell who to trust.</p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Influencees</h2>
        <p class="muted small">Founder &amp; CEO · Founded 2026 · Singapore ·
          <a href="https://www.influencees.com" rel="noopener">influencees.com</a></p>

        <p>Influencees is an AI-powered creator credibility and discovery platform for Southeast
          Asia. Rather than trusting the numbers creators report about themselves, Influencees syncs
          performance data directly from <strong>Instagram and TikTok</strong>, then layers
          credibility signals on top so brands can evaluate who is genuinely trusted by an audience.</p>

        <h3>What's in it</h3>
        <ul>
          <li><strong>Verified creator index</strong> — 1,200+ creators with engagement figures pulled from source, not screenshots.</li>
          <li><strong>Trust Check</strong> — a credibility assessment for individual creators.</li>
          <li><strong>Ai-kyo</strong> — an AI assistant for campaign insight and content ideation.</li>
          <li><strong>Campaign workspace</strong> — brief, shortlist, brief and track collaborations in one place.</li>
          <li><strong>Creator Pro</strong> — a dashboard letting creators surface their real performance to brands.</li>
        </ul>

        <h3>Story</h3>
        <p>Co-founded with <strong>Edwin Koh</strong>, whom I first met through the NUS Venture
          Initiation Programme (VIP@SoC) as a mentor. We've raised a six-figure round. Influencees
          also runs the <strong>Creator Creates Series</strong>, a creator hackathon.</p>

        <p><a class="btn ghost" href="https://www.influencees.com" rel="noopener">Visit Influencees</a></p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Autosave</h2>
        <p class="muted small">Founder · Founded 2022 · Autosave Pte. Ltd. (UEN 202431449C) ·
          <a href="https://www.autosave.club" rel="noopener">autosave.club</a></p>

        <p>Autosave is Singapore's most active automotive community — cars, media and meets. It
          started as a Telegram group and grew into a network of <strong>20,000+ members</strong>
          across Telegram and social channels, with owner meets that have drawn over a thousand
          attendees.</p>

        <h3>Brand campaigns</h3>
        <p class="muted">Mercedes-Benz · Shell · Porsche · Volkswagen Group · Cycle &amp; Carriage ·
          SGCarMart · Carousell Autos · Motorist · GetGo · SingSaver · MoneySmart</p>

        <h3>Recognition</h3>
        <ul>
          <li>APAC Insider Singapore Business Awards — 2025 and 2026</li>
          <li>Incubated at NUS Enterprise and BLOCK71</li>
        </ul>

        <h3>Channels</h3>
        <ul>
          <li><a href="https://baycityculture.com/" rel="noopener">Bay City Culture</a> — the motoring publication</li>
          <li>Telegram: @AutoSaveClub, @sgcarnews, @sgcarmeets</li>
        </ul>

        <p><a class="btn ghost" href="https://www.autosave.club" rel="noopener">Visit Autosave</a></p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Also involved in</h2>
        <div class="cards">
          <a class="card" href="https://roads.sg" rel="noopener">
            <div class="cardTop"><span class="cardName">ROADS.sg</span><span class="tag">Contributor</span></div>
            <p>Road safety media generating 20M+ monthly impressions across Singapore, working
              directly with the Traffic Police and the Land Transport Authority.</p>
            <span class="cardLink">roads.sg</span>
          </a>
          <a class="card" href="https://baycityculture.com/" rel="noopener">
            <div class="cardTop"><span class="cardName">Bay City Culture</span><span class="tag">Co-founder &amp; editor</span></div>
            <p>A Singapore motoring publication covering EVs, COE, ERP, charging infrastructure
              and the cost of car ownership.</p>
            <span class="cardLink">baycityculture.com</span>
          </a>
        </div>
      </div>
    </section>
"""

# ===========================================================================
# MEDIA
# ===========================================================================

MEDIA_BODY = """
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">Media</p>
        <h1>Davidson Chua in the press</h1>
        <p class="lead">Features, podcast appearances and speaking engagements. If you're a
          journalist looking for comment on the creator economy, community building or Singapore's
          automotive market, <a href="/contact">get in touch</a>.</p>
      </div>
    </section>

    <section class="section">
      <div class="shell">

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">The Straits Times</span><span class="tag">Feature</span></div>
          <h3>Singapore's tech ambitions</h3>
          <p class="muted">Contributed perspective alongside industry experts in a Straits Times
            feature on where Singapore's technology sector is heading.</p>
          <p class="small"><a href="https://str.sg/wVR6" rel="noopener">str.sg/wVR6</a> ·
            <a href="https://str.sg/wVR2" rel="noopener">str.sg/wVR2</a></p>
          <figure>
            <img src="/assets/media/straits-times-feature.webp" width="1000" height="1164" loading="lazy" decoding="async"
                 alt="The Straits Times feature quoting Davidson Chua on Singapore's tech ambitions">
          </figure>
          <p class="credit">Photo credit: The Straits Times</p>
        </article>

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">ST Work Talk podcast</span><span class="tag">Guest</span></div>
          <h3>Singapore's rise as a tech city — and what it means for Singaporeans</h3>
          <p class="muted">On what the country's technology growth actually means for people
            entering the workforce.</p>
          <p class="small"><a href="https://www.straitstimes.com/business/work-talk-podcast-singapore-s-rise-as-a-tech-city-and-what-it-means-for-singaporeans" rel="noopener">Listen to the episode</a></p>
          <figure>
            <img src="/assets/media/podcast-tech-city.webp" width="860" height="573" loading="lazy" decoding="async"
                 alt="Straits Times Work Talk podcast episode on Singapore as a tech city, featuring Davidson Chua">
          </figure>
          <p class="credit">Photo credit: The Straits Times</p>
        </article>

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">ST Work Talk podcast</span><span class="tag">Guest</span></div>
          <h3>Where the tech jobs are</h3>
          <p class="muted">A conversation on where technology roles are genuinely being created,
            and how graduates can navigate an increasingly competitive market.</p>
          <p class="small"><a href="https://www.straitstimes.com/business/work-talk-podcast-where-the-tech-jobs-are" rel="noopener">Listen to the episode</a></p>
          <figure>
            <img src="/assets/media/podcast-tech-jobs.webp" width="860" height="573" loading="lazy" decoding="async"
                 alt="Straits Times Work Talk podcast episode on tech jobs, featuring Davidson Chua">
          </figure>
          <p class="credit">Photo credit: The Straits Times</p>
        </article>

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">The Straits Times</span><span class="tag">Guest</span></div>
          <h3>Gen AI: you started work yet?</h3>
          <p class="muted">On beginning a career in a world shaped by tools like ChatGPT, and how
            expectations are shifting for young professionals.</p>
          <p class="small"><a href="https://www.straitstimes.com/business/gen-ai-you-started-work-yet" rel="noopener">Listen to the episode</a></p>
          <figure>
            <img src="/assets/media/podcast-gen-ai.webp" width="860" height="573" loading="lazy" decoding="async"
                 alt="Straits Times podcast on generative AI, featuring Davidson Chua">
          </figure>
          <p class="credit">Photo credit: The Straits Times</p>
        </article>

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">NUS Computing</span><span class="tag">Profile</span></div>
          <h3>How Influencees is building the AI layer for the creator economy</h3>
          <p class="muted">NUS School of Computing on the founding of Influencees, the NUS Venture
            Initiation Programme, and the thesis behind the platform.</p>
          <p class="small"><a href="https://www.comp.nus.edu.sg/news/how-influencees-is-building-the-ai-layer-for-the-creator-economy/" rel="noopener">Read the article</a></p>
        </article>

        <article class="mediaItem">
          <div class="mediaMeta"><span class="outlet">ChargedUp 2026</span><span class="tag">Speaker</span></div>
          <h3>Singapore's largest EV conference</h3>
          <p class="muted">Speaker at ChargedUp 2026, 23–24 July 2026, Perennial Business City,
            Singapore.</p>
          <p class="small"><a href="https://www.chargedup.asia/" rel="noopener">chargedup.asia</a></p>
        </article>

      </div>
    </section>
"""

# ===========================================================================
# CONTACT
# ===========================================================================

CONTACT_BODY = """
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">Contact</p>
        <h1>Contact Davidson Chua</h1>
        <p class="lead">Open to conversations about the creator economy, community building,
          brand partnerships, press comment and speaking.</p>

        <ul class="contactList">
          <li><span class="k">Email</span><a href="mailto:davidsonchua@outlook.com">davidsonchua@outlook.com</a></li>
          <li><span class="k">LinkedIn</span><a href="https://www.linkedin.com/in/davidsonchua/" rel="me noopener">linkedin.com/in/davidsonchua</a></li>
          <li><span class="k">Telegram</span><a href="https://t.me/davidsonchua" rel="me noopener">t.me/davidsonchua</a></li>
          <li><span class="k">X</span><a href="https://x.com/davidsonchua" rel="me noopener">@davidsonchua</a></li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>For journalists</h2>
        <p>I'm available for comment on the creator economy and influencer marketing in Southeast
          Asia, community building, and Singapore's automotive and EV market. I'm listed on
          <a href="https://www.helpareporter.com/journalist/davidsonchua" rel="noopener">Connectively (formerly HARO)</a>.</p>

        <h3>Short bio (for use in articles)</h3>
        <p class="muted">Davidson Chua is the founder and CEO of Influencees, an AI-powered creator
          credibility and discovery platform for Southeast Asia, and the founder of Autosave,
          Singapore's most active automotive community with over 20,000 members. He holds a BSc
          (Honours) in Business Analytics from the National University of Singapore.</p>

        <h3>Headshot</h3>
        <p class="small"><a href="/assets/profile-800.webp" download>Download high-resolution photo (800×800)</a></p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Business details</h2>
        <ul class="contactList">
          <li><span class="k">Influencees</span><a href="https://www.influencees.com" rel="noopener">influencees.com</a></li>
          <li><span class="k">Autosave</span><a href="https://www.autosave.club" rel="noopener">autosave.club — Autosave Pte. Ltd., UEN 202431449C</a></li>
          <li><span class="k">Location</span><span>Singapore</span></li>
        </ul>
      </div>
    </section>
"""

# ===========================================================================
# WRITING
# ===========================================================================

POSTS = [
    {
        "slug": "follower-count-is-a-bad-proxy-for-trust",
        "title": "Follower count is a bad proxy for trust",
        "desc": ("Why the creator economy's default metric measures the wrong thing, and what "
                 "building a 20,000-member community taught Davidson Chua about credibility."),
        "date": "2026-08-16",
        "readable_date": "16 August 2026",
        "body": """
        <p>I have spent the last four years on both sides of a lot of brand deals. First as the
        person running <a href="https://www.autosave.club" rel="noopener">Autosave</a>, a car
        community in Singapore that grew from a Telegram group into something with 20,000-odd
        members. Then as the person building
        <a href="https://www.influencees.com" rel="noopener">Influencees</a>, which exists because of
        a problem I kept running into from the first side.</p>

        <p>The problem is this. When a brand decides who to work with, the number they reach for
        first is follower count. It is the only number that is visible, standardised and free. And
        it is close to useless.</p>

        <h2>What follower count actually measures</h2>
        <p>Follower count measures accumulated reach. It tells you how many accounts, at some point,
        pressed a button. It does not tell you whether those accounts are still active, whether they
        see the content, whether they believe it, or whether they would act on a recommendation.</p>

        <p>In a car community you notice this fast, because the feedback loop is short and physical.
        Someone posts a recommendation about a workshop, a tint shop, a tyre. If they are trusted,
        people go. If they are not, nothing happens, and everyone can see that nothing happened.
        After a while you learn who moves people and who just has an audience.</p>

        <p>The two lists barely overlap.</p>

        <h2>The most valuable creators are often not the biggest</h2>
        <p>Some of the most valuable people I worked with at Autosave had a few thousand followers.
        They had spent years answering questions in comments, they owned the car they were talking
        about, and when they said something was worth buying, members bought it. Meanwhile plenty of
        larger accounts produced campaign posts that sank without trace.</p>

        <p>This is not a novel observation — everyone in the industry says it. What nobody had was a
        way to act on it. If you cannot measure credibility, you fall back on the number you can
        measure, even knowing it is the wrong one. That is not stupidity, it is the absence of an
        alternative.</p>

        <h2>Why self-reported data does not fix it</h2>
        <p>The usual patch is a media kit: a creator sends over engagement rates, audience
        demographics, past campaign results. The problem is obvious once you have seen a few. The
        creator picks which numbers to show, which window to show them over, and which campaigns to
        mention. It is a CV, not an audit.</p>

        <p>I do not think creators are being dishonest when they do this. Everybody presents their
        best case. But a market where every participant self-reports their own quality is a market
        with no price signal.</p>

        <h2>What we built instead</h2>
        <p>Influencees syncs performance data directly from Instagram and TikTok rather than
        accepting what a creator reports. That single change does most of the work: the same
        methodology applied to every creator, over the same window, without anyone choosing which
        slice to show.</p>

        <p>On top of that sits the part I actually care about — credibility signals. Consistency over
        time. Whether engagement comes from an audience that behaves like a real audience. Whether
        the creator's stated niche matches what they actually post. None of this is exotic
        analytics. It is just what you would check manually if you had the time, applied to 1,200+
        creators instead of five.</p>

        <p>The goal is not to replace judgement. It is to make sure the judgement starts from a
        number that means something.</p>

        <h2>The uncomfortable part</h2>
        <p>A trust layer only works if it is willing to say unflattering things. A credibility score
        that never comes back low is a marketing asset, not a measurement. That tension is the whole
        business, and it is the part we will get judged on.</p>

        <p>Communities taught me that trust is not a feature you ship. It is the accumulated
        residue of being right in public, repeatedly, including when it costs you something. I would
        like the infrastructure to reflect that.</p>
        """,
    }
]

EXTERNAL_WRITING = [
    ("Why are cars in Singapore getting bigger in 2025?",
     "https://medium.com/motoringclub/why-are-cars-in-singapore-getting-bigger-in-2025-1df9a1b4cb09",
     "MotoringClub"),
    ("ERP 2 location-based charging is coming",
     "https://baycityculture.com/", "Bay City Culture"),
    ("Nearly 6 in 10 new cars registered in Singapore are now EVs",
     "https://baycityculture.com/", "Bay City Culture"),
    ("When can an EV battery be repaired, and when must it be replaced?",
     "https://baycityculture.com/", "Bay City Culture"),
    ("The problem with bicycles in Singapore",
     "https://davidsonchua.medium.com/the-problem-with-bicycles-in-singapore-aec9947b6b03",
     "Medium"),
]


def writing_index_body():
    native = "\n".join(
        f"""          <li>
            <h3><a href="/writing/{p['slug']}">{html.escape(p['title'])}</a></h3>
            <div class="postMeta">{p['readable_date']}</div>
            <p>{html.escape(p['desc'])}</p>
          </li>""" for p in POSTS)
    external = "\n".join(
        f"""          <li>
            <h3><a href="{u}" rel="noopener">{html.escape(t)}</a></h3>
            <div class="postMeta">{html.escape(src)}</div>
          </li>""" for t, u, src in EXTERNAL_WRITING)
    return f"""
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">Writing</p>
        <h1>Writing by Davidson Chua</h1>
        <p class="lead">Notes on the creator economy, community building, and Singapore's
          automotive and EV market.</p>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Here</h2>
        <ul class="posts">
{native}
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="shell">
        <h2>Elsewhere</h2>
        <p class="muted small">Published on
          <a href="https://baycityculture.com/" rel="noopener">Bay City Culture</a> and
          <a href="https://davidsonchua.medium.com/" rel="noopener">Medium</a>.</p>
        <ul class="posts">
{external}
        </ul>
      </div>
    </section>
"""


def post_body(p):
    return f"""
    <article class="article">
      <div class="shell">
        <p class="eyebrow">Writing</p>
        <h1>{html.escape(p['title'])}</h1>
        <div class="articleMeta">By Davidson Chua · <time datetime="{p['date']}">{p['readable_date']}</time></div>
        <div class="articleBody">
{p['body']}
        </div>

        <div class="authorBox">
          <img src="/assets/profile-264.webp" width="56" height="56" loading="lazy"
               alt="Davidson Chua">
          <div>
            <strong>Davidson Chua</strong>
            <p>Founder &amp; CEO of <a href="https://www.influencees.com" rel="noopener">Influencees</a>
              and founder of <a href="https://www.autosave.club" rel="noopener">Autosave</a>, based in
              Singapore. <a href="/about">More about me →</a></p>
          </div>
        </div>
      </div>
    </article>
"""


# ===========================================================================
# 404
# ===========================================================================

NOTFOUND_BODY = """
    <section class="section tight">
      <div class="shell">
        <p class="eyebrow">404</p>
        <h1>Page not found</h1>
        <p class="lead">That page doesn't exist. Try the <a href="/">homepage</a> or read
          <a href="/about">about Davidson Chua</a>.</p>
      </div>
    </section>
"""


# ===========================================================================
# BUILD
# ===========================================================================

def build():
    # ---- Home
    write("/", page(
        path="/",
        title="Davidson Chua — Founder of Influencees & Autosave | Singapore",
        desc=("Davidson Chua is a Singapore-based founder and community builder. Founder & CEO of "
              "Influencees, the creator credibility platform for Southeast Asia, and founder of "
              "Autosave, Singapore's most active automotive community (20,000+ members)."),
        body=HOME_BODY,
        current="/",
        graph_extra=[{
            "@type": "WebPage",
            "@id": f"{BASE}/#webpage",
            "url": f"{BASE}/",
            "name": "Davidson Chua — Founder of Influencees & Autosave",
            "isPartOf": {"@id": SITE_ID},
            "about": {"@id": PERSON_ID},
            "primaryImageOfPage": {"@id": f"{BASE}/#primaryimage"},
            "inLanguage": "en-SG",
            "datePublished": "2026-01-01",
            "dateModified": TODAY,
        }],
    ))

    # ---- About (Entity Home: ProfilePage)
    write("/about", page(
        path="/about",
        title="About Davidson Chua — Singapore Founder, Influencees & Autosave",
        desc=("Full biography of Davidson Chua: Singapore-based founder and CEO of Influencees, "
              "founder of Autosave, NUS Business Analytics graduate. Career, ventures, education "
              "and verified profiles."),
        body=ABOUT_BODY,
        current="/about",
        og_type="profile",
        graph_extra=[{
            "@type": "ProfilePage",
            "@id": f"{BASE}/about#profilepage",
            "url": f"{BASE}/about",
            "name": "About Davidson Chua",
            "isPartOf": {"@id": SITE_ID},
            "mainEntity": {"@id": PERSON_ID},
            "about": {"@id": PERSON_ID},
            "primaryImageOfPage": {"@id": f"{BASE}/#primaryimage"},
            "inLanguage": "en-SG",
            "dateCreated": "2026-01-01",
            "dateModified": TODAY,
            "breadcrumb": {"@id": f"{BASE}/about#breadcrumb"},
        }, {
            "@type": "BreadcrumbList",
            "@id": f"{BASE}/about#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": "About", "item": f"{BASE}/about"},
            ],
        }],
    ))

    # ---- Ventures
    write("/ventures", page(
        path="/ventures",
        title="Ventures — Companies Founded by Davidson Chua",
        desc=("Influencees, the AI-powered creator credibility platform for Southeast Asia, and "
              "Autosave, Singapore's most active automotive community — both founded by Davidson Chua."),
        body=VENTURES_BODY,
        current="/ventures",
        graph_extra=[{
            "@type": "CollectionPage",
            "@id": f"{BASE}/ventures#webpage",
            "url": f"{BASE}/ventures",
            "name": "Ventures — Companies Founded by Davidson Chua",
            "isPartOf": {"@id": SITE_ID},
            "about": {"@id": PERSON_ID},
            "inLanguage": "en-SG",
            "dateModified": TODAY,
            "mainEntity": {
                "@type": "ItemList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "item": {"@id": INFLUENCEES_ID}},
                    {"@type": "ListItem", "position": 2, "item": {"@id": AUTOSAVE_ID}},
                ],
            },
            "breadcrumb": {"@id": f"{BASE}/ventures#breadcrumb"},
        }, {
            "@type": "BreadcrumbList",
            "@id": f"{BASE}/ventures#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": "Ventures", "item": f"{BASE}/ventures"},
            ],
        }],
    ))

    # ---- Media
    write("/media", page(
        path="/media",
        title="Media & Press — Davidson Chua",
        desc=("Press features, podcast appearances and speaking engagements for Davidson Chua, "
              "including The Straits Times, ST Work Talk, NUS Computing and ChargedUp 2026."),
        body=MEDIA_BODY,
        current="/media",
        graph_extra=[{
            "@type": "CollectionPage",
            "@id": f"{BASE}/media#webpage",
            "url": f"{BASE}/media",
            "name": "Media & Press — Davidson Chua",
            "isPartOf": {"@id": SITE_ID},
            "about": {"@id": PERSON_ID},
            "inLanguage": "en-SG",
            "dateModified": TODAY,
            "breadcrumb": {"@id": f"{BASE}/media#breadcrumb"},
        }, {
            "@type": "BreadcrumbList",
            "@id": f"{BASE}/media#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": "Media", "item": f"{BASE}/media"},
            ],
        }],
    ))

    # ---- Contact
    write("/contact", page(
        path="/contact",
        title="Contact Davidson Chua — Singapore",
        desc=("Get in touch with Davidson Chua, founder of Influencees and Autosave. Email, "
              "LinkedIn, Telegram, press bio and headshot."),
        body=CONTACT_BODY,
        current="/contact",
        graph_extra=[{
            "@type": "ContactPage",
            "@id": f"{BASE}/contact#webpage",
            "url": f"{BASE}/contact",
            "name": "Contact Davidson Chua",
            "isPartOf": {"@id": SITE_ID},
            "about": {"@id": PERSON_ID},
            "mainEntity": {"@id": PERSON_ID},
            "inLanguage": "en-SG",
            "dateModified": TODAY,
            "breadcrumb": {"@id": f"{BASE}/contact#breadcrumb"},
        }, {
            "@type": "BreadcrumbList",
            "@id": f"{BASE}/contact#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": "Contact", "item": f"{BASE}/contact"},
            ],
        }],
    ))

    # ---- Writing index
    write("/writing", page(
        path="/writing",
        title="Writing — Davidson Chua",
        desc=("Essays and notes by Davidson Chua on the creator economy, community building and "
              "Singapore's automotive and EV market."),
        body=writing_index_body(),
        current="/writing",
        graph_extra=[{
            "@type": "Blog",
            "@id": f"{BASE}/writing#blog",
            "url": f"{BASE}/writing",
            "name": "Writing — Davidson Chua",
            "description": "Essays on the creator economy, community building and Singapore motoring.",
            "isPartOf": {"@id": SITE_ID},
            "author": {"@id": PERSON_ID},
            "publisher": {"@id": PERSON_ID},
            "inLanguage": "en-SG",
            "blogPost": [{"@id": f"{BASE}/writing{p['slug']}/#article"} for p in POSTS],
            "breadcrumb": {"@id": f"{BASE}/writing#breadcrumb"},
        }, {
            "@type": "BreadcrumbList",
            "@id": f"{BASE}/writing#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                {"@type": "ListItem", "position": 2, "name": "Writing", "item": f"{BASE}/writing"},
            ],
        }],
    ))

    # ---- Posts
    for p in POSTS:
        url = f"{BASE}/writing{p['slug']}/"
        write(f"/writing/{p['slug']}", page(
            path=f"/writing/{p['slug']}",
            title=f"{p['title']} — Davidson Chua",
            desc=p["desc"],
            body=post_body(p),
            current="/writing",
            og_type="article",
            graph_extra=[{
                "@type": "BlogPosting",
                "@id": f"{url}#article",
                "headline": p["title"],
                "description": p["desc"],
                "url": url,
                "mainEntityOfPage": {"@type": "WebPage", "@id": url},
                "datePublished": p["date"],
                "dateModified": p["date"],
                "author": {"@id": PERSON_ID},
                "publisher": {"@id": PERSON_ID},
                "isPartOf": {"@id": f"{BASE}/writing#blog"},
                "image": {"@id": f"{BASE}/#primaryimage"},
                "inLanguage": "en-SG",
                "about": [
                    {"@type": "Thing", "name": "Creator economy"},
                    {"@type": "Thing", "name": "Influencer marketing"},
                    {"@id": INFLUENCEES_ID},
                ],
                "breadcrumb": {
                    "@type": "BreadcrumbList",
                    "itemListElement": [
                        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE}/"},
                        {"@type": "ListItem", "position": 2, "name": "Writing", "item": f"{BASE}/writing"},
                        {"@type": "ListItem", "position": 3, "name": p["title"], "item": url},
                    ],
                },
            }],
        ))

    # ---- 404 (flat file)
    nf = page(path="/404.html", title="Page not found — Davidson Chua",
              desc="Page not found on davidsonchua.cc", body=NOTFOUND_BODY)
    nf = nf.replace('<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">',
                    '<meta name="robots" content="noindex, follow">')
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(nf)
    print("wrote site/404.html")

    # ---- sitemap.xml
    urls = [("/", "1.0"), ("/about", "0.9"), ("/ventures", "0.8"),
            ("/writing", "0.8"), ("/media", "0.7"), ("/contact", "0.6")]
    urls += [(f"/writing/{p['slug']}", "0.7") for p in POSTS]
    entries = "\n".join(
        f"  <url>\n    <loc>{BASE}{u}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>"
        for u, _ in urls)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n')
    print("wrote site/sitemap.xml")

    # ---- robots.txt
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"""# davidsonchua.cc
User-agent: *
Allow: /

# AI crawlers are welcome — being cited in AI answers is a discovery channel.
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {BASE}/sitemap.xml
""")
    print("wrote site/robots.txt")

    # ---- llms.txt
    with open(os.path.join(OUT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(f"""# Davidson Chua

> Davidson Chua is a Singapore-based founder and community builder. He is the founder and
> CEO of Influencees, an AI-powered creator credibility and discovery platform for Southeast
> Asia, and the founder of Autosave, Singapore's most active automotive community with more
> than 20,000 members. He holds a BSc (Honours) in Business Analytics from the National
> University of Singapore.

## Pages

- [About Davidson Chua]({BASE}/about): Full biography, career history, education and verified profiles.
- [Ventures]({BASE}/ventures): Influencees and Autosave in detail.
- [Writing]({BASE}/writing): Essays on the creator economy and Singapore motoring.
- [Media]({BASE}/media): Press features, podcasts and speaking.
- [Contact]({BASE}/contact): Email, social profiles, press bio and headshot.

## Verified profiles

- LinkedIn: https://www.linkedin.com/in/davidsonchua/
- Crunchbase: https://www.crunchbase.com/person/davidson-chua-cc
- Medium: https://davidsonchua.medium.com/
- X: https://x.com/davidsonchua
- Telegram: https://t.me/davidsonchua

## Disambiguation

Other people share the name "Davidson Chua". This site refers specifically to the founder of
Influencees and Autosave, based in Singapore.
""")
    print("wrote site/llms.txt")

    # ---- RSS
    items = "\n".join(f"""    <item>
      <title>{html.escape(p['title'])}</title>
      <link>{BASE}/writing{p['slug']}/</link>
      <guid isPermaLink="true">{BASE}/writing{p['slug']}/</guid>
      <description>{html.escape(p['desc'])}</description>
      <dc:creator>Davidson Chua</dc:creator>
    </item>""" for p in POSTS)
    os.makedirs(os.path.join(OUT, "writing"), exist_ok=True)
    with open(os.path.join(OUT, "writing", "feed.xml"), "w", encoding="utf-8") as f:
        f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Davidson Chua — Writing</title>
    <link>{BASE}/writing</link>
    <atom:link href="{BASE}/writingfeed.xml" rel="self" type="application/rss+xml"/>
    <description>Essays on the creator economy, community building and Singapore motoring.</description>
    <language>en-SG</language>
{items}
  </channel>
</rss>
""")
    print("wrote site/writing/feed.xml")

    # ---- webmanifest
    with open(os.path.join(OUT, "site.webmanifest"), "w", encoding="utf-8") as f:
        json.dump({
            "name": "Davidson Chua",
            "short_name": "Davidson Chua",
            "start_url": "/",
            "display": "standalone",
            "background_color": "#ffffff",
            "theme_color": "#ffffff",
            "icons": [
                {"src": "/web-app-manifest-192x192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
                {"src": "/web-app-manifest-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
            ],
        }, f, indent=2)
    print("wrote site/site.webmanifest")

    # ---- vercel.json (matches the existing deployment: cleanUrls, no trailing slash)
    with open(os.path.join(OUT, "vercel.json"), "w", encoding="utf-8") as f:
        json.dump({
            "cleanUrls": True,
            "trailingSlash": False,
            "redirects": [
                {"source": "/index.html", "destination": "/", "permanent": True},
                {"source": "/about.html", "destination": "/about", "permanent": True},
            ],
            "headers": [
                {"source": "/(.*)", "headers": [
                    {"key": "X-Content-Type-Options", "value": "nosniff"},
                    {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                    {"key": "Strict-Transport-Security", "value": "max-age=63072000; includeSubDomains; preload"},
                    {"key": "X-Frame-Options", "value": "SAMEORIGIN"},
                    {"key": "Permissions-Policy", "value": "geolocation=(), microphone=(), camera=()"},
                ]},
                {"source": "/assets/(.*)", "headers": [
                    {"key": "Cache-Control", "value": "public, max-age=31536000, immutable"},
                ]},
            ],
        }, f, indent=2)
    print("wrote site/vercel.json")


if __name__ == "__main__":
    build()
