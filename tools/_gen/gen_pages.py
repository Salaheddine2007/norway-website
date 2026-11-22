"""Generates tools/pages/{en,no}/*.html for iptvnorwayone.com from one set of helpers + per-language copy."""
import json, os

ROOT = r"C:\Users\DELL\Desktop\norway-website"
BASE = "https://iptvnorwayone.com"
SITE = json.load(open(os.path.join(ROOT, "tools", "site.json"), encoding="utf-8"))
EUR, NOK = SITE["prices_eur"], SITE["prices_nok"]

def hdr(meta):
    return "<!--" + json.dumps(meta, ensure_ascii=False, indent=0).replace("\n", " ") + "-->\n"

def save(lang, slug, meta, body):
    meta = dict(meta); meta["slug"] = slug
    d = os.path.join(ROOT, "tools", "pages", lang); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, (slug or "index") + ".html"), "w", encoding="utf-8", newline="\n").write(hdr(meta) + body.strip() + "\n")


SLIDER_TXT = {
    "en": ("On your screen", "Norwegian TV brands and big-screen titles",
           "A taste of what Norwegian viewers look for. Ask us about a specific channel before you order.",
           "Channel names and logos belong to their owners and are shown only to identify the channels. IPTV Norway One has no affiliation with them, and the line-up can change over time. Posters are shown for illustration."),
    "no": ("På skjermen din", "Norske TV-merker og store titler",
           "Et utvalg av det norske seere leter etter. Spør oss om en bestemt kanal før du bestiller.",
           "Kanalnavn og logoer tilhører eierne og vises bare for å identifisere kanalene. IPTV Norway One har ingen tilknytning til dem, og kanalutvalget kan endre seg over tid. Plakatene vises som illustrasjon."),
}
LOGOS = [("nrk.svg", "NRK", 614, 220), ("tv2.webp", "TV 2", 108, 140), ("tv2-nyhetene.webp", "TV 2 Nyhetene", 581, 140), ("tv2-direkte.webp", "TV 2 Direkte", 574, 140), ("tv2-sport.webp", "TV 2 Sport", 409, 140), ("tvnorge.svg", "TVNorge", 512, 512), ("tv3.webp", "TV3", 140, 140), ("vsport1.webp", "V Sport 1", 126, 140), ("eurosport.webp", "Eurosport", 604, 140), ("sportkanalen.webp", "Sportkanalen", 104, 140), ("visjon-norge.webp", "TV Visjon Norge", 192, 140)]
POSTERS = ["p-last-kingdom", "p-sonic", "p-black-adam", "p-violent-night", "p-pathaan"]

def slider_html(lang):
    eyebrow, h2, p, note = SLIDER_TXT[lang]
    def lis(items, hidden):
        return "".join(items(hidden))
    def logo_items(hidden):
        for f, name, w, h in LOGOS:
            yield f'<li{" aria-hidden=\"true\"" if hidden else ""}><img src="/assets/channels/{f}" width="{w}" height="{h}" alt="{"" if hidden else name}" loading="lazy" decoding="async"></li>'
    def poster_items(hidden):
        for f in POSTERS:
            yield f'<li{" aria-hidden=\"true\"" if hidden else ""}><img src="/assets/posters/{f}.webp" width="520" height="293" alt="" loading="lazy" decoding="async"></li>'
    def track(cls, items):
        half = lis(items, False) + lis(items, True)
        return f'<div class="marq{cls}"><ul class="marq-track {"logos" if items is logo_items else "posters-row"}">{half}{lis(items, True)}{lis(items, True)}</ul></div>'
    return (f'<section class="sec sec-tight sl-sec" aria-labelledby="sl-h"><div class="wrap"><div class="sec-head center"><span class="eyebrow">{eyebrow}</span>'
            f'<h2 id="sl-h">{h2}</h2><p>{p}</p></div></div>{track("", logo_items)}{track(" marq-rev", poster_items)}'
            f'<p class="wrap measure sl-note">{note}</p></section>')

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def faq_html(items):
    return '<div class="faq center">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items) + "</div>"

def pricing_cards(lang, T):
    out = ['<div class="pricing">']
    for m in ("1", "3", "6", "12"):
        e, n = EUR["1"][m], NOK["1"][m]
        if lang == "en":
            amt = f'<span class="cur">€</span><span data-pp="{m}">{e:.2f}</span>'; alt = f"≈ {n} kr"; pt = f"€{e:.2f}"; pm = f"{e/int(m):.2f}"
            per = f'= €<span data-pm="{m}">{pm}</span>/month'
        else:
            amt = f'<span data-pp="{m}">{n}</span><small>kr</small>'; alt = f"≈ €{e:.2f}"; pt = f"{n} kr"; pm = str(round(n/int(m)))
            per = f'= <span data-pm="{m}">{pm}</span> kr/mnd'
        total = T["once"] if m == "1" else per
        best = m == "12"
        badge = f'<span class="badge">{T["best"]}</span>' if best else ""
        feats = "".join(f"<li>{{{{I:check}}}}{x}</li>" for x in T["incl"])
        msg = T["order_msg"].format(m=T["mon"][m], d=f'1 {T["screen"]}', p=pt)
        out.append(
            f'<div class="price{" best" if best else ""}">{badge}<h3>{T["mon"][m]}</h3><p class="sub">{T["sub"][m]}</p>'
            f'<div class="amount">{amt}</div><p class="alt-cur" data-ps="{m}">{alt}</p><p class="total">{total}</p>'
            f'<div class="p-bar" aria-hidden="true"><i style="--m:{m}"></i></div><ul>{feats}</ul>'
            f'<a class="btn{"" if best else " btn-line"} btn-block" data-track="buy_click" data-pwa="{m}" href="{{{{WA:{msg}}}}}" rel="noopener" target="_blank" '
            f'aria-label="{T["pick"].format(m=T["mon"][m])}">{T["pick"].format(m=T["mon"][m])}</a></div>')
    out.append("</div>")
    return "".join(out)

def channels_html(items):
    return '<ul class="channels">' + "".join(
        f'<li><span class="ch-ico">{{{{I:{ic}}}}}</span><b>{b}</b><small>{s}</small></li>' for ic, b, s in items) + "</ul>"

def cards(items):
    return "".join(f'<div class="card c-{c}"><div class="ico">{{{{I:{ic}}}}}</div><h3>{h}</h3><p>{p}</p></div>' for c, ic, h, p in items)

# =========================================================================================
# ENGLISH
# =========================================================================================
EN = dict(
    mon={"1": "1 month", "3": "3 months", "6": "6 months", "12": "12 months"}, screen="screen", once="one-off price, no renewal", best="Best value",
    sub={"1": "Good for trying it", "3": "One season", "6": "Half a year", "12": "A full year"},
    incl=["Norwegian and Nordic channels", "HD, and 4K where the channel has it", "TV guide (EPG)", "Install help on WhatsApp", "No automatic renewal"],
    order_msg="Hi! I'd like to order IPTV Norway One: {m}, {d} ({p}).", pick="Choose {m}")

def en_pages():
    faq = [
        ("What is IPTV Norway?", "IPTV Norway means television delivered over your internet connection instead of a dish, cable or aerial. With IPTV Norway One you watch Norwegian and Nordic channels in an app on your TV, box, phone or computer."),
        ("What is the difference between IPTV Norway and IPTV Nordic?", "IPTV Norway is about Norwegian channels and a Norwegian TV guide. IPTV Nordic means that channels from Sweden, Denmark and Finland are included as well. With IPTV Norway One you get both in the same plan."),
        ("What internet speed do I need?", "Plan for at least 10 Mbit/s per screen for HD and 25 Mbit/s for 4K. Measure on the TV or box itself, not on your phone. A network cable is almost always steadier than wifi."),
        ("Do I need to buy a box?", "Usually not. Samsung and LG TVs from recent years run IPTV with an app. On an older TV, a Fire TV Stick or an Android TV box is the cheapest way to get started."),
        ("Does the subscription renew automatically?", "No. We take no automatic payments and store no card details. When the period is ending you extend it yourself, if you want to."),
        ("How do I pay?", "You order on WhatsApp and get the payment details there. We accept Visa, Mastercard, Maestro, Apple Pay, Google Pay and PayPal, and from other EU countries also SEPA, iDEAL, Bancontact and giropay."),
        ("Can I try it before buying a longer plan?", "Yes. Start with one month for €15.99. It does not renew by itself, so there is nothing to cancel. If it works well, you can take a longer plan when the month is over."),
        ("Is IPTV legal in Norway?", "IPTV is just a technology, and it is legal. What matters is whether the channels you watch are licensed for distribution. We cannot give legal advice, so ask us what a plan includes before you order and read the information from <a href=\"https://www.medietilsynet.no/\" target=\"_blank\" rel=\"noopener\">Medietilsynet</a>. You are responsible for how you use the service."),
    ]
    T = EN
    # ---------------------------------------------------------------- HOME
    home_meta = {"speakable": True, "keyword": "iptv norway", "crumb": "Home", "alt": "",
        "title": "IPTV Norway 2026: Norwegian and Nordic TV in HD from €5.83/mo",
        "desc": "IPTV Norway for households: Norwegian and Nordic channels in HD, a TV guide and install help on WhatsApp. From €5.83/month, no contract. Order today.",
        "og": "IPTV Norway 2026: Norwegian and Nordic TV in HD from €5.83 a month",
        "img_alt": "IPTV Norway: Norwegian and Nordic TV in HD on Smart TV, box and phone",
        "images": [
            {"name": "en-home-devices", "title": "IPTV Norway on Smart TV, Fire TV Stick, Android TV and Apple TV", "alt": "IPTV Norway on Smart TV, Fire TV Stick, Android TV, Apple TV and MAG box"},
            {"name": "en-home-nordic", "title": "IPTV Nordic: Norwegian, Swedish, Danish and Finnish channels in one app", "alt": "IPTV Nordic with Norwegian, Swedish, Danish and Finnish channels in the same app"},
            {"name": "en-home-steps", "title": "Get started with IPTV Norway in three steps", "alt": "Get started with IPTV Norway in three steps on WhatsApp"}],
        "schema": [
            {"@context": "https://schema.org", "@type": "Product", "name": "IPTV Norway One subscription", "brand": {"@type": "Brand", "name": "IPTV Norway One"},
             "description": "IPTV subscription with Norwegian and Nordic channels in HD for Smart TV, Android TV, Apple TV, phone and computer.",
             "image": BASE + "/assets/og/en-home.png",
             "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "15.99", "highPrice": "169.99", "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/en/iptv-subscription-norway/"}},
            faq_schema(faq)]}
    home = f"""
<section class="hero">
  <div class="wrap hero-in">
    <div>
      <span class="pill"><span class="dot"></span>Live now · Norwegian and Nordic TV in HD</span>
      <h1>IPTV Norway <span class="grad-text">for Norwegian and Nordic TV</span> in HD</h1>
      <p class="lead">IPTV Norway should be simple: <b>Norwegian and Nordic channels in HD</b>, in an app on the TV you already own. With IPTV Norway One you pick 1, 3, 6 or 12 months and we help you install it on WhatsApp.</p>
      <div class="hero-cta">
        <a class="btn" data-track="buy_click" href="{{{{WA:Hi! I'd like to order IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Order on WhatsApp</a>
        <a class="btn btn-ghost" href="#pricing">See the prices →</a>
      </div>
      <ul class="chips">
        <li>{{{{I:check}}}} No contract</li>
        <li>{{{{I:check}}}} HD, and 4K where available</li>
        <li>{{{{I:check}}}} Smart TV to phone</li>
        <li>{{{{I:check}}}} Prices in EUR and NOK</li>
      </ul>
    </div>
    <div class="screen-wrap" aria-hidden="true">
      <div class="browser">
        <div class="browser-bar"><i></i><i></i><i></i><span>IPTV Norway One · Films and series</span></div>
        <div class="posters">
          <figure><img src="/assets/posters/poster-1.webp" width="1200" height="677" alt="" fetchpriority="high"><figcaption><b class="live">LIVE</b><b>HD</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-2.webp" width="1200" height="677" alt="" loading="lazy"><figcaption><b>4K</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-3.webp" width="900" height="508" alt="" loading="lazy"><figcaption><b>HD</b></figcaption></figure>
        </div>
      </div>
      <div class="f-badge b1"><span class="ic">{{{{I:shield}}}}</span><span>No contract<small>nothing renews by itself</small></span></div>
      <div class="f-badge b2"><span class="ic">{{{{I:zap}}}}</span><span>€5.83/month<small>on the 12-month plan</small></span></div>
      <div class="f-badge b3"><span class="ic">{{{{I:spark}}}}</span><span>HD + 4K<small>where the channel has it</small></span></div>
    </div>
  </div>
</section>

<div class="wrap tiles" role="list" aria-label="IPTV Norway One in numbers">
  <div role="listitem"><b>€5.83</b><span>per month on 12 months</span></div>
  <div role="listitem"><b>0</b><span>days of contract</span></div>
  <div role="listitem"><b>4</b><span>Nordic countries in the plan</span></div>
  <div role="listitem"><b>3</b><span>screens at the same time, if you want</span></div>
</div>

<section class="strip" aria-label="Works on">
  <div class="wrap">
    <p>Works on the screens you already have</p>
    <ul>
      <li>{{{{I:tv}}}} Samsung</li><li>{{{{I:tv}}}} LG</li><li>{{{{I:box}}}} Android TV</li><li>{{{{I:box}}}} Fire TV Stick</li>
      <li>{{{{I:tv}}}} Apple TV</li><li>{{{{I:phone}}}} iPhone and Android</li><li>{{{{I:laptop}}}} Windows and Mac</li><li>{{{{I:box}}}} MAG box</li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap measure">
    <p>This page is written for anyone searching for IPTV Norway who wants to know what they actually get. We go through the channels, the prices, which screens work and how to get started. We also tell you when we are not the right choice. Prefer to read in Norwegian? Go to the <a href="/" hreflang="nb" lang="nb">Norwegian version</a>.</p>
    <h2 class="center-h">IPTV Norway One at a glance</h2>
    <dl class="facts">
      <div><dt>Price</dt><dd>€15.99 to €169.99, from €5.83/month</dd></div>
      <div><dt>Plans</dt><dd>1, 3, 6 or 12 months, same content</dd></div>
      <div><dt>Contract</dt><dd>None, nothing renews automatically</dd></div>
      <div><dt>Channels</dt><dd>Norwegian plus Sweden, Denmark and Finland</dd></div>
      <div><dt>Picture</dt><dd>HD, and 4K where the channel broadcasts in 4K</dd></div>
      <div><dt>Speed</dt><dd>10 Mbit/s per screen for HD, 25 for 4K</dd></div>
      <div><dt>Devices</dt><dd>Smart TV, Fire TV, Android TV, Apple TV, phone, computer, MAG</dd></div>
      <div><dt>Ordering</dt><dd>WhatsApp, in English or Norwegian</dd></div>
      <div><dt>Payment</dt><dd>Card, Apple Pay, Google Pay, PayPal</dd></div>
    </dl>
    <!--TOC-->
  </div>
</section>

<section class="sec sec-tight">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">What is included</span>
      <h2>Why IPTV Norway One suits Norwegian households</h2>
      <p>Good IPTV is not about the longest channel list. It is about the TV starting when you press the remote, the guide showing the right programme and having someone to ask. This is how that looks with us.</p>
    </div>
  </div>
  <div class="wrap feat">
    {cards([
      ("cyan", "globe", "Norwegian and Nordic channels", "News, entertainment, children's channels and sport, plus channels from Sweden, Denmark and Finland. The line-up can change over time. Ask us about a specific channel before you order and you get a straight answer."),
      ("violet", "spark", "HD as standard, 4K where it exists", "Channels are delivered in HD, and in 4K where the channel itself broadcasts in 4K. How sharp it looks at home also depends on your TV and connection. Read more in the guide to <a href=\"/en/guides/\">IPTV guides</a>."),
      ("pink", "calendar", "A TV guide (EPG) in the app", "A schedule that shows what is on now and later on every channel, like normal TV. It is what makes IPTV feel like television and not a list of links."),
      ("green", "wifi", "A steady picture on a Saturday night", "The picture should hold even between 19:00 and 22:00, when everyone is online. Most things that make IPTV freeze sit inside the home, usually wifi, and we help you sort that out."),
      ("blue", "chat", "Everything in one chat", "Ordering, payment and help with the setup all happen in the same WhatsApp thread, in English or Norwegian."),
    ])}
  </div>
</section>

<section class="sec sec-night">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Included in the plan</span>
      <h2>A channel line-up for the whole household</h2>
      <p>Norwegian channels first, then the other Nordic countries and international ones. Ask us about a specific channel before you order.</p>
    </div>
    {channels_html([("globe","Norwegian channels","News, entertainment and local"),("tv","Nordic channels","Sweden, Denmark and Finland"),("zap","Sport","Football, winter sports and more live"),("film","Films and series","Film channels and series"),("spark","Kids and family","Children's channels"),("calendar","Documentary and nature","Facts, nature and history"),("chat","News","Norwegian and international"),("monitor","International","Channels from more countries")])}
    <p class="price-note" style="color:var(--on-night-muted)">The channel line-up can change over time.</p>
  </div>
</section>

{slider_html("en")}

<section class="sec sec-tight" id="pricing">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Prices</span>
      <h2>What IPTV Norway costs: four plans, same content</h2>
      <p>Choose how many screens you want to watch on at the same time, then how long. Channels and picture quality are the same in every plan. Prices are shown in euro with the Norwegian krone amount beside them.</p>
    </div>
    <!--DEVICES-->
    {pricing_cards("en", T)}
    <div class="measure">
      <!--PRICETABLE-->
      <p class="ruler-note">For the lowest price per month, twelve months is the right choice. With 2 or 3 screens, more people in the household can watch at the same time. Payment, more screens and terms are on the <a href="/en/iptv-subscription-norway/">IPTV subscription Norway page</a>. The krone amounts use a rate of about {SITE["nok_rate"]} NOK per euro and are guidance, the euro price is what you pay.</p>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">Screens</span>
      <h2>IPTV Norway on the screens you already have</h2>
      <p>IPTV should work on what you have at home. An app from the device's own app store is enough, and we tell you which one works best on your model.</p>
    </div>
    <!--IMG:en-home-devices-->
  </div>
  <div class="wrap devs" style="margin-top:28px">
    {cards([
      ("cyan", "tv", "Samsung and LG Smart TV", "Most models from roughly 2018 and later run it with an app. Which apps exist depends on the model and year, so send us the model number."),
      ("green", "box", "Fire TV Stick and Android TV", "The widest choice of apps and often the steadiest picture. A Fire TV Stick makes an older TV smart for a modest price."),
      ("pink", "phone", "Apple TV, iPhone and iPad", "An IPTV player from the App Store, with the same app on all your Apple devices. Apple explains how to install apps on the <a href=\"https://support.apple.com/apple-tv\" target=\"_blank\" rel=\"noopener\">Apple TV support pages</a>."),
      ("amber", "laptop", "MAG box and computer", "A MAG box is linked to your account with the box's MAC address, and we do that setting for you. On a computer both VLC and IPTV apps work."),
    ])}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Getting started</span>
      <h2>Get started with IPTV Norway in three steps</h2>
      <p>Most people are watching the same evening. What takes time is rarely the app, it is finding the right app for your TV.</p>
    </div>
    <ol class="steps">
      <li><h3>Choose how long</h3><p>All plans have the same content. If you are unsure, start with one month.</p></li>
      <li><h3>Write to us on WhatsApp</h3><p>Tell us which plan you want and which TV or box you have. We reply with payment details and the right app for your screen.</p></li>
      <li><h3>Log in and watch</h3><p>You get the login and a short instruction for your own TV. If you get stuck we keep helping in the chat.</p></li>
    </ol>
    <p style="margin-top:28px;text-align:center"><a class="btn" data-track="buy_click" href="{{{{WA:Hi! I'd like to try IPTV Norway One for one month (€15.99).}}}}" rel="noopener" target="_blank">Try one month for €15.99</a></p>
    <div class="measure" style="text-align:center"><!--IMG:en-home-steps--><p>The full walkthrough, device by device, is in the guide to <a href="/en/install-iptv/">installing IPTV</a>.</p></div>
  </div>
</section>

<section class="sec sec-night">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">IPTV Norway, IPTV Nordic and IPTV Norge</span>
      <h2>IPTV Norway, IPTV Nordic and IPTV Norge: what is the difference?</h2>
      <p>The words are used interchangeably, but they mean slightly different things. This is how we usually explain it.</p>
    </div>
    <ul>
      <li><strong>IPTV Norway and Norwegian IPTV:</strong> Norwegian channels with a Norwegian TV guide, for people who mainly want to watch Norwegian TV.</li>
      <li><strong>IPTV Nordic and Nordic IPTV:</strong> Norwegian channels plus channels from Sweden, Denmark and Finland. We cover it on the <a href="/en/iptv-nordic/">IPTV Nordic page</a>.</li>
      <li><strong>IPTV Norge:</strong> the same thing in Norwegian. Our <a href="/" hreflang="nb" lang="nb">Norwegian site</a> is written for people who search that way.</li>
    </ul>
    <p>With IPTV Norway One both are in the same plan, so you do not have to choose between Norwegian and Nordic IPTV.</p>
    <!--IMG:en-home-nordic-->
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Comparison</span>
      <h2>IPTV compared with cable TV and streaming</h2>
      <p>IPTV is not right for everyone. This is how IPTV in Norway compares with cable TV and streaming services.</p>
    </div>
    <ul class="checks">
      <li>{{{{I:check}}}}<span>No 12 or 24 month contract</span></li>
      <li>{{{{I:check}}}}<span>No dish, no cable outlet, no technician at home</span></li>
      <li>{{{{I:check}}}}<span>The same service at the cabin if there is internet</span></li>
      <li>{{{{I:check}}}}<span>A TV guide and channel switching like normal TV</span></li>
      <li>{{{{I:check}}}}<span>Nordic channels in the same plan</span></li>
      <li>{{{{I:check}}}}<span>Works on TV, phone and computer</span></li>
    </ul>
    <div class="vs-wrap" tabindex="0" role="region" aria-label="Comparison: IPTV Norway One, cable TV and streaming"><table class="vs"><thead><tr><th scope="col">Feature</th><th scope="col" class="us"><span class="vs-logo"><img class="mark" src="/assets/icons/mark.svg" width="28" height="28" alt=""><span class="wm"><b>IPTV</b><i>Norway</i><sup>One</sup></span></span></th><th scope="col">Cable TV</th><th scope="col">Streaming</th></tr></thead><tbody>
      <tr><th scope="row">Norwegian channels</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Yes</span></span></td><td><span class="yes">{{{{I:check}}}}<span class="sr">Yes</span></span></td><td>Partly</td></tr>
      <tr><th scope="row">Nordic channels (Sweden, Denmark, Finland)</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Yes</span></span></td><td>Partly</td><td>Rarely</td></tr>
      <tr><th scope="row">Live TV with a TV guide</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Yes</span></span></td><td><span class="yes">{{{{I:check}}}}<span class="sr">Yes</span></span></td><td>Rarely</td></tr>
      <tr><th scope="row">HD and 4K</th><td class="us">HD, 4K where broadcast</td><td>Depends on package</td><td>Depends on service</td></tr>
      <tr><th scope="row">Price per month</th><td class="us">From €5.83</td><td>Often several hundred kroner</td><td>Per service</td></tr>
      <tr><th scope="row">Contract</th><td class="us">None</td><td>Often 12 to 24 months</td><td>None</td></tr>
      <tr><th scope="row">Installation</th><td class="us">One app</td><td>Outlet and box</td><td>One app</td></tr>
      <tr><th scope="row">Works at the cabin</th><td class="us">If there is internet</td><td><span class="no">{{{{I:x}}}}<span class="sr">No</span></span></td><td>If there is internet</td></tr>
      <tr><th scope="row">Support</th><td class="us">WhatsApp, English or Norwegian</td><td>Customer service</td><td>Email or chat</td></tr>
    </tbody></table></div>
    <p>If your connection is slow or uneven, cable TV or a dish is the safer choice. Below 10 Mbit/s to the TV no service is the right IPTV for you, however good it is.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure why">
    <div class="sec-head center">
      <span class="eyebrow">Why us</span>
      <h2>Why people choose IPTV Norway One</h2>
    </div>
    <h3>Support on WhatsApp</h3>
    <p>You write to a person, not a form. Send a photo of the screen and we see straight away what is going on.</p>
    <h3>Plain terms</h3>
    <p>No contract, no automatic renewal and prices in euro with the krone amount beside them. IPTV should be as easy to stop as to start. It is all in our <a href="/en/terms/">terms</a>.</p>
    <h3>If something does not work</h3>
    <p>Write to us on WhatsApp with a photo of the screen and we go through the connection, the app and the settings with you. What applies to a purchase is in our <a href="/en/terms/">terms</a>.</p>
    <h3>When we are not the right choice</h3>
    <p>If your connection is under 10 Mbit/s per screen, or you want a box that someone installs at your home, a traditional operator suits you better. Then we are not the right IPTV for you, and it is more honest to say so now than after you have paid.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Guides</span>
      <h2>Guides from our support team</h2>
      <p>Installation, apps and troubleshooting, written from the questions we get.</p>
    </div>
    <ul class="checks"><li>{{{{I:check}}}}<span><a href="/en/best-iptv-norway/">Best IPTV in Norway: 7 checks before you subscribe</a></span></li><li>{{{{I:check}}}}<span><a href="/en/iptv-nordic/">IPTV Nordic: four countries of TV in one app</a></span></li><li>{{{{I:check}}}}<span><a href="/en/install-iptv/">Install IPTV on Smart TV, Fire TV and phone</a></span></li></ul>
    <p><a href="/en/guides/">All IPTV guides for Norway</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Questions and answers</span>
      <h2>Common questions about IPTV Norway</h2>
    </div>
    {faq_html(faq)}
    <p style="margin-top:24px">More answers are on the <a href="/en/faq/">IPTV FAQ page</a>.</p>
  </div>
</section>

<section class="band">
  <div class="wrap band-in">
    <div><h2>Try IPTV Norway on your own TV tonight.</h2><p>Tell us which TV you have and we tell you which plan and app suit it.</p></div>
    <a class="btn" data-track="buy_click" href="{{{{WA:Hi! I have a question before I order IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Write to us on WhatsApp</a>
  </div>
</section>
"""
    save("en", "", home_meta, home)
    return faq


def en_rest(faq):
    T = EN
    # ---------------------------------------------------------------- PLANS
    plans_faq = [
        ("Can I change the number of screens later?", "Yes. Write to us on WhatsApp before your period ends and say how many screens you want next time. The price follows the screen tier you choose."),
        ("What happens when the period is over?", "The service stops. Nothing renews automatically, and we do not store your card details. If you want to continue, you order again."),
        ("Are prices shown with VAT?", "The prices on this page are the prices you pay. We show euro with the Norwegian krone amount beside it. The krone amount is guidance based on a rate of about 11.7 NOK per euro."),
    ]
    save("en", "iptv-subscription-norway", {"keyword": "iptv subscription norway", "crumb": "IPTV subscription Norway", "alt": "iptv-norway-abonnement",
        "title": "IPTV Subscription Norway: 12 Plans from €15.99 | One",
        "desc": "IPTV subscription Norway: 1, 3, 6 or 12 months for 1, 2 or 3 screens, from €5.83/month with no contract. All prices in euro and kroner on one page.",
        "og": "IPTV subscription Norway: 12 plans from €15.99",
        "tldr": "An IPTV subscription in Norway from IPTV Norway One costs €15.99 for one month and €69.99 for twelve months on one screen, which is €5.83 a month. Two and three screens cost more. Nothing renews automatically.",
        "schema": [{"@context": "https://schema.org", "@type": "Product", "name": "IPTV Norway One subscription", "brand": {"@type": "Brand", "name": "IPTV Norway One"},
                    "image": BASE + "/assets/og/en-iptv-subscription-norway.png",
                    "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR", "lowPrice": "15.99", "highPrice": "169.99", "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/en/iptv-subscription-norway/"}},
                   faq_schema(plans_faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Prices</span><h1>IPTV subscription Norway: plans and prices</h1>
<p>One service, four lengths and three screen tiers. Pick how many screens should work at the same time, then how long you want to subscribe.</p></div></section>
<section class="sec sec-tight"><div class="wrap">
<!--TOC-->
<!--DEVICES-->
{pricing_cards("en", T)}
<div class="measure">
<h2>What an IPTV subscription Norway plan includes</h2>
<p>Every IPTV subscription Norway plan has the same content: Norwegian and Nordic channels in HD, 4K where the channel broadcasts it, a TV guide and help with the installation on WhatsApp. The only things that change between plans are the length and the number of screens.</p>
<h2>All prices for 1, 2 and 3 screens</h2>
<!--PRICETABLE-->
<p>Euro is the price you pay, and the krone amount is guidance based on about {SITE["nok_rate"]} NOK per euro. A longer plan always gives a lower price per month.</p>
<h2>How to pay for your IPTV subscription</h2>
<p>You order on WhatsApp and get the payment details there. We accept Visa, Mastercard, Maestro, Apple Pay, Google Pay and PayPal, and from other EU countries also SEPA, iDEAL, Bancontact and giropay. We do not store card details and nothing renews on its own.</p>
<h2>Choosing an IPTV subscription Norway households can rely on</h2>
<p>When you compare an IPTV subscription Norway sellers offer, look at the contract, the renewal and the support, not just the channel count. Our IPTV subscription Norway plans have no contract and no automatic renewal. To understand your consumer rights before you buy any IPTV subscription Norway offers, the <a href="https://www.forbrukerradet.no/" target="_blank" rel="noopener">Norwegian Consumer Council</a> has plain-language guides.</p>
<h2>Which plan should you choose?</h2>
<ul><li><strong>Not sure yet:</strong> one month. It does not renew, so there is nothing to cancel.</li><li><strong>Lowest cost per month:</strong> twelve months.</li><li><strong>Several people watching at once:</strong> pick the 2 or 3 screen tier.</li></ul>
<p>Not sure what suits your TV? Read how to <a href="/en/install-iptv/">install IPTV</a> first, or go back to the <a href="/en/">IPTV Norway home page</a>. Terms are in our <a href="/en/terms/">terms of service</a>.</p>
<h2>Questions about plans</h2>
{faq_html(plans_faq)}
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Ready to order?</h2><p>Tell us the plan and the TV you have.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hi! I'd like to order IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Order on WhatsApp</a></div></section>
""")

    # ---------------------------------------------------------------- NORDIC (trunk 2)
    nordic_faq = [
        ("What is IPTV Nordic?", "Also called Nordic IPTV, it means TV over the internet with channels from all the Nordic countries in one app: Norway, Sweden, Denmark and Finland."),
        ("Is IPTV Nordic the same as IPTV Norway?", "Not exactly. IPTV Norway focuses on Norwegian channels. Nordic IPTV adds the Swedish, Danish and Finnish ones. With IPTV Norway One both are in the same plan."),
        ("Can I ask about a specific channel?", "Yes. Write to us on WhatsApp before you order and we tell you straight whether the channel is in the plan. The line-up can change over time."),
    ]
    save("en", "iptv-nordic", {"keyword": "iptv nordic", "crumb": "IPTV Nordic", "alt": "iptv-nordic",
        "title": "IPTV Nordic 2026: 4 Countries of TV in One App | One",
        "desc": "IPTV Nordic explained: Norwegian, Swedish, Danish and Finnish channels in one app, what you need to watch, and how it compares with IPTV Norway.",
        "og": "IPTV Nordic 2026: four countries of TV in one app",
        "tldr": "IPTV Nordic means Norwegian, Swedish, Danish and Finnish channels in one IPTV app. With IPTV Norway One the Nordic channels are included in the same plan as the Norwegian ones, from €5.83 a month.",
        "schema": [faq_schema(nordic_faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Nordic TV</span><h1>IPTV Nordic: four countries of TV in one app</h1>
<p>If you follow television from more than one Nordic country, Nordic IPTV puts it in one place. Here is what it is, what you need and how it relates to IPTV Norway.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>IPTV Nordic is a plain idea: one subscription and one app with channels from Norway, Sweden, Denmark and Finland. Nordic IPTV suits families with roots in more than one country, people who work across the border and anyone who likes to watch the neighbours' news, sport and series.</p>
<h2>What IPTV Nordic includes</h2>
<p>With IPTV Norway One the Nordic channels sit in the same plan as the Norwegian ones. That means Norwegian channels first, then channels from Sweden, Denmark and Finland, with a TV guide in the app. The line-up can change over time, so ask us about a specific channel before you order.</p>
<!--IMG:en-nordic-iptv-->
<h2>Nordic IPTV compared with IPTV Norway</h2>
<ul><li><strong>IPTV Norway:</strong> Norwegian channels and a Norwegian guide. Read the <a href="/en/">IPTV Norway overview</a>.</li><li><strong>Nordic IPTV:</strong> the Norwegian channels plus Sweden, Denmark and Finland.</li><li><strong>Norwegian version:</strong> the same information in Norwegian is on <a href="/iptv-nordic/" hreflang="nb" lang="nb">IPTV Nordic på norsk</a>.</li></ul>
<h2>What you need to watch Nordic IPTV</h2>
<p>You need an internet connection of at least 10 Mbit/s per screen for HD, and 25 Mbit/s for 4K, and a device with an app. Samsung and LG TVs, Android TV, Fire TV Stick, Apple TV, iPhone, Android and computers all work. The steps are in the guide to <a href="/en/install-iptv/">installing IPTV</a>.</p>
<h2>Who Nordic IPTV is for</h2>
<p>Nordic IPTV is for households that follow television from more than one country. That can be a family with relatives in Sweden or Denmark, a couple where one grew up in Finland, or someone who commutes across the border and wants the local news in both places. It also suits people who simply enjoy comparing how the neighbouring countries make their news, sport and series.</p>
<h2>How the TV guide works across countries</h2>
<p>The TV guide (EPG) in the app lists what is on now and later for each channel, grouped by country. You move between countries in the channel list the same way you move between channel groups on a normal TV. If a programme time looks wrong, tell us the channel and we check the guide data with you.</p>
<h2>What to expect from the channel line-up</h2>
<p>The Nordic countries share a lot of culture, but each one has its own broadcasters and its own rights. That is why we never promise a list we cannot prove. Ask about the channels you care about before you order, and remember that the line-up can change over time. For background on how the Nordic countries cooperate, see the <a href="https://www.norden.org/en" target="_blank" rel="noopener">Nordic cooperation website</a>.</p>
<h2>What Nordic IPTV costs</h2>
<p>The plans start at €15.99 for one month, and twelve months on one screen is €69.99, which is €5.83 a month. All prices for 1, 2 and 3 screens are on the <a href="/en/iptv-subscription-norway/">IPTV subscription Norway page</a>.</p>
<h2>Language, subtitles and the TV guide</h2>
<p>Each channel broadcasts in its own language, so Swedish channels are in Swedish, Danish ones in Danish and Finnish ones in Finnish. Whether a programme has subtitles depends on the channel and the programme, not on the app. The TV guide (EPG) shows titles and times for each channel, and if a time or title looks wrong, tell us which channel it is and we check it with you.</p>
<h2>How many screens does a Nordic household need?</h2>
<p>One screen is enough if one person watches at a time. Choose two screens if two people want to watch different channels at the same time, for example the news in one room and a match in another, and three if the whole family has their own screen. The price follows the number of screens: for twelve months it is €69.99 for one screen, €119.99 for two and €169.99 for three, and the plan content is the same.</p>
<h2>A short checklist before you order IPTV Nordic</h2>
<ul><li>Write down the model of your TV or box.</li><li>Measure your internet speed on that device.</li><li>List the channels you care about and ask us about them.</li><li>Pick one month first if you are unsure.</li><li>Read our <a href="/en/terms/">terms</a> so you know what applies.</li></ul>
<h2>Questions about IPTV Nordic</h2>
{faq_html(nordic_faq)}
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Want the Nordic channels at home?</h2><p>Ask about a channel before you order.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hi! I'm interested in IPTV Nordic from IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Write to us on WhatsApp</a></div></section>
""".replace("<!--IMG:en-nordic-iptv-->", ""))

    # ---------------------------------------------------------------- INSTALL
    save("en", "install-iptv", {"keyword": "install iptv", "crumb": "Install IPTV", "alt": "installer-iptv",
        "title": "Install IPTV in 3 Steps on Smart TV, Fire TV and Phone",
        "desc": "How to install IPTV on Samsung and LG Smart TV, Fire TV Stick, Android TV, Apple TV, iPhone and computer. Steps, speed needs and where to get help.",
        "og": "Install IPTV in 3 steps on Smart TV, Fire TV and phone",
        "tldr": "To install IPTV you pick a plan, get your login on WhatsApp and put an IPTV app on your TV, box or phone. It takes a few minutes if you have 10 Mbit/s per screen and the right app for your model."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Setup</span><h1>Install IPTV: Smart TV, Fire TV, Apple TV and phone</h1>
<p>You do not need special equipment. You need an app for your device, your login and a connection that is fast enough.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>To install IPTV on a TV, a box or a phone you follow the same three steps on every device. The details differ by brand, which is why we ask for your model before we recommend an app.</p>
<h2>Before you install IPTV: check your internet</h2>
<p>Plan for at least 10 Mbit/s per screen for HD and 25 Mbit/s for 4K. Measure on the TV or the box, not on your phone, because the TV is often further from the router. A network cable is almost always steadier than wifi.</p>
<h2>Three steps to install IPTV</h2>
<ol><li><strong>Order and get your login.</strong> Write to us on WhatsApp with the plan you want and your TV or box model.</li><li><strong>Install the app.</strong> Open the app store on your device, install the IPTV player we recommend for your model and open it.</li><li><strong>Log in.</strong> Enter the details we send you. The channel list and the TV guide load within a minute or two.</li></ol>
<h2>Install IPTV on Samsung and LG Smart TV</h2>
<p>Most models from roughly 2018 and later can run an IPTV app from the TV's own app store. Which apps are available depends on the model and year, so send us the model number from the label on the back.</p>
<h2>Install IPTV on Fire TV Stick and Android TV</h2>
<p>These give the widest choice of apps. Open the app store, search for the player we recommend and install it. Amazon explains the basics on its <a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=GYXQJZZ2VAXYW9H9" target="_blank" rel="noopener">Fire TV help pages</a>.</p>
<h2>Install IPTV on Apple TV, iPhone and iPad</h2>
<p>Install an IPTV player from the App Store, then log in with the details we send. Apple's own <a href="https://support.apple.com/apple-tv" target="_blank" rel="noopener">Apple TV support pages</a> cover how to install apps.</p>
<h2>Install IPTV on a MAG box or a computer</h2>
<p>A MAG box is linked to your account with the box's MAC address, and we set that up for you. On a computer you can use VLC or an IPTV app.</p>
<h2>If the picture stutters after you install IPTV</h2>
<p>Move the TV to a network cable, restart the router and close other streaming on the network. If it still stutters, send us a photo of the screen on WhatsApp.</p>
<h2>Tips for a steadier picture</h2>
<p>Place the router in the same room as the TV if you can, and keep it away from thick walls. If you must use wifi, choose the 5 GHz band, which is faster over short distances than 2.4 GHz. Close other apps that stream video while you test, and restart the app once after the first login so the channel list and the guide load cleanly.</p>
<h2>What you need before you start</h2>
<ul><li>Your TV or box model, from the label or the settings menu.</li><li>An internet connection of at least 10 Mbit/s per screen.</li><li>Your login from us on WhatsApp.</li><li>An account in the device's app store (Samsung, LG, Google, Amazon or Apple).</li></ul>
<h2>How long the setup takes</h2>
<p>With the right app for your model, most people finish within a few minutes. Finding the right app takes longer than the setup itself, so tell us your model first and we point you to the right one.</p>
<p>Ready to start? See the <a href="/en/iptv-subscription-norway/">plans and prices</a>, read about <a href="/en/iptv-nordic/">Nordic channels</a> or go back to <a href="/en/">IPTV Norway</a>.</p>
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Stuck on a step?</h2><p>Send your TV model and we tell you what to do.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hi! I need help installing IPTV on my TV.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Ask on WhatsApp</a></div></section>
""")

    # ---------------------------------------------------------------- FAQ
    save("en", "faq", {"crumb": "FAQ", "alt": "vanlige-sporsmal",
        "title": "IPTV Norway FAQ: Questions and Answers | IPTV Norway One",
        "desc": "Answers about IPTV Norway One: plans, payment, speed, devices, renewal and legality. Short and straight, written by our support team.",
        "schema": [faq_schema(faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">FAQ</span><h1>Frequently asked questions about IPTV</h1>
<p>The questions we get most often, answered straight.</p></div></section>
<section class="sec sec-tight"><div class="wrap">{faq_html(faq)}
<p style="margin-top:24px">Something missing? <a href="/en/contact/">Contact us</a> or see the <a href="/en/iptv-subscription-norway/">plans</a>, or go back to <a href="/en/">IPTV Norway</a>.</p></div></section>
""")

    # ---------------------------------------------------------------- ABOUT
    save("en", "about", {"crumb": "About us", "alt": "om-oss",
        "title": "About IPTV Norway One: Who Writes the Guides and Why",
        "desc": "About IPTV Norway One: an independent IPTV service for Norway, how our support team writes the guides and which facts we will and will not claim.",
        "schema": [{"@context": "https://schema.org", "@type": "AboutPage", "name": "About us", "url": BASE + "/en/about/", "inLanguage": "en"}]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">About</span><h1>About IPTV Norway One</h1>
<p>An independent IPTV service for households in Norway, with support on WhatsApp.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<p>IPTV Norway One sells IPTV subscriptions with Norwegian and Nordic channels. We have no affiliation with the TV companies, apps or manufacturers mentioned on this site. Ordering, payment and help all happen on WhatsApp.</p>
<h2 id="how-we-write">How we write the guides</h2>
<p>The guides are written by the support team, the same people who answer on WhatsApp. We write about questions customers actually ask. Settings and app features are checked against the manufacturers' own help pages, which we link under each guide, and we correct the text when something changes.</p>
<h2>What we will not claim</h2>
<p>We do not publish invented numbers such as uptime percentages, review scores or channel counts we cannot prove. When we do not know something, we say so. The channel line-up can change over time, so we ask you to check a specific channel with us before you order.</p>
<p>Read our <a href="/en/terms/">terms</a>, <a href="/en/privacy/">privacy policy</a> or go to <a href="/en/contact/">contact</a>.</p>
</div></div></section>
""")

    # ---------------------------------------------------------------- CONTACT
    save("en", "contact", {"crumb": "Contact", "alt": "kontakt",
        "title": "Contact IPTV Norway One: WhatsApp and Contact Form",
        "desc": "Contact IPTV Norway One on WhatsApp for orders, installation and troubleshooting, or use the contact form. What to include in your first message.",
        "schema": [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact", "url": BASE + "/en/contact/", "inLanguage": "en"}]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Contact</span><h1>Contact us</h1>
<p>WhatsApp is fastest, for both ordering and help with the installation. Tell us which TV or box you have, so we can answer the right thing.</p></div></section>
<div class="wrap"><div class="prose">
<p><a class="btn" data-track="buy_click" href="{{{{WA:Hi! I have a question about IPTV Norway One.}}}}" rel="noopener" target="_blank">Write on WhatsApp</a></p>
<div class="table-wrap"><table><tbody><tr><th scope="row">WhatsApp</th><td>{SITE["whatsapp_display"]}</td></tr><tr><th scope="row">Languages</th><td>English and Norwegian</td></tr></tbody></table></div>
<h2>Include this in your first message</h2>
<p>For help with the installation, write the brand and model of the TV or box, and send a photo of the screen if an error shows. For an order, write which plan you want. Prices are on the <a href="/en/iptv-subscription-norway/">IPTV subscription Norway page</a>. Setup steps are in <a href="/en/install-iptv/">how to install IPTV</a>, and our <a href="/en/terms/">terms</a> explain what applies to an order.</p>
<h2>Prefer a form?</h2>
<p>Use the contact form at the bottom of the page and we reply to the address you give us.</p>
</div></div>
""")

    # ---------------------------------------------------------------- LEGAL
    save("en", "terms", {"crumb": "Terms", "alt": "vilkar",
        "title": "Terms of Service for IPTV Norway One | Plans and Renewal",
        "desc": "Terms of service for IPTV Norway One: plans, payment, no automatic renewal, support, acceptable use and your rights as a consumer in Norway."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Terms</span><h1>Terms of service</h1><p>Short and plain. Last updated November 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>The service</h2><p>IPTV Norway One sells access to an IPTV service with Norwegian and Nordic channels. The channel line-up can change over time. You can ask us about a specific channel on WhatsApp before you order.</p>
<h2>Plans and payment</h2><p>You choose a length (1, 3, 6 or 12 months) and a number of screens (1, 2 or 3). You order and pay through WhatsApp. Prices are shown in euro with the Norwegian krone amount beside them as guidance.</p>
<h2>Renewal</h2><p>Nothing renews automatically. We do not store card details. When the period ends the service stops unless you order again.</p>
<h2>Support and problems</h2><p>If something does not work, write to us on WhatsApp with a photo of the screen and we go through the connection, the app and the settings with you.</p>
<h2>Your rights</h2><p>Your statutory rights as a consumer under Norwegian law are not affected by these terms.</p>
<h2>Acceptable use</h2><p>The service is for private use in your household. You are responsible for how you use it and for following the law that applies to you.</p>
<p>Questions? <a href="/en/contact/">Contact us</a>. See also the <a href="/en/privacy/">privacy policy</a> and the <a href="/en/iptv-subscription-norway/">plans</a>.</p>
</div></div>
""")
    save("en", "privacy", {"crumb": "Privacy policy", "alt": "personvern",
        "title": "Privacy Policy for IPTV Norway One | What We Store and Why",
        "desc": "Privacy policy for IPTV Norway One: what we collect when you order or use the contact form, how long we keep it and how to ask us to delete it."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Privacy</span><h1>Privacy policy</h1><p>What we store and why. Last updated November 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>What we collect</h2><p>When you write to us on WhatsApp we see your phone number and the messages you send. When you use the contact form we receive the name, contact details and message you type. We use this only to answer you and deliver your order.</p>
<h2>What we do not do</h2><p>We do not sell your data, we do not store card details and we do not use advertising trackers.</p>
<h2>Statistics</h2><p>If you accept, we count page views and clicks to improve the site. No cookies are used. If you decline, nothing is counted. You can change your choice on the <a href="/en/cookies/">cookies and statistics page</a>.</p>
<h2>Your rights</h2><p>You can ask us to show, correct or delete what we hold about you. Write to us on <a href="/en/contact/">the contact page</a>.</p>
<p>See also our <a href="/en/terms/">terms</a> and the <a href="/en/">home page</a>.</p>
</div></div>
""")
    save("en", "cookies", {"crumb": "Cookies and statistics", "alt": "cookies",
        "title": "Cookies and Statistics at IPTV Norway One | Your Choice",
        "desc": "IPTV Norway One uses no cookies. Optional statistics count visits and clicks only if you accept. Here is how it works and how to change your choice."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Cookies</span><h1>Cookies and statistics</h1></div></section>
<div class="wrap"><div class="prose">
<p>This site sets no cookies. Optional statistics count page views and clicks to help us improve the site, and they only load if you press Accept. Declining is the default.</p>
<p><button class="btn btn-sm btn-line" type="button" data-consent-reset>Change my choice</button></p>
<p>More in the <a href="/en/privacy/">privacy policy</a>. See also the <a href="/en/terms/">terms</a>, the <a href="/en/">home page</a> and <a href="/en/contact/">contact</a>.</p>
</div></div>
""")
    save("en", "404", {"crumb": "Not found", "robots": "noindex, follow", "title": "Page not found | IPTV Norway One", "desc": "This page does not exist. Go back to the home page or see the IPTV plans."},
f"""
<section class="page-head"><div class="wrap"><h1>Page not found</h1><p>The page you are looking for does not exist. Go to the <a href="/en/">home page</a> or see the <a href="/en/iptv-subscription-norway/">plans</a>.</p></div></section>
""")


if __name__ == "__main__":
    f = en_pages()
    en_rest(f)
    print("EN pages written")
