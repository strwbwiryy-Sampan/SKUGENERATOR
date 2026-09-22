from pyscript import display, document

def display_char(e):
   document.getElementById("output1").innerHTML = ""


   document.getElementById('div_id_here').innerHTML = " "

   Categories = document.getElementById("Categories")
   Product_Name = document.ElementById("Product Name")
   Stock_Quantity = document.ElementById("Stock Quantity")
 
 
 
 #Create the SKU variable using 
 SKU_name_here = category_variable[:3].upper() + "-" + product_name_variable[:4].upper() + "-" + str(stock_qty)

#Display the SKU
 display("SKU: ", SKU_name_here, target='div_id_here')