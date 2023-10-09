from os import system, path

filename = "items.csv"

def displayAllItems() -> None:
    system("cls")
    print("Display All Items")
    print("-------------------- ")
    message = "\nFile Not Found"
    item_totals = {}
    
    if path.exists(filename):
        f = open(filename, 'r')
        ilist = f.readlines()
        f.close()
        
        if len(ilist) > 0:
            print("{:<10} {:<20} {:<10} {:<5} {:<10}".format("Item Code", "Item Name", "Price", "Qty", "Total"))
            for item in ilist:
                item_info = item.strip().split(',')
                itemCode, itemName, price, qty = item_info
                price = float(price)
                qty = int(qty)
                item_total = price * qty
                
                if itemCode in item_totals:
                    item_totals[itemCode] += item_total
                else:
                    item_totals[itemCode] = item_total
                
                print("{:<10} {:<20} {:<10} {:<5} {:<10}".format(itemCode, itemName, price, qty, item_total))
            
            message = "Nothing Follows..."
        else:
            message = "\nThe list is empty!!"
    
    print(message)

def main() -> None:
    displayAllItems()

if __name__ == "__main__":
    main()
