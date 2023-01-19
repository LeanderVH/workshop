import xlrd
import json



def find_all_persons_and_groups(xlf):
    wb = xlrd.open_workbook (xlf)
    sheet = wb.sheet_by_index(0)
    number_row = sheet.nrows
    all_members = []
    for r in range(number_row):
        if r > 0 :
            member_dict = {"person_name": "x", "email": "y", "group": "z"}
            COL_A = sheet.cell_value(r,0)
            COL_B = sheet.cell_value(r,1)
            COL_C = sheet.cell_value(r,2)
            member_dict["group"] = COL_A
            member_dict["person_name"] = COL_B
            member_dict["email"] = COL_C
            all_members.append(member_dict.copy())
    return all_members


def make_list_of_groups(membr_list):
    all_groups = []
    mem = None
    for rec in membr_list:
        g = rec["group"]
        if mem != g:
            all_groups.append(g)
        mem=g
    all_groups.pop()
    return all_groups



def attach_members_to_groups(group_name, membr_list):
    membr_dict = {}
    all_group_members = [membr_dict]
    for membr in membr_list:
        if membr["group"] == group_name:
            if membr["person_name"] != None:
                membr_dict["person_name"] = membr["person_name"]
                membr_dict["email"] = membr["email"]
                all_group_members.append(membr_dict.copy())
    return all_group_members


def main():
    member_list = find_all_persons_and_groups("webex_groups.xlsx")
    group_list = make_list_of_groups(member_list)
    all_members = []
    groups_struc = {}
    groups_struc["groups"] = []
    for group_rec in group_list:
        all_members = attach_members_to_groups(group_rec, member_list)
        del all_members[0]
        group_dict = {"group": {"group_name": group_rec, "members": all_members}}
        groups_struc["groups"].append(group_dict.copy())
    res = json.dumps(groups_struc)
    print(res)


if __name__ == '__main__':
    main()
