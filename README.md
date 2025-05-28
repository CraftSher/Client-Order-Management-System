![Project Banner](banner.png)

# Client Order Management System

A simple Python-based command-line application for managing and analyzing customer orders. This system allows users to view all orders, analyze client purchase behavior, and add new orders easily.

## Features

- **Display All Orders**: View the complete list of customer orders.  
- **Client Order Count**: Check how many orders a specific client has placed.  
- **Product Quantities**: See the total quantity ordered for each product.  
- **Top Clients**: Identify clients with the highest total number of items ordered.  
- **Add New Orders**: Add a new order by specifying client name, product, and quantity.

## How It Works

Orders are stored as a list of dictionaries, each representing one order with the following structure:

```python
{
    "client": "Client Name",
    "product": "Product Name",
    "quantity": number_of_items
}
```

## How to Run

Run the program from your terminal by executing:

```bash
python inventory_manager.py
```

## Example Usage

When running, the program shows a menu with options:

```
1 - Display all orders  
2 - Show how many orders a client has placed  
3 - Show how many items of each product were ordered  
4 - Show clients with the highest number of total items ordered  
5 - Add a new order  
0 - Exit
```

## Screenshot of Program Output

![Terminal Output](assets/output_terminal.png)

## Author

Created by CraftSher
