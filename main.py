from pyscript import display, document

def generate_sku(e):
    document.getElementById("output1").innerHTML = ""
    document.getElementById("SKU_result").innerHTML = ""


    category_variable = document.getElementById("Categories").value
    product_name_variable = document.getElementById("prodname").value
    stock_qty = document.getElementById("stkqty").value

    SKU_name = category_variable[:3].upper() + "-" + product_name_variable[:4].upper() + "-" + str(stock_qty)

    #Display SKU 
    display(f"SKU: {SKU_name}", target='SKU_result')