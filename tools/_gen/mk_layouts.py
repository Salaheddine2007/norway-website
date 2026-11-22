import re, os
ROOT = r"C:\Users\DELL\Desktop\norway-website\tools"
src = open(os.path.join(r"C:\Users\DELL\Desktop\basta-website\tools", "layout.html"), encoding="utf-8").read()

LANGS = {
 "en": dict(html="en", skip="Skip to content",
   ticker=["Nordic and Norwegian TV in HD", "From €5.83/month", "No contract", "Install help on WhatsApp", "Smart TV, Fire TV, Apple TV and mobile"],
   brandlabel="IPTV Norway One, home",
   nav=[("/en/iptv-subscription-norway/", "Plans"), ("/en/iptv-nordic/", "Nordic"), ("/en/install-iptv/", "Install"), ("/en/guides/", "Guides"), ("/en/contact/", "Contact")],
   navlabel="Main menu", theme="Switch between light and dark mode", order="Order",
   foot="IPTV subscriptions with Norwegian and Nordic channels in HD. Order and support on WhatsApp.",
   fnav=[("/en/iptv-subscription-norway/", "IPTV plans and prices"), ("/en/iptv-nordic/", "IPTV Nordic"), ("/en/install-iptv/", "Install IPTV"), ("/en/best-iptv-norway/", "Best IPTV in Norway"), ("/en/faq/", "FAQ"),
         ("/en/guides/", "Guides"), ("/en/about/", "About us"), ("/en/contact/", "Contact"), ("/en/terms/", "Terms"), ("/en/privacy/", "Privacy policy"), ("/en/cookies/", "Cookies and statistics")],
   footnav="Footer",
   legal="IPTV Norway One is an independent service with no affiliation to the TV companies, apps or manufacturers mentioned on this site. The channel line-up can change over time. © 2026 IPTV Norway One",
   wa_float="Order on WhatsApp", form="Write to us", formlabel="Write to us in the contact form", stick="Order via WhatsApp", stick_s="from €5.83/month",
   consent="We would like to count visits and clicks to improve the site. No cookies, no ad trackers.", more="Read more", no="No thanks", yes="Accept", consentlabel="Statistics",
   sw_text="Norsk", sw_label="Norsk versjon", sw_lang="nb", home="/en/", contact="/en/contact/", cookies="/en/cookies/", loc="en_US"),
 "no": dict(html="nb", skip="Hopp til innholdet",
   ticker=["Norsk og nordisk TV i HD", "Fra 68 kr/mnd", "Ingen binding", "Hjelp med installasjonen på WhatsApp", "Smart-TV, Fire TV, Apple TV og mobil"],
   brandlabel="IPTV Norway One, forside",
   nav=[("/iptv-norway-abonnement/", "Priser"), ("/iptv-nordic/", "Nordic"), ("/installer-iptv/", "Installasjon"), ("/guider/", "Guider"), ("/kontakt/", "Kontakt")],
   navlabel="Hovedmeny", theme="Bytt mellom lyst og mørkt modus", order="Bestill",
   foot="IPTV-abonnement med norske og nordiske kanaler i HD. Bestilling og support på WhatsApp.",
   fnav=[("/iptv-norway-abonnement/", "IPTV-abonnement og priser"), ("/iptv-nordic/", "IPTV Nordic"), ("/installer-iptv/", "Installer IPTV"),
         ("/beste-iptv-norge/", "Beste IPTV Norge"), ("/norsk-iptv/", "Norsk IPTV"), ("/vanlige-sporsmal/", "Vanlige spørsmål"), ("/guider/", "Guider"), ("/om-oss/", "Om oss"), ("/kontakt/", "Kontakt"),
         ("/vilkar/", "Vilkår"), ("/personvern/", "Personvern"), ("/cookies/", "Cookies og statistikk")],
   footnav="Bunntekst",
   legal="IPTV Norway One er en uavhengig tjeneste og har ingen tilknytning til TV-selskapene, appene eller produsentene som nevnes på siden. Kanalutvalget kan endre seg over tid. © 2026 IPTV Norway One",
   wa_float="Bestill på WhatsApp", form="Skriv til oss", formlabel="Skriv til oss i kontaktskjemaet", stick="Bestill via WhatsApp", stick_s="fra 68 kr/mnd",
   consent="Vi vil gjerne telle besøk og klikk for å forbedre siden. Ingen cookies, ingen annonsesporere.", more="Les mer", no="Nei takk", yes="Godta", consentlabel="Statistikk",
   sw_text="English", sw_label="English version", sw_lang="en", home="/", contact="/kontakt/", cookies="/cookies/", loc="nb_NO"),
}

def mk(lang):
    L = LANGS[lang]
    s = src
    s = s.replace('<html lang="sv">', f'<html lang="{L["html"]}" data-site="iptvnorwayone">')
    s = s.replace('<meta property="og:locale" content="sv_SE">', f'<meta property="og:locale" content="{L["loc"]}">')
    s = s.replace('content="BästaIPTVHD"', 'content="IPTV Norway One"').replace("#08001A", "#050E24")
    s = s.replace("Hoppa till innehållet", L["skip"])
    t = "".join(f"<span>{x}</span>" for x in L["ticker"] * 2)
    s = re.sub(r'<div class="ticker" aria-hidden="true"><div class="ticker-in">.*?</div></div>',
               lambda m: f'<div class="ticker" aria-hidden="true"><div class="ticker-in">{t}</div></div>', s, flags=re.S)
    s = s.replace('<span class="wm"><b>Bästa</b><i>IPTV</i><sup>HD</sup></span>', '<span class="wm"><b>IPTV</b><i>Norway</i><sup>One</sup></span>')
    s = s.replace('href="/" aria-label="BästaIPTVHD, startsida"', f'href="{L["home"]}" aria-label="{L["brandlabel"]}"')
    nav = "".join(f'<a href="{h}">{n}</a>' for h, n in L["nav"])
    s = re.sub(r'(<nav class="nav" aria-label=")Huvudmeny(">\s*).*?(\s*<button class="theme")',
               lambda m: m.group(1) + L["navlabel"] + m.group(2) + nav + m.group(3), s, flags=re.S)
    s = s.replace('aria-label="Byt mellan ljust och mörkt läge"', f'aria-label="{L["theme"]}"')
    sw = f'<a class="lang-sw" hreflang="{L["sw_lang"]}" lang="{L["sw_lang"]}" href="{{{{ALT}}}}" aria-label="{L["sw_label"]}">{L["sw_text"]}</a>'
    s = s.replace('</button>\n      <a class="btn btn-sm nav-cta"', '</button>\n      ' + sw + '\n      <a class="btn btn-sm nav-cta"')
    s = s.replace('rel="noopener" target="_blank">Beställ</a>', f'rel="noopener" target="_blank">{L["order"]}</a>')
    s = s.replace("Abonnemang för svensk och nordisk tv i HD. Beställning och support via WhatsApp.", L["foot"])
    fn = "".join(f'<a href="{h}">{n}</a>' for h, n in L["fnav"])
    s = re.sub(r'(<nav class="foot-nav" aria-label=")Sidfot(">\s*).*?(\s*</nav>)',
               lambda m: m.group(1) + L["footnav"] + m.group(2) + fn + m.group(3), s, flags=re.S)
    s = re.sub(r'<p class="wrap foot-legal">.*?</p>', lambda m: f'<p class="wrap foot-legal">{L["legal"]}</p>', s, flags=re.S)
    s = s.replace('aria-label="Beställ på WhatsApp"', f'aria-label="{L["wa_float"]}"').replace("</svg>Beställ på WhatsApp</a>", f'</svg>{L["wa_float"]}</a>')
    s = s.replace('href="/kontakt/" aria-label="Skriv till oss i kontaktformuläret"', f'href="{L["contact"]}" aria-label="{L["formlabel"]}"')
    s = s.replace("<span>Skriv till oss</span>", f'<span>{L["form"]}</span>')
    s = s.replace("Beställ via WhatsApp <span>från 64 kr/mån</span>", f'{L["stick"]} <span>{L["stick_s"]}</span>')
    s = s.replace('<aside aria-label="Beställ">', f'<aside aria-label="{L["order"]}">')
    s = s.replace('aria-label="Statistik"', f'aria-label="{L["consentlabel"]}"')
    s = re.sub(r"<p>Vi vill räkna.*?</p>", lambda m: f'<p>{L["consent"]} <a href="{L["cookies"]}">{L["more"]}</a></p>', s, flags=re.S)
    s = s.replace(">Nej tack<", f'>{L["no"]}<').replace(">Godkänn<", f'>{L["yes"]}<')
    return s

for l in ("en", "no"):
    out = mk(l)
    open(os.path.join(ROOT, f"layout.{l}.html"), "w", encoding="utf-8").write(out)
    left = re.findall(r"Bästa|svensk|Beställ|Sidfot|Hoppa|Huvudmeny|Statistik|Godkänn", out)
    print(l, "leftover:", left)
