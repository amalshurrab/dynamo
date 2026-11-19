# Dynamo character system: flat vector, code-drawn. One shared style, 13 distinct people.
import os, subprocess
INK="#2B2633"; OR="#FF5A1A"; PAPER="#F6F1E8"; DISC="#EBE2D3"; SW=5.5
S=f'stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'

def body(garment, col, skin):
    out=[]
    out.append(f'<path d="M190 1080 C200 820 330 740 540 740 C750 740 880 820 890 1080 Z" fill="{col}" {S}/>')
    if garment=="shirt":   # v collar
        out.append(f'<path d="M470 745 L540 860 L610 745" fill="#F0E6D8" {S}/>')
        out.append(f'<path d="M470 745 L500 790 L540 760 L580 790 L610 745" fill="{col}" {S}/>')
    elif garment=="crew":
        out.append(f'<path d="M478 748 Q540 800 602 748" fill="#F0E6D8" {S}/>')
    elif garment=="apron":
        out.append(f'<path d="M470 745 L540 860 L610 745" fill="#F0E6D8" {S}/>')
        out.append(f'<path d="M430 870 L650 870 L670 1080 L410 1080 Z" fill="#3B3A3F" {S}/>')
        out.append(f'<path d="M455 870 L470 790 M625 870 L610 790" fill="none" {S}/>')
        out.append(f'<ellipse cx="610" cy="990" rx="14" ry="22" fill="#5B4FC9" transform="rotate(20 610 990)"/>')
    elif garment=="hoodie":
        out.append(f'<path d="M420 760 C440 700 640 700 660 760 C650 800 600 830 540 830 C480 830 430 800 420 760 Z" fill="{col}" {S}/>')
        out.append(f'<path d="M505 830 L495 1000 M575 830 L585 1000" fill="none" {S}/>')
        out.append(f'<ellipse cx="495" cy="1010" rx="9" ry="14" fill="{INK}"/><ellipse cx="585" cy="1010" rx="9" ry="14" fill="{INK}"/>')
    elif garment=="polo":
        out.append(f'<path d="M478 745 L540 820 L602 745" fill="#F0E6D8" {S}/>')
        out.append(f'<path d="M478 745 L455 790 L520 785 L540 820 L560 785 L625 790 L602 745" fill="{col}" {S}/>')
    elif garment=="blazer":
        out.append(f'<path d="M430 760 L540 1080 L650 760 Z" fill="#F3EEE6" {S}/>')
        out.append(f'<path d="M430 760 L470 745 L540 930 L610 745 L650 760 L560 1080 L520 1080 Z" fill="{col}" {S}/>')
    elif garment=="thobe":
        out.append(f'<path d="M500 745 Q540 790 580 745" fill="#F0E6D8" {S}/>')
        out.append(f'<path d="M540 790 L540 1080" fill="none" {S}/>')
        out.append(f'<circle cx="540" cy="840" r="6" fill="{INK}"/><circle cx="540" cy="900" r="6" fill="{INK}"/><circle cx="540" cy="960" r="6" fill="{INK}"/>')
    elif garment=="cardigan":
        out.append(f'<path d="M455 760 L540 1080 L625 760 Z" fill="#FFFFFF" {S}/>')
        out.append(f'<path d="M455 760 L480 745 L540 900 L600 745 L625 760 L600 1080 L480 1080 Z" fill="{col}" {S}/>')
        out.append(f'<circle cx="500" cy="930" r="6" fill="{INK}"/><circle cx="505" cy="990" r="6" fill="{INK}"/>')
    elif garment=="button":
        out.append(f'<path d="M478 745 L540 820 L602 745" fill="#F0E6D8" {S}/>')
        out.append(f'<path d="M478 745 L455 790 L520 785 L540 820 L560 785 L625 790 L602 745" fill="{col}" {S}/>')
        out.append(f'<path d="M540 820 L540 1080" fill="none" {S}/>')
        out.append(f'<circle cx="540" cy="880" r="6" fill="{INK}"/><circle cx="540" cy="950" r="6" fill="{INK}"/>')
    return "\n".join(out)

def neck(skin): return f'<path d="M490 640 L490 760 Q540 800 590 760 L590 640 Z" fill="{skin}" {S}/>'

def head(skin, tilt, hair, hair_col, face, extras):
    out=[f'<g transform="rotate({tilt} 540 480)">']
    # hair behind head
    if hair in ("bob",):
        out.append(f'<path d="M380 430 C380 300 450 240 540 240 C630 240 700 300 700 430 L705 650 C690 690 650 700 620 690 L600 540 L480 540 L460 690 C430 700 390 690 375 650 Z" fill="{hair_col}" {S}/>')
    if hair in ("wavy","longup"):
        out.append(f'<path d="M370 440 C370 290 450 230 540 230 C630 230 710 290 710 440 C720 560 740 640 715 740 C690 760 660 740 650 700 C640 760 600 770 590 720 L600 540 L480 540 L490 720 C480 770 440 760 430 700 C420 740 390 760 365 740 C340 640 360 560 370 440 Z" fill="{hair_col}" {S}/>')
    if hair=="bun": out.append(f'<circle cx="700" cy="330" r="78" fill="{hair_col}" {S}/>')
    out.append(f'<path d="M396 460 C396 330 455 252 540 252 C625 252 684 330 684 460 C684 575 626 672 540 672 C454 672 396 575 396 460 Z" fill="{skin}" {S}/>')
    out.append(f'<ellipse cx="398" cy="478" rx="18" ry="26" fill="{skin}" {S}/>')
    # beard / stubble (under hair)
    if "beard" in extras:
        out.append(f'<path d="M402 500 C408 598 458 684 540 684 C622 684 672 598 678 500 C660 565 620 612 540 612 C460 612 420 565 402 500 Z" fill="{hair_col}" {S}/>')
    if "stubble" in extras:
        out.append(f'<path d="M408 500 C415 600 460 680 540 680 C620 680 665 600 672 500 C660 560 620 610 540 610 C460 610 420 560 408 500 Z" fill="{hair_col}" opacity=".28"/>')
    # hair front
    if hair in ("short","shortgrey","white","neat"):
        out.append(f'<path d="M398 450 C392 330 450 240 540 240 C640 240 690 320 684 450 C670 410 640 370 600 360 C560 352 520 372 490 380 C450 392 420 420 398 450 Z" fill="{hair_col}" {S}/>')
        if hair=="shortgrey":
            out.append(f'<path d="M398 450 C396 410 410 390 440 385 C430 410 420 430 398 450 Z" fill="#CFC6B8"/><path d="M684 450 C686 410 672 390 645 385 C655 410 665 430 684 450 Z" fill="#CFC6B8"/>')
        if hair=="neat":
            out.append(f'<path d="M470 383 C520 330 600 335 660 380" fill="none" {S}/>')
    elif hair=="curly":
        out.append(f'<path d="M398 450 C380 420 385 390 405 375 C390 345 405 315 435 310 C430 280 455 258 485 265 C495 238 530 232 550 250 C575 232 610 240 618 268 C650 262 672 285 665 315 C695 322 705 352 688 378 C705 395 702 425 684 450 C670 410 640 370 600 360 C560 352 520 372 490 380 C450 392 420 420 398 450 Z" fill="{hair_col}" {S}/>')
    elif hair=="bun":
        out.append(f'<path d="M398 450 C392 330 450 240 540 240 C640 240 690 320 684 450 C650 400 610 350 560 345 C520 345 490 385 470 420 C450 440 420 450 398 450 Z" fill="{hair_col}" {S}/>')
    elif hair=="bob":
        out.append(f'<path d="M398 450 C392 330 450 240 540 240 C640 240 690 320 684 450 C660 420 630 395 600 392 C570 390 545 405 520 420 C490 440 440 455 398 450 Z" fill="{hair_col}" {S}/>')
    elif hair=="wavy":
        out.append(f'<path d="M398 450 C392 330 450 240 540 240 C640 240 690 320 684 450 C660 420 650 380 620 365 C590 352 560 372 540 380 C510 392 480 372 455 395 C435 415 420 440 398 450 Z" fill="{hair_col}" {S}/>')
    elif hair=="longup":
        out.append(f'<path d="M398 450 C392 330 450 240 540 240 C640 240 690 320 684 450 C660 410 630 380 600 372 C560 362 520 382 490 392 C450 404 420 425 398 450 Z" fill="{hair_col}" {S}/>')
        # glasses pushed up into the hair
        out.append(f'<g fill="none" {S}><rect x="455" y="318" width="70" height="40" rx="12"/><rect x="555" y="318" width="70" height="40" rx="12"/><path d="M525 335 L555 335 M455 335 L420 350 M625 335 L660 350"/></g>')
    out.append(face)
    for e in extras:
        if e=="glasses_orange":
            out.append(f'<g fill="none" stroke="{OR}" stroke-width="6"><circle cx="492" cy="485" r="34"/><circle cx="600" cy="485" r="34"/><path d="M526 485 L566 485"/></g>')
        if e=="glasses_round":
            out.append(f'<g fill="none" {S}><circle cx="492" cy="485" r="36"/><circle cx="600" cy="485" r="36"/><path d="M528 485 L564 485 M456 485 L420 478"/></g>')
        if e=="earring": out.append(f'<circle cx="402" cy="512" r="9" fill="{OR}" stroke="{INK}" stroke-width="5"/>')
        if e=="marker_ear": out.append(f'<rect x="372" y="430" width="16" height="110" rx="6" fill="{OR}" {S} transform="rotate(-12 380 485)"/>')
        if e=="pencil_ear": out.append(f'<rect x="372" y="430" width="14" height="110" rx="4" fill="{OR}" {S} transform="rotate(-12 380 485)"/>')
        if e=="earbud": out.append(f'<circle cx="398" cy="500" r="13" fill="{OR}" {S}/>')
    out.append('</g>'); return "\n".join(out)

def face(eyes="open", brows="level", mouth="half"):
    B=f'stroke="{INK}" stroke-linecap="round" fill="none"'
    o=[]
    # blush
    o.append(f'<ellipse cx="462" cy="548" rx="26" ry="14" fill="#E8907A" opacity=".35"/><ellipse cx="626" cy="548" rx="26" ry="14" fill="#E8907A" opacity=".35"/>')
    # brows (short, soft)
    bro={"level":("M470 446 Q492 436 514 444","M574 444 Q596 436 618 446"),
         "raised":("M470 436 Q492 422 514 432","M574 432 Q596 422 618 436"),
         "oneup":("M470 446 Q492 436 514 444","M574 430 Q596 418 618 430"),
         "flat":("M470 446 L514 444","M574 444 L618 446"),
         "frown":("M470 444 Q492 446 514 452","M574 452 Q596 446 618 444")}[brows]
    o+= [f'<path d="{bro[0]}" {B} stroke-width="5"/>', f'<path d="{bro[1]}" {B} stroke-width="5"/>']
    # eyes
    def eye(cx):
        return (f'<ellipse cx="{cx}" cy="488" rx="11" ry="14" fill="{INK}"/>'
                f'<circle cx="{cx+4}" cy="482" r="4" fill="#FFFFFF"/>')
    if eyes=="open": o+= [eye(492), eye(596)]
    elif eyes=="happy": o+= [f'<path d="M478 492 Q492 476 506 492" {B} stroke-width="6"/>', f'<path d="M582 492 Q596 476 610 492" {B} stroke-width="6"/>']
    elif eyes=="narrow": o+= [f'<path d="M478 486 Q492 478 506 486" {B} stroke-width="6"/><ellipse cx="492" cy="490" rx="10" ry="7" fill="{INK}"/>', f'<path d="M582 486 Q596 478 610 486" {B} stroke-width="6"/><ellipse cx="596" cy="490" rx="10" ry="7" fill="{INK}"/>']
    elif eyes=="down": o+= [f'<path d="M478 488 Q492 500 506 488" {B} stroke-width="6"/>', f'<path d="M582 488 Q596 500 610 488" {B} stroke-width="6"/>']
    elif eyes=="wink": o+= [eye(492), f'<path d="M582 488 Q596 498 610 488" {B} stroke-width="6"/>']
    # tiny nose
    o.append(f'<path d="M536 540 Q546 550 558 540" {B} stroke-width="5"/>')
    # mouth
    m={"half":f'<path d="M512 588 Q546 612 580 586" {B} stroke-width="6"/>',
       "wide":f'<path d="M500 584 Q546 636 592 584 Z" fill="#FFFFFF" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>',
       "line":f'<path d="M516 592 Q546 600 576 590" {B} stroke-width="6"/>',
       "open":f'<path d="M520 584 Q546 630 572 584 Z" fill="#6B3A3A" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>',
       "smirk":f'<path d="M514 592 Q552 614 586 584" {B} stroke-width="6"/>',
       "pressed":f'<path d="M516 594 Q546 600 576 592" {B} stroke-width="6"/>'}[mouth]
    o.append(m)
    return "\n".join(o)

def hand(x,y,skin,rot=0):  # simple closed hand
    return f'<path transform="rotate({rot} {x} {y})" d="M{x-50} {y+40} L{x-50} {y-30} C{x-50} {y-60} {x-20} {y-72} {x+10} {y-62} L{x+80} {y-40} C{x+105} {y-32} {x+106} {y-2} {x+82} {y+8} L{x+75} {y+10} C{x+100} {y+20} {x+100} {y+52} {x+72} {y+58} C{x+90} {y+70} {x+84} {y+90} {x+60} {y+92} L{x-20} {y+92} C{x-45} {y+92} {x-50} {y+70} {x-50} {y+40} Z" fill="{skin}" {S}/><path transform="rotate({rot} {x} {y})" d="M{x+20} {y+10} L{x+78} {y+10} M{x+20} {y+58} L{x+70} {y+58}" fill="none" {S}/>'

def prop(kind, skin):
    if kind=="notebook_two_fingers":   # mukhattit: orange notebook at chest + two fingers up
        return (f'<rect x="420" y="800" width="150" height="200" rx="12" fill="{OR}" {S} transform="rotate(-6 495 900)"/>'
                f'<path d="M455 835 L540 835 M455 870 L540 870" fill="none" {S} transform="rotate(-6 495 900)" opacity=".5"/>'
                + hand(470,960,skin,-6) +
                f'<g transform="translate(700 0)"><path d="M-20 1080 L-20 900 C-20 870 10 858 36 868 L36 760 C36 736 70 736 70 760 L70 850 L78 745 C80 720 112 722 112 748 L106 860 C130 866 140 900 128 930 L120 1080 Z" fill="{skin}" {S}/></g>')
    if kind=="card":  # wassam: holds a card up by the face
        return (f'<g transform="rotate(10 330 640)"><rect x="250" y="560" width="160" height="110" rx="10" fill="#FFFFFF" {S}/>'
                f'<path d="M275 600 L385 600 M275 630 L350 630" fill="none" {S}/><rect x="275" y="645" width="40" height="8" rx="4" fill="{OR}"/></g>'
                f'<path d="M300 1080 L300 760 C300 720 340 700 370 715 L372 680 C372 655 404 650 410 672 L412 700 L440 700 C470 705 480 735 470 760 L470 1080 Z" fill="{skin}" {S}/>'
                f'<g transform="rotate(-20 640 900)"><rect x="590" y="820" width="130" height="90" rx="8" fill="#FFFFFF" {S}/><rect x="610" y="810" width="130" height="90" rx="8" fill="#FFFFFF" {S}/><rect x="630" y="800" width="130" height="90" rx="8" fill="#FFFFFF" {S}/></g>' + hand(690,960,skin,-10))
    if kind=="sketchbook":  # naqqash
        return (f'<g transform="rotate(-6 540 930)"><rect x="400" y="830" width="280" height="200" rx="10" fill="#F3EEE6" {S}/><path d="M540 830 L540 1030" fill="none" {S}/>'
                f'<path d="M440 900 Q480 860 520 900 M580 880 L640 880 M580 920 L650 920 M450 960 L510 960" fill="none" {S} opacity=".6"/></g>'
                + hand(420,1000,skin,0) + hand(680,1000,skin,0))
    if kind=="tablet":  # lawwan
        return (f'<g transform="rotate(-8 330 900)"><rect x="215" y="760" width="230" height="300" rx="18" fill="{INK}"/><rect x="229" y="774" width="202" height="272" rx="10" fill="{PAPER}"/>'
                f'<rect x="250" y="800" width="90" height="12" rx="6" fill="{INK}" opacity=".85"/><rect x="250" y="830" width="160" height="110" rx="10" fill="#D9CDB8"/><rect x="250" y="960" width="70" height="26" rx="13" fill="{OR}"/></g>'
                + hand(440,980,skin,-8))
    if kind=="headphones_notebook":  # rawi
        return (f'<path d="M430 760 C430 700 650 700 650 760" fill="none" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>'
                f'<rect x="405" y="740" width="46" height="70" rx="16" fill="{INK}"/><rect x="629" y="740" width="46" height="70" rx="16" fill="{INK}"/>'
                f'<path d="M652 800 C690 850 700 930 680 1000" fill="none" stroke="{OR}" stroke-width="7" stroke-linecap="round"/>'
                f'<g transform="rotate(8 320 930)"><rect x="220" y="830" width="200" height="210" rx="10" fill="#FFFFFF" {S}/><path d="M250 870 L390 870 M250 905 L370 905 M250 940 L395 940 M250 975 L340 975" fill="none" {S} opacity=".5"/><path d="M250 905 L370 905" stroke="{OR}" stroke-width="5"/></g>'
                + hand(300,1010,skin,8) +
                f'<g transform="rotate(-30 700 940)"><rect x="690" y="800" width="18" height="190" rx="6" fill="{INK}"/><path d="M690 800 L699 775 L708 800 Z" fill="{OR}"/></g>' + hand(700,980,skin,-10))
    if kind=="folder_finger":  # muharrir
        return (f'<g transform="rotate(-4 540 940)"><rect x="380" y="840" width="320" height="230" rx="8" fill="#F3EEE6" {S}/>'
                f'<path d="M420 890 L660 890 M420 930 L640 930 M420 970 L660 970 M420 1010 L600 1010" fill="none" {S} opacity=".55"/>'
                f'<rect x="560" y="820" width="80" height="34" rx="8" fill="{OR}" {S}/></g>'
                + hand(400,1030,skin,0) +
                f'<path d="M560 1080 L560 990 C560 970 580 960 600 965 L640 975 L646 940 C650 920 680 920 680 944 L676 985 C690 992 696 1010 690 1030 L684 1080 Z" fill="{skin}" {S}/>')
    if kind=="laptop":  # bannaa
        return (f'<g transform="translate(0 -70) rotate(-10 480 930)"><path d="M300 980 L620 980 L600 860 L320 860 Z" fill="#3B3A3F" {S}/><path d="M320 860 L600 860 L612 940 L308 940 Z" fill="#F6F1E8" {S}/>'
                f'<path d="M350 885 L430 885 M350 905 L480 905 M350 925 L410 925" fill="none" stroke="{OR}" stroke-width="6"/><rect x="420" y="990" width="90" height="10" rx="5" fill="{INK}" opacity=".6"/></g>'
                + hand(340,940,skin,0))
    if kind=="phone_watch":  # maher: phone with a falling bar, orange watch strap on the other wrist
        return (f'<g transform="rotate(-6 640 880)"><rect x="585" y="780" width="110" height="180" rx="14" fill="{INK}"/><rect x="597" y="792" width="86" height="156" rx="8" fill="{PAPER}"/>'
                f'<rect x="612" y="900" width="14" height="36" fill="{OR}"/><rect x="632" y="880" width="14" height="56" fill="#B9B0A2"/><rect x="652" y="850" width="14" height="86" fill="#B9B0A2"/><path d="M612 870 L668 835" fill="none" stroke="{OR}" stroke-width="5"/></g>'
                + hand(690,900,skin,-6) +
                f'<path d="M300 1080 L300 960 C300 920 340 905 370 920 L440 950 C470 962 470 1000 445 1008 L440 1010 C462 1020 460 1050 436 1056 L430 1058 C445 1068 440 1080 420 1080 Z" fill="{skin}" {S}/>'
                f'<rect x="300" y="905" width="76" height="40" rx="10" fill="{INK}" {S}/><rect x="286" y="912" width="14" height="26" fill="{OR}"/><rect x="376" y="912" width="14" height="26" fill="{OR}"/>'
                f'<circle cx="338" cy="925" r="10" fill="none" stroke="{PAPER}" stroke-width="4"/>')
    if kind=="clipboard":  # mudaqqiq
        return (f'<g transform="rotate(6 560 940)"><rect x="420" y="820" width="260" height="260" rx="12" fill="{INK}"/><rect x="434" y="834" width="232" height="246" rx="8" fill="{PAPER}"/>'
                f'<path d="M470 890 L500 890 M470 940 L500 940 M470 990 L500 990 M470 1040 L500 1040" fill="none" {S}/>'
                f'<path d="M452 888 L462 898 L478 876 M452 938 L462 948 L478 926" fill="none" stroke="#3B9B6E" stroke-width="7" stroke-linecap="round"/><path d="M450 982 L472 1000 M472 982 L450 1000" fill="none" stroke="{OR}" stroke-width="7" stroke-linecap="round"/>'
                f'<path d="M520 890 L640 890 M520 940 L620 940 M520 990 L640 990 M520 1040 L600 1040" fill="none" {S} opacity=".5"/></g>'
                + hand(430,1040,skin,6) +
                f'<g transform="rotate(-35 720 900)"><rect x="710" y="780" width="16" height="200" rx="6" fill="{OR}" {S}/></g>' + hand(720,1000,skin,-20))
    if kind=="two_phones":  # nashir
        return (f'<g transform="rotate(-12 330 920)"><rect x="270" y="800" width="120" height="220" rx="16" fill="{INK}"/><rect x="282" y="812" width="96" height="196" rx="10" fill="{PAPER}"/><rect x="300" y="840" width="60" height="50" rx="6" fill="#D9CDB8"/><rect x="300" y="905" width="60" height="8" rx="4" fill="{INK}" opacity=".5"/></g>'
                f'<g transform="rotate(8 400 920)"><rect x="350" y="790" width="120" height="220" rx="16" fill="{INK}"/><rect x="362" y="802" width="96" height="196" rx="10" fill="{PAPER}"/><rect x="380" y="830" width="60" height="50" rx="6" fill="{OR}"/><rect x="380" y="895" width="60" height="8" rx="4" fill="{INK}" opacity=".5"/></g>'
                + hand(380,1010,skin,0) +
                f'<rect x="650" y="950" width="64" height="48" rx="12" fill="{PAPER}" {S}/><circle cx="682" cy="974" r="12" fill="none" {S}/><path d="M682 966 L682 974 L688 978" fill="none" {S}/><rect x="640" y="958" width="10" height="32" fill="#3B3A3F"/><rect x="714" y="958" width="10" height="32" fill="#3B3A3F"/>'
                + hand(690,1040,skin,0))
    if kind=="chart_board":  # mulin
        return (f'<g transform="rotate(-5 560 930)"><rect x="410" y="820" width="300" height="220" rx="10" fill="#FFFFFF" {S}/>'
                f'<rect x="450" y="960" width="40" height="50" fill="#B9B0A2"/><rect x="510" y="920" width="40" height="90" fill="#B9B0A2"/><rect x="570" y="940" width="40" height="70" fill="#B9B0A2"/><rect x="630" y="880" width="40" height="130" fill="{OR}"/>'
                f'<path d="M440 1012 L690 1012" fill="none" {S}/><path d="M450 900 L680 860" fill="none" stroke="{INK}" stroke-width="5" stroke-dasharray="10 10"/></g>'
                + hand(430,1030,skin,0) + hand(700,1030,skin,0))
    if kind=="greeting":  # safeer: open hand raised in greeting + phone with a half-typed message
        return (f'<path d="M330 1080 L330 930 C330 900 345 880 370 880 L370 800 C370 778 400 778 400 800 L400 870 L404 760 C406 736 438 736 438 760 L436 870 L446 780 C450 756 482 760 480 786 L470 876 L484 820 C490 798 518 804 514 830 L498 920 C530 930 540 960 530 990 L520 1080 Z" fill="{skin}" {S}/>'
                f'<path d="M400 870 L404 900 M436 870 L436 905 M470 876 L466 905" fill="none" {S} opacity=".5"/>'
                f'<g transform="rotate(-10 680 930)"><rect x="620" y="820" width="120" height="220" rx="16" fill="{INK}"/><rect x="632" y="832" width="96" height="196" rx="10" fill="{PAPER}"/><rect x="648" y="860" width="64" height="18" rx="9" fill="#D9CDB8"/><rect x="648" y="890" width="50" height="18" rx="9" fill="#D9CDB8"/><rect x="662" y="980" width="50" height="18" rx="9" fill="{OR}"/></g>'
                + hand(690,1030,skin,-10))
    if kind=="binder_pen":  # mudawwin
        return (f'<g transform="rotate(4 330 940)"><rect x="200" y="800" width="230" height="280" rx="8" fill="{OR}" {S}/><rect x="200" y="800" width="36" height="280" fill="{INK}" opacity=".25"/><rect x="260" y="840" width="130" height="60" rx="6" fill="{PAPER}"/><path d="M280 860 L370 860 M280 882 L350 882" fill="none" {S} opacity=".5"/></g>'
                + hand(330,1020,skin,4) +
                f'<g transform="rotate(-40 700 900)"><rect x="690" y="760" width="20" height="220" rx="7" fill="{INK}"/><path d="M690 760 L700 730 L710 760 Z" fill="#B9B0A2"/><rect x="690" y="800" width="20" height="10" fill="{OR}"/></g>' + hand(705,990,skin,-15))
    return ""

def shemagh():
    return (f'<path d="M560 745 C640 760 720 820 760 900 L800 1080 L700 1080 L660 900 C630 850 600 800 560 745 Z" fill="#FFFFFF" {S}/>'
            f'<path d="M585 770 C650 800 700 860 730 940" fill="none" stroke="{OR}" stroke-width="5"/>')

def scarf():
    return (f'<path d="M430 728 C470 800 610 800 650 728 C680 760 672 800 640 820 C590 850 490 850 440 820 C408 800 400 760 430 728 Z" fill="{OR}" {S}/>'
            f'<path d="M585 815 C620 870 650 930 640 1000 C615 1010 590 1005 575 995 C580 930 560 870 548 830 Z" fill="{OR}" {S}/>')

def bracelet(skin): return f'<rect x="300" y="960" width="80" height="22" rx="8" fill="{OR}" {S} transform="rotate(-8 340 970)"/>'

CH=[
 # slug, skin, hair, hair_col, tilt, garment, garment_col, face(eyes,brows,mouth), prop, extras, overlays
 ("mukhattit","#B9794F","shortgrey","#3A2A22",-3,"shirt","#E7DCC6",("open","raised","line"),"notebook_two_fingers",["stubble"],[]),
 ("wassam","#D9A77C","neat","#2B1B14",4,"crew","#6E7B86",("narrow","oneup","smirk"),"card",["glasses_orange"],[]),
 ("naqqash","#C68B5E","short","#2B1B14",0,"apron","#F0E6D8",("open","flat","line"),"sketchbook",["stubble","marker_ear"],[]),
 ("lawwan","#C68B5E","bun","#2B1B14",6,"shirt","#FFFFFF",("open","level","half"),"tablet",["earring"],["scarf"]),
 ("rawi","#B07A55","curly","#1F1410",-5,"crew","#5B6B5A",("open","raised","open"),"headphones_notebook",[],[]),
 ("muharrir","#E0B48C","longup","#4A2E1E",0,"cardigan","#7A8450",("open","level","pressed"),"folder_finger",[],[]),
 ("bannaa","#C98F63","short","#2B1B14",5,"hoodie","#2F2B3A",("open","raised","smirk"),"laptop",[],["bracelet"]),
 ("maher","#A86B45","short","#1F1410",0,"polo","#1F2A44",("open","level","half"),"phone_watch",["beard"],[]),
 ("mudaqqiq","#D4A079","bob","#2B1B14",-4,"shirt","#F3EEE6",("down","oneup","pressed"),"clipboard",[],[]),
 ("nashir","#C68B5E","neat","#2B1B14",3,"button","#8FA3B8",("open","level","wide"),"two_phones",["earbud"],[]),
 ("mulin","#D9A77C","wavy","#3A2218",-2,"blazer","#4F7C7A",("open","oneup","half"),"chart_board",["pencil_ear"],[]),
 ("safeer","#B9794F","short","#2B1B14",2,"thobe","#FFFFFF",("happy","raised","wide"),"greeting",["stubble"],["shemagh"]),
 ("mudawwin","#E3BFA0","white","#ECE6DC",0,"crew","#3B3A3F",("open","level","smirk"),"binder_pen",["glasses_round"],[]),
]
os.makedirs("svg",exist_ok=True); os.makedirs("png",exist_ok=True)
for slug,skin,hair,hc,tilt,garm,gc,fc,pr,extras,ov in CH:
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1080" width="1080" height="1080">',
           f'<defs><clipPath id="c"><circle cx="540" cy="540" r="480"/></clipPath></defs>',
           f'<rect width="1080" height="1080" fill="{PAPER}"/><circle cx="540" cy="540" r="480" fill="{DISC}"/><g clip-path="url(#c)"><g transform="translate(540 600) scale(1.12) translate(-540 -600)">']
    parts.append(body(garm,gc,skin))
    if "shemagh" in ov: parts.append(shemagh())
    parts.append(neck(skin))
    if "scarf" in ov: parts.append(scarf())
    parts.append(prop(pr,skin))
    if "bracelet" in ov: parts.append(bracelet(skin))
    parts.append(head(skin,tilt,hair,hc,face(*fc),extras))
    parts.append(f'</g></g><circle cx="540" cy="540" r="480" fill="none" stroke="{INK}" stroke-width="8"/></svg>')
    open(f"svg/{slug}.svg","w",encoding="utf-8").write("\n".join(parts))
# contact sheet
tiles="".join(f'<figure><img src="svg/{c[0]}.svg"><figcaption>{c[0]}</figcaption></figure>' for c in CH)
open("sheet.html","w",encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:{PAPER};font-family:Inter,Arial;padding:40px}}.g{{display:grid;grid-template-columns:repeat(7,1fr);gap:28px}}figure{{margin:0;text-align:center}}img{{width:100%;display:block}}figcaption{{font-size:22px;color:{INK};margin-top:10px}}</style></head><body><div class="g">{tiles}</div></body></html>')
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([CHROME,"--headless=new","--hide-scrollbars","--force-device-scale-factor=1","--window-size=2400,920","--screenshot=sheet.png",f"file://{os.getcwd()}/sheet.html"],stderr=subprocess.DEVNULL)
for c in CH:
    open("one.html","w",encoding="utf-8").write(f'<!doctype html><html><head><meta charset="utf-8"><style>html,body{{margin:0;background:{PAPER}}}img{{display:block;width:512px;height:512px}}</style></head><body><img src="svg/{c[0]}.svg"></body></html>')
    subprocess.run([CHROME,"--headless=new","--hide-scrollbars","--force-device-scale-factor=1","--window-size=512,512",f"--screenshot=png/{c[0]}-512.png",f"file://{os.getcwd()}/one.html"],stderr=subprocess.DEVNULL)
os.remove("one.html"); print("ok")
