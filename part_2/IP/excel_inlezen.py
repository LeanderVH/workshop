import xlrd
import json

def find_all_interfaces(xlf):

    wb = xlrd.open_workbook(xlf)
    sheet = wb.sheet_by_index(0)
    number_rows = sheet.nrows
    dev_interfaces = []
    for r in range(number_rows):
        if r > 0: ### first row contains columns names
            inventory_dict = {}
            COL_A =  sheet.cell_value(r, 0)  
            COL_B =  sheet.cell_value(r, 1)  
            COL_C =  sheet.cell_value(r, 2)  
            COL_D =  sheet.cell_value(r, 3)  
            COL_E =  sheet.cell_value(r, 4)  
            inventory_dict["device"]      = COL_A
            inventory_dict["role"]        = COL_B
            inventory_dict["interface"]   = COL_C 
            inventory_dict["ipaddress"]   = COL_D
            inventory_dict["subnetmask"]  = COL_E
            dev_interfaces.append(inventory_dict.copy()) 
    return dev_interfaces


def make_list_of_devices_and_roles(inventory):  
    dev_list  = []
    dev_dict  = {}
    mem       = {}
    for rec in inventory:
        dev_dict["dev_name"] = rec["device"]
        dev_dict["role"]     = rec["role"]
        if mem != dev_dict["dev_name"]:
            dev_list.append(dev_dict.copy())  
        mem = dev_dict["dev_name"]
    #for rec in loc_g:    
        #print(rec)
    #del loc_g[0] ### if last item copied as first item
    return dev_list


def attach_interfaces_to_devices(dev_name, inventory):    
    intf_dict = {}
    intf_list = [intf_dict]
    for item in inventory:
        if item["device"] == dev_name:
            if item["device"] != None:
                intf_dict["interface"]   = item["interface"]
                intf_dict["ipaddress"]   = item["ipaddress"]
                intf_dict["subnetmask"]  = item["subnetmask"]
                intf_list.append(intf_dict.copy())
    del intf_list[0] ### if last item copied as first item
    print(intf_list)
    return intf_list



def main():
    inventory_list = find_all_interfaces("ipdevices.xlsx")
    #print(inventory_list)
    device_list = make_list_of_devices_and_roles(inventory_list)
    #print(device_list)
    dev_dict = {}
    rack_struc = []      
    for device_rec in device_list:  
        intf_list  = attach_interfaces_to_devices(device_rec["dev_name"], inventory_list)
        dev_dict["device"] = { "device": device_rec , "interfaces": intf_list }
        rack_struc.append(dev_dict)
        print(dev_dict)
        print(rack_struc)
    print(dev_dict) 
    js_rack = json.dumps(rack_struc)


if __name__ == '__main__':
    main()