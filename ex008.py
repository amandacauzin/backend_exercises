dist = float(input('Uma distância em metros:'))
km = dist / 1000
hm = dist / 100
dam = dist / 10
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print('A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(dist, km, hm, dam, dm, cm, mm))