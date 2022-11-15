thisdict ={
	"brand":"ford",
	"model":"mustang",
	"year":1964
	}
print(type(thisdict))
print(thisdict)
x=thisdict["model"]
print(x)
x=thisdict["year"]
print (x)
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x, y in thisdict.items():
    print(x, y)
for x in thisdict.values():
    print(x)
thisdict.pop("brand")
print(thisdict)
            
