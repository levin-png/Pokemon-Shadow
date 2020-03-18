define hugh = Character("Hugh")
define vater = Character("Vater")

label start:

    scene bg room

    show hugh

    hugh "(YOO Heute werd ich endlich ein echter Trainer!)"
    transform moveright:
        linear 0.3 xpos 0.75

    show hugh:
        xalign 0.5
        moveright

    vater "Hahahaha, Sohnemann!!"
    show vater
    vater "Grosser Tag für dich heute was? Du kriegst endlich dein erstes eigenes Pokemon und du kannst den Weg deines Alten einschlagen!"
    hugh "Nein Dad, ich werde kein scheiss Arenaleiter..."
    hugh "ICH"
    hugh "WERDE"
    hugh "DER"
    hugh "FUCKING CHAMPION SEIN"
    vater "Grosse Träume sind was gutes, aber komm mal ein bisschen von deinem Film runter."
    hugh "Inshallah ich werde Champ du wirst sehen."
    vater "Hahaha soooo nicht minjung! Spätestens wenn du gegen mich antrittst, wars das für dich."
    vater "Ich verwette einen Shishakopf drauf!"

    menu:
        "Wette annehmen":
            hugh "Alles klar alter Mann, mach schon mal die Kohle heiss."
            vater "Ich glaube nicht."

        "Wette ablehnen":
            hugh "Hm, ne das ist mir jetzt doch ein wenig zu riskant, ich würde
            ungern einen Zwanziger verlieren wegen so einer spontanen und komplett aus dem Kontext gerissenen Wette."
            vater "Alman."
            hugh "Was für Alman i-"

    vater "Egal, besuch mal deinen Homie Jens."
    hugh "Sag mir nicht was ich machen soll, ich bin jetzt 14!"
    vater "Ihr wolltet doch zusammen zum Professor"
    hugh "Ja, also... schon ja."

label rival_house:
    scene bg room rival
    show hugh
    hugh "..."
    hugh "(Wo ist diser Zemel? Wir haben uns doch hier verabredet...)"
    transform moveright:
        linear 0.3 xpos 0.75

    show hugh:
        xalign 0.5
        moveright

    show rivale
    rivale "ICH BIIIN DAA DUU KEELB."
    rivale "Ich war fett kacki machen. Sry man."
    rivale "Ups habe ich dich etwa erschreckt?"
    menu:
        "Ja":
            hugh "Natürlich du Zemel..."
            rivale "Oh dann tuts mir ja gar nicht leid dass du eine Muschi bist."
        "Nein":
            hugh "Sicher nicht erschreck ich mich von einem Zemel."
            rivale "Red nicht so. Deine Hose hängt hinten schon nach unten und es stinkt nach kacki."

    rivale "Also ich habe dich gerufen um zusammen zum Professor zu gehen. Du kommst oder?"
    menu:
        "Ja":
            rivale "Besser isses"
        "nein":
            rivale "Bist du dumm? Wie viel mal hat dich dein Vater auf den Boden fallen gelassen?"
            rivale "Und wie viele davon waren absichtlich? Ist jetzt eigentlich egal. Du kommst jetzt."
    jump rival_house

#label lab:
#    scene bg lab
#    show hugh
#    hugh "hi"
#    jump lab
#

    # This ends the game.

    return
