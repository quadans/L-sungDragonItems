inv = {'gold coin': 42, 'rope': 1}
loot = ['ruby','gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):

	for i in range(len(addedItems)):
		
		if addedItems[i] in inventory:	
			inventory[addedItems[i]]+=1
	
		else:
			inventory.setdefault(addedItems[i],1)
	return inventory	

def displayInventory(drin):
	print("Inventory:")
	item_total = 0
	for k, v in drin.items():
		print(k,v)
		item_total+=v
	print("Total number of items: " + str(item_total))

inv = addToInventory(inv, loot)
displayInventory(inv)
