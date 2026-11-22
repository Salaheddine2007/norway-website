import sys
sys.path.insert(0, r"C:\Users\DELL\AppData\Local\Temp\claude\ac5e4f4ff9d25599\1da4b7fd-101c-468b-9d88-b4a6ba448f91\scratchpad")
from gen_pages import *

NO = dict(
    mon={"1": "1 måned", "3": "3 måneder", "6": "6 måneder", "12": "12 måneder"}, screen="skjerm", once="engangspris, ingen fornyelse", best="Best verdi",
    sub={"1": "Bra for å teste", "3": "En sesong", "6": "Et halvt år", "12": "Et helt år"},
    incl=["Norske og nordiske kanaler", "HD, og 4K der kanalen har det", "TV-guide (EPG)", "Hjelp med installasjonen på WhatsApp", "Ingen automatisk fornyelse"],
    order_msg="Hei! Jeg vil bestille IPTV Norway One: {m}, {d} ({p}).", pick="Velg {m}")
T = NO

def no_pages():
    faq = [
        ("Hva er IPTV Norge?", "IPTV Norge betyr TV levert over internettforbindelsen din i stedet for parabol, kabel eller antenne. Med IPTV Norway One ser du norske og nordiske kanaler i en app på TV-en, boksen, mobilen eller datamaskinen."),
        ("Hva er forskjellen på IPTV Norge og IPTV Nordic?", "IPTV Norge handler om norske kanaler og en norsk TV-guide. IPTV Nordic betyr at kanaler fra Sverige, Danmark og Finland også er med. Med IPTV Norway One får du begge deler i samme pakke."),
        ("Hvilken internetthastighet trenger jeg?", "Regn med minst 10 Mbit/s per skjerm for HD og 25 Mbit/s for 4K. Mål på TV-en eller boksen, ikke på mobilen. En nettverkskabel gir nesten alltid jevnere bilde enn wifi."),
        ("Må jeg kjøpe en boks?", "Som regel ikke. Samsung- og LG-TV fra de siste årene klarer IPTV med en app. Har du en eldre TV er en Fire TV Stick eller en Android TV-boks den billigste måten å komme i gang på."),
        ("Fornyes abonnementet automatisk?", "Nei. Vi trekker ingen penger automatisk og lagrer ingen kortopplysninger. Når perioden nærmer seg slutten, forlenger du selv hvis du vil."),
        ("Hvordan betaler jeg?", "Du bestiller på WhatsApp og får betalingsinformasjonen der. Vi tar imot Visa, Mastercard, Maestro, Apple Pay, Google Pay og PayPal, og fra andre EU-land også SEPA, iDEAL, Bancontact og giropay."),
        ("Kan jeg teste før jeg kjøper en lengre pakke?", "Ja. Start med én måned for 189 kr. Den fornyes ikke av seg selv, så det er ingenting å si opp. Fungerer alt, kan du ta en lengre pakke når måneden er over."),
        ("Er IPTV lovlig i Norge?", "IPTV er bare en teknologi, og den er lovlig. Det som avgjør er om kanalene du ser på har rettigheter til å distribueres. Vi kan ikke gi juridisk rådgivning, så spør oss hva en pakke inneholder før du bestiller, og les informasjonen fra <a href=\"https://www.medietilsynet.no/\" target=\"_blank\" rel=\"noopener\">Medietilsynet</a>. Du er selv ansvarlig for hvordan du bruker tjenesten."),
    ]
    home_meta = {"speakable": True, "keyword": "iptv norge", "crumb": "Hjem", "alt": "",
        "title": "IPTV Norge 2026: norsk og nordisk TV i HD fra 68 kr/mnd",
        "desc": "IPTV Norge for norske hjem: norske og nordiske kanaler i HD, TV-guide og hjelp med installasjonen på WhatsApp. Fra 68 kr/mnd uten binding. Bestill i dag.",
        "og": "IPTV Norge 2026: norsk og nordisk TV i HD fra 68 kr i måneden",
        "img_alt": "IPTV Norge: norsk og nordisk TV i HD på smart-TV, boks og mobil",
        "images": [
            {"name": "no-home-enheter", "title": "IPTV Norge på smart-TV, Fire TV Stick, Android TV og Apple TV", "alt": "IPTV Norge på smart-TV, Fire TV Stick, Android TV, Apple TV og MAG-boks"},
            {"name": "no-home-nordic", "title": "IPTV Nordic: norske, svenske, danske og finske kanaler i én app", "alt": "IPTV Nordic med norske, svenske, danske og finske kanaler i samme app"},
            {"name": "no-home-steg", "title": "Kom i gang med IPTV Norge i tre steg", "alt": "Kom i gang med IPTV Norge i tre steg via WhatsApp"}],
        "schema": [
            {"@context": "https://schema.org", "@type": "Product", "name": "IPTV Norway One abonnement", "brand": {"@type": "Brand", "name": "IPTV Norway One"},
             "description": "IPTV-abonnement med norske og nordiske kanaler i HD for smart-TV, Android TV, Apple TV, mobil og datamaskin.",
             "image": BASE + "/assets/og/no-home.png",
             "offers": {"@type": "AggregateOffer", "priceCurrency": "NOK", "lowPrice": str(NOK["1"]["1"]), "highPrice": str(NOK["3"]["12"]), "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/no/iptv-abonnement-norge/"}},
            faq_schema(faq)]}
    home = f"""
<section class="hero">
  <div class="wrap hero-in">
    <div>
      <span class="pill"><span class="dot"></span>Live nå · norsk og nordisk TV i HD</span>
      <h1>IPTV Norge <span class="grad-text">for norsk og nordisk TV</span> i HD</h1>
      <p class="lead">IPTV Norge skal være enkelt: <b>norske og nordiske kanaler i HD</b>, i en app på TV-en du allerede har. Hos IPTV Norway One velger du 1, 3, 6 eller 12 måneder, og vi hjelper deg med installasjonen på WhatsApp.</p>
      <div class="hero-cta">
        <a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg vil bestille IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Bestill på WhatsApp</a>
        <a class="btn btn-ghost" href="#priser">Se prisene →</a>
      </div>
      <ul class="chips">
        <li>{{{{I:check}}}} Ingen binding</li>
        <li>{{{{I:check}}}} HD, og 4K der det finnes</li>
        <li>{{{{I:check}}}} Smart-TV til mobil</li>
        <li>{{{{I:check}}}} Priser i NOK og EUR</li>
      </ul>
    </div>
    <div class="screen-wrap" aria-hidden="true">
      <div class="browser">
        <div class="browser-bar"><i></i><i></i><i></i><span>IPTV Norway One · Filmer og serier</span></div>
        <div class="posters">
          <figure><img src="/assets/posters/poster-1.webp" width="1200" height="677" alt="" fetchpriority="high"><figcaption><b class="live">LIVE</b><b>HD</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-2.webp" width="1200" height="677" alt="" loading="lazy"><figcaption><b>4K</b></figcaption></figure>
          <figure><img src="/assets/posters/poster-3.webp" width="900" height="508" alt="" loading="lazy"><figcaption><b>HD</b></figcaption></figure>
        </div>
      </div>
      <div class="f-badge b1"><span class="ic">{{{{I:shield}}}}</span><span>Ingen binding<small>ingenting fornyes av seg selv</small></span></div>
      <div class="f-badge b2"><span class="ic">{{{{I:zap}}}}</span><span>68 kr/mnd<small>med 12 måneder</small></span></div>
      <div class="f-badge b3"><span class="ic">{{{{I:spark}}}}</span><span>HD + 4K<small>der kanalen har det</small></span></div>
    </div>
  </div>
</section>

<div class="wrap tiles" role="list" aria-label="IPTV Norway One i tall">
  <div role="listitem"><b>68 kr</b><span>per måned med 12 måneder</span></div>
  <div role="listitem"><b>0</b><span>dagers binding</span></div>
  <div role="listitem"><b>4</b><span>nordiske land i pakken</span></div>
  <div role="listitem"><b>3</b><span>skjermer samtidig, hvis du vil</span></div>
</div>

<section class="strip" aria-label="Fungerer på">
  <div class="wrap">
    <p>Fungerer på skjermene du allerede har</p>
    <ul>
      <li>{{{{I:tv}}}} Samsung</li><li>{{{{I:tv}}}} LG</li><li>{{{{I:box}}}} Android TV</li><li>{{{{I:box}}}} Fire TV Stick</li>
      <li>{{{{I:tv}}}} Apple TV</li><li>{{{{I:phone}}}} iPhone og Android</li><li>{{{{I:laptop}}}} Windows og Mac</li><li>{{{{I:box}}}} MAG-boks</li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap measure">
    <p>Denne siden er skrevet for deg som leter etter IPTV Norge og vil vite hva du faktisk får. Vi går gjennom kanalene, prisene, hvilke skjermer som fungerer og hvordan du kommer i gang. Vi sier også fra når vi ikke er riktig valg. Vil du heller lese på engelsk? Gå til den <a href="/" hreflang="en" lang="en">engelske versjonen</a>.</p>
    <h2 class="center-h">IPTV Norway One i korte trekk</h2>
    <dl class="facts">
      <div><dt>Pris</dt><dd>189 til 1 989 kr, fra 68 kr/mnd</dd></div>
      <div><dt>Pakker</dt><dd>1, 3, 6 eller 12 måneder, samme innhold</dd></div>
      <div><dt>Binding</dt><dd>Ingen, ingenting fornyes automatisk</dd></div>
      <div><dt>Kanaler</dt><dd>Norske pluss Sverige, Danmark og Finland</dd></div>
      <div><dt>Bilde</dt><dd>HD, og 4K der kanalen sender i 4K</dd></div>
      <div><dt>Hastighet</dt><dd>10 Mbit/s per skjerm for HD, 25 for 4K</dd></div>
      <div><dt>Enheter</dt><dd>Smart-TV, Fire TV, Android TV, Apple TV, mobil, PC, MAG</dd></div>
      <div><dt>Bestilling</dt><dd>WhatsApp, på norsk eller engelsk</dd></div>
      <div><dt>Betaling</dt><dd>Kort, Apple Pay, Google Pay, PayPal</dd></div>
    </dl>
    <!--TOC-->
  </div>
</section>

<section class="sec sec-tight">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">Dette er inkludert</span>
      <h2>Derfor passer IPTV Norway One for norske hjem</h2>
      <p>God IPTV Norge handler ikke om den lengste kanallisten. Det handler om at TV-en starter når du trykker på fjernkontrollen, at guiden viser riktig program og at det finnes noen å spørre. Slik ser det ut hos oss.</p>
    </div>
  </div>
  <div class="wrap feat">
    {cards([
      ("cyan", "globe", "Norske og nordiske kanaler", "Nyheter, underholdning, barnekanaler og sport, pluss kanaler fra Sverige, Danmark og Finland. Utvalget kan endre seg over tid. Spør oss om en bestemt kanal før du bestiller, så får du et ærlig svar."),
      ("violet", "spark", "HD som standard, 4K der det finnes", "Kanalene leveres i HD, og i 4K der kanalen selv sender i 4K. Hvor skarpt bildet blir hjemme avhenger også av TV-en og nettet ditt. Les mer i <a href=\"/no/guider/\">IPTV-guidene</a>."),
      ("pink", "calendar", "TV-guide (EPG) i appen", "En oversikt som viser hva som går nå og senere på hver kanal, som vanlig TV. Det er den som gjør at IPTV føles som TV og ikke som en liste med lenker."),
      ("green", "wifi", "Stabilt bilde en lørdagskveld", "Bildet skal holde også mellom 19 og 22, når alle bruker nettet samtidig. Det meste som får IPTV til å fryse sitter hjemme hos deg, oftest wifi, og det hjelper vi deg å løse."),
      ("blue", "chat", "Alt i én chat", "Bestilling, betaling og hjelp med oppsettet skjer i samme WhatsApp-tråd, på norsk eller engelsk."),
    ])}
  </div>
</section>

<section class="sec sec-night">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Med i pakken</span>
      <h2>Kanalutvalg for hele husholdningen</h2>
      <p>Norske kanaler først, så resten av Norden og internasjonale kanaler. Spør oss om en bestemt kanal før du bestiller.</p>
    </div>
    {channels_html([("globe","Norske kanaler","Nyheter, underholdning og lokalt"),("tv","Nordiske kanaler","Sverige, Danmark og Finland"),("zap","Sport","Fotball, vintersport og mer direkte"),("film","Film og serier","Filmkanaler og serier"),("spark","Barn og familie","Barnekanaler"),("calendar","Dokumentar og natur","Fakta, natur og historie"),("chat","Nyheter","Norske og internasjonale"),("monitor","Internasjonalt","Kanaler fra flere land")])}
    <p class="price-note" style="color:var(--on-night-muted)">Kanalutvalget kan endre seg over tid.</p>
  </div>
</section>

<section class="sec sec-tight" id="priser">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Priser</span>
      <h2>Hva IPTV Norge koster: fire pakker, samme innhold</h2>
      <p>Velg hvor mange skjermer dere vil se på samtidig, og så hvor lenge. Kanalene og bildekvaliteten er de samme i alle pakker. Prisene står i kroner med euro-beløpet ved siden av.</p>
    </div>
    <!--DEVICES-->
    {pricing_cards("no", T)}
    <div class="measure">
      <!--PRICETABLE-->
      <p class="ruler-note">Vil du ha lavest pris per måned, er tolv måneder riktig valg. Med 2 eller 3 skjermer kan flere i husholdningen se samtidig. Betaling, flere skjermer og vilkår står på siden om <a href="/no/iptv-abonnement-norge/">IPTV-abonnement i Norge</a>. Kronebeløpene er regnet ut fra en kurs på omtrent {SITE["nok_rate"]} kr per euro, og euro er prisen du faktisk betaler.</p>
    </div>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">Skjermer</span>
      <h2>IPTV Norge på skjermene du allerede har</h2>
      <p>IPTV Norge skal fungere på det du har hjemme. En app fra enhetens egen appbutikk er nok, og vi sier hvilken som fungerer best på din modell.</p>
    </div>
    <!--IMG:no-home-enheter-->
  </div>
  <div class="wrap devs" style="margin-top:28px">
    {cards([
      ("cyan", "tv", "Samsung og LG smart-TV", "De fleste modeller fra omtrent 2018 og senere klarer det med en app. Hvilke apper som finnes avhenger av modell og år, så send oss modellnummeret."),
      ("green", "box", "Fire TV Stick og Android TV", "Størst utvalg av apper og ofte det jevneste bildet. En Fire TV Stick gjør en eldre TV smart for en rimelig pris."),
      ("pink", "phone", "Apple TV, iPhone og iPad", "En IPTV-spiller fra App Store, med samme app på alle Apple-enhetene dine. Apple forklarer hvordan du installerer apper på <a href=\"https://support.apple.com/no-no/apple-tv\" target=\"_blank\" rel=\"noopener\">supportsidene for Apple TV</a>."),
      ("amber", "laptop", "MAG-boks og PC", "En MAG-boks kobles til kontoen med boksens MAC-adresse, og den innstillingen gjør vi for deg. På PC fungerer både VLC og IPTV-apper."),
    ])}
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Slik kommer du i gang</span>
      <h2>Kom i gang med IPTV Norge i tre steg</h2>
      <p>De fleste er i gang samme kveld. Det som tar tid i IPTV Norge er sjelden appen, men å finne riktig app til akkurat din TV.</p>
    </div>
    <ol class="steps">
      <li><h3>Velg hvor lenge</h3><p>Alle pakker har samme innhold. Er du usikker, start med én måned.</p></li>
      <li><h3>Skriv til oss på WhatsApp</h3><p>Si hvilken pakke du vil ha og hvilken TV eller boks du har. Vi svarer med betaling og riktig app for skjermen din.</p></li>
      <li><h3>Logg inn og se</h3><p>Du får innloggingen og en kort veiledning for din TV. Står du fast, hjelper vi deg videre i chatten.</p></li>
    </ol>
    <p style="margin-top:28px;text-align:center"><a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg vil prøve IPTV Norway One i én måned (189 kr).}}}}" rel="noopener" target="_blank">Prøv én måned for 189 kr</a></p>
    <div class="measure" style="text-align:center"><!--IMG:no-home-steg--><p>Hele gjennomgangen, enhet for enhet, finner du i guiden om å <a href="/no/installer-iptv/">installere IPTV</a>.</p></div>
  </div>
</section>

<section class="sec sec-night">
  <div class="wrap measure">
    <div class="sec-head center">
      <span class="eyebrow">IPTV Norge og IPTV Nordic</span>
      <h2>IPTV Norge, IPTV Nordic og IPTV Norway: hva er forskjellen?</h2>
      <p>Ordene brukes om hverandre, men de betyr litt forskjellige ting. Slik pleier vi å forklare det.</p>
    </div>
    <ul>
      <li><strong>IPTV Norge og norsk IPTV:</strong> norske kanaler med norsk TV-guide, for deg som hovedsakelig vil se norsk TV.</li>
      <li><strong>IPTV Nordic og Nordic IPTV:</strong> norske kanaler pluss kanaler fra Sverige, Danmark og Finland. Vi forklarer det på siden om <a href="/no/iptv-nordic/">IPTV Nordic</a>.</li>
      <li><strong>IPTV Norway:</strong> det samme på engelsk. Den <a href="/" hreflang="en" lang="en">engelske siden</a> er skrevet for dem som søker slik.</li>
    </ul>
    <p>Hos IPTV Norway One er begge med i samme pakke, så du trenger ikke å velge mellom norsk og nordisk IPTV.</p>
    <!--IMG:no-home-nordic-->
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <span class="eyebrow">Sammenligning</span>
      <h2>IPTV sammenlignet med kabel-TV og strømming</h2>
      <p>IPTV er ikke riktig for alle. Slik står IPTV Norge seg mot kabel-TV og strømmetjenester.</p>
    </div>
    <ul class="checks">
      <li>{{{{I:check}}}}<span>Ingen binding på 12 eller 24 måneder</span></li>
      <li>{{{{I:check}}}}<span>Ingen parabol, ingen kabeluttak, ingen tekniker hjemme</span></li>
      <li>{{{{I:check}}}}<span>Samme tjeneste på hytta hvis det finnes internett</span></li>
      <li>{{{{I:check}}}}<span>TV-guide og kanalbytte som på vanlig TV</span></li>
      <li>{{{{I:check}}}}<span>Nordiske kanaler i samme pakke</span></li>
      <li>{{{{I:check}}}}<span>Fungerer på TV, mobil og PC</span></li>
    </ul>
    <div class="vs-wrap" tabindex="0" role="region" aria-label="Sammenligning: IPTV Norway One, kabel-TV og strømming"><table class="vs"><thead><tr><th scope="col">Funksjon</th><th scope="col" class="us"><span class="vs-logo"><img class="mark" src="/assets/icons/mark.svg" width="28" height="28" alt=""><span class="wm"><b>IPTV</b><i>Norway</i><sup>One</sup></span></span></th><th scope="col">Kabel-TV</th><th scope="col">Strømming</th></tr></thead><tbody>
      <tr><th scope="row">Norske kanaler</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Ja</span></span></td><td><span class="yes">{{{{I:check}}}}<span class="sr">Ja</span></span></td><td>Delvis</td></tr>
      <tr><th scope="row">Nordiske kanaler (Sverige, Danmark, Finland)</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Ja</span></span></td><td>Delvis</td><td>Sjelden</td></tr>
      <tr><th scope="row">Direkte-TV med TV-guide</th><td class="us"><span class="yes">{{{{I:check}}}}<span class="sr">Ja</span></span></td><td><span class="yes">{{{{I:check}}}}<span class="sr">Ja</span></span></td><td>Sjelden</td></tr>
      <tr><th scope="row">HD og 4K</th><td class="us">HD, 4K der det sendes</td><td>Avhenger av pakke</td><td>Avhenger av tjeneste</td></tr>
      <tr><th scope="row">Pris per måned</th><td class="us">Fra 68 kr</td><td>Ofte flere hundre kroner</td><td>Per tjeneste</td></tr>
      <tr><th scope="row">Binding</th><td class="us">Ingen</td><td>Ofte 12 til 24 måneder</td><td>Ingen</td></tr>
      <tr><th scope="row">Installasjon</th><td class="us">En app</td><td>Uttak og boks</td><td>En app</td></tr>
      <tr><th scope="row">Fungerer på hytta</th><td class="us">Hvis det finnes internett</td><td><span class="no">{{{{I:x}}}}<span class="sr">Nei</span></span></td><td>Hvis det finnes internett</td></tr>
      <tr><th scope="row">Support</th><td class="us">WhatsApp, norsk eller engelsk</td><td>Kundeservice</td><td>E-post eller chat</td></tr>
    </tbody></table></div>
    <p>Er nettet ditt tregt eller ujevnt, er kabel-TV eller parabol et tryggere valg. Under 10 Mbit/s til TV-en er ingen tjeneste riktig IPTV Norge for deg, uansett hvor god den er.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap measure why">
    <div class="sec-head center">
      <span class="eyebrow">Hvorfor oss</span>
      <h2>Derfor velger folk IPTV Norway One</h2>
    </div>
    <h3>Support på WhatsApp</h3>
    <p>Du skriver til et menneske, ikke til et skjema. Send et bilde av skjermen, så ser vi med en gang hva det gjelder.</p>
    <h3>Rette vilkår</h3>
    <p>Ingen binding, ingen automatisk fornyelse og priser i kroner med euro ved siden av. IPTV skal være like lett å slutte med som å begynne med. Alt står i <a href="/no/vilkar/">vilkårene</a>.</p>
    <h3>Hvis noe ikke fungerer</h3>
    <p>Skriv til oss på WhatsApp med et bilde av skjermen, så går vi gjennom nett, app og innstillinger sammen med deg. Hva som gjelder ved kjøp står i <a href="/no/vilkar/">vilkårene</a>.</p>
    <h3>Når vi ikke er riktig valg</h3>
    <p>Har du under 10 Mbit/s per skjerm, eller vil du ha en boks som noen installerer hjemme hos deg, passer en tradisjonell operatør bedre. Da er vi ikke riktig IPTV for deg, og det er ærligere å si det nå enn etter at du har betalt.</p>
  </div>
</section>

<section class="sec sec-alt">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Guider</span>
      <h2>Guider fra supporten vår</h2>
      <p>Installasjon, apper og feilsøking, skrevet ut fra spørsmålene vi får.</p>
    </div>
    <p><a href="/no/guider/">Alle IPTV-guider for Norge</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Spørsmål og svar</span>
      <h2>Vanlige spørsmål om IPTV Norge</h2>
    </div>
    {faq_html(faq)}
    <p style="margin-top:24px">Flere svar finner du under <a href="/no/vanlige-sporsmal/">vanlige spørsmål om IPTV</a>.</p>
  </div>
</section>

<section class="band">
  <div class="wrap band-in">
    <div><h2>Prøv IPTV Norge på din egen TV i kveld.</h2><p>Si hvilken TV du har, så sier vi hvilken pakke og app som passer.</p></div>
    <a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg har et spørsmål før jeg bestiller IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Skriv til oss på WhatsApp</a>
  </div>
</section>
"""
    save("no", "", home_meta, home)
    return faq


def no_rest(faq):
    plans_faq = [
        ("Kan jeg endre antall skjermer senere?", "Ja. Skriv til oss på WhatsApp før perioden din går ut og si hvor mange skjermer du vil ha neste gang. Prisen følger skjermnivået du velger."),
        ("Hva skjer når perioden er over?", "Tjenesten stopper. Ingenting fornyes automatisk, og vi lagrer ikke kortopplysningene dine. Vil du fortsette, bestiller du på nytt."),
        ("Er prisene oppgitt med mva?", "Prisene på denne siden er det du betaler. Vi viser kroner med euro-beløpet ved siden av. Beløpet i kroner er veiledende og regnet ut fra en kurs på omtrent 11,7 kr per euro."),
    ]
    save("no", "iptv-abonnement-norge", {"keyword": "iptv abonnement norge", "crumb": "IPTV-abonnement Norge", "alt": "iptv-subscription-norway",
        "title": "IPTV Abonnement Norge: 12 pakker fra 189 kr | Norway One",
        "desc": "IPTV abonnement Norge: 1, 3, 6 eller 12 måneder for 1, 2 eller 3 skjermer, fra 68 kr/mnd uten binding. Alle priser i kroner og euro samlet på én side.",
        "og": "IPTV abonnement Norge: 12 pakker fra 189 kr",
        "tldr": "Et IPTV-abonnement i Norge fra IPTV Norway One koster 189 kr for én måned og 819 kr for tolv måneder på én skjerm, som er 68 kr i måneden. To og tre skjermer koster mer. Ingenting fornyes automatisk.",
        "schema": [{"@context": "https://schema.org", "@type": "Product", "name": "IPTV Norway One abonnement", "brand": {"@type": "Brand", "name": "IPTV Norway One"},
                    "image": BASE + "/assets/og/no-iptv-abonnement-norge.png",
                    "offers": {"@type": "AggregateOffer", "priceCurrency": "NOK", "lowPrice": str(NOK["1"]["1"]), "highPrice": str(NOK["3"]["12"]), "offerCount": "12", "availability": "https://schema.org/InStock", "url": BASE + "/no/iptv-abonnement-norge/"}},
                   faq_schema(plans_faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Priser</span><h1>IPTV abonnement Norge: pakker og priser</h1>
<p>Én tjeneste, fire lengder og tre skjermnivåer. Velg hvor mange skjermer som skal fungere samtidig, og så hvor lenge du vil abonnere.</p></div></section>
<section class="sec sec-tight"><div class="wrap">
<!--TOC-->
<!--DEVICES-->
{pricing_cards("no", T)}
<div class="measure">
<h2>Hva et IPTV abonnement Norge inneholder</h2>
<p>Alle pakker for IPTV abonnement Norge har samme innhold: norske og nordiske kanaler i HD, 4K der kanalen sender det, TV-guide og hjelp med installasjonen på WhatsApp. Det eneste som varierer mellom pakkene er lengden og antall skjermer.</p>
<h2>Alle priser for 1, 2 og 3 skjermer</h2>
<!--PRICETABLE-->
<p>Euro er prisen du betaler, og kronebeløpet er veiledende ut fra omtrent {SITE["nok_rate"]} kr per euro. En lengre pakke gir alltid lavere pris per måned.</p>
<h2>Slik betaler du for IPTV-abonnementet</h2>
<p>Du bestiller på WhatsApp og får betalingsinformasjonen der. Vi tar imot Visa, Mastercard, Maestro, Apple Pay, Google Pay og PayPal, og fra andre EU-land også SEPA, iDEAL, Bancontact og giropay. Vi lagrer ikke kortopplysninger, og ingenting fornyes av seg selv.</p>
<h2>Slik velger du IPTV abonnement Norge kan stole på</h2>
<p>Når du sammenligner IPTV abonnement Norge tilbyr, se på bindingen, fornyelsen og supporten, ikke bare på antall kanaler. Våre pakker for IPTV abonnement Norge har ingen binding og ingen automatisk fornyelse. Vil du kjenne rettighetene dine som forbruker før du kjøper IPTV abonnement Norge selger, har <a href="https://www.forbrukerradet.no/" target="_blank" rel="noopener">Forbrukerrådet</a> gode veiledere.</p>
<h2>Hvilken pakke bør du velge?</h2>
<ul><li><strong>Usikker så langt:</strong> én måned. Den fornyes ikke, så det er ingenting å si opp.</li><li><strong>Lavest pris per måned:</strong> tolv måneder.</li><li><strong>Flere som ser samtidig:</strong> velg nivået med 2 eller 3 skjermer.</li></ul>
<p>Usikker på hva som passer TV-en din? Les først hvordan du <a href="/no/installer-iptv/">installerer IPTV</a>, eller gå tilbake til <a href="/no/">forsiden om IPTV Norge</a>. Vilkårene står i <a href="/no/vilkar/">vilkårene</a>.</p>
<h2>Spørsmål om pakkene</h2>
{faq_html(plans_faq)}
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Klar til å bestille?</h2><p>Si hvilken pakke og hvilken TV du har.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg vil bestille IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Bestill på WhatsApp</a></div></section>
""")

    nordic_faq = [
        ("Hva er IPTV Nordic?", "Også kalt Nordic IPTV, betyr det TV over internett med kanaler fra alle de nordiske landene i én app: Norge, Sverige, Danmark og Finland."),
        ("Er IPTV Nordic det samme som IPTV Norge?", "Ikke helt. IPTV Norge handler om norske kanaler. Nordic IPTV legger til de svenske, danske og finske. Med IPTV Norway One er begge med i samme pakke."),
        ("Kan jeg spørre om en bestemt kanal?", "Ja. Skriv til oss på WhatsApp før du bestiller, så sier vi ærlig fra om kanalen er med i pakken. Utvalget kan endre seg over tid."),
    ]
    save("no", "iptv-nordic", {"keyword": "iptv nordic", "crumb": "IPTV Nordic", "alt": "iptv-nordic",
        "title": "IPTV Nordic 2026: 4 land med TV i én app | Norway One",
        "desc": "IPTV Nordic forklart: norske, svenske, danske og finske kanaler i én app, hva du trenger for å se, og hvordan det henger sammen med IPTV Norge.",
        "og": "IPTV Nordic 2026: fire land med TV i én app",
        "tldr": "IPTV Nordic betyr norske, svenske, danske og finske kanaler i én IPTV-app. Hos IPTV Norway One er de nordiske kanalene med i samme pakke som de norske, fra 68 kr i måneden.",
        "schema": [faq_schema(nordic_faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Nordisk TV</span><h1>IPTV Nordic: fire land med TV i én app</h1>
<p>Følger du TV fra mer enn ett nordisk land, samler Nordic IPTV alt på ett sted. Her er hva det er, hva du trenger og hvordan det henger sammen med IPTV Norge.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>IPTV Nordic er en enkel idé: ett abonnement og én app med kanaler fra Norge, Sverige, Danmark og Finland. Nordic IPTV passer for familier med røtter i mer enn ett land, for dem som jobber over grensa og for alle som liker å se nabolandenes nyheter, sport og serier.</p>
<h2>Hva IPTV Nordic inneholder</h2>
<p>Hos IPTV Norway One ligger de nordiske kanalene i samme pakke som de norske. Det betyr norske kanaler først, så kanaler fra Sverige, Danmark og Finland, med TV-guide i appen. Utvalget kan endre seg over tid, så spør oss om en bestemt kanal før du bestiller.</p>
<h2>Nordic IPTV sammenlignet med IPTV Norge</h2>
<ul><li><strong>IPTV Norge:</strong> norske kanaler og norsk guide. Les <a href="/no/">oversikten om IPTV Norge</a>.</li><li><strong>Nordic IPTV:</strong> de norske kanalene pluss Sverige, Danmark og Finland.</li><li><strong>Engelsk versjon:</strong> samme informasjon på engelsk står på <a href="/iptv-nordic/" hreflang="en" lang="en">IPTV Nordic in English</a>.</li></ul>
<h2>Hva du trenger for å se Nordic IPTV</h2>
<p>Du trenger internett på minst 10 Mbit/s per skjerm for HD og 25 Mbit/s for 4K, og en enhet med en app. Samsung- og LG-TV, Android TV, Fire TV Stick, Apple TV, iPhone, Android og PC fungerer alle. Stegene står i guiden om å <a href="/no/installer-iptv/">installere IPTV</a>.</p>
<h2>Hvem Nordic IPTV passer for</h2>
<p>Nordic IPTV passer for husholdninger som følger TV fra mer enn ett land. Det kan være en familie med slekt i Sverige eller Danmark, et par der den ene vokste opp i Finland, eller en som pendler over grensa og vil ha lokale nyheter begge steder. Det passer også for dem som rett og slett liker å sammenligne hvordan nabolandene lager nyheter, sport og serier.</p>
<h2>Slik fungerer TV-guiden på tvers av land</h2>
<p>TV-guiden (EPG) i appen viser hva som går nå og senere på hver kanal, gruppert etter land. Du bytter mellom land i kanallisten på samme måte som du bytter kanalgruppe på vanlig TV. Ser et programtidspunkt feil ut, si fra hvilken kanal det gjelder, så sjekker vi guidedataene sammen med deg.</p>
<h2>Hva du kan forvente av kanalutvalget</h2>
<p>De nordiske landene deler mye kultur, men hvert land har egne kringkastere og egne rettigheter. Derfor lover vi aldri en liste vi ikke kan bevise. Spør om kanalene du bryr deg om før du bestiller, og husk at utvalget kan endre seg over tid. For bakgrunn om hvordan de nordiske landene samarbeider, se <a href="https://www.norden.org/no" target="_blank" rel="noopener">nettsiden til Nordisk samarbeid</a>.</p>
<h2>Hva Nordic IPTV koster</h2>
<p>Pakkene starter på 189 kr for én måned, og tolv måneder på én skjerm er 819 kr, som er 68 kr i måneden. Alle priser for 1, 2 og 3 skjermer står på siden om <a href="/no/iptv-abonnement-norge/">IPTV abonnement Norge</a>.</p>
<h2>Spørsmål om IPTV Nordic</h2>
{faq_html(nordic_faq)}
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Vil du ha de nordiske kanalene hjemme?</h2><p>Spør om en kanal før du bestiller.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg er interessert i IPTV Nordic fra IPTV Norway One.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Skriv til oss på WhatsApp</a></div></section>
""")

    save("no", "installer-iptv", {"keyword": "installer iptv", "crumb": "Installer IPTV", "alt": "install-iptv",
        "title": "Installer IPTV i 3 steg på smart-TV, Fire TV og mobil",
        "desc": "Installer IPTV på Samsung og LG smart-TV, Fire TV Stick, Android TV, Apple TV, iPhone og PC. Steg, hastighetskrav og hvor du får hjelp.",
        "og": "Installer IPTV i 3 steg på smart-TV, Fire TV og mobil",
        "tldr": "For å installere IPTV velger du en pakke, får innloggingen på WhatsApp og legger en IPTV-app på TV-en, boksen eller mobilen. Det tar noen minutter hvis du har 10 Mbit/s per skjerm og riktig app for modellen din."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Oppsett</span><h1>Installer IPTV: smart-TV, Fire TV, Apple TV og mobil</h1>
<p>Du trenger ikke spesialutstyr. Du trenger en app for enheten din, innloggingen din og et nett som er raskt nok.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<!--TOC-->
<p>For å installere IPTV på en TV, en boks eller en mobil følger du de samme tre stegene på alle enheter. Detaljene varierer mellom merker, og derfor spør vi om modellen din før vi anbefaler en app.</p>
<h2>Før du installerer IPTV: sjekk nettet</h2>
<p>Regn med minst 10 Mbit/s per skjerm for HD og 25 Mbit/s for 4K. Mål på TV-en eller boksen, ikke på mobilen, for TV-en står ofte lengre fra ruteren. En nettverkskabel gir nesten alltid jevnere bilde enn wifi.</p>
<h2>Tre steg for å installere IPTV</h2>
<ol><li><strong>Bestill og få innloggingen.</strong> Skriv til oss på WhatsApp med pakken du vil ha og modellen på TV-en eller boksen.</li><li><strong>Installer appen.</strong> Åpne appbutikken på enheten, installer IPTV-spilleren vi anbefaler for din modell og åpne den.</li><li><strong>Logg inn.</strong> Skriv inn opplysningene vi sender deg. Kanallisten og TV-guiden laster i løpet av et minutt eller to.</li></ol>
<h2>Installer IPTV på Samsung og LG smart-TV</h2>
<p>De fleste modeller fra omtrent 2018 og senere kan kjøre en IPTV-app fra TV-ens egen appbutikk. Hvilke apper som finnes avhenger av modell og år, så send oss modellnummeret fra etiketten på baksiden.</p>
<h2>Installer IPTV på Fire TV Stick og Android TV</h2>
<p>Disse gir størst utvalg av apper. Åpne appbutikken, søk etter spilleren vi anbefaler og installer den. Amazon forklarer det grunnleggende på sine <a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=GYXQJZZ2VAXYW9H9" target="_blank" rel="noopener">hjelpesider for Fire TV</a>.</p>
<h2>Installer IPTV på Apple TV, iPhone og iPad</h2>
<p>Installer en IPTV-spiller fra App Store, og logg inn med opplysningene vi sender. Apples egne <a href="https://support.apple.com/no-no/apple-tv" target="_blank" rel="noopener">supportsider for Apple TV</a> forklarer hvordan du installerer apper.</p>
<h2>Installer IPTV på MAG-boks eller PC</h2>
<p>En MAG-boks kobles til kontoen din med boksens MAC-adresse, og det setter vi opp for deg. På PC kan du bruke VLC eller en IPTV-app.</p>
<h2>Hvis bildet henger etter at du har installert IPTV</h2>
<p>Flytt TV-en over på nettverkskabel, start ruteren på nytt og steng annen strømming på nettet. Hvis det fortsatt henger, send oss et bilde av skjermen på WhatsApp.</p>
<h2>Slik velger du riktig app</h2>
<p>Velg appen etter modellen på TV-en, ikke etter navnet på appen. Samsung og LG har hver sin appbutikk, og utvalget varierer mellom årsmodeller. Spør oss først, så sparer du tid, og står du fast på et steg sender du oss et bilde av skjermen, så peker vi på neste trykk.</p>
<h2>Tips for et jevnere bilde</h2>
<p>Plasser ruteren i samme rom som TV-en hvis du kan, og unngå tykke vegger. Må du bruke wifi, velg 5 GHz-båndet, som er raskere over korte avstander enn 2,4 GHz. Steng andre apper som strømmer video mens du tester, og start appen på nytt én gang etter første innlogging, slik at kanallisten og guiden laster ordentlig.</p>
<h2>Dette trenger du før du starter</h2>
<ul><li>Modellen på TV-en eller boksen, fra etiketten eller innstillingsmenyen.</li><li>Internett på minst 10 Mbit/s per skjerm.</li><li>Innloggingen din fra oss på WhatsApp.</li><li>En konto i enhetens appbutikk (Samsung, LG, Google, Amazon eller Apple).</li></ul>
<h2>Hvor lang tid oppsettet tar</h2>
<p>Med riktig app for modellen din blir de fleste ferdige i løpet av noen få minutter. Å finne riktig app tar lengre tid enn selve oppsettet, så si modellen din først, så peker vi deg til riktig en.</p>
<p>Klar til å starte? Se <a href="/no/iptv-abonnement-norge/">pakker og priser</a>, les om de <a href="/no/iptv-nordic/">nordiske kanalene</a> eller gå tilbake til <a href="/no/">IPTV Norge</a>.</p>
</div></div></section>
<section class="band"><div class="wrap band-in"><div><h2>Står du fast på et steg?</h2><p>Send TV-modellen din, så sier vi hva du skal gjøre.</p></div>
<a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg trenger hjelp med å installere IPTV på TV-en min.}}}}" rel="noopener" target="_blank">{{{{I:chat}}}} Spør på WhatsApp</a></div></section>
""")

    save("no", "vanlige-sporsmal", {"crumb": "Vanlige spørsmål", "alt": "faq",
        "title": "IPTV Norge: vanlige spørsmål og svar | IPTV Norway One",
        "desc": "Svar om IPTV Norway One: pakker, betaling, hastighet, enheter, fornyelse og lovlighet. Korte og rake svar, skrevet av supporten vår.",
        "schema": [faq_schema(faq)]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Spørsmål</span><h1>Vanlige spørsmål om IPTV</h1>
<p>Spørsmålene vi får oftest, besvart rett fram.</p></div></section>
<section class="sec sec-tight"><div class="wrap">{faq_html(faq)}
<p style="margin-top:24px">Mangler noe? <a href="/no/kontakt/">Kontakt oss</a> eller se <a href="/no/iptv-abonnement-norge/">pakkene</a>, eller gå tilbake til <a href="/no/">IPTV Norge</a>.</p></div></section>
""")

    save("no", "om-oss", {"crumb": "Om oss", "alt": "about",
        "title": "Om IPTV Norway One: hvem skriver guidene og hvorfor",
        "desc": "Om IPTV Norway One: en uavhengig IPTV-tjeneste for Norge, hvordan supporten skriver guidene og hvilke fakta vi vil og ikke vil påstå.",
        "schema": [{"@context": "https://schema.org", "@type": "AboutPage", "name": "Om oss", "url": BASE + "/no/om-oss/", "inLanguage": "nb"}]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Om oss</span><h1>Om IPTV Norway One</h1>
<p>En uavhengig IPTV-tjeneste for husholdninger i Norge, med support på WhatsApp.</p></div></section>
<section class="sec sec-tight"><div class="wrap"><div class="measure prose">
<p>IPTV Norway One selger IPTV-abonnement med norske og nordiske kanaler. Vi har ingen tilknytning til TV-selskapene, appene eller produsentene som nevnes på siden. Bestilling, betaling og hjelp skjer på WhatsApp.</p>
<h2 id="how-we-write">Slik skriver vi guidene</h2>
<p>Guidene skrives av supporten, de samme som svarer på WhatsApp. Vi skriver om spørsmål kundene faktisk stiller. Innstillinger og appfunksjoner kontrolleres mot produsentenes egne hjelpesider, som vi lenker til under hver guide, og vi retter teksten når noe endrer seg.</p>
<h2>Hva vi ikke vil påstå</h2>
<p>Vi publiserer ikke oppdiktede tall som oppetid i prosent, anmeldelsesscore eller kanalantall vi ikke kan bevise. Når vi ikke vet noe, sier vi det. Kanalutvalget kan endre seg over tid, så vi ber deg sjekke en bestemt kanal med oss før du bestiller.</p>
<p>Les <a href="/no/vilkar/">vilkårene</a>, <a href="/no/personvern/">personvernerklæringen</a> eller gå til <a href="/no/kontakt/">kontakt</a>.</p>
</div></div></section>
""")

    save("no", "kontakt", {"crumb": "Kontakt", "alt": "contact",
        "title": "Kontakt IPTV Norway One: WhatsApp og kontaktskjema",
        "desc": "Kontakt IPTV Norway One på WhatsApp for bestilling, installasjon og feilsøking, eller bruk kontaktskjemaet. Hva du bør ha med i første melding.",
        "schema": [{"@context": "https://schema.org", "@type": "ContactPage", "name": "Kontakt", "url": BASE + "/no/kontakt/", "inLanguage": "nb"}]},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Kontakt</span><h1>Kontakt oss</h1>
<p>WhatsApp er raskest, både for bestilling og hjelp med installasjonen. Si hvilken TV eller boks du har, så kan vi svare på riktig ting.</p></div></section>
<div class="wrap"><div class="prose">
<p><a class="btn" data-track="buy_click" href="{{{{WA:Hei! Jeg har et spørsmål om IPTV Norway One.}}}}" rel="noopener" target="_blank">Skriv på WhatsApp</a></p>
<div class="table-wrap"><table><tbody><tr><th scope="row">WhatsApp</th><td>{SITE["whatsapp_display"]}</td></tr><tr><th scope="row">Språk</th><td>Norsk og engelsk</td></tr></tbody></table></div>
<h2>Ta gjerne med dette i første melding</h2>
<p>Trenger du hjelp med installasjonen, skriv merke og modell på TV-en eller boksen, og send et bilde av skjermen hvis det vises en feilmelding. Gjelder det en bestilling, skriv hvilken pakke du vil ha. Prisene står på siden om <a href="/no/iptv-abonnement-norge/">IPTV abonnement Norge</a>. Oppsettet står i <a href="/no/installer-iptv/">installer IPTV</a>, og <a href="/no/vilkar/">vilkårene</a> forklarer hva som gjelder for en bestilling.</p>
<h2>Foretrekker du et skjema?</h2>
<p>Bruk kontaktskjemaet nederst på siden, så svarer vi til adressen du oppgir.</p>
</div></div>
""")

    save("no", "vilkar", {"crumb": "Vilkår", "alt": "terms",
        "title": "Vilkår for IPTV Norway One | Pakker og fornyelse",
        "desc": "Vilkår for IPTV Norway One: pakker, betaling, ingen automatisk fornyelse, support, bruk av tjenesten og dine rettigheter som forbruker i Norge."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Vilkår</span><h1>Vilkår</h1><p>Korte og rett fram. Sist oppdatert november 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>Tjenesten</h2><p>IPTV Norway One selger tilgang til en IPTV-tjeneste med norske og nordiske kanaler. Kanalutvalget kan endre seg over tid. Du kan spørre oss om en bestemt kanal på WhatsApp før du bestiller.</p>
<h2>Pakker og betaling</h2><p>Du velger en lengde (1, 3, 6 eller 12 måneder) og et antall skjermer (1, 2 eller 3). Du bestiller og betaler via WhatsApp. Prisene vises i kroner med euro-beløpet ved siden av.</p>
<h2>Fornyelse</h2><p>Ingenting fornyes automatisk. Vi lagrer ikke kortopplysninger. Når perioden er over, stopper tjenesten med mindre du bestiller på nytt.</p>
<h2>Support og problemer</h2><p>Hvis noe ikke fungerer, skriv til oss på WhatsApp med et bilde av skjermen, så går vi gjennom nett, app og innstillinger sammen med deg.</p>
<h2>Dine rettigheter</h2><p>Dine lovbestemte rettigheter som forbruker etter norsk rett påvirkes ikke av disse vilkårene.</p>
<h2>Bruk av tjenesten</h2><p>Tjenesten er til privat bruk i din husholdning. Du er selv ansvarlig for hvordan du bruker den og for å følge lovene som gjelder for deg.</p>
<p>Spørsmål? <a href="/no/kontakt/">Kontakt oss</a>. Se også <a href="/no/personvern/">personvernerklæringen</a> og <a href="/no/iptv-abonnement-norge/">pakkene</a>.</p>
</div></div>
""")
    save("no", "personvern", {"crumb": "Personvern", "alt": "privacy",
        "title": "Personvernerklæring for IPTV Norway One | Hva vi lagrer",
        "desc": "Personvern hos IPTV Norway One: hva vi samler inn når du bestiller eller bruker kontaktskjemaet, hvor lenge vi lagrer det og hvordan du ber om sletting."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Personvern</span><h1>Personvernerklæring</h1><p>Hva vi lagrer og hvorfor. Sist oppdatert november 2026.</p></div></section>
<div class="wrap"><div class="prose">
<h2>Hva vi samler inn</h2><p>Når du skriver til oss på WhatsApp ser vi telefonnummeret ditt og meldingene du sender. Når du bruker kontaktskjemaet får vi navnet, kontaktopplysningene og meldingen du skriver. Vi bruker dette bare for å svare deg og levere bestillingen.</p>
<h2>Hva vi ikke gjør</h2><p>Vi selger ikke dataene dine, vi lagrer ikke kortopplysninger og vi bruker ikke annonsesporere.</p>
<h2>Statistikk</h2><p>Hvis du godtar, teller vi sidevisninger og klikk for å forbedre siden. Det brukes ingen cookies. Hvis du sier nei, telles ingenting. Du kan endre valget på siden om <a href="/no/cookies/">cookies og statistikk</a>.</p>
<h2>Dine rettigheter</h2><p>Du kan be oss vise, rette eller slette det vi har om deg. Skriv til oss på <a href="/no/kontakt/">kontaktsiden</a>.</p>
<p>Se også <a href="/no/vilkar/">vilkårene</a> og <a href="/no/">forsiden</a>.</p>
</div></div>
""")
    save("no", "cookies", {"crumb": "Cookies og statistikk", "alt": "cookies",
        "title": "Cookies og statistikk hos IPTV Norway One | Ditt valg",
        "desc": "IPTV Norway One bruker ingen cookies. Valgfri statistikk teller besøk og klikk bare hvis du godtar. Slik fungerer det og slik endrer du valget."},
f"""
<section class="page-head"><div class="wrap"><span class="eyebrow">Cookies</span><h1>Cookies og statistikk</h1></div></section>
<div class="wrap"><div class="prose">
<p>Denne siden setter ingen cookies. Valgfri statistikk teller sidevisninger og klikk for å hjelpe oss å forbedre siden, og den lastes bare hvis du trykker Godta. Nei er standard.</p>
<p><button class="btn btn-sm btn-line" type="button" data-consent-reset>Endre valget mitt</button></p>
<p>Mer i <a href="/no/personvern/">personvernerklæringen</a>. Se også <a href="/no/vilkar/">vilkårene</a>, <a href="/no/">forsiden</a> og <a href="/no/kontakt/">kontakt</a>.</p>
</div></div>
""")
    save("no", "404", {"crumb": "Ikke funnet", "robots": "noindex, follow", "title": "Siden finnes ikke | IPTV Norway One", "desc": "Denne siden finnes ikke. Gå tilbake til forsiden eller se IPTV-pakkene."},
f"""
<section class="page-head"><div class="wrap"><h1>Siden finnes ikke</h1><p>Siden du leter etter finnes ikke. Gå til <a href="/no/">forsiden</a> eller se <a href="/no/iptv-abonnement-norge/">pakkene</a>.</p></div></section>
""")


if __name__ == "__main__":
    f = en_pages(); en_rest(f)
    nf = no_pages(); no_rest(nf)
    print("EN+NO pages written")
