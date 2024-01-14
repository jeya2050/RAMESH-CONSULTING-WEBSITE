from flask import Flask, render_template, request, Response,send_file
from datetime import *
import os
import pandas as pd
# import openpyxl
from df_update import df_edit,df_edit_update
# date1, cus_id, name, ph_number, address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num,sel_date,buy_name,buy_num,buy_adhaar,buy_add,buy_notes,amt2buyer,profit=df_edit(check="RC025")

# print(date1)
# print(cus_id)
now = datetime.now()
Date = str(date.today())
Time = str(now.strftime("%H:%M:%S"))

app = Flask(__name__)
cwd = os.getcwd()
# print(cwd)
path = r'overall_data.xlsx'
df = pd.read_excel('overall_data.xlsx', sheet_name='from jan 2024')


def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    # dataframe = dataframe.applymap(lambda x: int(x) if pd.notna(x) and isinstance(x, (float, int)) else x)
    # dataframe = dataframe.astype(int,errors='ignore')
    dataframe = dataframe.fillna("nan")
    table_html = dataframe.to_html(table_id="table")
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html>
    <header>
    <title>Ramesh consulting</title>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body style="background-color:rgb(243, 233, 175);text-align:center;">
    <div class="head" style="text-align:center; margin-top: 25px;
            font-size: 30px;
            color: rgba(238, 52, 52, 0.867);
            font-weight: bold;"> RAMESH CONSULTING </div>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html


def excel_render():
    df = pd.read_excel('overall_data.xlsx', sheet_name='from jan 2024')
    html = generate_html(df)
    os.chdir(r"templates")
    open("excel_Data.html", "w").write(html)
    os.chdir(cwd)


# Pass the required route to the decorator.
@app.route("/")
def main_page():
    return render_template('mainpage.html')


@app.route('/DataSearch', methods=['POST', 'GET'])
def DataSearch():
    excel_render()
    return render_template('excel_Data.html')


@app.route('/DataAdd', methods=['POST', 'GET'])
def DataAdd():
    global cus_id
    df = pd.read_excel(path)
    len_df = len(df)
    # print(len_df)
    cus_id = str(f"RC0{len_df}")
    # print(cus_id)
    return render_template('data add.html', variable=cus_id)


@app.route('/Updatedata', methods=['POST', 'GET'])
def Updatedata():
    # if request.method == "POST":
        # cus_id1= str(request.form.get("cus_id1"))
    return render_template('update data.html')
    #     date1, cus_id, name, ph_number, address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num,sel_date,buy_name,buy_num,buy_adhaar,buy_add,buy_notes,amt2buyer,profit=df_edit(check=cus_id1)

    # return render_template('update data.html',date1=date1,cus_id=cus_id,name=name, ph_number=ph_number, address=address, aathar_number=aathar_number, vehicle_model=vehicle_model, vehicle_year=vehicle_year,rc_book=rc_book, noc_Details=noc_Details, insurance_Details=insurance_Details, notes=notes, purchase_amt=purchase_amt, commission_amt=commission_amt, sapre_spt_amt=sapre_spt_amt, total_purchase_amt=total_purchase_amt, vehicle_num=vehicle_num,sel_date=sel_date,buy_name=buy_name,buy_num=buy_num,buy_adhaar=buy_adhaar,buy_add=buy_add,buy_notes=buy_notes,amt2buyer=amt2buyer,profit=profit)
@app.route('/Updatedata1', methods=['POST', 'GET'])
def Updatedata1():
    if request.method == "POST":
        cus_id1= str(request.form.get("cus_id1"))
        redd=df_edit(check=cus_id1)
        date1, cus_id, name, ph_number, address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num,sel_date,buy_name,buy_num,buy_adhaar,buy_add,buy_notes,amt2buyer,profit=df_edit(check=cus_id1)
        # print("date......",date1)
    return render_template('update data.html',date1=date1,cus_id=cus_id,name=name, ph_number=ph_number, address=address, aathar_number=aathar_number, vehicle_model=vehicle_model, vehicle_year=vehicle_year,rc_book=rc_book, noc_Details=noc_Details, insurance_Details=insurance_Details, notes=notes, purchase_amt=purchase_amt, commission_amt=commission_amt, sapre_spt_amt=sapre_spt_amt, total_purchase_amt=total_purchase_amt, vehicle_num=vehicle_num,sel_date=sel_date,buy_name=buy_name,buy_num=buy_num,buy_adhaar=buy_adhaar,buy_add=buy_add,buy_notes=buy_notes,amt2buyer=amt2buyer,profit=profit)

@app.route('/download_excel', methods=['POST', 'GET'])
def download_excel():
    df=pd.read_excel("overall_data.xlsx")
    excel_file_path = 'RC_data.xlsx'
    df.to_excel(excel_file_path, index=False)

    # Send the file as a response
    return send_file(excel_file_path, as_attachment=True)
#    return render_template('mainpage.html')


@app.route('/save', methods=["GET", "POST"])
def fun_save():
    act_colums = df.shape[1]
    if request.method == "POST":
        date = str(request.form.get("i1"))
        cus_id= str(request.form.get("cus_id_label"))
        name = (str(request.form.get("i2"))).upper()
        ph_number = str(request.form.get("i3"))
        address = str(request.form.get("i4"))
        aathar_number = str(request.form.get("i5"))
        vehicle_model = str(request.form.get("i6"))
        vehicle_year = str(request.form.get("i7"))
        rc_book = str(request.form.get("i8"))
        noc_Details = str(request.form.get("i9"))
        insurance_Details = str(request.form.get("i10"))
        notes = str(request.form.get("i11"))
        purchase_amt = str(request.form.get("i12"))
        commission_amt = str(request.form.get("i13"))
        sapre_spt_amt = str(request.form.get("i14"))
        total_purchase_amt = str(request.form.get("i15"))
        vehicle_num = str(request.form.get("i16"))

        res = [date, cus_id ,name, ph_number, address, aathar_number, vehicle_num, vehicle_model, vehicle_year, rc_book, noc_Details,
               insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, " ", " ", " ", " ", " ", " ", " ", " "]
        if int(len(res)) == int(act_colums):
            path = r'overall_data.xlsx'
            with pd.ExcelWriter(path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df.loc[len(df)] = res

                df.to_excel(writer, sheet_name='from jan 2024', index=False)
            return f"Data uploaded please check.....customer name {name} and {ph_number}"
    return "data not stroed correctly try again"



@app.route('/save1', methods=["GET", "POST"])
def fun_save1():
    if request.method == "POST":
        date1 = str(request.form.get("i1"))
        cus_id= str(request.form.get("cus_id_label"))
        name = (str(request.form.get("i2"))).upper()
        ph_number = str(request.form.get("i3"))
        address = str(request.form.get("i4"))
        aathar_number = str(request.form.get("i5"))
        vehicle_model = str(request.form.get("i6"))
        vehicle_year = str(request.form.get("i7"))
        rc_book = str(request.form.get("i8"))
        noc_Details = str(request.form.get("i9"))
        insurance_Details = str(request.form.get("i10"))
        notes = str(request.form.get("i11"))
        purchase_amt = str(request.form.get("i12"))
        commission_amt = str(request.form.get("i13"))
        sapre_spt_amt = str(request.form.get("i14"))
        total_purchase_amt = str(request.form.get("i15"))
        vehicle_num = str(request.form.get("i16"))
        sel_date = str(request.form.get("i17"))
        buy_name = (str(request.form.get("i18"))).upper()
        buy_num = str(request.form.get("i19"))
        buy_adhaar = str(request.form.get("i20"))
        buy_add =str(request.form.get("i21"))
        buy_notes =str(request.form.get("i22"))
        amt2buyer = str(request.form.get("i23"))
        profit = str(request.form.get("i24"))
    df_edit_update(cus_id,date1, cus_id, name, ph_number,address, aathar_number, vehicle_model, vehicle_year, rc_book, noc_Details, insurance_Details, notes, purchase_amt, commission_amt, sapre_spt_amt, total_purchase_amt, vehicle_num, sel_date, buy_name, buy_num, buy_adhaar, buy_add, buy_notes, amt2buyer, profit)
    return "data update is done"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
