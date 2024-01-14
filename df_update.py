import pandas as pd
# check = "RC025"


def df_edit(check):
    path = r'overall_data.xlsx'
    df = pd.read_excel(path)
    li = df["CUSTOMER ID"]
    print(li)
    for index, i in enumerate(li):
        print("check.....", check)
        print("checkiiii.....", i)
        if str(i) == str(check):
            print("needed rows", df.iloc[index])
            date1 = df.iloc[index, 0]
            cus_id = df.iloc[index, 1]
            name = df.iloc[index, 2]
            ph_number = df.iloc[index, 3]
            address = df.iloc[index, 4]
            aathar_number = df.iloc[index, 5]
            vehicle_model = df.iloc[index, 6]
            vehicle_year = df.iloc[index, 7]
            rc_book = df.iloc[index, 8]
            noc_Details = df.iloc[index, 9]
            insurance_Details = df.iloc[index, 10]
            notes = df.iloc[index, 11]
            purchase_amt = df.iloc[index, 12]
            commission_amt = df.iloc[index, 13]
            sapre_spt_amt = df.iloc[index, 14]
            total_purchase_amt = df.iloc[index, 15]
            vehicle_num = df.iloc[index, 16]
            sel_date = df.iloc[index, 17]
            buy_name = df.iloc[index, 18]
            buy_num = df.iloc[index, 19]
            buy_adhaar = df.iloc[index, 20]
            buy_add = df.iloc[index, 21]
            buy_notes = df.iloc[index, 22]
            amt2buyer = df.iloc[index, 23]
            profit = df.iloc[index, 24]
            print("all the values are gotted")
            return [date1, cus_id, name, ph_number,address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num, sel_date, buy_name, buy_num, buy_adhaar, buy_add, buy_notes, amt2buyer, profit]
    return None


def df_edit_update(check,date1, cus_id, name, ph_number,address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num, sel_date, buy_name, buy_num, buy_adhaar, buy_add, buy_notes, amt2buyer, profit):
    path = r'overall_data.xlsx'
    df = pd.read_excel(path)
    df = df.fillna('')
    li = df["CUSTOMER ID"]  
    print("check",check)
    for index, i in enumerate(li):
        if str(i) == str(check):
            print("needed rows",df.iloc[index])
            df.iloc[index, 0]=date1
            df.iloc[index, 1]=cus_id
            df.iloc[index, 2]=name
            df.iloc[index, 3]=ph_number
            df.iloc[index, 4]=address
            df.iloc[index, 5]=aathar_number
            df.iloc[index, 6]=vehicle_model
            df.iloc[index, 7]=vehicle_year
            df.iloc[index, 8]=rc_book
            df.iloc[index, 9]=noc_Details
            df.iloc[index, 10]=insurance_Details
            df.iloc[index, 11]=notes
            df.iloc[index, 12]=purchase_amt
            df.iloc[index, 13]=commission_amt
            df.iloc[index, 14]=sapre_spt_amt
            df.iloc[index, 15]=total_purchase_amt
            df.iloc[index, 16]=vehicle_num
            df.iloc[index, 17]=sel_date
            df.iloc[index, 18]=buy_name
            df.iloc[index, 19]=buy_num
            df.iloc[index, 20]=buy_adhaar
            df.iloc[index, 21]=buy_add
            df.iloc[index, 22]=buy_notes
            df.iloc[index, 23]=amt2buyer
            df.iloc[index, 24]=profit
            print("profit.....",profit)
    # print(df.tail(2))
    path = r'overall_data.xlsx'
    with pd.ExcelWriter(path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # df = df.fillna('')
        df.to_excel(writer, sheet_name='from jan 2024', index=False)

if __name__ == "__main__":
    df_edit()
