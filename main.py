from pyscript import display, document

def display_char(e):
   document.getElementById("output1").innerHTML = ""


   document.getElementById('div_id_here').innerHTML = " "

   Categories = document.getElementById("Categories")
   Product_Name = document.getElementById("Product Name")
   Stock_Quantity = document.ElementById("Stock Quantity")
 
   category_catergories = Categories.value
   product_name_variable = Product_Name.value
   stock_qty = Stock_Quantity.value
    
    def generate_sku(e):
     document.getElementById("output1").innerHTML = ""
     
         sku1 =   document.getElementById('Product Name')
         sku2 =   document.getElementById('Product Name').innerHTML = " "
         sku3 =   document.getElementById('Product Name').innerHTML = " "
         sku4 =   document.getElementById('Product Name').innerHTML = " "
         aku5 =   document.getElementById('Product Name').innerHTML = " "
      
   # Create the SKU variable using the form values.
   SKU_name_here = category_catergories[:3].upper() + "-" + product_name_variable[:4].upper() + "-" + str(stock_qty)

   # Display the SKU.
   display("SKU: ", SKU_name_here, target='div_id_here')