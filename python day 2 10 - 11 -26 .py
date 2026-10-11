store_name= "mart,47"
manager_name= "ali hammad"
manager_age= 30
branch_name= "lahore dha rahber"
branch_code= 1125
#products
dalda= "2590,pkr"
chana= "450,pkr"
rice= "420,pkr"
sugar= "159,pkr"
olive_oil= "3850,pkr"
diapers= "1150,pkr"
#type castings
dalda = int("2590")
chana = int("450")
rice = int("420")
sugar = int("159")
olive_oil = int("3850")
diapers = int("1150")
#quantities
dalda_quantity= 10
chana_quantity= 20
rice_quantity= 15
sugar_quantity= 25
olive_oil_quantity= 5
diapers_quantity= 12
#discounts
first_coustomer_discount=100
#delivery
delivery_charges= 50

#retail to tge coustomer
totel_price_dalda= dalda-first_coustomer_discount+delivery_charges
totel_price_chana= chana-first_coustomer_discount+delivery_charges
totel_price_rice= rice-first_coustomer_discount+delivery_charges 
totel_price_sugar= sugar-first_coustomer_discount+delivery_charges
totel_price_olive_oil= olive_oil-first_coustomer_discount+delivery_charges
totel_price_diapers= diapers-first_coustomer_discount+delivery_charges       
#totel invenroy cost
totel_inventory_cost= dalda_quantity*dalda + chana_quantity*chana + rice_quantity*rice + sugar_quantity*sugar + olive_oil_quantity*olive_oil + diapers_quantity*diapers
#pringting process
print("store name: ", store_name)
print("manager name: ", manager_name)
print("manager age: ", manager_age)
print("branch name: ", branch_name)
print("branch code: ", branch_code)
print("dalda price: ", dalda, "pkr")
print("chana price: ", chana, "pkr")
print("rice price: ", rice, "pkr")
print("sugar price: ", sugar, "pkr")
print("olive oil price: ", olive_oil, "pkr")
print("diapers price: ", diapers, "pkr")
print("dalda quantity: ", dalda_quantity, "units")
print("chana quantity: ", chana_quantity, "units")
print("rice quantity: ", rice_quantity, "units")
print("sugar quantity: ", sugar_quantity, "units")
print("olive oil quantity: ", olive_oil_quantity, "units")
print("diapers quantity: ", diapers_quantity, "units")
print("total price: ", totel_price_dalda, "pkr")
print("total price: ", totel_price_chana, "pkr")
print("total price: ", totel_price_rice, "pkr")
print("total price: ", totel_price_sugar, "pkr")
print("total price: ", totel_price_olive_oil, "pkr")
print("total price: ", totel_price_diapers, "pkr")
print("total inventory cost: ", totel_inventory_cost, "pkr")