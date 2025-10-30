
oil_output = 367.8

raw_oil_consume = 20
petrolium_out = 9



nr_oil_reg = round(oil_output/ raw_oil_consume)
curr_refinery = 10+4
nr_rigs_needed = nr_oil_reg - curr_refinery
total_petrolium_produce = curr_refinery*petrolium_out

# solid fuel
nr_solid_fuel_fac = 2 -2 # -2 because its not working for now
solid__petrolium_consume = 20
solid_produce = 1

total_solid = nr_solid_fuel_fac * solid_produce


# plastic
nr_plastic_fac = 4
plastic__petrolium_consume =20
pastic_coal_consume = 1
plastic_output = 2



# sulfur
nr_sulfur_fac = 4
sulfur_water =30
sulfur_petrolium = 30
sulfur_output = 2

# sulfuric acid
nr_sulfuric_acid_fac = 1
su_acid_iron_plate = 1
su_acid_sulfur = 5
su_acid_water = 100

su_acid_out = 50


# battery

nr_battery_fac = 1
battery_iron_plate = 0.25
battery_copper_plate = 0.25
battery_su_acid = 5

battery_out = 0.25


total_petrolium_consume = nr_plastic_fac*plastic__petrolium_consume + nr_solid_fuel_fac* solid__petrolium_consume  + nr_sulfur_fac * sulfur_petrolium


print(f"nr of oil ref required:  {nr_oil_reg},")
print(f"nr of oil rigs still neded:  {nr_rigs_needed} ")
print(f"total petrolium consumed: {total_petrolium_consume}")
print(f"total petrolium produced: {total_petrolium_produce}")

total_plastic = nr_plastic_fac * plastic_output
total_sulfur = nr_sulfur_fac * sulfur_output
total_sulfuric_acid = nr_sulfuric_acid_fac * su_acid_out
total_battery = nr_battery_fac * battery_out
print("\n\n\n")
# Add these print statements before the existing ones
print(f"Total plastic produced: {total_plastic}")
print(f"Total sulfur produced: {total_sulfur}")
print(f"Total sulfuric acid produced: {total_sulfuric_acid}")
print(f"Total batteries produced: {total_battery}")
print(f"Total solid fuel produced: {total_solid}")
