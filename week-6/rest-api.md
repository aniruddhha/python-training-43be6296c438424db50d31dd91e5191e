## APIs Required for CRM System

### Admin Resource
- Activate User -> PUT
- Deactivate User -> PUT
- login -> POST

### Customer Resource
- Create New Customer -> POST 
- Block Customer -> PUT
- Update Customer -> PUT
- Show Order History From customer_id -> GET
- Check mobile is availabe in database or not -> GET
- List Customers By Location -> GET
- List Customers By Age -> GET

### Order Resource
- Create New Order -> POST
- Update Order -> PUT
- Cancel Order -> PUT
- List Orders for perticular kitchen -> GET

### Menu Resource
- Create New Menu Item -> POST
- Update Menu Item -> PUT
- Delete Menu Item -> DELETE
- List Menu from name -> GET

### Promotion Resource
- Create New Promotion -> POST
- Update Promotion -> PUT
- Delete Promotion -> DELETE
- List All Promotions -> GET
- Send Promotion to Selected Customers -> POST
- Send Promotion to All Customers -> PUT
- Send Age Wise Promotion -> PUT
- Send Age Location Promotion -> PUT
- Send Promotion to top 10 customers -> PUT

