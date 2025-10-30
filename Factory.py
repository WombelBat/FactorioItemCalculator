from factorio_obj import ReadItemsFromFile,factorioItem ,getItemConsputionList,printConsumptionList,getItemProductionList,printProductionList,checkValidityOfconsumptin


item_list: dict[str, factorioItem] = {}

file_name = "items.json"

item_list = ReadItemsFromFile(file_name)

# objects with no propper structure:
# 
# resource outputs as a dict
resource_outputs: dict[str, float] = {
    "crude_oil": 367.8,
    "iron_ore": 0.0,
    "stone": 0.0,
    "copper_ore": 0.0,
    "water" :0.0,
    "coal": 0.0,
    "uranium_ore":0.0

}

# real items

# just change the ones that have specific values
for i in item_list.values():
    if i.getChosenMethod() =="":
        i.chose_method(2)

item_list["plastic"].setFactories(4)
item_list["sulfur"].setFactories(4)
item_list["Electronic circuit"].setFactories(5)
item_list["iron plate"].setFactories(36)
item_list["copper plate"].setFactories(18)
item_list["Advanced circuit"].setFactories(8)
item_list["Petroleum"].setFactories(14)
item_list["steel plate"].setFactories(6)
item_list["iron gear wheel"].setFactories(8)
item_list["transport belt"].setFactories(6)
item_list["copper cable"].setFactories(7)
item_list["assembling machine 1"].setFactories(0)
item_list["battery"].setFactories(4)
item_list["sulfuric acid"].setFactories(1)
item_list["processing unit"].setFactories(0)
item_list["engine unit"].setFactories(8)
item_list["electric engine unit"].setFactories(0)
item_list["pipe"].setFactories(6)
item_list["low density structure"].setFactories(0)
item_list["rocket fuel"].setFactories(0)
item_list["speed module"].setFactories(0)
item_list["efficiency module"].setFactories(0)
item_list["productivity module"].setFactories(0)
item_list["satellite"].setFactories(0)
item_list["rocket part"].setFactories(0)
item_list["automation science pack"].setFactories(6)
item_list["logistic science pack"].setFactories(14)
item_list["military science pack"].setFactories(8)
item_list["chemical science pack"].setFactories(16)
item_list["production science pack"].setFactories(0)
item_list["utility science pack"].setFactories(0)
item_list["space science pack"].setFactories(0)
item_list["speed module 2"].setFactories(0)
item_list["productivity module 2"].setFactories(0)
item_list["efficiency module 2"].setFactories(0)
item_list["Stone brick"].setFactories(6)
item_list["rail"].setFactories(3)
item_list["wall"].setFactories(6)
item_list["firearm magazine"].setFactories(6)
item_list["piercing rounds magazine"].setFactories(6)
item_list["uranium rounds magazine"].setFactories(0)
item_list["shotgun shells"].setFactories(0)
item_list["piercing shotgun shells"].setFactories(0)
item_list["cannon shell"].setFactories(0)
item_list["explosive cannon shell"].setFactories(0)
item_list["artillery shell"].setFactories(0)
item_list["rocket"].setFactories(0)
item_list["explosive rocket"].setFactories(0)
item_list["atomic bomb"].setFactories(0)
item_list["Flamethrower ammo"].setFactories(0)
item_list["Explosives"].setFactories(0)
item_list["grenade"].setFactories(6)
item_list["inserter"].setFactories(4)
item_list["iron stick"].setFactories(4)

item_list["lubricant"].setFactories(0)
item_list["solid fuel"].setFactories(0)
item_list["solar panel"].setFactories(0)
item_list["accumulator"].setFactories(0)
item_list["radar"].setFactories(0)
item_list["electric furnace"].setFactories(0)
item_list["flying robot frame"].setFactories(0)
item_list["uranium-238"].setFactories(0)
item_list["express transport belt"].setFactories(0)
item_list["express underground belt"].setFactories(0)
item_list["express splitter"].setFactories(0)
item_list["fast transport belt"].setFactories(0)
item_list["fast underground belt"].setFactories(0)
item_list["fast splitter"].setFactories(0)

# changed methods

# assemblers  
item_list["inserter"].chose_method(1)
item_list["transport belt"].chose_method(1)
item_list["wall"].chose_method(1)
item_list["automation science pack"].chose_method(1)
item_list["logistic science pack"].chose_method(1)
item_list["Electronic circuit"].chose_method(1)


# output side
item_list["processing unit"].factoriesTOgetOutputX(2,verbose = True)
item_list["processing unit"].resourcesToGetOutputX(2,verbose=True)

item_consumption_list:{str,float} = getItemConsputionList(item_list)
item_production_list:{str,float} = getItemProductionList(item_list)



# printConsumptionList(item_consumption_list)

# printProductionList(item_production_list)

checkValidityOfconsumptin(item_production_list,item_consumption_list,resource_outputs)

