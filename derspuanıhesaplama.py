isim = input("isminizi giriniz:")
soyisim=input("soyisminizi giriniz:")
öğrencinumarası=input("öğrenci numaranızı giriniz")
medenihukukvizesi = input('medeni hukuk için vize Notunuz : ')
idarehukukuvizesi = input('idare hukuku için vize Notunuz : ')
icrahukukuvizesi = input('icra hukuku için vize Notunuz : ')
iktisatvizesi = input('iktisat için vize Notunuz : ')
medenihukukfinali = input('medeni hukuk Final Notunuz : ')
idarehukukufinali = input('idare hukuku Final Notunuz : ')
icrahukukufinali = input('icra hukuku Final Notunuz : ')
iktisatfinali = input('iktisat Final Notunuz : ')
medenihukukortalaması = (float(medenihukukvizesi) * 0.4) + (float(medenihukukfinali) * 0.6)
idarehukukuortalaması = (float(idarehukukuvizesi) * 0.4) + (float(idarehukukufinali) * 0.6)
icrahukukuortalaması = (float(icrahukukuvizesi) * 0.4) + (float(icrahukukufinali) * 0.6)
iktisatortalaması = (float(iktisatvizesi) * 0.4) + (float(iktisatfinali) * 0.6)
print(isim,soyisim,öğrencinumarası)

print("medenihukukortalaması :{0} ".format(medenihukukortalaması))
print("idarehukukuortalaması :{0} ".format(idarehukukuortalaması))
print("icrahukukuortalaması :{0} ".format(icrahukukuortalaması))
print("iktisatortalaması :{0} ".format(iktisatortalaması))
if (medenihukukortalaması < 50):
    print("medeni hukuktan kaldınız")
else:
    print("medeni hukuktan geçtiniz")
if (idarehukukuortalaması < 50):
    print("idare hukukundan kaldınız")
else:
    print("idare hukukundan geçtiniz")
if (icrahukukuortalaması< 50):
    print("icra hukukundan kaldınız")
else:
    print("icra hukukundan geçtiniz")
if (iktisatortalaması < 50):
    print("iktisattan kaldınız")
else:
    print("iktisattan geçtiniz")


