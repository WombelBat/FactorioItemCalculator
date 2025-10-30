import json
from math import ceil

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
        self.method = dict(zip(method_name, method_time/100))
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
        for key,val in self.output.items(): 
            if verbose:
                print(f"{key} = {val} per second")

        return self.final_output


    def defineOUtput(self):
        for key,val in self.output.items(): 

            quanity_modifier = self.getQuantityMod()
            items =(val*quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( (self.time_req/self.method[ self.chosen_method ])* speed_modifier )

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
        for key,val in self.input.items(): 
            
            if verbose:
                print(f"{key} = {val} per second")

        return self.final_input
    

    def factoriesTOgetOutputX(self,output_wanted:float,verbose =False,output_name=""):
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:
            nec_out = output_wanted - self.getOutput()[output_name]
            
            quanity_modifier = self.getQuantityMod()
            items =(self.output[output_name] * quanity_modifier) 
            
            speed_modifier = self.getSpeedMod()
            time_nec =( (self.time_req/self.method[ self.chosen_method ])* speed_modifier )

            nec_fact = ceil(nec_out /items * time_nec)
            if verbose:
                print(f"To get {output_wanted} /sec {output_name} you need an extra: {nec_fact} {self.chosen_method} for a total of { nec_fact+self.nr_factories} ")
    
            return nec_fact
        
        print("output dosent exist")
        return
    
    def resourcesToGetOutputX(self,output_wanted:float,output_name="",verbose =False):
        if output_name =="":
            output_name = list(self.output.keys())
            output_name = output_name[0]
        if output_name in self.output:

            total_fact = self.nr_factories + self.factoriesTOgetOutputX(output_wanted,output_name)

            total_input={}
            if verbose:
                print(f"To get {output_wanted} /sec {output_name} using {self.chosen_method} you need: ")
            for key,val in self.input.items(): 

                speed_modifier = self.getSpeedMod()
                time_nec = ( (self.time_req/self.method[ self.chosen_method ]) * speed_modifier)
                                                                                                             
                total_input[key] = total_fact * val / time_nec

                if verbose:
                    print(f"{key}: {total_input[key] } /sec")
    
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