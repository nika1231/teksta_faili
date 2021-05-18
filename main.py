f = open('teksts.txt')
saturs = f.read()
f.close()
print(saturs)


z = open('tagad_taisam.txt','w')
z.write('tev sanāca arī šis!')
z.close()