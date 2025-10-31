import json
from math import ceil
import re
class factorioItem():    
    name=""
    nr_factories=0

    output={}
    time_req =0.0
    final_output={}
    
    input={}
    final_input={}

    chosen_speed_mod="none"
    nr_speed_mod =0
    speed_modifier={"none":0,"mk1":20/100,"mk2":30/100,"mk3": 50/100}

    chosen_quantity_mod="none"
    nr_quantity_mod =0
    quantity_modifier={"none":0,"mk1":4/100,"mk2":6/100,"mk3": 10/100}
    quantity_modifier_speed ={"none":0,"mk1":-5/100,"mk2":-10/100,"mk3": -15/100}
    
    method={}
    chosen_method =""
    bool_method=False

    def __init__(self, name:str, output_name:list, output_value:list ,time_req:float, 
                 method_name:list  ,method_time:list ,
                 input_name:list,input_value:list ):
        
        self.name = name

        if len(output_name) != len(output_value):
            raise ValueError("output_name and output_value must have the same length")
        if len(method_name) != len(method_time):
            raise ValueError("method_name and method_time must have the same length")
        if len(input_name) != len(input_value):
            raise ValueError("input_name and input_value must have the same length")

        self.output = dict(zip(output_name, output_value))
        self.time_req = time_req
        self.final_output = dict(zip(output_name, output_value))
        self.method = dict(zip(method_name, method_time))
        self.input = dict(zip(input_name, input_value)) 
        self.final_input = dict(zip(input_name, input_value)) 
        
        if len(self.output) == 1:
            self.chose_method(1)
        

    def __init__(self,d:dict):
        self.name = d["name"]

        if len(d["output_name"]) != len(d["output_value"]):
            raise ValueError("output_name and output_value must have the same length")
        if len(d["method_name"]) != len(d["method_time"]):
            raise ValueError("method_name and method_time must have the same length")
        if len(d["input_name"]) != len(d["input_value"]):
            raise ValueError("input_name and input_value must have the same length")

        self.output = dict(zip(d["output_name"], d["output_value"]))
        self.final_output = dict(zip(d["output_name"], d["output_value"]))
        self.time_req = d["time_req"]
        self.method = dict(zip(d["method_name"], d["method_time"]))
        self.input = dict(zip(d["input_name"], d["input_value"]))
        self.final_input = dict(zip(d["input_name"], d["input_value"]))
        
        if len(self.method) == 1:
            self.chose_method(1)
       

    def addSpeedMods(self,type:int , nr:int ):
        if type >3 :
            print("mod dosent exist")
            return
        self.chosen_speed_mod = list(self.speed_modifier.keys())[type-1]
        self.nr_speed_mod = nr

    def addQuantityMods(self, type:int , nr:int ):
        if type > 3 :
            print("mod dosent exist")
            return
        self.chosen_quantity_mod = list(self.quantity_modifier.keys())[type-1]
        self.nr_quantity_mod = nr
    
    def getChosenMethod(self):
        return self.chosen_method
    
    def chose_method_by_name(self,method_name:str):
        if method_name not in self.method:
            print("Error method not  available")
            exit()

        self.chosen_method = method_name.lower()

    def chose_method(self,method_itt:int):
        
        temp = list(self.method.keys())
        if method_itt > len(temp) or method_itt < 1:
            print("Error method not  available")
            exit()

        self.chosen_method = temp[method_itt-1]
    
    def setFactories(self,nr_fact:int):
        self.nr_factories = nr_fact
    
    def addFactories(self,nr_fact:int):
        self.nr_factories +=nr_fact
    
    def subtractFactories(self,nr_fact:int):
        self.nr_factories -=nr_fact
    
    def getSpeedMod(self):
        return  ( 1  + self.speed_modifier[ self.chosen_speed_mod ] *
                                self.nr_speed_mod +
                                self.quantity_modifier_speed[ self.chosen_quantity_mod ]*
                                self.nr_quantity_mod )
        
    def getQuantityMod(self):
        return (1 + 
                                 self.quantity_modifier[self.chosen_quantity_mod] *
                                 self.nr_quantity_mod  )
    
    def getOutput(self,verbose=False):
        if self.chosen_method == "":
            print("Warning: No factory method chosen! Please choose a method first.")
            return {}
        self.defineOUtput()
        if verbose:
            for key,val in self.output.items(): 
                print(f"{key} = {val} per second")

        return self.final_output


    def defineOUtput(self):
        for key,val in self.output.items(): 

            quanity_modifier = self.getQuantityMod()
            items =(val*quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( (self.time_req/ self.method[ self.chosen_method ])* speed_modifier )

            self.final_output[key] = self.nr_factories * items/ time_nec 

    
    def defineInput(self):
        for key,val in self.input.items(): 

            speed_modifier = self.getSpeedMod()
            time_nec = ( (self.time_req/self.method[ self.chosen_method ]) * speed_modifier)
                                                                                                             
            self.final_input[key] = self.nr_factories * val / time_nec

    def getInput(self,verbose=False):
        if self.chosen_method == "":
            print("Warning: No factory method chosen! Please choose a method first.")
            return {}
        self.defineInput()
        if verbose:
            for key,val in self.input.items(): 
            
                print(f"{key} = {val} per second")

        return self.final_input
    
    def convertToTimeUnit(self,time_unit:str):
        t_u_vec = {"s": 1, "sec": 1, "min": 60, "h": 3600, "hour": 3600, "d": 86400, "day": 86400, "days": 86400}

        t_nr = [int(s) for s in re.findall(r'\b\d+\b',time_unit)]
        if len(t_nr) > 1:
            print("error in the time unit you can only use whole numbers of one type of unit")
        elif len(t_nr) < 1:
            t_nr = 1
        else:
            t_nr = t_nr[0]
        
        for key, val in t_u_vec.items():
            if key in time_unit:
                # print(f"{key}:{val} , {time_unit}")
                return t_nr * val
        print("Invalid time unit provided.")
        return None
               

    def factoriesTOgetOutputX(self,output_wanted:float,verbose =False,output_name="",time_unit ='s'):
        # tells how many more factories you need to get output_wanted of the output selected
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)

            nec_out = output_wanted/time_unit_nr - self.getOutput()[output_name]
            
            quanity_modifier = self.getQuantityMod()
            items =(self.output[output_name] * quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( (self.time_req/self.method[ self.chosen_method ])* speed_modifier )

            nec_fact = ceil(nec_out /items * time_nec)
            if verbose:
                print(f"To get {output_wanted} /{time_unit} {output_name.capitalize()} you need an extra: {nec_fact} {self.chosen_method} for a total of { nec_fact+self.nr_factories} ")
    
            return nec_fact
        
        print("output dosent exist")
        return
    def factoriesTOget_X_MORE_OUTPUT(self,output_wanted:float,verbose =False,output_name="",time_unit = "sec"):
        # gives the amount of factories needed to get output_wanted more output than already posible
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)
            # print(f"time uinit:{time_unit_nr} \n")
            nec_out = output_wanted /time_unit_nr
            self.defineOUtput()
            quanity_modifier = self.getQuantityMod()
            items =(self.output[output_name] * quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( self.time_req / (self.method[ self.chosen_method ]* speed_modifier ))

            nec_fact = ceil(nec_out /items * time_nec)
            if verbose:
                print(f"To get {output_wanted} /{time_unit} {output_name.upper()} MORE you need: {nec_fact} {self.chosen_method}")
                print(f"For a total of {nec_fact+self.nr_factories} {self.chosen_method} and total production of {output_wanted+self.final_output[output_name]*time_unit_nr}/{time_unit} ( original {self.final_output[output_name]*time_unit_nr}/{time_unit})\n")

            return nec_fact
        
        print("output dosent exist")
        return
    def resourcesToGetOutputX(self,output_wanted:float,output_name="",verbose =False,time_unit='s'):
        # tells how many more reasources of each type you need to get output_wanted of the wanted output
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)

            total_fact = self.nr_factories + self.factoriesTOgetOutputX(output_wanted/time_unit_nr,output_name)

            total_input={}
            if verbose:
                print(f"To get {output_wanted } /{time_unit_nr} {output_name} using {self.chosen_method} you need: ")
            for key,val in self.input.items(): 

                speed_modifier = self.getSpeedMod()
                time_nec = ( (self.time_req/self.method[ self.chosen_method ]) * speed_modifier)
                                                                                                             
                total_input[key] = total_fact * val / time_nec

                if verbose:
                    print(f"{key}: {total_input[key] *time_unit_nr} /{time_unit}")
    
            return total_input
        
        print("output dosent exist")
        return

    def resourcesTOget_X_MORE_OUTPUTX(self,output_wanted:float,output_name="",verbose =False,time_unit='s'):
        # tells how many more reasources of each type  you need to get output_wanted more output
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)

            total_fact = self.factoriesTOget_X_MORE_OUTPUT(output_wanted/time_unit_nr,output_name)

            total_input={}
            if verbose:
                print(f"To get {output_wanted } /{time_unit_nr} MORE {output_name}  using {self.chosen_method} you need: ")
            for key,val in self.input.items(): 

                speed_modifier = self.getSpeedMod()
                time_nec = ( (self.time_req/self.method[ self.chosen_method ]) * speed_modifier)
                                                                                                             
                total_input[key] = total_fact * val / time_nec

                if verbose:
                    print(f"{key}: {total_input[key] *time_unit_nr} /{time_unit}")
    
            return total_input
        
        print("output dosent exist")
        return
    
    def getFactoriesNeededToGetXoutput(self,output_wanted:float,output_name="",verbose =False,time_unit='s'):
        # tells how many  factories you need (assumes you have 0) to get output_wanted of the output selected
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)

            nec_out = output_wanted/time_unit_nr
            
            quanity_modifier = self.getQuantityMod()
            items =(self.output[output_name] * quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( (self.time_req/self.method[ self.chosen_method ])* speed_modifier )

            nec_fact = ceil(nec_out /items * time_nec)
            if verbose:
                print(f"To get {output_wanted} /{time_unit} {output_name.capitalize()} you need: {nec_fact} {self.chosen_method} ")
    
            return nec_fact
        
        print("output dosent exist")
        return
    def getResourcesNeededToGetOutputX(self,output_wanted:float,output_name="",verbose =False,time_unit='s'):
        # assumes you have 0 factories unlike other options
        # tells how many more reasources of each type you need to get output_wanted of the wanted output
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:
            time_unit_nr = self.convertToTimeUnit(time_unit)

            total_fact = self.getFactoriesNeededToGetXoutput(output_wanted/time_unit_nr,output_name)

            total_input={}
            if verbose:
                print(f"To get {output_wanted } /{time_unit_nr} {output_name} using {self.chosen_method} you need: ")
            for key,val in self.input.items(): 

                speed_modifier = self.getSpeedMod()
                time_nec = ( (self.time_req/self.method[ self.chosen_method ]) * speed_modifier)
                                                                                                             
                total_input[key] = total_fact * val / time_nec

                if verbose:
                    print(f"{key}: {total_input[key] *time_unit_nr} /{time_unit}")
    
            return total_input
        
        print("output dosent exist")
        return

def ReadItemsFromFile(file_name:str):
    item_list = {}
    with open(file_name) as f:
        d = json.load(f)

    for i in d["items"]:
        item_list.update( {i["name"]:factorioItem(i)} )
    
    return item_list

def getItemConsumptionList(il: dict[str, factorioItem]):
    icl:{str,float} = {}
    for i in il.values():
        temp_in = i.getInput()

        for j_key, j_val in temp_in.items():
            if j_key in icl:
                icl[j_key] +=j_val
            else:
                icl.update({j_key: j_val })
    return icl



def printItemConsumptionList(icl:dict[str,float]):
    print("\nConsumption list: \n")
    for key,val in icl.items():
        if val > 0:
            print(f"{val} {key} /sec consumed")


def getItemProductionList(il: dict[str, factorioItem]):
    ipl:{str,float} = {}
    for i in il.values():
        temp_in = i.getOutput()

        for j_key, j_val in temp_in.items():
            if j_key in ipl:
                ipl[j_key] +=j_val
            else:
                ipl.update({j_key: j_val })
    return ipl

def printProductionList(ipl:dict[str,float]):
    print("\nConsumption list: \n")
    for key,val in ipl.items():
        if val > 0:
            print(f"{val} {key} /sec produced")

def checkValidityOfconsumptin(ipl:dict[str,float], icl:{str,float},res_out: dict[str, float], 
                              verbose_notListed= True, verbose_not_cov = False,verbose_cov=False ):
    
    # gives a list of production - consumption for each reasource 
    # can print if verbose for ones covered by current setup and/or 
    # not covered by current setup  
    
    validity_list:dict[str:float]={}
    validity_raw_list:dict[str:float]={}
    print()
    if verbose_cov or verbose_not_cov:
        print("Item validity list: \n")
    for key,val in icl.items():
        if key in ipl:
            # from assemblres and stuff
            validity_list.update({key: ipl[key] - val}  )
            if validity_list[key] >=0:
                if verbose_cov:
                    print(f"{key} is covered")
                
            else:
                if verbose_not_cov:
                    print(f"{key} is not covered by { validity_list[key] }")
        
        elif key in res_out:
            # raw resources
            validity_raw_list.update({key: res_out[key] - val}  )
            if validity_raw_list[key] >=0:
                if verbose_cov:
                    print(f"{key} RAW is covered")
                
            else:
                if verbose_not_cov:
                    print(f"{key} RAW is not covered by { validity_raw_list[key] }")
        else:
            # not included
            validity_list.update( {key: 0 - val}  )
            if verbose_notListed:
                print(f"Item {key} is not listed in the  production list or raw resources RECHECK")
        
    return validity_list,validity_raw_list

def necesarryFactories(il: dict[str, factorioItem],raw_resources_out: dict[str, float],verbose=True):
    # gives a list (and prints it if verbose) of how many factories you need 
    # in order to fully fullfill the requirments of all currently existing factories in your factorie 

    ipl:dict[str,float]=getItemProductionList(il)
    icl:{str,float}=getItemConsumptionList(il)
    factory_need_list:{str,[str,int]} = {}
    vl:dict[str:float]={}
    vrl:dict[str:float]={}

    vl,vrl = checkValidityOfconsumptin(ipl,icl,raw_resources_out,verbose_notListed=True)

    for i in il.values():
        for j in i.getOutput().keys():
            if j in vl:
                if vl[j]<0:
                    factory_need_list.update({j: [i.getChosenMethod(),i.factoriesTOget_X_MORE_OUTPUT(-vl[j],verbose=verbose)]})
    if verbose:
        print("\nClean Factory needed List:\n")
        for key,tot in factory_need_list.items():
            print(f"{tot[1]} {key} {tot[0]}")


    return factory_need_list


def getItemsThatNeedX(item_name:str,il: dict[str, factorioItem],need_factory=True,verbose = True,verbose_empty=True):
    # need_factory parameter refers to does it need to have factories in order to add to the list or just any recepi
    inl=[]
    # if verbose :
    #     print(f"\n{item_name.capitalize()} is needed in: ")
    for i in il.values():
        for j in i.getInput().keys():
            if need_factory and i.nr_factories>0:
                if item_name == j:
                    inl.append(i.name)
            elif not need_factory:
                if item_name == j:
                    inl.append(i.name)
    if  (verbose and verbose_empty) or ( verbose  and not verbose_empty and len(inl)>0 ) :
        print(f"\n{item_name.capitalize()} is needed in {len(inl)}: ",end=" ")
        for i in inl:
            print(f"{i}", end=", ")
        # print("\n")
            
    return inl
def getListALLItemsWhereNeeded(il: dict[str, factorioItem],raw_resources_out: dict[str, float],need_factory=True,verbose = False,verbose_empty=False):
    icl:{str,float} = getItemConsumptionList(il)
    inl :{str,list}={}
    for key in icl.keys():
         
        inl.update({key:getItemsThatNeedX(key,il,need_factory=need_factory,verbose=verbose,verbose_empty = verbose_empty)})
    
    return inl

