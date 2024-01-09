Practical 1 : Add Global Discount in Sales Order
-------------------------------------------------

1) Add a selection field named 'Discount Applies To' inside the Sales Order Form View.
   The default selection value of the field is Global and Order line.

2) After That Add Two Fields in Sales Order and Sale Order Line
	1. Discount Method: Selection field(Fixed and Percentage)
	2. Discount Amount: Float field

3) Add One Mandatory field 'Discount' in the Sales order form after the Total field.
   Based on selection get the discount amount.

4) In Discount Applies to Selection Field Select Orde Line Discount So Sale Order Line Two 
   Fields are Visible If Select The Global So Sale Order Two Fields are Visible.

5) In Report Also Same Above Condition Are Apply and After That Print Report Based on Condition.


Practical 2: Select the product category-based product
-------------------------------------------------------

1) Add One field product category(Many2one) before the product in the sales order line.

2) If the product category is selected then only that product category data is shown in the
   product dropdown.

3) If the Product category is not selected all products will be visible in the
   dropdown.


Practical 3: Search Customer
------------------------------

1) First of All Create New Model 'search.customer' with a Added 3 Fields 
		1. Customer_id(Customer) Many2one
		2. mobile(Char)
		3. phone(Char)

2) After That Create New Wizard Model 'search.customer.wizard' with a Added 3 Fields 
		1. Customer_id(Customer) Many2one
		2. mobile(Char)
		3. phone(Char)

3) Create the one-button 'Search Customer' when clicking on the button it redirects the
   contact view and shows customer details only.

4) Added New Button Special Cancel in Wizard.

5) Create the button 'Print Customer' When clicking on the button print the report of the customer
   data(Name, Image, Address, phone, mobile, email, website, and parent partner details).

   
Installed Module in Projects
---------------------------------
base, sale_management, contacts