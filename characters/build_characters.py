# Dynamo characters v2: outline-less flat illustration with soft shading. 13 distinct people, one style.
import os, subprocess
OR="#FF5A1A"; PAPER="#F6F1E8"; INK="#2B2633"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def shade(hex_, f):  # darken (f<1) or lighten (f>1)
    h=hex_.lstrip('#'); r,g,b=[int(h[i:i+2],16) for i in (0,2,4)]
    if f<1: r,g,b=[int(c*f) for c in (r,g,b)]
    else: r,g,b=[int(c+(255-c)*(f-1)) for c in (r,g,b)]
    return '#%02x%02x%02x'%(r,g,b)

def hand(x,y,skin,rot=0,scale=1):  # soft mitten hand, no outline
    d=shade(skin,.88)
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({scale})">'
            f'<rect x="-55" y="-45" width="120" height="100" rx="40" fill="{skin}"/>'
            f'<circle cx="-40" cy="-20" r="26" fill="{skin}"/>'
            f'<path d="M-10 -45 Q20 -60 50 -40" fill="none" stroke="{d}" stroke-width="6" stroke-linecap="round" opacity=".6"/>'
            f'<path d="M10 55 L10 10 M40 55 L40 10" fill="none" stroke="{d}" stroke-width="5" stroke-linecap="round" opacity=".5"/></g>')

def body(garment,col,skin):
    d=shade(col,.86); l=shade(col,1.12); o=[]
    o.append(f'<path d="M150 1080 C160 850 320 760 540 760 C760 760 920 850 930 1080 Z" fill="{col}"/>')
    o.append(f'<path d="M150 1080 C160 850 320 760 540 760 C520 800 500 900 490 1080 Z" fill="{d}" opacity=".35"/>')
    if garment in ("shirt","apron"):
        o.append(f'<path d="M470 762 L540 880 L610 762 Z" fill="{shade(skin,.95)}"/>')
        o.append(f'<path d="M470 762 L500 812 L540 790 L580 812 L610 762 L580 758 L540 775 L500 758 Z" fill="{l}"/>')
    if garment=="apron":
        o.append(f'<path d="M425 890 L655 890 L680 1080 L400 1080 Z" fill="#4A4652"/><path d="M450 890 L470 790 M630 890 L610 790" fill="none" stroke="#4A4652" stroke-width="12"/>')
    if garment=="crew": o.append(f'<path d="M470 765 Q540 830 610 765 Q540 800 470 765 Z" fill="{shade(skin,.95)}"/>')
    if garment=="hoodie":
        o.append(f'<path d="M410 790 C430 710 650 710 670 790 C660 840 600 860 540 860 C480 860 420 840 410 790 Z" fill="{d}"/>')
        o.append(f'<path d="M430 790 C450 735 630 735 650 790 C640 825 600 840 540 840 C480 840 440 825 430 790 Z" fill="{shade(skin,.95)}"/>')
        o.append(f'<path d="M505 850 L495 1010 M575 850 L585 1010" fill="none" stroke="{l}" stroke-width="7" stroke-linecap="round"/>')
    if garment in ("polo","button"):
        o.append(f'<path d="M478 762 L540 840 L602 762 Z" fill="{shade(skin,.95)}"/>')
        o.append(f'<path d="M478 762 L450 810 L525 800 L540 840 L555 800 L630 810 L602 762 Z" fill="{d}"/>')
        if garment=="button": o.append(f'<path d="M540 840 L540 1080" stroke="{d}" stroke-width="5"/><circle cx="540" cy="900" r="6" fill="{l}"/><circle cx="540" cy="970" r="6" fill="{l}"/>')
    if garment=="blazer":
        o.append(f'<path d="M430 775 L540 1080 L650 775 Z" fill="#F3EEE6"/>')
        o.append(f'<path d="M430 775 L470 760 L540 950 L610 760 L650 775 L560 1080 L520 1080 Z" fill="{d}"/>')
    if garment=="thobe":
        o.append(f'<path d="M500 762 Q540 810 580 762 Z" fill="{shade(skin,.95)}"/><path d="M540 810 L540 1080" stroke="#E6E0D4" stroke-width="5"/>'
                 f'<circle cx="540" cy="860" r="5" fill="#CFC8BB"/><circle cx="540" cy="920" r="5" fill="#CFC8BB"/><circle cx="540" cy="980" r="5" fill="#CFC8BB"/>')
    if garment=="cardigan":
        o.append(f'<path d="M455 775 L540 1080 L625 775 Z" fill="#FFFFFF"/>')
        o.append(f'<path d="M455 775 L485 760 L540 920 L595 760 L625 775 L600 1080 L480 1080 Z" fill="{d}"/>')
    return "\n".join(o)

def head(skin,tilt,hair,hc,face_svg,extras):
    d=shade(skin,.86); hl=shade(hc,1.25); o=[f'<g transform="rotate({tilt} 540 500)">']
    # hair behind
    if hair=="bob": o.append(f'<path d="M372 450 C372 300 450 232 540 232 C630 232 708 300 708 450 L712 660 C712 700 660 712 630 696 L610 560 L470 560 L450 696 C420 712 368 700 368 660 Z" fill="{hc}"/>')
    if hair in ("wavy","longup"): o.append(f'<path d="M360 450 C360 280 450 220 540 220 C630 220 720 280 720 450 C730 580 750 660 720 760 C690 780 660 760 650 710 C640 775 600 785 585 735 L600 560 L480 560 L495 735 C480 785 440 775 430 710 C420 760 390 780 360 760 C330 660 350 580 360 450 Z" fill="{hc}"/>')
    if hair=="bun": o.append(f'<circle cx="705" cy="330" r="82" fill="{hc}"/><path d="M660 300 Q700 270 745 300" fill="none" stroke="{hl}" stroke-width="10" stroke-linecap="round" opacity=".6"/>')
    # neck shadow + head
    o.append(f'<path d="M388 470 C388 320 452 240 540 240 C628 240 692 320 692 470 C692 590 630 690 540 690 C450 690 388 590 388 470 Z" fill="{skin}"/>')
    o.append(f'<path d="M640 300 C690 360 700 520 650 620 C620 670 580 690 540 690 C630 690 692 590 692 470 C692 400 672 340 640 300 Z" fill="{d}" opacity=".35"/>')
    o.append(f'<circle cx="392" cy="490" r="26" fill="{skin}"/><circle cx="688" cy="490" r="26" fill="{d}"/>')
    # beard / stubble
    if "beard" in extras: o.append(f'<path d="M396 520 C402 620 460 700 540 700 C620 700 678 620 684 520 C664 585 620 628 540 628 C460 628 416 585 396 520 Z" fill="{hc}"/>')
    if "stubble" in extras: o.append(f'<path d="M402 520 C408 612 460 686 540 686 C620 686 672 612 678 520 C660 580 620 622 540 622 C460 622 420 580 402 520 Z" fill="{hc}" opacity=".22"/>')
    # hair front
    front={"short":"M386 465 C380 330 450 230 540 230 C640 230 700 320 694 465 C680 420 650 378 606 368 C566 360 526 380 494 390 C452 402 416 430 386 465 Z",
           "curly":"M386 465 C366 430 374 395 398 382 C382 350 400 318 432 316 C428 284 456 262 486 272 C498 244 534 238 554 258 C580 240 616 250 622 280 C656 276 678 300 670 330 C700 340 706 372 688 396 C708 416 702 446 694 465 C680 420 650 378 606 368 C566 360 526 380 494 390 C452 402 416 430 386 465 Z",
           "bun":"M386 465 C380 330 450 230 540 230 C640 230 700 320 694 465 C656 405 612 355 562 350 C520 350 490 392 470 428 C448 450 416 462 386 465 Z",
           "bob":"M386 465 C380 330 450 230 540 230 C640 230 700 320 694 465 C668 430 636 402 604 400 C572 398 548 414 522 430 C490 450 438 470 386 465 Z",
           "wavy":"M386 465 C380 330 450 230 540 230 C640 230 700 320 694 465 C670 432 660 388 628 372 C596 358 566 380 544 390 C512 402 482 380 456 404 C434 426 414 452 386 465 Z",
           "longup":"M386 465 C380 330 450 230 540 230 C640 230 700 320 694 465 C670 420 638 388 606 380 C566 370 526 390 494 400 C452 412 416 436 386 465 Z"}
    key={"shortgrey":"short","white":"short","neat":"short"}.get(hair,hair)
    o.append(f'<path d="{front[key]}" fill="{hc}"/>')
    o.append(f'<path d="M470 300 Q520 262 590 272" fill="none" stroke="{hl}" stroke-width="12" stroke-linecap="round" opacity=".55"/>')
    if hair=="shortgrey": o.append(f'<path d="M386 465 C384 420 398 398 430 392 C420 420 410 442 386 465 Z" fill="#D8D0C4"/><path d="M694 465 C696 420 682 398 650 392 C660 420 670 442 694 465 Z" fill="#D8D0C4"/>')
    if hair=="longup": o.append(f'<g fill="none" stroke="{INK}" stroke-width="7" opacity=".85"><rect x="452" y="312" width="74" height="42" rx="14"/><rect x="554" y="312" width="74" height="42" rx="14"/><path d="M526 330 L554 330 M452 330 L418 346 M628 330 L662 346"/></g>')
    o.append(face_svg)
    for e in extras:
        if e=="glasses_orange": o.append(f'<g fill="none" stroke="{OR}" stroke-width="7"><circle cx="490" cy="492" r="38"/><circle cx="600" cy="492" r="38"/><path d="M528 492 L562 492"/></g>')
        if e=="glasses_round": o.append(f'<g fill="none" stroke="{INK}" stroke-width="7"><circle cx="490" cy="492" r="40"/><circle cx="600" cy="492" r="40"/><path d="M530 492 L560 492 M450 492 L410 486"/></g>')
        if e=="earring": o.append(f'<circle cx="394" cy="528" r="10" fill="{OR}"/>')
        if e in ("marker_ear","pencil_ear"): o.append(f'<rect x="366" y="430" width="16" height="118" rx="7" fill="{OR}" transform="rotate(-12 374 489)"/>')
        if e=="earbud": o.append(f'<circle cx="392" cy="512" r="13" fill="{OR}"/>')
    o.append('</g>'); return "\n".join(o)

def face(eyes="open",brows="level",mouth="half",hc="#2B1B14",skin="#C68B5E"):
    B=f'fill="none" stroke="{hc}" stroke-width="9" stroke-linecap="round"'
    M=f'fill="none" stroke="{shade(skin,.6)}" stroke-width="7" stroke-linecap="round"'
    o=[f'<ellipse cx="455" cy="560" rx="30" ry="16" fill="#E8907A" opacity=".38"/><ellipse cx="625" cy="560" rx="30" ry="16" fill="#E8907A" opacity=".38"/>']
    bro={"level":("M462 448 Q490 436 518 446","M572 446 Q600 436 628 448"),"raised":("M462 436 Q490 420 518 432","M572 432 Q600 420 628 436"),
         "oneup":("M462 448 Q490 436 518 446","M572 430 Q600 416 628 430"),"flat":("M462 448 L518 446","M572 446 L628 448"),"frown":("M462 446 Q490 448 518 456","M572 456 Q600 448 628 446")}[brows]
    o+=[f'<path d="{bro[0]}" {B}/>',f'<path d="{bro[1]}" {B}/>']
    def eye(cx): return f'<ellipse cx="{cx}" cy="494" rx="12" ry="16" fill="{INK}"/><circle cx="{cx+4}" cy="487" r="4.5" fill="#FFFFFF"/>'
    L=f'fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"'
    if eyes=="open": o+=[eye(490),eye(600)]
    elif eyes=="happy": o+=[f'<path d="M474 498 Q490 480 506 498" {L}/>',f'<path d="M584 498 Q600 480 616 498" {L}/>']
    elif eyes=="narrow": o+=[f'<ellipse cx="490" cy="496" rx="12" ry="9" fill="{INK}"/><path d="M474 486 Q490 480 506 486" {L}/>',f'<ellipse cx="600" cy="496" rx="12" ry="9" fill="{INK}"/><path d="M584 486 Q600 480 616 486" {L}/>']
    elif eyes=="down": o+=[f'<path d="M474 494 Q490 508 506 494" {L}/>',f'<path d="M584 494 Q600 508 616 494" {L}/>']
    elif eyes=="wink": o+=[eye(490),f'<path d="M584 494 Q600 506 616 494" {L}/>']
    o.append(f'<path d="M534 548 Q546 558 560 548" {M}/>')
    m={"half":f'<path d="M510 598 Q546 624 582 596" {M}/>',
       "wide":f'<path d="M498 592 Q546 648 594 592 Z" fill="#FFFFFF"/><path d="M498 592 Q546 648 594 592" {M}/>',
       "line":f'<path d="M516 602 Q546 610 576 600" {M}/>',
       "open":f'<path d="M518 592 Q546 642 574 592 Z" fill="#7A3B3B"/>',
       "smirk":f'<path d="M512 602 Q552 626 588 594" {M}/>',
       "pressed":f'<path d="M516 604 Q546 612 576 602" {M}/>'}[mouth]
    o.append(m); return "\n".join(o)

def prop(kind,skin):
    if kind=="notebook_two_fingers":
        return (f'<g transform="rotate(-6 495 900)"><rect x="415" y="790" width="160" height="210" rx="14" fill="{OR}"/><rect x="415" y="790" width="22" height="210" rx="8" fill="{shade(OR,.8)}"/><path d="M460 830 L545 830 M460 862 L530 862" stroke="#FFD9C8" stroke-width="7" stroke-linecap="round"/></g>'
                + hand(480,985,skin,-6) +
                f'<g><rect x="690" y="880" width="110" height="200" rx="40" fill="{skin}"/><rect x="700" y="740" width="34" height="170" rx="17" fill="{skin}"/><rect x="742" y="730" width="34" height="180" rx="17" fill="{skin}"/><circle cx="690" cy="930" r="28" fill="{skin}"/></g>')
    if kind=="card":
        return (f'<g transform="rotate(10 330 640)"><rect x="245" y="555" width="170" height="118" rx="14" fill="#FFFFFF"/><path d="M272 598 L388 598 M272 628 L352 628" stroke="#D9D2C7" stroke-width="7" stroke-linecap="round"/><rect x="272" y="645" width="44" height="9" rx="4" fill="{OR}"/></g>'
                f'<rect x="300" y="700" width="150" height="400" rx="60" fill="{skin}"/><rect x="372" y="640" width="36" height="120" rx="18" fill="{skin}"/>'
                f'<g transform="rotate(-20 640 900)"><rect x="590" y="820" width="130" height="90" rx="10" fill="#FFFFFF"/><rect x="612" y="808" width="130" height="90" rx="10" fill="#F7F3EC"/><rect x="634" y="796" width="130" height="90" rx="10" fill="#FFFFFF"/></g>' + hand(690,965,skin,-10))
    if kind=="sketchbook":
        return (f'<g transform="rotate(-6 540 930)"><rect x="395" y="825" width="290" height="210" rx="12" fill="#FFFFFF"/><path d="M540 825 L540 1035" stroke="#E4DDD2" stroke-width="6"/><path d="M440 900 Q480 858 520 900 M580 882 L644 882 M580 922 L652 922 M450 962 L512 962" fill="none" stroke="#B9B0A2" stroke-width="7" stroke-linecap="round"/><circle cx="620" cy="980" r="14" fill="{OR}"/></g>'
                + hand(420,1005,skin,0) + hand(680,1005,skin,0))
    if kind=="tablet":
        return (f'<g transform="rotate(-8 330 900)"><rect x="210" y="755" width="240" height="310" rx="22" fill="{INK}"/><rect x="224" y="769" width="212" height="282" rx="14" fill="{PAPER}"/><rect x="246" y="796" width="96" height="12" rx="6" fill="#B9B0A2"/><rect x="246" y="826" width="168" height="116" rx="12" fill="#E3D8C4"/><rect x="246" y="962" width="76" height="28" rx="14" fill="{OR}"/></g>'
                + hand(445,985,skin,-8))
    if kind=="headphones_notebook":
        return (f'<path d="M425 780 C425 700 655 700 655 780" fill="none" stroke="{INK}" stroke-width="20" stroke-linecap="round"/><rect x="398" y="760" width="52" height="78" rx="20" fill="{INK}"/><rect x="630" y="760" width="52" height="78" rx="20" fill="{INK}"/>'
                f'<path d="M656 830 C700 880 708 950 690 1010" fill="none" stroke="{OR}" stroke-width="8" stroke-linecap="round"/>'
                f'<g transform="rotate(8 320 930)"><rect x="215" y="825" width="210" height="220" rx="12" fill="#FFFFFF"/><path d="M248 866 L392 866 M248 902 L372 902 M248 938 L396 938 M248 974 L340 974" stroke="#D9D2C7" stroke-width="7" stroke-linecap="round"/><path d="M248 902 L372 902" stroke="{OR}" stroke-width="6" stroke-linecap="round"/></g>'
                + hand(305,1010,skin,8) + f'<g transform="rotate(-30 700 940)"><rect x="690" y="800" width="20" height="200" rx="8" fill="{INK}"/><path d="M690 800 L700 772 L710 800 Z" fill="{OR}"/></g>' + hand(705,985,skin,-10))
    if kind=="folder_finger":
        return (f'<g transform="rotate(-4 540 940)"><rect x="375" y="835" width="330" height="240" rx="12" fill="#F7F3EC"/><path d="M420 890 L660 890 M420 932 L640 932 M420 974 L660 974 M420 1016 L600 1016" stroke="#D9D2C7" stroke-width="7" stroke-linecap="round"/><rect x="560" y="815" width="84" height="36" rx="10" fill="{OR}"/></g>'
                + hand(400,1035,skin,0) + f'<rect x="560" y="975" width="130" height="110" rx="45" fill="{skin}"/><rect x="640" y="925" width="38" height="110" rx="19" fill="{skin}"/>')
    if kind=="laptop":
        return (f'<g transform="translate(0 -70) rotate(-10 480 930)"><path d="M300 980 L620 980 L600 860 L320 860 Z" fill="#4A4652"/><path d="M322 862 L598 862 L610 940 L310 940 Z" fill="{PAPER}"/><path d="M350 886 L432 886 M350 906 L482 906 M350 926 L412 926" stroke="{OR}" stroke-width="7" stroke-linecap="round"/><rect x="420" y="990" width="90" height="10" rx="5" fill="#6B6675"/></g>'
                + hand(345,945,skin,0))
    if kind=="phone_watch":
        return (f'<g transform="rotate(-6 640 880)"><rect x="582" y="775" width="116" height="190" rx="18" fill="{INK}"/><rect x="594" y="787" width="92" height="166" rx="12" fill="{PAPER}"/><rect x="610" y="905" width="14" height="38" fill="{OR}"/><rect x="630" y="885" width="14" height="58" fill="#C9C0B2"/><rect x="650" y="855" width="14" height="88" fill="#C9C0B2"/><path d="M610 876 L666 838" stroke="{OR}" stroke-width="6" stroke-linecap="round"/></g>'
                + hand(692,905,skin,-6) + f'<rect x="290" y="960" width="200" height="130" rx="60" fill="{skin}"/>'
                f'<rect x="296" y="900" width="82" height="46" rx="12" fill="{INK}"/><rect x="282" y="908" width="14" height="30" rx="4" fill="{OR}"/><rect x="378" y="908" width="14" height="30" rx="4" fill="{OR}"/><circle cx="337" cy="923" r="11" fill="none" stroke="{PAPER}" stroke-width="4"/>')
    if kind=="clipboard":
        return (f'<g transform="rotate(6 560 940)"><rect x="415" y="815" width="270" height="270" rx="16" fill="{INK}"/><rect x="429" y="829" width="242" height="256" rx="10" fill="{PAPER}"/><path d="M452 890 L462 900 L480 876 M452 940 L462 950 L480 926" fill="none" stroke="#3B9B6E" stroke-width="8" stroke-linecap="round"/><path d="M452 982 L474 1002 M474 982 L452 1002" stroke="{OR}" stroke-width="8" stroke-linecap="round"/><path d="M520 890 L640 890 M520 940 L620 940 M520 990 L640 990 M520 1040 L600 1040" stroke="#D9D2C7" stroke-width="7" stroke-linecap="round"/></g>'
                + hand(435,1045,skin,6) + f'<g transform="rotate(-35 720 900)"><rect x="710" y="775" width="18" height="210" rx="8" fill="{OR}"/></g>' + hand(722,1005,skin,-20))
    if kind=="two_phones":
        return (f'<g transform="rotate(-12 330 920)"><rect x="265" y="795" width="126" height="230" rx="20" fill="{INK}"/><rect x="277" y="807" width="102" height="206" rx="12" fill="{PAPER}"/><rect x="296" y="836" width="64" height="54" rx="8" fill="#E3D8C4"/><rect x="296" y="905" width="64" height="9" rx="4" fill="#C9C0B2"/></g>'
                f'<g transform="rotate(8 400 920)"><rect x="345" y="785" width="126" height="230" rx="20" fill="{INK}"/><rect x="357" y="797" width="102" height="206" rx="12" fill="{PAPER}"/><rect x="376" y="826" width="64" height="54" rx="8" fill="{OR}"/><rect x="376" y="895" width="64" height="9" rx="4" fill="#C9C0B2"/></g>'
                + hand(385,1015,skin,0) + f'<rect x="640" y="945" width="76" height="52" rx="14" fill="{PAPER}"/><circle cx="678" cy="971" r="13" fill="none" stroke="{INK}" stroke-width="5"/><path d="M678 962 L678 971 L685 976" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><rect x="628" y="953" width="12" height="36" rx="3" fill="#4A4652"/><rect x="716" y="953" width="12" height="36" rx="3" fill="#4A4652"/>'
                + hand(692,1045,skin,0))
    if kind=="chart_board":
        return (f'<g transform="rotate(-5 560 930)"><rect x="405" y="815" width="310" height="230" rx="14" fill="#FFFFFF"/><rect x="450" y="960" width="40" height="52" rx="4" fill="#C9C0B2"/><rect x="510" y="920" width="40" height="92" rx="4" fill="#C9C0B2"/><rect x="570" y="940" width="40" height="72" rx="4" fill="#C9C0B2"/><rect x="630" y="878" width="40" height="134" rx="4" fill="{OR}"/><path d="M440 1014 L690 1014" stroke="#D9D2C7" stroke-width="6"/><path d="M452 900 L682 858" stroke="{INK}" stroke-width="5" stroke-dasharray="10 10" stroke-linecap="round"/></g>'
                + hand(435,1035,skin,0) + hand(700,1035,skin,0))
    if kind=="greeting":
        return (f'<g><rect x="330" y="880" width="190" height="220" rx="70" fill="{skin}"/><rect x="352" y="770" width="36" height="150" rx="18" fill="{skin}"/><rect x="396" y="745" width="36" height="170" rx="18" fill="{skin}"/><rect x="440" y="752" width="36" height="165" rx="18" fill="{skin}"/><rect x="484" y="790" width="34" height="130" rx="17" fill="{skin}"/><ellipse cx="335" cy="930" rx="30" ry="40" fill="{skin}" transform="rotate(30 335 930)"/></g>'
                f'<g transform="rotate(-10 680 930)"><rect x="615" y="815" width="126" height="230" rx="20" fill="{INK}"/><rect x="627" y="827" width="102" height="206" rx="12" fill="{PAPER}"/><rect x="644" y="856" width="68" height="20" rx="10" fill="#E3D8C4"/><rect x="644" y="888" width="52" height="20" rx="10" fill="#E3D8C4"/><rect x="660" y="980" width="52" height="20" rx="10" fill="{OR}"/></g>'
                + hand(695,1035,skin,-10))
    if kind=="binder_pen":
        return (f'<g transform="rotate(4 330 940)"><rect x="195" y="795" width="240" height="290" rx="12" fill="{OR}"/><rect x="195" y="795" width="40" height="290" rx="10" fill="{shade(OR,.8)}"/><rect x="258" y="836" width="136" height="64" rx="8" fill="{PAPER}"/><path d="M280 858 L372 858 M280 880 L350 880" stroke="#C9C0B2" stroke-width="6" stroke-linecap="round"/></g>'
                + hand(335,1025,skin,4) + f'<g transform="rotate(-40 700 900)"><rect x="690" y="755" width="22" height="230" rx="9" fill="{INK}"/><path d="M690 755 L701 722 L712 755 Z" fill="#C9C0B2"/><rect x="690" y="798" width="22" height="12" fill="{OR}"/></g>' + hand(708,995,skin,-15))
    return ""

def scarf(): return (f'<path d="M425 745 C470 825 610 825 655 745 C688 780 680 822 645 842 C592 874 488 874 435 842 C400 822 392 780 425 745 Z" fill="{OR}"/>'
                     f'<path d="M588 838 C624 894 654 954 644 1026 C618 1036 592 1032 576 1020 C582 954 562 892 550 850 Z" fill="{shade(OR,.9)}"/>')
def shemagh(): return (f'<path d="M560 762 C645 778 725 840 765 920 L805 1080 L700 1080 L662 920 C632 868 602 816 560 762 Z" fill="#FFFFFF"/>'
                       f'<path d="M586 788 C650 820 702 880 732 960" fill="none" stroke="{OR}" stroke-width="5" stroke-linecap="round"/><path d="M600 775 C680 800 745 870 785 980" fill="none" stroke="#E6E0D4" stroke-width="4"/>')
def bracelet(): return f'<rect x="298" y="955" width="86" height="24" rx="10" fill="{OR}" transform="rotate(-8 340 967)"/>'

#  slug, skin, hair, hair_col, tilt, garment, garment_col, disc, (eyes,brows,mouth), prop, extras, overlays
CH=[
 ("mukhattit","#B9794F","shortgrey","#3A2A22",-3,"shirt","#E9DCC3","#E6D5B4",("open","raised","half"),"notebook_two_fingers",["stubble"],[]),
 ("wassam","#D9A77C","neat","#2B1B14",4,"crew","#7A8794","#D3DBCB",("narrow","oneup","smirk"),"card",["glasses_orange"],[]),
 ("naqqash","#C68B5E","short","#2B1B14",0,"apron","#F3EEE6","#DAD5CC",("open","flat","line"),"sketchbook",["stubble","marker_ear"],[]),
 ("lawwan","#C68B5E","bun","#2B1B14",6,"shirt","#FFFFFF","#F0D3C5",("open","level","half"),"tablet",["earring"],["scarf"]),
 ("rawi","#B07A55","curly","#1F1410",-5,"crew","#5F6F5E","#CBDDDA",("open","raised","open"),"headphones_notebook",[],[]),
 ("muharrir","#E0B48C","longup","#4A2E1E",0,"cardigan","#8A9460","#DCD5E6",("open","level","pressed"),"folder_finger",[],[]),
 ("bannaa","#C98F63","short","#2B1B14",5,"hoodie","#34303F","#CFD9E6",("open","raised","smirk"),"laptop",[],["bracelet"]),
 ("maher","#A86B45","short","#1F1410",0,"polo","#24314F","#E6D5B4",("open","level","half"),"phone_watch",["beard"],[]),
 ("mudaqqiq","#D4A079","bob","#2B1B14",-4,"shirt","#F7F3EC","#D3DBCB",("down","oneup","pressed"),"clipboard",[],[]),
 ("nashir","#C68B5E","neat","#2B1B14",3,"button","#95A9BE","#F0D3C5",("open","level","wide"),"two_phones",["earbud"],[]),
 ("mulin","#D9A77C","wavy","#3A2218",-2,"blazer","#4F7C7A","#CBDDDA",("open","oneup","half"),"chart_board",["pencil_ear"],[]),
 ("safeer","#B9794F","short","#2B1B14",2,"thobe","#FFFFFF","#DCD5E6",("happy","raised","wide"),"greeting",["stubble"],["shemagh"]),
 ("mudawwin","#E3BFA0","white","#ECE6DC",0,"crew","#3E3A47","#DAD5CC",("open","level","smirk"),"binder_pen",["glasses_round"],[]),
]
os.makedirs("svg",exist_ok=True); os.makedirs("png",exist_ok=True)
for slug,skin,hair,hc,tilt,garm,gc,disc,fc,pr,extras,ov in CH:
    p=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080">',
       f'<defs><clipPath id="c"><circle cx="540" cy="540" r="490"/></clipPath></defs>',
       f'<rect width="1080" height="1080" fill="{PAPER}"/><circle cx="540" cy="540" r="490" fill="{disc}"/>',
       f'<g clip-path="url(#c)"><g transform="translate(540 600) scale(1.12) translate(-540 -600)">']
    p.append(body(garm,gc,skin))
    if "shemagh" in ov: p.append(shemagh())
    p.append(f'<path d="M488 640 L488 775 Q540 815 592 775 L592 640 Z" fill="{skin}"/><path d="M488 640 L592 640 L592 690 Q540 720 488 690 Z" fill="{shade(skin,.86)}" opacity=".5"/>')
    if "scarf" in ov: p.append(scarf())
    p.append(prop(pr,skin))
    if "bracelet" in ov: p.append(bracelet())
    p.append(head(skin,tilt,hair,hc,face(*fc,hc=("#4A3A32" if hair=="white" else hc),skin=skin),extras))
    p.append('</g></g></svg>')
    open(f"svg/{slug}.svg","w",encoding="utf-8").write("\n".join(p))
tiles="".join(f'<figure><img src="svg/{c[0]}.svg"><figcaption>{c[0]}</figcaption></figure>' for c in CH)
open("sheet.html","w",encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:{PAPER};font-family:Inter,Arial;padding:40px}}.g{{display:grid;grid-template-columns:repeat(7,1fr);gap:28px}}figure{{margin:0;text-align:center}}img{{width:100%;display:block;border-radius:50%}}figcaption{{font-size:22px;color:{INK};margin-top:10px}}</style></head><body><div class="g">{tiles}</div></body></html>')
subprocess.run([CHROME,"--headless=new","--hide-scrollbars","--force-device-scale-factor=1","--window-size=2400,920","--screenshot=sheet.png",f"file://{os.getcwd()}/sheet.html"],stderr=subprocess.DEVNULL)
for c in CH:
    open("one.html","w",encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:{PAPER}}}img{{display:block;width:512px;height:512px}}</style></head><body><img src="svg/{c[0]}.svg"></body></html>')
    subprocess.run([CHROME,"--headless=new","--hide-scrollbars","--force-device-scale-factor=1","--window-size=512,512",f"--screenshot=png/{c[0]}-512.png",f"file://{os.getcwd()}/one.html"],stderr=subprocess.DEVNULL)
os.remove("one.html"); print("ok")
