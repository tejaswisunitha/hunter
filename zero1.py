a,b=raw_input().split()
a=int(a)
b=int(b)
l=[]
s=0
pos=[]
oy=[]
ui=[]
for i in range(0,a):
    a=raw_input().split()
    l.append(a)
for i in range(0,len(l)):
    k=l[i]
    t=l[i]
    for j in range(0,len(k)):
        if '0' in k:
            u=[index for index, ink in enumerate(k) if ink=='0']
            for et in range(0,len(u)):
                ui.append(u[et])
            k=[]
            for r in range(0,len(l[i])):
                k.append('0')
            oy.append(k)
            k=[]
            break
        else:
            s=s+1
    if s==b:
        for z in range(0,b):
            pos.append(t[z])
        oy.append(pos)
        pos=[]
    s=0
for i in oy:
  new=i
  for j in range(0,len(new)):
    if j in ui:
      new.insert(j+1,'0')
      new.remove(new[j])
  for i in range(0,len(new)):
    print new[i],
  print "\n",
