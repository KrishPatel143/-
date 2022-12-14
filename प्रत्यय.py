from प्रत्याहार import *

def प्रत्ययअर्थ(शब्दः):
    if प्रत्ययअस्ति(शब्दः) == False:
        return ''
    प्रत्यय = []
    संचिका = open(u"सूत्र_१_१.संस्कृत","r+",encoding="utf-8")
    दत्तांश = संचिका.read()
    वाक्यानि = दत्तांश.splitlines()
    संचिका.close()

    for वाक्य in वाक्यानि:
        if शब्दः in वाक्य:
            क = वाक्य.split(' ')
            शब्दाः = क[0].split('-')
            for अयंशब्दः in शब्दाः:
                if प्रत्याहारअस्ति(अयंशब्दः):
                    र = प्रत्याहारअर्थ(अयंशब्दः)
                    for पत्रम् in र:
                        प्रत्यय.append(पत्रम्)
                if अयंशब्दः[-2:] == "त्":
                    प्रत्यय.append(अयंशब्दः[:-2])
            
    return प्रत्यय

def प्रत्ययअस्ति(शब्दः):    
    संचिका = open(u"प्रत्यय.संस्कृत","r+",encoding="utf-8")
    दत्तांश = संचिका.read()
    प्रत्यय = दत्तांश.splitlines()
    संचिका.close()
    if शब्दः in प्रत्यय:
        return True
    return False

if __name__ == "__main__":
    
    प्रत्याहार = प्रत्ययअस्ति("गुणः")
    print(प्रत्याहार)