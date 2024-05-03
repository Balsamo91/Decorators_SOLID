# for (balance) I need to OVERWRITE the amount saved in amount.txt

def read_balance(balance_file):
    try:
        with open(balance_file, "r") as file:
            return float(file.read())# Read the content of the file and convert it to float
    # Handle FileNotFoundError by returning 0
    except FileNotFoundError:
        return 0
    # Handle ValueError by returning 0
    except ValueError:
        return 0

def write_balance(balance_file, account):
    try:
        with open(balance_file, "w") as file:
            file.write(str(account))# Write the account balance to the file
            file.close()# Close the file
            print("\nBalance updated in balance file.\n")
    # Handle any exception by printing an error message
    except Exception as e:
        print(f"\nError saving balance data: {e}")


# for (Warehouse) inventory I need to UPDATE/OVERWRITE the file warehouse.txt

def read_inventory(inventory_file):
    import json
    warehouse_list = []
    try:
        with open(inventory_file, "r") as file:
            # Iterate through each line in the file
            for line in file:
                try:
                    # Convert each line to a dictionary using JSON parsing
                    item = json.loads(line)
                    warehouse_list.append(item)
                except json.JSONDecodeError as e:
                    # Print an error message for JSON decoding errors
                    print(f"Error decoding line '{line.strip()}': {e}")
    except FileNotFoundError:
        print("Inventory file not found.")
    except Exception as e:
        print(f"Error reading inventory data: {e}")
    return warehouse_list


def write_inventory(inventory, warehouse_list):
    import json
    try:
        with open(inventory, "w") as file:
            # Iterate through each item in the warehouse_list
            for item in warehouse_list:
                # Write each dictionary as a JSON string on a separate line
                file.write(json.dumps(item) + '\n')
            file.close()
        print("Inventory updated in warehouse file.\n")
    except Exception as e:
        print(f"Error saving inventory: {e}")


# for (history) operations I need to APPEND every operations

def history(operations_recorded, history_file):

    try:
        with open(history_file, "a") as file:
            # Iterate through each operation recorded
            for h in operations_recorded:
                file.write(str(h) + "\n")# Write each operation to a new line in the file
            file.close()
    except Exception as e:
        print(f"Error saving history: {e}")

