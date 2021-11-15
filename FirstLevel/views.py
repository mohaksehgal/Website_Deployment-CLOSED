from django.shortcuts import render
from .forms import UserForm, LoginForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
import pandas as pd
import numpy as np
import os
import warnings
import math
warnings.filterwarnings('ignore')

from .models import Employee
from .resources import EmployeeResources
from django.contrib import messages
from tablib import Dataset

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

# Create your views here.

# front Page
def index(request):
    return render(request, 'FirstLevel/index.html')

# Client Page
def clients(request):
    return render(request, 'FirstLevel/clients.html')

def vision(request):
    return render(request, 'FirstLevel/vision_mission.html')

def principle(request):
    return render(request, 'FirstLevel/principle.html')

def strength(request):
    return render(request, 'FirstLevel/strength.html')

def whatwedo(request):
    return render(request, 'FirstLevel/whatwedo.html')

# After Login- Logout redirect page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))

# for user register
def register(request):
    if request.method == 'POST':
        # taking all data from UserForm in user_form
        user_form = UserForm(data=request.POST)
        # checking the validity of user_form
        if user_form.is_valid():
            # saving the user form
            user = user_form.save()
            user.save()
            return HttpResponseRedirect(reverse('basic_app:after_register'))
        # if there will be an error
        else:
            user_form = UserForm()
            return render(request, 'FirstLevel/register.html', {'user_form': user_form, 'Error': 'MAKE SURE PASSWORD or EMAIL MATCHES!!!'})
    # for first initialisation of registration page
    else:
        user_form = UserForm()
    return render(request, 'FirstLevel/register.html', {'user_form': user_form})

# login form / login page

def user_login(request):
    # checking of login form
    D=''
    Incentive = 0
    excel_data = []
    excel_data2 = []
    excel_data3 = []
    excel_data4 = []
    excel_data5 = []
    excel_data6 = []
    C = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    Fixed_Payout_FOS = 0
    Incentive_Payout_FOS = 0
    Total_Salary_FOS = 0
    Final_Salary = 0
    FULLERTON_INCENTIVE_FOS = 0
    FULLERTON_FIXED_FOS = 0
    IDFC_HL_FIXED_FOS = 0
    IDFC_HL_INCENTIVE_FOS = 0

    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        # taking to username for the database
        username = request.POST.get('username')
        empp = request.POST.get('Emp_ID')
        # employee_status = request.POST.get("DESIGNATION")

        EE = Employee.objects.order_by('NAMES')
        for E in EE:
            employeeid = E.EMPLOYEE_ID
            if (empp != employeeid):
                continue
            else:
                D = E.DEPARTMENT
                Pro = E.PROCESS
                uu = username
                Emp_Status = E.DESIGNATION
                Salary = E.SALARY
                print(D,Pro,uu,Emp_Status)

                global DEP
                def DEP():
                    return (D)
                global COMPANY_PROCESS
                def COMPANY_PROCESS():
                    return (Pro)
                global Employee_Login_name
                def Employee_Login_name():
                    return(uu)
                global Employee_Designation
                def Employee_Designation():
                    return(Emp_Status)

                global SALARY
                def SALARY():
                    return (Salary)

                if (Emp_Status == 'TC') or (Emp_Status == 'FOS'):
                    if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
                        if os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary).xlsx')):
                            if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')):
                                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx')):
                                    fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    AA1 = pd.read_excel(AA)
                                    AA2 = pd.read_excel(AA2)
                                    AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    AA5 = pd.read_excel(AA5)
                                    AA6 = pd.read_excel(AA6)


                                    AA1['FINAL PAYOUT'] = AA1['PAYOUT']+AA1['RB_PAYOUT']

                                    AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    for j in range(0, len(AA['TC NAME'])):
                                        if AA.loc[j,'TC NAME']==uu:
                                            Incentive = AA.loc[j,'FINAL PAYOUT']
                                        else:
                                            continue

                                    C = list(AA1.columns)

                                    for j in range(0, len(AA1[C[0]])):
                                        if AA1.loc[j, 'TC NAME'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C)):
                                                row_data.append(str(AA1.loc[j, C[col]]))
                                        else:
                                            continue
                                        excel_data.append(row_data)

                                    C2 = list(AA2.columns)
                                    C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    C5 = list(AA5.columns)
                                    C6 = list(AA6.columns)

                                    for j in range(0, len(AA2[C2[0]])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C2)):
                                                row_data.append(str(AA2.loc[j, C2[col]]))
                                        else:
                                            continue
                                        excel_data2.append(row_data)

                                    for j in range(0, len(AA3[C3[0]])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C3)):
                                                row_data.append(str(AA3.loc[j, C3[col]]))
                                        else:
                                            continue
                                        excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    for j in range(0, len(AA5[C5[0]])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C5)):
                                                row_data.append(str(AA5.loc[j, C5[col]]))
                                        else:
                                            continue
                                        excel_data5.append(row_data)

                                    for j in range(0, len(AA6[C6[0]])):
                                        if AA6.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C6)):
                                                row_data.append(str(AA6.loc[j, C6[col]]))
                                        else:
                                            continue
                                        excel_data6.append(row_data)

                                    AA5['INCENTIVE'] = AA5['PER PAID CASE']+AA5['RB PAYOUT']

                                    AA2['RB_INCENTIVE'].fillna(0,inplace=True)

                                    AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    for j in range(0, len(AA2['ALLOCATED FOS'])):
                                        if AA2.loc[j,'ALLOCATED FOS'] in Incentive_FOS:
                                            for k in range(0,len(AA3['FINAL PAID FOS'])):
                                                if AA2.loc[j,'ALLOCATED FOS'] == AA3.loc[k,'FINAL PAID FOS']:
                                                    if AA2.loc[j,'ALLOCATED FOS'] == uu:
                                                        Fixed_Payout_FOS = AA2.loc[j,'FINAL PAYOUT']
                                                        Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                        # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                    else:
                                                        continue
                                        elif AA2.loc[j,'ALLOCATED FOS'] not in Incentive_FOS:
                                            if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                Fixed_Payout_FOS = AA2.loc[j,'FINAL PAYOUT']
                                                # Total_Salary_FOS = Fixed_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA3['FINAL PAID FOS'])):
                                        if AA3.loc[j,'FINAL PAID FOS'] not in Fixed_FOS:
                                            if AA3.loc[j,'FINAL PAID FOS'] == uu:
                                                Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                # Total_Salary_FOS = Incentive_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0,len(AA4['FOS'])):
                                        if AA4.loc[j,'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j,'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j,'FIXED_PAYOUT']
                                        else:
                                            continue

                                    for j in range(0,len(AA5['FOS'])):
                                        if AA5.loc[j,'FOS'] == uu:
                                            IDFC_HL_INCENTIVE_FOS = AA5.loc[j,'INCENTIVE']
                                            IDFC_HL_FIXED_FOS = AA5.loc[j,'FIXED SALARY']
                                        else:
                                            continue
                                else:
                                    fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    AA1 = pd.read_excel(AA)
                                    AA2 = pd.read_excel(AA2)
                                    AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    # AA5 = pd.read_excel(AA5)
                                    # AA6 = pd.read_excel(AA6)

                                    AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    for j in range(0, len(AA['TC NAME'])):
                                        if AA.loc[j, 'TC NAME'] == uu:
                                            Incentive = AA.loc[j, 'FINAL PAYOUT']
                                        else:
                                            continue

                                    C = list(AA1.columns)

                                    for j in range(0, len(AA1[C[0]])):
                                        if AA1.loc[j, 'TC NAME'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C)):
                                                row_data.append(str(AA1.loc[j, C[col]]))
                                        else:
                                            continue
                                        excel_data.append(row_data)

                                    C2 = list(AA2.columns)
                                    C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    # C5 = list(AA5.columns)
                                    # C6 = list(AA6.columns)

                                    for j in range(0, len(AA2[C2[0]])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C2)):
                                                row_data.append(str(AA2.loc[j, C2[col]]))
                                        else:
                                            continue
                                        excel_data2.append(row_data)

                                    for j in range(0, len(AA3[C3[0]])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C3)):
                                                row_data.append(str(AA3.loc[j, C3[col]]))
                                        else:
                                            continue
                                        excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    # for j in range(0, len(AA5[C5[0]])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C5)):
                                    #             row_data.append(str(AA5.loc[j, C5[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data5.append(row_data)
                                    #
                                    # for j in range(0, len(AA6[C6[0]])):
                                    #     if AA6.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C6)):
                                    #             row_data.append(str(AA6.loc[j, C6[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data6.append(row_data)

                                    # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                    AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                    AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    for j in range(0, len(AA2['ALLOCATED FOS'])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                            for k in range(0, len(AA3['FINAL PAID FOS'])):
                                                if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                                    if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                        Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                        Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                        # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                    else:
                                                        continue
                                        elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                            if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                # Total_Salary_FOS = Fixed_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA3['FINAL PAID FOS'])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                            if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                                Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                # Total_Salary_FOS = Incentive_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA4['FOS'])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                        else:
                                            continue

                                    # for j in range(0, len(AA5['FOS'])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                    #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                    #     else:
                                    #         continue
                            else:
                                fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                # fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                # AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                AA1 = pd.read_excel(AA)
                                AA2 = pd.read_excel(AA2)
                                AA3 = pd.read_excel(AA3)
                                # AA4 = pd.read_excel(AA4)
                                # AA5 = pd.read_excel(AA5)
                                # AA6 = pd.read_excel(AA6)

                                AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                for j in range(0, len(AA['TC NAME'])):
                                    if AA.loc[j, 'TC NAME'] == uu:
                                        Incentive = AA.loc[j, 'FINAL PAYOUT']
                                    else:
                                        continue

                                C = list(AA1.columns)

                                for j in range(0, len(AA1[C[0]])):
                                    if AA1.loc[j, 'TC NAME'] == uu:
                                        row_data = list()
                                        for col in range(0, len(C)):
                                            row_data.append(str(AA1.loc[j, C[col]]))
                                    else:
                                        continue
                                    excel_data.append(row_data)

                                C2 = list(AA2.columns)
                                C3 = list(AA3.columns)
                                # C4 = list(AA4.columns)
                                # C5 = list(AA5.columns)
                                # C6 = list(AA6.columns)

                                for j in range(0, len(AA2[C2[0]])):
                                    if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                        row_data = list()
                                        for col in range(0, len(C2)):
                                            row_data.append(str(AA2.loc[j, C2[col]]))
                                    else:
                                        continue
                                    excel_data2.append(row_data)

                                for j in range(0, len(AA3[C3[0]])):
                                    if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                        row_data = list()
                                        for col in range(0, len(C3)):
                                            row_data.append(str(AA3.loc[j, C3[col]]))
                                    else:
                                        continue
                                    excel_data3.append(row_data)

                                # for j in range(0, len(AA4[C4[0]])):
                                #     if AA4.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C4)):
                                #             row_data.append(str(AA4.loc[j, C4[col]]))
                                #     else:
                                #         continue
                                #     excel_data4.append(row_data)

                                # for j in range(0, len(AA5[C5[0]])):
                                #     if AA5.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C5)):
                                #             row_data.append(str(AA5.loc[j, C5[col]]))
                                #     else:
                                #         continue
                                #     excel_data5.append(row_data)
                                #
                                # for j in range(0, len(AA6[C6[0]])):
                                #     if AA6.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C6)):
                                #             row_data.append(str(AA6.loc[j, C6[col]]))
                                #     else:
                                #         continue
                                #     excel_data6.append(row_data)

                                # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                for j in range(0, len(AA2['ALLOCATED FOS'])):
                                    if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                        for k in range(0, len(AA3['FINAL PAID FOS'])):
                                            if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                                if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                    Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                    Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                    # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                else:
                                                    continue
                                    elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                            # Total_Salary_FOS = Fixed_Payout_FOS
                                        else:
                                            continue
                                    else:
                                        continue

                                for j in range(0, len(AA3['FINAL PAID FOS'])):
                                    if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                            # Total_Salary_FOS = Incentive_Payout_FOS
                                        else:
                                            continue
                                    else:
                                        continue

                                # for j in range(0, len(AA4['FOS'])):
                                #     if AA4.loc[j, 'FOS'] == uu:
                                #         FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                #         FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                #     else:
                                #         continue

                                # for j in range(0, len(AA5['FOS'])):
                                #     if AA5.loc[j, 'FOS'] == uu:
                                #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                #     else:
                                #         continue
                        else:
                            fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                            # fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                            # fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                            # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                            AA = fs.open('IDFC_TW TC Incentive.xlsx')
                            # AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                            # AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                            # AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                            # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                            # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                            AA1 = pd.read_excel(AA)
                            # AA2 = pd.read_excel(AA2)
                            # AA3 = pd.read_excel(AA3)
                            # AA4 = pd.read_excel(AA4)
                            # AA5 = pd.read_excel(AA5)
                            # AA6 = pd.read_excel(AA6)

                            AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                            AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                            for j in range(0, len(AA['TC NAME'])):
                                if AA.loc[j, 'TC NAME'] == uu:
                                    Incentive = AA.loc[j, 'FINAL PAYOUT']
                                else:
                                    continue

                            C = list(AA1.columns)

                            for j in range(0, len(AA1[C[0]])):
                                if AA1.loc[j, 'TC NAME'] == uu:
                                    row_data = list()
                                    for col in range(0, len(C)):
                                        row_data.append(str(AA1.loc[j, C[col]]))
                                else:
                                    continue
                                excel_data.append(row_data)

                            # C2 = list(AA2.columns)
                            # C3 = list(AA3.columns)
                            # C4 = list(AA4.columns)
                            # C5 = list(AA5.columns)
                            # C6 = list(AA6.columns)

                            # for j in range(0, len(AA2[C2[0]])):
                            #     if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                            #         row_data = list()
                            #         for col in range(0, len(C2)):
                            #             row_data.append(str(AA2.loc[j, C2[col]]))
                            #     else:
                            #         continue
                            #     excel_data2.append(row_data)
                            #
                            # for j in range(0, len(AA3[C3[0]])):
                            #     if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                            #         row_data = list()
                            #         for col in range(0, len(C3)):
                            #             row_data.append(str(AA3.loc[j, C3[col]]))
                            #     else:
                            #         continue
                            #     excel_data3.append(row_data)

                            # for j in range(0, len(AA4[C4[0]])):
                            #     if AA4.loc[j, 'FOS'] == uu:
                            #         row_data = list()
                            #         for col in range(0, len(C4)):
                            #             row_data.append(str(AA4.loc[j, C4[col]]))
                            #     else:
                            #         continue
                            #     excel_data4.append(row_data)

                            # for j in range(0, len(AA5[C5[0]])):
                            #     if AA5.loc[j, 'FOS'] == uu:
                            #         row_data = list()
                            #         for col in range(0, len(C5)):
                            #             row_data.append(str(AA5.loc[j, C5[col]]))
                            #     else:
                            #         continue
                            #     excel_data5.append(row_data)
                            #
                            # for j in range(0, len(AA6[C6[0]])):
                            #     if AA6.loc[j, 'FOS'] == uu:
                            #         row_data = list()
                            #         for col in range(0, len(C6)):
                            #             row_data.append(str(AA6.loc[j, C6[col]]))
                            #     else:
                            #         continue
                            #     excel_data6.append(row_data)

                            # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                            # AA2['RB_INCENTIVE'].fillna(0, inplace=True)
                            #
                            # AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                            # AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                            # AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                            # Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                            # Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                            # for j in range(0, len(AA2['ALLOCATED FOS'])):
                            #     if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                            #         for k in range(0, len(AA3['FINAL PAID FOS'])):
                            #             if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                            #                 if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                            #                     Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                            #                     Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                            #                     # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                            #                 else:
                            #                     continue
                            #     elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                            #         if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                            #             Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                            #             # Total_Salary_FOS = Fixed_Payout_FOS
                            #         else:
                            #             continue
                            #     else:
                            #         continue
                            #
                            # for j in range(0, len(AA3['FINAL PAID FOS'])):
                            #     if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                            #         if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                            #             Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                            #             # Total_Salary_FOS = Incentive_Payout_FOS
                            #         else:
                            #             continue
                            #     else:
                            #         continue

                            # for j in range(0, len(AA4['FOS'])):
                            #     if AA4.loc[j, 'FOS'] == uu:
                            #         FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                            #         FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                            #     else:
                            #         continue

                            # for j in range(0, len(AA5['FOS'])):
                            #     if AA5.loc[j, 'FOS'] == uu:
                            #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                            #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                            #     else:
                            #         continue
                    else:
                        if os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary).xlsx')):
                            if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')):
                                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx')):
                                    # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    # AA1 = pd.read_excel(AA)
                                    AA2 = pd.read_excel(AA2)
                                    AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    AA5 = pd.read_excel(AA5)
                                    AA6 = pd.read_excel(AA6)

                                    # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    # for j in range(0, len(AA['TC NAME'])):
                                    #     if AA.loc[j, 'TC NAME'] == uu:
                                    #         Incentive = AA.loc[j, 'FINAL PAYOUT']
                                    #     else:
                                    #         continue
                                    #
                                    # C = list(AA1.columns)

                                    # for j in range(0, len(AA1[C[0]])):
                                    #     if AA1.loc[j, 'TC NAME'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C)):
                                    #             row_data.append(str(AA1.loc[j, C[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data.append(row_data)

                                    C2 = list(AA2.columns)
                                    C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    C5 = list(AA5.columns)
                                    C6 = list(AA6.columns)

                                    for j in range(0, len(AA2[C2[0]])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C2)):
                                                row_data.append(str(AA2.loc[j, C2[col]]))
                                        else:
                                            continue
                                        excel_data2.append(row_data)

                                    for j in range(0, len(AA3[C3[0]])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C3)):
                                                row_data.append(str(AA3.loc[j, C3[col]]))
                                        else:
                                            continue
                                        excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    for j in range(0, len(AA5[C5[0]])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C5)):
                                                row_data.append(str(AA5.loc[j, C5[col]]))
                                        else:
                                            continue
                                        excel_data5.append(row_data)

                                    for j in range(0, len(AA6[C6[0]])):
                                        if AA6.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C6)):
                                                row_data.append(str(AA6.loc[j, C6[col]]))
                                        else:
                                            continue
                                        excel_data6.append(row_data)

                                    AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                    AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                    AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    for j in range(0, len(AA2['ALLOCATED FOS'])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                            for k in range(0, len(AA3['FINAL PAID FOS'])):
                                                if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                                    if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                        Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                        Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                        # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                    else:
                                                        continue
                                        elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                            if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                # Total_Salary_FOS = Fixed_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA3['FINAL PAID FOS'])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                            if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                                Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                # Total_Salary_FOS = Incentive_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA4['FOS'])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                        else:
                                            continue

                                    for j in range(0, len(AA5['FOS'])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                            IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                        else:
                                            continue
                                else:
                                    # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    # AA1 = pd.read_excel(AA)
                                    AA2 = pd.read_excel(AA2)
                                    AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    # AA5 = pd.read_excel(AA5)
                                    # AA6 = pd.read_excel(AA6)

                                    # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    for j in range(0, len(AA['TC NAME'])):
                                        if AA.loc[j, 'TC NAME'] == uu:
                                            Incentive = AA.loc[j, 'FINAL PAYOUT']
                                        else:
                                            continue

                                    # C = list(AA1.columns)

                                    # for j in range(0, len(AA1[C[0]])):
                                    #     if AA1.loc[j, 'TC NAME'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C)):
                                    #             row_data.append(str(AA1.loc[j, C[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data.append(row_data)

                                    C2 = list(AA2.columns)
                                    C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    # C5 = list(AA5.columns)
                                    # C6 = list(AA6.columns)

                                    for j in range(0, len(AA2[C2[0]])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C2)):
                                                row_data.append(str(AA2.loc[j, C2[col]]))
                                        else:
                                            continue
                                        excel_data2.append(row_data)

                                    for j in range(0, len(AA3[C3[0]])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C3)):
                                                row_data.append(str(AA3.loc[j, C3[col]]))
                                        else:
                                            continue
                                        excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    # for j in range(0, len(AA5[C5[0]])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C5)):
                                    #             row_data.append(str(AA5.loc[j, C5[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data5.append(row_data)
                                    #
                                    # for j in range(0, len(AA6[C6[0]])):
                                    #     if AA6.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C6)):
                                    #             row_data.append(str(AA6.loc[j, C6[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data6.append(row_data)

                                    # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                    AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                    AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    for j in range(0, len(AA2['ALLOCATED FOS'])):
                                        if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                            for k in range(0, len(AA3['FINAL PAID FOS'])):
                                                if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                                    if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                        Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                        Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                        # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                    else:
                                                        continue
                                        elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                            if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                # Total_Salary_FOS = Fixed_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA3['FINAL PAID FOS'])):
                                        if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                            if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                                Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                # Total_Salary_FOS = Incentive_Payout_FOS
                                            else:
                                                continue
                                        else:
                                            continue

                                    for j in range(0, len(AA4['FOS'])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                        else:
                                            continue

                                    # for j in range(0, len(AA5['FOS'])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                    #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                    #     else:
                                    #         continue
                            else:
                                # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                # fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                # AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                # AA1 = pd.read_excel(AA)
                                AA2 = pd.read_excel(AA2)
                                AA3 = pd.read_excel(AA3)
                                # AA4 = pd.read_excel(AA4)
                                # AA5 = pd.read_excel(AA5)
                                # AA6 = pd.read_excel(AA6)

                                # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                # for j in range(0, len(AA['TC NAME'])):
                                #     if AA.loc[j, 'TC NAME'] == uu:
                                #         Incentive = AA.loc[j, 'FINAL PAYOUT']
                                #     else:
                                #         continue

                                # C = list(AA1.columns)

                                # for j in range(0, len(AA1[C[0]])):
                                #     if AA1.loc[j, 'TC NAME'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C)):
                                #             row_data.append(str(AA1.loc[j, C[col]]))
                                #     else:
                                #         continue
                                #     excel_data.append(row_data)

                                C2 = list(AA2.columns)
                                C3 = list(AA3.columns)
                                # C4 = list(AA4.columns)
                                # C5 = list(AA5.columns)
                                # C6 = list(AA6.columns)

                                for j in range(0, len(AA2[C2[0]])):
                                    if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                        row_data = list()
                                        for col in range(0, len(C2)):
                                            row_data.append(str(AA2.loc[j, C2[col]]))
                                    else:
                                        continue
                                    excel_data2.append(row_data)

                                for j in range(0, len(AA3[C3[0]])):
                                    if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                        row_data = list()
                                        for col in range(0, len(C3)):
                                            row_data.append(str(AA3.loc[j, C3[col]]))
                                    else:
                                        continue
                                    excel_data3.append(row_data)

                                # for j in range(0, len(AA4[C4[0]])):
                                #     if AA4.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C4)):
                                #             row_data.append(str(AA4.loc[j, C4[col]]))
                                #     else:
                                #         continue
                                #     excel_data4.append(row_data)
                                #
                                # for j in range(0, len(AA5[C5[0]])):
                                #     if AA5.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C5)):
                                #             row_data.append(str(AA5.loc[j, C5[col]]))
                                #     else:
                                #         continue
                                #     excel_data5.append(row_data)

                                # for j in range(0, len(AA6[C6[0]])):
                                #     if AA6.loc[j, 'FOS'] == uu:
                                #         row_data = list()
                                #         for col in range(0, len(C6)):
                                #             row_data.append(str(AA6.loc[j, C6[col]]))
                                #     else:
                                #         continue
                                #     excel_data6.append(row_data)

                                # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                for j in range(0, len(AA2['ALLOCATED FOS'])):
                                    if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                        for k in range(0, len(AA3['FINAL PAID FOS'])):
                                            if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                                if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                                    Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                                    Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                                    # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                                else:
                                                    continue
                                    elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                        if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                            Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                            # Total_Salary_FOS = Fixed_Payout_FOS
                                        else:
                                            continue
                                    else:
                                        continue

                                for j in range(0, len(AA3['FINAL PAID FOS'])):
                                    if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                        if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                            Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                            # Total_Salary_FOS = Incentive_Payout_FOS
                                        else:
                                            continue
                                    else:
                                        continue

                                # for j in range(0, len(AA4['FOS'])):
                                #     if AA4.loc[j, 'FOS'] == uu:
                                #         FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                #         FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                #     else:
                                #         continue
                                #
                                # for j in range(0, len(AA5['FOS'])):
                                #     if AA5.loc[j, 'FOS'] == uu:
                                #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                #     else:
                                #         continue
                        else:
                            if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')):
                                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx')):
                                    # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    # fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    # AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    # AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    # AA1 = pd.read_excel(AA)
                                    # AA2 = pd.read_excel(AA2)
                                    # AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    AA5 = pd.read_excel(AA5)
                                    AA6 = pd.read_excel(AA6)

                                    # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    # for j in range(0, len(AA['TC NAME'])):
                                    #     if AA.loc[j, 'TC NAME'] == uu:
                                    #         Incentive = AA.loc[j, 'FINAL PAYOUT']
                                    #     else:
                                    #         continue
                                    #
                                    # C = list(AA1.columns)

                                    # for j in range(0, len(AA1[C[0]])):
                                    #     if AA1.loc[j, 'TC NAME'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C)):
                                    #             row_data.append(str(AA1.loc[j, C[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data.append(row_data)

                                    # C2 = list(AA2.columns)
                                    # C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    C5 = list(AA5.columns)
                                    C6 = list(AA6.columns)

                                    # for j in range(0, len(AA2[C2[0]])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C2)):
                                    #             row_data.append(str(AA2.loc[j, C2[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data2.append(row_data)
                                    #
                                    # for j in range(0, len(AA3[C3[0]])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C3)):
                                    #             row_data.append(str(AA3.loc[j, C3[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    for j in range(0, len(AA5[C5[0]])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C5)):
                                                row_data.append(str(AA5.loc[j, C5[col]]))
                                        else:
                                            continue
                                        excel_data5.append(row_data)

                                    for j in range(0, len(AA6[C6[0]])):
                                        if AA6.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C6)):
                                                row_data.append(str(AA6.loc[j, C6[col]]))
                                        else:
                                            continue
                                        excel_data6.append(row_data)

                                    AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                    # AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                    # AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    # AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    # AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    # Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    # Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    # for j in range(0, len(AA2['ALLOCATED FOS'])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                    #         for k in range(0, len(AA3['FINAL PAID FOS'])):
                                    #             if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                    #                 if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #                     Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #                     Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #                     # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                    #                 else:
                                    #                     continue
                                    #     elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                    #         if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #             Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #             # Total_Salary_FOS = Fixed_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue
                                    #
                                    # for j in range(0, len(AA3['FINAL PAID FOS'])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                    #         if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #             Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #             # Total_Salary_FOS = Incentive_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue

                                    for j in range(0, len(AA4['FOS'])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                        else:
                                            continue

                                    for j in range(0, len(AA5['FOS'])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                            IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                        else:
                                            continue
                                else:
                                    # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    # fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    # fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    # AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    # AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    # AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    # AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    # AA1 = pd.read_excel(AA)
                                    # AA2 = pd.read_excel(AA2)
                                    # AA3 = pd.read_excel(AA3)
                                    AA4 = pd.read_excel(AA4)
                                    # AA5 = pd.read_excel(AA5)
                                    # AA6 = pd.read_excel(AA6)

                                    # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    # for j in range(0, len(AA['TC NAME'])):
                                    #     if AA.loc[j, 'TC NAME'] == uu:
                                    #         Incentive = AA.loc[j, 'FINAL PAYOUT']
                                    #     else:
                                    #         continue
                                    #
                                    # C = list(AA1.columns)

                                    # for j in range(0, len(AA1[C[0]])):
                                    #     if AA1.loc[j, 'TC NAME'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C)):
                                    #             row_data.append(str(AA1.loc[j, C[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data.append(row_data)

                                    # C2 = list(AA2.columns)
                                    # C3 = list(AA3.columns)
                                    C4 = list(AA4.columns)
                                    # C5 = list(AA5.columns)
                                    # C6 = list(AA6.columns)

                                    # for j in range(0, len(AA2[C2[0]])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C2)):
                                    #             row_data.append(str(AA2.loc[j, C2[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data2.append(row_data)

                                    # for j in range(0, len(AA3[C3[0]])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C3)):
                                    #             row_data.append(str(AA3.loc[j, C3[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data3.append(row_data)

                                    for j in range(0, len(AA4[C4[0]])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C4)):
                                                row_data.append(str(AA4.loc[j, C4[col]]))
                                        else:
                                            continue
                                        excel_data4.append(row_data)

                                    # for j in range(0, len(AA5[C5[0]])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C5)):
                                    #             row_data.append(str(AA5.loc[j, C5[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data5.append(row_data)
                                    #
                                    # for j in range(0, len(AA6[C6[0]])):
                                    #     if AA6.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C6)):
                                    #             row_data.append(str(AA6.loc[j, C6[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data6.append(row_data)
                                    #
                                    # AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']
                                    #
                                    # AA2['RB_INCENTIVE'].fillna(0, inplace=True)
                                    #
                                    # AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']
                                    #
                                    # AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    # AA3 = pd.DataFrame(
                                    #     AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()
                                    #
                                    # Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    # Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())
                                    #
                                    # for j in range(0, len(AA2['ALLOCATED FOS'])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                    #         for k in range(0, len(AA3['FINAL PAID FOS'])):
                                    #             if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                    #                 if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #                     Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #                     Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #                     # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                    #                 else:
                                    #                     continue
                                    #     elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                    #         if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #             Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #             # Total_Salary_FOS = Fixed_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue
                                    #
                                    # for j in range(0, len(AA3['FINAL PAID FOS'])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                    #         if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #             Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #             # Total_Salary_FOS = Incentive_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue

                                    for j in range(0, len(AA4['FOS'])):
                                        if AA4.loc[j, 'FOS'] == uu:
                                            FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                            FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                        else:
                                            continue

                                    # for j in range(0, len(AA5['FOS'])):
                                    #     if AA5.loc[j, 'FOS'] == uu:
                                    #         IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                    #         IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                    #     else:
                                    #         continue
                            else:
                                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx')):
                                    # fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                                    # fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                                    # fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                                    fs4 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')

                                    # AA = fs.open('IDFC_TW TC Incentive.xlsx')
                                    # AA2 = fs1.open('PER PAID CASE(Including Fixed Salary).xlsx')
                                    # AA3 = fs1.open('PER PAID CASE(PIVOT).xlsx')
                                    # AA4 = fs3.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                                    AA5 = fs4.open('FINAL PAYOUT IDFC-HL.xlsx')
                                    AA6 = fs4.open('BKT-WISE PAYOUT.xlsx')

                                    # AA1 = pd.read_excel(AA)
                                    # AA2 = pd.read_excel(AA2)
                                    # AA3 = pd.read_excel(AA3)
                                    # AA4 = pd.read_excel(AA4)
                                    AA5 = pd.read_excel(AA5)
                                    AA6 = pd.read_excel(AA6)

                                    # AA1['FINAL PAYOUT'] = AA1['PAYOUT'] + AA1['RB_PAYOUT']

                                    # AA = pd.DataFrame(AA1.groupby('TC NAME')['FINAL PAYOUT'].sum()).reset_index()

                                    # for j in range(0, len(AA['TC NAME'])):
                                    #     if AA.loc[j, 'TC NAME'] == uu:
                                    #         Incentive = AA.loc[j, 'FINAL PAYOUT']
                                    #     else:
                                    #         continue
                                    #
                                    # C = list(AA1.columns)

                                    # for j in range(0, len(AA1[C[0]])):
                                    #     if AA1.loc[j, 'TC NAME'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C)):
                                    #             row_data.append(str(AA1.loc[j, C[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data.append(row_data)

                                    # C2 = list(AA2.columns)
                                    # C3 = list(AA3.columns)
                                    # C4 = list(AA4.columns)
                                    C5 = list(AA5.columns)
                                    C6 = list(AA6.columns)

                                    # for j in range(0, len(AA2[C2[0]])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C2)):
                                    #             row_data.append(str(AA2.loc[j, C2[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data2.append(row_data)
                                    #
                                    # for j in range(0, len(AA3[C3[0]])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C3)):
                                    #             row_data.append(str(AA3.loc[j, C3[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data3.append(row_data)

                                    # for j in range(0, len(AA4[C4[0]])):
                                    #     if AA4.loc[j, 'FOS'] == uu:
                                    #         row_data = list()
                                    #         for col in range(0, len(C4)):
                                    #             row_data.append(str(AA4.loc[j, C4[col]]))
                                    #     else:
                                    #         continue
                                    #     excel_data4.append(row_data)

                                    for j in range(0, len(AA5[C5[0]])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C5)):
                                                row_data.append(str(AA5.loc[j, C5[col]]))
                                        else:
                                            continue
                                        excel_data5.append(row_data)

                                    for j in range(0, len(AA6[C6[0]])):
                                        if AA6.loc[j, 'FOS'] == uu:
                                            row_data = list()
                                            for col in range(0, len(C6)):
                                                row_data.append(str(AA6.loc[j, C6[col]]))
                                        else:
                                            continue
                                        excel_data6.append(row_data)

                                    AA5['INCENTIVE'] = AA5['PER PAID CASE'] + AA5['RB PAYOUT']

                                    # AA2['RB_INCENTIVE'].fillna(0, inplace=True)

                                    # AA2['FINAL PAYOUT'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                                    # AA2 = pd.DataFrame(AA2.groupby('ALLOCATED FOS')['FINAL PAYOUT'].sum()).reset_index()
                                    # AA3 = pd.DataFrame(AA3.groupby('FINAL PAID FOS')['PER PAID CASE'].sum()).reset_index()

                                    # Fixed_FOS = list(AA2['ALLOCATED FOS'].unique())
                                    # Incentive_FOS = list(AA3['FINAL PAID FOS'].unique())

                                    # for j in range(0, len(AA2['ALLOCATED FOS'])):
                                    #     if AA2.loc[j, 'ALLOCATED FOS'] in Incentive_FOS:
                                    #         for k in range(0, len(AA3['FINAL PAID FOS'])):
                                    #             if AA2.loc[j, 'ALLOCATED FOS'] == AA3.loc[k, 'FINAL PAID FOS']:
                                    #                 if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #                     Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #                     Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #                     # Total_Salary_FOS = Fixed_Payout_FOS+Incentive_Payout_FOS
                                    #                 else:
                                    #                     continue
                                    #     elif AA2.loc[j, 'ALLOCATED FOS'] not in Incentive_FOS:
                                    #         if AA2.loc[j, 'ALLOCATED FOS'] == uu:
                                    #             Fixed_Payout_FOS = AA2.loc[j, 'FINAL PAYOUT']
                                    #             # Total_Salary_FOS = Fixed_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue
                                    #
                                    # for j in range(0, len(AA3['FINAL PAID FOS'])):
                                    #     if AA3.loc[j, 'FINAL PAID FOS'] not in Fixed_FOS:
                                    #         if AA3.loc[j, 'FINAL PAID FOS'] == uu:
                                    #             Incentive_Payout_FOS = AA3.loc[k, 'PER PAID CASE']
                                    #             # Total_Salary_FOS = Incentive_Payout_FOS
                                    #         else:
                                    #             continue
                                    #     else:
                                    #         continue

                                    # for j in range(0, len(AA4['FOS'])):
                                    #     if AA4.loc[j, 'FOS'] == uu:
                                    #         FULLERTON_INCENTIVE_FOS = AA4.loc[j, 'INCENTIVE']
                                    #         FULLERTON_FIXED_FOS = AA4.loc[j, 'FIXED_PAYOUT']
                                    #     else:
                                    #         continue

                                    for j in range(0, len(AA5['FOS'])):
                                        if AA5.loc[j, 'FOS'] == uu:
                                            IDFC_HL_INCENTIVE_FOS = AA5.loc[j, 'INCENTIVE']
                                            IDFC_HL_FIXED_FOS = AA5.loc[j, 'FIXED SALARY']
                                        else:
                                            continue

                    Total_Salary_FOS = Fixed_Payout_FOS + Incentive_Payout_FOS + IDFC_HL_INCENTIVE_FOS + IDFC_HL_FIXED_FOS + FULLERTON_INCENTIVE_FOS + FULLERTON_FIXED_FOS

                    Final_Salary = Incentive+Salary


        # Again Checking the form validity
        if login_form.is_valid():
            return render(request, 'FirstLevel/home.html', {'name': username, 'DEPARTMENT': D, 'PROCESS': Pro, 'Emp_Status' : Emp_Status, 'Emp_Salary': Salary, "Incentive" : Incentive, 'Final_Salary' : Final_Salary, 'excel': excel_data, 'columns': C, 'excel2': excel_data2, 'columns2': C2, 'excel3': excel_data3, 'columns3': C3, 'excel4': excel_data4, 'columns4': C4, 'excel5': excel_data5, 'columns5': C5, 'excel6': excel_data6, 'columns6': C6, "Fixed_Payout_FOS" : Fixed_Payout_FOS, "Incentive_Payout_FOS" : Incentive_Payout_FOS, "Total_Salary_FOS" : Total_Salary_FOS, 'FULLERTON_INCENTIVE_FOS' : FULLERTON_INCENTIVE_FOS, 'FULLERTON_FIXED_FOS' : FULLERTON_FIXED_FOS, 'IDFC_HL_INCENTIVE_FOS' : IDFC_HL_INCENTIVE_FOS, 'IDFC_HL_FIXED_FOS' : IDFC_HL_FIXED_FOS})
        else:
            login_form = LoginForm()
            return render(request, 'FirstLevel/login.html', {'login_form': login_form, 'Error': 'MAKE SURE PASSWORD or EMAIL MATCHES!!!'})
    else:
        login_form = LoginForm()
    return render(request, 'FirstLevel/login.html', {'login_form': login_form})

# def logged_in(request):
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     uu = Employee_Login_name()
#     return render(request, 'FirstLevel/home.html', {'name': uu, 'DEPARTMENT': final_dep, 'PROCESS': final_process})

def after_register(request):
    # checking of login form
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        # taking to username for the database
        username = request.POST.get('username')
        # Again Checking the form validity
        if login_form.is_valid():
            return render(request, 'FirstLevel/home.html', {'name': username})
        else:
            login_form = LoginForm()
            return render(request, 'FirstLevel/login.html', {'login_form': login_form, 'Error': 'MAKE SURE PASSWORD or EMAIL MATCHES!!!'})
    else:
        re= 'THANKS FOR REGISTER'
        login_form = LoginForm()
    return render(request, 'FirstLevel/login.html', {'login_form': login_form,'re':re})

def employee_database(request):
    if request.method == 'POST':
        person_resource = EmployeeResources()
        dataset=Dataset()
        new_person=request.FILES['employee']

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong formate')
            return render(request,'FirstLevel/employee_database.html')
        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value = Employee(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10],
                data[11], data[12], data[13], data[14], data[15], data[16])
            value.save()
        a = pd.read_excel(new_person)
        a.to_excel('media/Employees/Employee_Database.xlsx', index=False)
    return render(request,'FirstLevel/employee_database.html')

def L_T_PERFORMANCE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/L_T/MIS/Performance_L_T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=MIS L&T.xlsx"
    return response

def BAJAJ_CD_PERFORMANCE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/BAJAJ-CD/MIS/BAJAJ_PERFORMANCE.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=MIS BAJAJ-CD.xlsx"
    return response

def IDFC_TW_PERFORMANCE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=MIS IDFC-TW.xlsx"
    return response

def IDFC_HL_PERFORMANCE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_HL/MIS/Performance_IDFC_HL.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=MIS IDFC-HL.xlsx"
    return response

# def FULLERTON_OTR_PERFORMANCE_DOWNLOAD(request):
#     # fill these variables with real values
#     filename = os.path.join(BASE_DIR, 'media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx')
#
#     excel = open(filename, 'rb')
#     response = HttpResponse(excel,
#                             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = "attachment; filename=a.xlsx"
#     return response

def FULLERTON_RECOVERY_PERFORMANCE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/MIS/MIS_FULLERTON_RECOVERY.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=MIS FULLERTON-RECOVERY.xlsx"
    return response

def FULLERTON_RECOVERY_BILLING_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/BILLING/PAYOUT_FULLERTON_RECOVERY.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=FULLERTON_BILLING.xlsx"
    return response

def FULLERTON_RECOVERY_SALARY_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=FULLERTON_FOS_SALARY.xlsx"
    return response

def L_T_BILLING_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/L_T/Billing/Final_Billing_L_T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Final Billing L&T.xlsx"
    return response

def BAJAJ_CD_BILLING_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/BAJAJ-CD/Billing/BAJAJ PAYOUT.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Final Billing BAJAJ-CD.xlsx"
    return response

def IDFC_TW_BILLING_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_TW/Billing/Final_Billing_IDFC_TW.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Final Billing IDFC-TW.xlsx"
    return response

def IDFC_HL_BILLING_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_HL/Billing/Final_Billing_IDFC_HL.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Final Billing IDFC-HL.xlsx"
    return response

# def FULLERTON_OTR_BILLING_DOWNLOAD(request):
#     # fill these variables with real values
#     filename = os.path.join(BASE_DIR, 'media/FULLERTON_OTR/Billing/MIS_FULLERTON_OTR.xlsx')
#
#     excel = open(filename, 'rb')
#     response = HttpResponse(excel,
#                             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = "attachment; filename=a.xlsx"
#     return response
#
# def FULLERTON_RECOVERY_BILLING_DOWNLOAD(request):
#     # fill these variables with real values
#     filename = os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/MIS/MIS_FULLERTON_RECOVERY.xlsx')
#
#     excel = open(filename, 'rb')
#     response = HttpResponse(excel,
#                             content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     response['Content-Disposition'] = "attachment; filename=a.xlsx"
#     return response

def L_T_SALARY_FIXED_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) L&T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE(Including Fixed Salary) L&T.xlsx"
    return response

def L_T_SALARY_INCENTIVE_PIVOT_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(PIVOT) L&T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE(PIVOT) L&T.xlsx"
    return response

def L_T_SALARY_INCENTIVE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE L&T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE L&T.xlsx"
    return response

def L_T_TC_SALARY_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/L_T/TC Incentive/TC Performance L_T.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=TC Incentive L&T.xlsx"
    return response

def IDFC_TW_SALARY_FIXED_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx"
    return response

def IDFC_TW_SALARY_INCENTIVE_PIVOT_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(PIVOT) IDFC-TW.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE(PIVOT) IDFC-TW.xlsx"
    return response

def IDFC_TW_SALARY_INCENTIVE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE IDFC-TW.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=PER PAID CASE IDFC-TW.xlsx"
    return response

def IDFC_TW_TC_SALARY_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=TC INCENTIVE IDFC-TW.xlsx"
    return response

def BAJAJ_CD_SALARY_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/BAJAJ-CD/MIS/BAJAJ TC-WISE MIS.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=BAJAJ TC-WISE MIS.xlsx"
    return response

def IDFC_HL_SALARY_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=BKT-WISE PAYOUT.xlsx"
    return response

def IDFC_HL_TL_INCENTIVE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/FINAL INCENTIVE IDFC-HL(TL).xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=FINAL INCENTIVE IDFC-HL(TL).xlsx"
    return response

def IDFC_HL_FINAL_SALARY_INCENTIVE_DOWNLOAD(request):
    # fill these variables with real values
    filename = os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/FINAL PAYOUT IDFC-HL.xlsx')

    excel = open(filename, 'rb')
    response = HttpResponse(excel,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=FINAL PAYOUT IDFC-HL.xlsx"
    return response

# to upload a file
# def L_T_MIS(request):
#     excel_data = []
#     F1 = pd.DataFrame()
#     if request.method == 'POST':
#         Allocation1 = request.FILES['Allocation']
#         Paidfile1 = request.FILES['Paid_File']
#         A = pd.read_excel(Allocation1)
#         B = pd.read_excel(Paidfile1)
#         # for check of file
#         for i in range(0, len(A['AGREEMENTID'])):
#             if pd.isnull(A['AGREEMENTID'][i]) == True:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES','DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i,'CUSTOMERNAME'],str)==False:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i,'TC NAME'],str)==False:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i,'TL'],str)==False:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i,'FOS'],str)==False:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i,'AREA'],str)==False:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif isinstance(A.loc[i,'BKT'],np.int64)==False or pd.isnull(A['BKT'][i]) == True:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'BKT DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif isinstance(A.loc[i,'POS'],np.float64)==False or pd.isnull(A['POS'][i]) == True:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             elif isinstance(A.loc[i,'EMI'],np.int64)==False or pd.isnull(A['EMI'][i]) == True:
#                 print('error',i)
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#             else:
#                 continue
#
#         fs = FileSystemStorage(location='media/L_T/MIS')
#         fs.save(Allocation1.name, Allocation1)
#         fs.save(Paidfile1.name, Paidfile1)
#         print(A.head())
#
#         B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             for k in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] != 'FORECLOSE' and B.loc[k, 'AGAINST'] != 'SETTLEMENT'):
#                     for j in range(0, len(B1['AGREEMENTID'])):
#                         if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                             if (A.loc[i, 'BKT'] != 0 and A.loc[i, 'BKT'] != 12) and (A.loc[i, 'BKT'] != 1):
#                                 a = (int(A.loc[i, 'BKT']) + 1) * A.loc[i, 'EMI']
#                                 b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
#                                 if (B1.loc[j, 'PAID AMOUNT'] >= a) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
#                                     A.loc[i, 'STATUS'] = 'NM'
#                                 elif (B1.loc[j, 'PAID AMOUNT'] >= b) and (B1.loc[j, 'PAID AMOUNT'] < a) and (B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'POS']):
#                                     A.loc[i, 'STATUS'] = 'RB'
#                                 elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
#                                     A.loc[i, 'STATUS'] = 'SB'
#                                 elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                     A.loc[i, 'STATUS'] = 'PART PAID'
#                             elif A.loc[i, 'BKT'] == 1:
#                                 b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
#                                 if (B1.loc[j, 'PAID AMOUNT'] >= b) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
#                                     A.loc[i, 'STATUS'] = 'NM'
#                                 elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
#                                     A.loc[i, 'STATUS'] = 'SB'
#                                 elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                     A.loc[i, 'STATUS'] = 'PART PAID'
#                             elif A.loc[i, 'BKT'] == 12:
#                                 c = (int(A.loc[i, 'BKT']) + 1) * A.loc[i, 'EMI']
#                                 d = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
#                                 if (B1.loc[j, 'PAID AMOUNT'] >= c) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
#                                     A.loc[i, 'STATUS'] = 'NM'
#                                 elif (B1.loc[j, 'PAID AMOUNT'] >= d) and (B1.loc[j, 'PAID AMOUNT'] < c) and (B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'POS']):
#                                     A.loc[i, 'STATUS'] = 'RB'
#                                 elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < d):
#                                     A.loc[i, 'STATUS'] = 'SB'
#                                 elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                     A.loc[i, 'STATUS'] = 'PART PAID'
#                             elif A.loc[i, 'BKT'] == 0:
#                                 if B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                     A.loc[i, 'STATUS'] = 'PART PAID'
#                                 else:
#                                     A.loc[i, 'STATUS'] = 'SB'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'FORECLOSE'):
#                     A.loc[i, 'STATUS'] = 'FORECLOSE'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'SETTLEMENT'):
#                     A.loc[i, 'STATUS'] = 'SETTLEMENT'
#         A['STATUS'].fillna('FLOW', inplace=True)
#         for i in range(0, len(A['AGREEMENTID'])):
#             for j in range(0, len(B1['PAID AMOUNT'])):
#                 if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                     A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']
#
#         M = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['POS'].sum()).reset_index()
#
#         M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)
#
#         R = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['AGREEMENTID'].count()).reset_index()
#
#         F = M.merge(R, how='outer')
#
#         F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)
#
#         R1 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE', 'STATUS'])['AGREEMENTID'].count()).reset_index()
#
#         P = F.copy()
#
#         P = P.iloc[:, :3]
#
#         P.head()
#
#         P['FLOW'] = np.nan
#         P['SB'] = np.nan
#         P['RB'] = np.nan
#         P['NM'] = np.nan
#         P['PART PAID'] = np.nan
#         P['FORECLOSE'] = np.nan
#         P['SETTLEMENT'] = np.nan
#
#         COL = P.columns
#
#         for i in range(0, len(R1['COMPANY'])):
#             for j in range(0, len(P['COMPANY'])):
#                 for k in range(0, len(COL)):
#                     if ((R1.loc[i, ['COMPANY', 'BKT', 'STATE']] == P.loc[j, ['COMPANY', 'BKT', 'STATE']]).all()) and R1.loc[i, 'STATUS'] == COL[k]:
#                         P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']
#
#         F = F.merge(P, how='outer')
#
#         F.fillna(0, inplace=True)
#
#         F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
#                   'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES'}, axis=1,
#                  inplace=True)
#
#         R2 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE', 'STATUS'])['POS'].sum()).reset_index()
#
#         for i in range(0, len(R2['COMPANY'])):
#             for j in range(0, len(P['COMPANY'])):
#                 for k in range(0, len(COL)):
#                     if ((R2.loc[i, ['COMPANY', 'BKT', 'STATE']] == P.loc[j, ['COMPANY', 'BKT', 'STATE']]).all()) and R2.loc[i, 'STATUS'] == COL[k]:
#                         P.loc[j, COL[k]] = R2.loc[i, 'POS']
#
#         F = F.merge(P, how='outer')
#
#         F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
#                   'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS'}, axis=1, inplace=True)
#
#         F.fillna(0, inplace=True)
#
#         for i in range(0, len(F['FLOW_CASES'])):
#             F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'], 2)
#             F.loc[i, 'TOTAL_POS'] = round(F.loc[i, 'TOTAL_POS'], 2)
#             F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
#             F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
#             F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#
#         TP = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['TOTAL PAID'].sum()).reset_index()
#
#         F = F.merge(TP, how='outer')
#
#         for i in range(0, len(F['NM_CASES'])):
#             F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'NM_POS%'] + F.loc[
#                 i, 'FORECLOSE_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#             F.loc[i, 'Additional_Performance'] = F.loc[i, 'RB_POS%'] + F.loc[i, 'NM_POS%'] + F.loc[
#                 i, 'FORECLOSE_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#
#         for i in range(0, len(F['FLOW_CASES'])):
#             F.loc[i, 'PERFORMANCE'] = round(F.loc[i, 'PERFORMANCE'], 2)
#             F.loc[i, 'Additional_Performance'] = round(F.loc[i, 'Additional_Performance'], 2)
#
#         F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
#                   'SETTLEMENT_CASES': 'SC_CASES',
#                   'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
#                   'FORECLOSE_POS%': 'FC_POS%',
#                   'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
#                  inplace=True)
#
#         print(F)
#         F.to_excel('media/L_T/MIS/Performance_L_T.xlsx',index=False)
#         F.to_excel('media/L_T/Billing/Performance_L_T.xlsx', index=False)
#         F1 = F.copy()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             s = 0
#             for j in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and ((A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'SB')) and ((B.loc[j, 'MODE'] != 'ECS') and (B.loc[j, 'MODE'] != 'ADJUSTED')):
#                     s = s + B.loc[j, 'PAID AMOUNT']
#             A.loc[i, 'Billing PAID AMT.'] = s
#         for i in range(0, len(A['STATE'])):
#             if A.loc[i, 'STATUS'] == 'SB':
#                 if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']:
#                     A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
#         A.to_excel('media/L_T/MIS/MASTER FILE L_T.xlsx', index=False)
#         A.to_excel('media/L_T/Billing/MASTER FILE L_T.xlsx', index=False)
#         A.to_excel('media/L_T/TC Performance/MASTER FILE L_T.xlsx', index=False)
#         A.to_excel('media/L_T/FOS Salary/MASTER FILE L_T.xlsx', index=False)
#         A.to_excel('media/L_T/TC Incentive/MASTER FILE L_T.xlsx', index=False)
#     elif request.method != 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/Performance_L_T.xlsx'):
#             fs = FileSystemStorage(location='media/L_T/MIS')
#             AA = fs.open('Performance_L_T.xlsx')
#             F1 = pd.read_excel(AA)
#         else:
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#             return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#     C = list(F1.columns)
#
#     for j in range(0, len(F1[C[0]])):
#         row_data = list()
#         for col in range(0,len(C)):
#             row_data.append(str(F1.loc[j,C[col]]))
#         excel_data.append(row_data)
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#     return render(request, 'FirstLevel/upload_excel.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

# def L_T_BILLING(request):
#     excel_data1 = []
#     F2 = pd.DataFrame()
#     if request.method == 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/Billing/MASTER FILE L_T.xlsx'):
#             fs = FileSystemStorage(location='media/L_T/Billing')
#             AA = fs.open('Performance_L_T.xlsx')
#             AA1 = fs.open('MASTER FILE L_T.xlsx')
#             AA2 = fs.open('AddPayout.xlsx')
#             AA3 = fs.open('AddResolution.xlsx')
#             AA4 = fs.open('Payout.xlsx')
#             AA5 = fs.open('Resolution.xlsx')
#             P = pd.read_excel(AA)
#             A = pd.read_excel(AA1)
#             PA = pd.read_excel(AA4)
#             R = pd.read_excel(AA5)
#             APA = pd.read_excel(AA2)
#             AR = pd.read_excel(AA3)
#
#             l1 = R.columns
#
#             # =============================================================================
#             # BKT 1
#             # =============================================================================
#
#             for i in range(0, len(A['BKT'])):
#                 if A.loc[i, 'BKT'] == 1:
#                     for j in range(0, len(P['BKT'])):
#                         if A.loc[i, 'BKT'] == P.loc[j, 'BKT']:
#                             for k in range(0, len(l1)):
#                                 if l1[k] == A.loc[i, 'BKT']:
#                                     for l in range(0, len(PA[1])):
#                                         for y in range(0, len(APA[1])):
#                                             if l == 0:
#                                                 if P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]]:
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB' or A.loc[i, 'STATUS'] == 'NM'):
#                                                         a = A.loc[i, 'Billing PAID AMT.'] * PA.loc[l, l1[k]] / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = a
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], a, P.loc[j, 'BKT'])
#                                                     # =============================================================================
#                                                     #                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                                     #                                             a=(A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[1]
#                                                     #                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                             A.loc[i,'MOHAK']=a
#                                                     #                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             elif l > 0:
#                                                 if ((P.loc[j, 'POS_RES%'] > R.loc[l - 1, l1[k]]) and (P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]])):
#                                                     # =============================================================================
#                                                     #                                          if (A.loc[i,'STATUS']=='RB') or (A.loc[i,'STATUS']=='NM'):
#                                                     #                                              c=(A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[1]
#                                                     #                                              A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                              A.loc[i,'MOHAK']=int(c)
#                                                     #                                              print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB'):
#                                                         d = A.loc[i, 'Billing PAID AMT.'] * (PA.loc[l, l1[k]]) / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = d
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], d, P.loc[j, 'BKT'])
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             elif l == 6:
#                                                 if ((P.loc[j, 'POS_RES%'] > R.loc[l - 1, l1[k]]) and (P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]])):
#                                                     if (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
#                                                         c = A.loc[i, 'Billing PAID AMT.'] * (PA.loc[l, l1[k]] + APA.loc[y - 1, l1[k]]) / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]] + APA.loc[y - 1, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = c
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l - 1, l1[k]], APA.loc[y, l1[k]], c, P.loc[j, 'BKT'])
#                                                     elif A.loc[i, 'STATUS'] == 'SB':
#                                                         d = A.loc[i, 'Billing PAID AMT.'] * (PA.loc[l, l1[k]]) / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = d
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], APA.loc[y, l1[k]], d, P.loc[j, 'BKT'])
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], APA.loc[y, l1[k]], 0, P.loc[j, 'BKT'])
#
#             # =============================================================================
#             # BKT 2
#             # =============================================================================
#
#             for i in range(0, len(A['BKT'])):
#                 if A.loc[i, 'BKT'] == 2:
#                     for j in range(0, len(P['BKT'])):
#                         if A.loc[i, 'BKT'] == P.loc[j, 'BKT']:
#                             for k in range(0, len(l1)):
#                                 if l1[k] == A.loc[i, 'BKT']:
#                                     for l in range(0, len(PA[2])):
#                                         for y in range(0, len(APA[1])):
#                                             if l == 0:
#                                                 if P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]]:
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
#                                                         a = A.loc[i, 'Billing PAID AMT.'] * PA.loc[l, l1[k]] / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = a
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], a, P.loc[j, 'BKT'])
#                                                     # =============================================================================
#                                                     #                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                                     #                                             a=(A.oc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[2]
#                                                     #                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                             A.loc[i,'MOHAK']=a
#                                                     #                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             elif l > 0:
#                                                 if ((P.loc[j, 'POS_RES%'] > R.loc[l - 1, l1[k]]) and (P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]])):
#                                                     # =============================================================================
#                                                     #                                         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                                     #                                             c=(A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100)+APA[2]
#                                                     #                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                             A.loc[i,'MOHAK']=int(c)
#                                                     #                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB'):
#                                                         d = A.loc[i, 'Billing PAID AMT.'] * (PA.loc[l, l1[k]]) / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = d
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l - 1, l1[k]], d, P.loc[j, 'BKT'])
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             # elif l>0:
#                                             #     if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and \
#                                             #     ((P.loc[j,'Additional_Performance']>AR.loc[y-1,l1[k]]) and (P.loc[j,'Additional_Performance']<=AR.loc[y,l1[k]])):
#                                             #         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             #             c=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])/100
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=c
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],APA.loc[y,l1[k]],c,P.loc[j,'BKT'])
#                                             #         elif A.loc[i,'STATUS']=='SB':
#                                             #             d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=d
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],d,P.loc[j,'BKT'])
#                                             #         else:
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=0
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],0,P.loc[j,'BKT'])
#
#             # =============================================================================
#             # BKT 3
#             # =============================================================================
#
#             for i in range(0, len(A['BKT'])):
#                 if A.loc[i, 'BKT'] == 3:
#                     for j in range(0, len(P['BKT'])):
#                         if A.loc[i, 'BKT'] == P.loc[j, 'BKT']:
#                             for k in range(0, len(l1)):
#                                 if l1[k] == A.loc[i, 'BKT']:
#                                     for l in range(0, len(PA[3])):
#                                         for y in range(0, len(APA[1])):
#                                             if l == 0:
#                                                 if P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]]:
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
#                                                         a = A.loc[i, 'Billing PAID AMT.'] * PA.loc[l, l1[k]] / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = a
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], a, P.loc[j, 'BKT'])
#                                                     # =============================================================================
#                                                     #                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                                     #                                             a=(A.oc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[2]
#                                                     #                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                             A.loc[i,'MOHAK']=a
#                                                     #                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             elif l > 0:
#                                                 if ((P.loc[j, 'POS_RES%'] > R.loc[l - 1, l1[k]]) and (P.loc[j, 'POS_RES%'] <= R.loc[l, l1[k]])):
#                                                     # =============================================================================
#                                                     #                                         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                                     #                                             c=(A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100)+APA[2]
#                                                     #                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                                     #                                             A.loc[i,'MOHAK']=int(c)
#                                                     #                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
#                                                     # =============================================================================
#                                                     if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB'):
#                                                         d = A.loc[i, 'Billing PAID AMT.'] * (PA.loc[l, l1[k]]) / 100
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = d
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l - 1, l1[k]], d, P.loc[j, 'BKT'])
#                                                     else:
#                                                         A.loc[i, 'PERCENTAGE'] = str(PA.loc[l, l1[k]]) + '%'
#                                                         A.loc[i, 'MOHAK'] = 0
#                                                         print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'BKT'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], PA.loc[l, l1[k]], 0, P.loc[j, 'BKT'])
#                                             # elif l>0 and y>0:
#                                             #     if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and \
#                                             #     ((P.loc[j,'Additional_Performance']>AR.loc[y-1,l1[k]]) and (P.loc[j,'Additional_Performance']<=AR.loc[y,l1[k]])):
#                                             #         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             #             c=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])/100
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=c
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],APA.loc[y,l1[k]],c,P.loc[j,'BKT'])
#                                             #         elif A.loc[i,'STATUS']=='SB':
#                                             #             d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=d
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],d,P.loc[j,'BKT'])
#                                             #         else:
#                                             #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             #             A.loc[i,'MOHAK']=0
#                                             #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],0,P.loc[j,'BKT'])
#
#             # =============================================================================
#             # SETTLEMENT
#             # =============================================================================
#
#             for i in range(0, len(A['BKT'])):
#                 if A.loc[i, 'STATUS'] == 'SETTLEMENT':
#                     dd = A.loc[i, 'Billing PAID AMT.'] * 12 / 100
#                     A.loc[i, 'MOHAK'] = dd
#                     A.loc[i, 'PERCENTAGE'] = str(12) + '%'
#                 elif A.loc[i, 'STATUS'] == 'FORECLOSE':
#                     dd = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
#                     A.loc[i, 'MOHAK'] = dd
#                     A.loc[i, 'PERCENTAGE'] = str(20) + '%'
#             # =============================================================================
#             #     elif (A.loc[i,'BKT']==2 or A.loc[i,'BKT']==3) and A.loc[i,'STATUS']=='FORECLOSE':
#             #         c=A.loc[i,'TOTAL COLLECTABLE']*16/100
#             #         A.loc[i,'MOHAK']=c
#             # =============================================================================
#
#             A['MOHAK'].replace(np.nan, 0, inplace=True)
#
#             A.rename({'MOHAK': 'PAYOUT'}, axis=1, inplace=True)
#
#
#             A.to_excel('media/L_T/Billing/Final_Billing_L_T.xlsx', index=False)
#
#             F = pd.DataFrame(A.groupby('BKT')['PAYOUT'].sum()).reset_index()
#             for i in range(0,len(F['PAYOUT'])):
#                 F.loc[i,'PAYOUT']=round(F.loc[i,'PAYOUT'],2)
#             F.to_excel('media/L_T/Billing/BKT_Billing_L_T.xlsx', index=False)
#             F2 = F.copy()
#
#             Total_Payout = round(sum(A['PAYOUT']),2)
#
#
#     elif request.method != 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/Billing/Final_Billing_L_T.xlsx'):
#             fs = FileSystemStorage(location='media/L_T/Billing')
#             AA = fs.open('BKT_Billing_L_T.xlsx')
#             F2 = pd.read_excel(AA)
#             Total_Payout = round(sum(F2['PAYOUT']), 2)
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/Billing/MASTER FILE L_T.xlsx'):
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#             return render(request, 'FirstLevel/Billing.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#         else:
#             return HttpResponseRedirect(reverse('basic_app:L_T_MIS'))
#
#     C1 = list(F2.columns)
#
#     for j in range(0, len(F2[C1[0]])):
#         row_data1 = list()
#         for col in range(0, len(C1)):
#             row_data1.append(str(F2.loc[j, C1[col]]))
#         excel_data1.append(row_data1)
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#     return render(request, 'FirstLevel/Billing.html', {'Billing': excel_data1, 'columns': C1, 'Total_Payout': Total_Payout, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_TW_MIS(request):
    excel_data = []
    F1 = pd.DataFrame()

    if request.method == 'POST':
        Allocation1 = request.FILES['Allocation']
        Paidfile1 = request.FILES['Paid_File']
        A = pd.read_excel(Allocation1)
        B = pd.read_excel(Paidfile1)
        # for check of file

        for i in range(0, len(A['AGREEMENTID'])):
            if pd.isnull(A['AGREEMENTID'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i, 'CUSTOMERNAME'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i, 'TC NAME'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i, 'TL'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i, 'FOS'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i, 'AREA'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'BKT'], np.int64) == False or pd.isnull(A['BKT'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'BKT DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'POS'], np.float64) == True and pd.isnull(A['POS'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'EMI'], np.float64) == True and pd.isnull(A['EMI'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            else:
                continue

        fs = FileSystemStorage(location='media/IDFC_TW/MIS')
        fs.save(Allocation1.name, Allocation1)
        fs.save(Paidfile1.name, Paidfile1)
        print(A.head())

        B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

        for i in range(0, len(A['AGREEMENTID'])):
            for k in range(0, len(B['AGREEMENTID'])):
                if (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and ((B.loc[k, 'AGAINST'] != 'FORECLOSE') and (B.loc[k, 'AGAINST'] != 'SETTLEMENT')):
                    for j in range(0, len(B1['AGREEMENTID'])):
                        if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
                            if A.loc[i, 'BKT'] == 0:
                                if B.loc[k, 'AGAINST'] == 'RT':
                                    A.loc[i, 'STATUS'] == 'RT'
                                elif B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                                else:
                                    A.loc[i, 'STATUS'] = 'UNPAID'
                            elif A.loc[i, 'BKT'] != 1:
                                a = (A.loc[i, 'BKT'] + 1) * A.loc[i, 'EMI']
                                b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                                if B.loc[k, 'AGAINST'] == 'RT':
                                    A.loc[i, 'STATUS'] = 'RT'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= a) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
                                    A.loc[i, 'STATUS'] = 'NM'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= b) and ((B1.loc[j, 'PAID AMOUNT'] < a) and (B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'POS'])):
                                    A.loc[i, 'STATUS'] = 'RB'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                            elif A.loc[i, 'BKT'] == 1:
                                b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                                if B.loc[k, 'AGAINST'] == 'RT':
                                    A.loc[i, 'STATUS'] = 'RT'
                                elif B1.loc[j, 'PAID AMOUNT'] >= b:
                                    A.loc[i, 'STATUS'] = 'RB'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'FORECLOSE'):
                    A.loc[i, 'STATUS'] = 'FORECLOSE'
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'SETTLEMENT'):
                    A.loc[i, 'STATUS'] = 'SETTLEMENT'
        A['STATUS'].fillna('FLOW', inplace=True)
        for i in range(0, len(A['AGREEMENTID'])):
            for j in range(0, len(B1['PAID AMOUNT'])):
                if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
                    A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']

        M = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['POS'].sum()).reset_index()

        M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)

        R = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['AGREEMENTID'].count()).reset_index()

        F = M.merge(R, how='outer')

        F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)

        R1 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE', 'STATUS'])['AGREEMENTID'].count()).reset_index()

        P = F.copy()

        P = P.iloc[:, :3]

        P['FLOW'] = np.nan
        P['SB'] = np.nan
        P['RB'] = np.nan
        P['NM'] = np.nan
        P['PART PAID'] = np.nan
        P['FORECLOSE'] = np.nan
        P['SETTLEMENT'] = np.nan
        P['RT'] = np.nan

        COL = P.columns

        for i in range(0, len(R1['COMPANY'])):
            for j in range(0, len(P['COMPANY'])):
                for k in range(0, len(COL)):
                    if ((R1.loc[i, ['COMPANY', 'BKT', 'STATE']] == P.loc[j, ['COMPANY', 'BKT', 'STATE']]).all()) and (R1.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']

        F = F.merge(P, how='outer')

        F.fillna(0, inplace=True)

        F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
                'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES', 'RT': 'RT_CASES'},
             axis=1, inplace=True)

        R2 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE', 'STATUS'])['POS'].sum()).reset_index()

        for i in range(0, len(R2['COMPANY'])):
            for j in range(0, len(P['COMPANY'])):
                for k in range(0, len(COL)):
                    if ((R2.loc[i, ['COMPANY', 'BKT', 'STATE']] == P.loc[j, ['COMPANY', 'BKT', 'STATE']]).all()) and (R2.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R2.loc[i, 'POS']

        F = F.merge(P, how='outer')

        F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
              'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS', 'RT': 'RT_POS'}, axis=1, inplace=True)

        F.fillna(0, inplace=True)

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'RT_POS%'] = round((F.loc[i, 'RT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)

        TP = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'STATE'])['TOTAL PAID'].sum()).reset_index()

        F = F.merge(TP, how='outer')

        for i in range(0, len(F['SB_POS'])):
            F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + F.loc[i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%'] + F.loc[i, 'RT_POS%']
            F.loc[i, 'Additional_Performance'] = F.loc[i, 'RB_POS%'] + F.loc[i, 'NM_POS%']

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'PERFORMANCE'] = round(F.loc[i, 'PERFORMANCE'], 2)
            F.loc[i, 'Additional_Performance'] = round(F.loc[i, 'Additional_Performance'], 2)


        F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES', 'SETTLEMENT_CASES': 'SC_CASES', 'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS', 'FORECLOSE_POS%': 'FC_POS%', 'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1, inplace=True)

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'TOTAL_POS'] = round(F.loc[i, 'TOTAL_POS'], 2)
            F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
            F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
            F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'], 2)
            F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'], 2)
            F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
            F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
            F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
            F.loc[i, 'RT_POS'] = round(F.loc[i, 'RT_POS'], 2)
            F.loc[i, 'TOTAL PAID'] = round(F.loc[i, 'TOTAL PAID'], 2)

        print(F)
        F.to_excel('media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx', index=False)
        F.to_excel('media/IDFC_TW/Billing/Performance_IDFC_TW.xlsx', index=False)
        F1 = F.copy()

        for i in range(0, len(A['AGREEMENTID'])):
            s = 0
            for j in range(0, len(B['AGREEMENTID'])):
                if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and ((A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'SB')) and ((B.loc[j, 'MODE'] != 'ECS') and (B.loc[j, 'MODE'] != 'ADJUSTED')):
                    s = s + B.loc[j, 'PAID AMOUNT']
            A.loc[i, 'Billing PAID AMT.'] = s
        for i in range(0, len(A['STATE'])):
            if A.loc[i, 'STATUS'] == 'SB':
                if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']:
                    A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
        for i in range(0, len(A['AGREEMENTID'])):
            if A.loc[i, 'STATUS'] == 'SETTLEMENT' or A.loc[i, 'STATUS'] == 'FORECLOSE':
                A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'TOTAL PAID']
            elif (A.loc[i, 'BKT'] == 1) and (A.loc[i, 'STATUS'] == 'RB'):
                if A.loc[i, 'Billing PAID AMT.'] > ((A.loc[i, 'EMI']) * 2):
                    A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                else:
                    A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'TOTAL PAID']
        for i in range(0, len(A['STATE'])):
            if A.loc[i, 'STATUS'] == 'SB':
                if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']:
                    A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']

        F.to_excel(r'media/IDFC_TW/MIS/MIS_IDFC_TW.xlsx', index=False)

        F.replace(np.nan, 0, inplace=True)

        F.to_excel(r'media/IDFC_TW/Billing/Performance_IDFC_TW.xlsx', index=False)

        for i in range(0, len(A['AGREEMENTID'])):
            s = 0
            for j in range(0, len(B['AGREEMENTID'])):
                if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and ((A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'SB')) and ((B.loc[j, 'MODE'] != 'ECS') and (B.loc[j, 'MODE'] != 'ADJUSTED')):
                    s = s + B.loc[j, 'PAID AMOUNT']
            A.loc[i, 'Billing PAID AMT.'] = s

        A.to_excel(r'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx', index=False)
        A.to_excel(r'media/IDFC_TW/Billing/MASTER FILE IDFC_TW.xlsx', index=False)
        A.to_excel(r'media/IDFC_TW/TC Performance/MASTER FILE IDFC_TW.xlsx', index=False)
        A.to_excel(r'media/IDFC_TW/FOS Salary/MASTER FILE IDFC_TW.xlsx', index=False)
        A.to_excel(r'media/IDFC_TW/TC Incentive/MASTER FILE IDFC_TW.xlsx', index=False)

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_TW/MIS')
            AA = fs.open('Performance_IDFC_TW.xlsx')
            F1 = pd.read_excel(AA)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C = list(F1.columns)

    for j in range(0, len(F1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(F1.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/upload_excel.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_TW_BILLING(request):
    excel_data1 = []
    F2 = pd.DataFrame()
    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/Billing/MASTER FILE IDFC_TW.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_TW/Billing')
            AA = fs.open('Performance_IDFC_TW.xlsx')
            AA1 = fs.open('MASTER FILE IDFC_TW.xlsx')
            AA2 = fs.open('BKT0.xlsx')
            AA3 = fs.open('BKT 1.xlsx')
            AA4 = fs.open('BKT 1 Target.xlsx')
            AA5 = fs.open('BKT 2.xlsx')
            AA6 = fs.open('BKT 2 Target.xlsx')
            AA7 = fs.open('BKT 3.xlsx')
            AA8 = fs.open('BKT 3 Target.xlsx')
            AA9 = fs.open('BKT 4.xlsx')
            AA10 = fs.open('BKT 4 Target.xlsx')
            AA11 = fs.open('BKT 5.xlsx')
            AA12 = fs.open('BKT 5 Target.xlsx')
            AA13 = fs.open('BKT 6.xlsx')
            AA14 = fs.open('BKT 6 Target.xlsx')

            BKT0 = pd.read_excel(AA2)
            BKT1 = pd.read_excel(AA3)
            BKT1T = pd.read_excel(AA4)
            BKT2 = pd.read_excel(AA5)
            BKT2T = pd.read_excel(AA6)
            BKT3 = pd.read_excel(AA7)
            BKT3T = pd.read_excel(AA8)
            BKT4 = pd.read_excel(AA9)
            BKT4T = pd.read_excel(AA10)
            BKT5 = pd.read_excel(AA11)
            BKT5T = pd.read_excel(AA12)
            BKT6 = pd.read_excel(AA13)
            BKT6T = pd.read_excel(AA14)

            A = pd.read_excel(AA1)
            P = pd.read_excel(AA)

            l1 = list(BKT1.columns)
            l2 = list(BKT2.columns)
            l3 = list(BKT3.columns)
            l4 = list(BKT4.columns)
            l5 = list(BKT5.columns)
            l6 = list(BKT6.columns)

            # BKT 0

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 0:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 0:
                            for l in range(0, len(BKT0)):
                                if l == 0:
                                    if A.loc[i, 'STATUS'] == 'RT':
                                        A.loc[i, 'MOHAK'] = 0
                                    elif (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'RB'):
                                        if P.loc[j, 'POS_RES%'] <= BKT0.loc[l, 'TARGET']:
                                            a = A.loc[i, 'Billing PAID AMT.'] * BKT0.loc[l, 'CAT C'] / 100
                                            A.loc[i, 'percentage'] = str(BKT0.loc[l, 'CAT C']) + '%'
                                            A.loc[i, 'MOHAK'] = a
                                            print(A.loc[i, 'AGREEMENTID'], BKT0.loc[l, 'CAT C'], A.loc[i, 'MOHAK'])
                                        elif l > 0:
                                            if (P.loc[j, 'POS_RES%'] >= BKT0.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT0.loc[l, 'TARGET']):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT0.loc[l - 1, 'CAT C'] / 100
                                                A.loc[i, 'percentage'] = str(BKT0.loc[l - 1, 'CAT C']) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT0.loc[l, 'CAT C'], A.loc[i, 'MOHAK'])
                                        elif l == 9:
                                            if P.loc[j, 'POS_RES%'] >= BKT0.loc[l, 'TARGET']:
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT0.loc[l, 'CAT C'] / 100
                                                A.loc[i, 'percentage'] = str(BKT0.loc[l, 'CAT C']) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT0.loc[l, 'CAT C'], A.loc[i, 'MOHAK'])
                                    else:
                                        A.loc[i, 'percentage'] = str(BKT0.loc[l, 'CAT C']) + '%'
                                        A.loc[i, 'MOHAK'] = 0

            # BKT 1

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 1:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 1:
                            for k in range(0, len(l1)):
                                for l in range(0, len(BKT1)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif (P.loc[j, 'Additional_Performance'] < l1[k]) and (P.loc[j, 'POS_RES%'] <= BKT1T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif (P.loc[j, 'Additional_Performance'] >= l1[k - 1]) and (P.loc[j, 'POS_RES%'] <= BKT1T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif (P.loc[j, 'Additional_Performance'] < l1[k]) and ((P.loc[j, 'POS_RES%'] >= BKT1T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT1T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif (P.loc[j, 'Additional_Performance'] >= l1[k - 1]) and ((P.loc[j, 'POS_RES%'] >= BKT1T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT1T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l - 1, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l - 1, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l == 9):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif (P.loc[j, 'Additional_Performance'] >= l1[k]) and (P.loc[j, 'POS_RES%'] >= BKT1T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 0
                                        elif ((P.loc[j, 'Additional_Performance'] >= l1[k - 1]) and (P.loc[j, 'Additional_Performance'] < l1[k])) and (P.loc[j, 'POS_RES%'] <= BKT1T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] >= l1[k - 1]) and (P.loc[j, 'Additional_Performance'] < l1[k])) and ((P.loc[j, 'POS_RES%'] > BKT1T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT1T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT1.loc[l, l1[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT1.loc[l, l1[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT1.loc[l, l1[k]], A.loc[i, 'MOHAK'])

            # =============================================================================
            # BKT-2
            # =============================================================================

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 2:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 2:
                            for k in range(0, len(l2)):
                                for l in range(0, len(BKT2)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif (P.loc[j, 'Additional_Performance'] <= l2[k]) and (P.loc[j, 'POS_RES%'] <= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif ((P.loc[j, 'Additional_Performance'] >= l2[k - 1]) and (P.loc[j, 'Additional_Performance'] < l2[k])) and (P.loc[j, 'POS_RES%'] <= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= int(l2[k])) and (
                                                P.loc[j, 'POS_RES%'] <= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB' or A.loc[i, 'STATUS'] == 'RB' or A.loc[
                                                i, 'STATUS'] == 'NM' or A.loc[i, 'STATUS'] == 'FORECLOSE' or A.loc[
                                                i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif (P.loc[j, 'Additional_Performance'] <= l2[k]) and ((P.loc[j, 'POS_RES%'] >= BKT2T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT2T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l2[k]) and (P.loc[j, 'POS_RES%'] <= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif ((P.loc[j, 'Additional_Performance'] >= l2[k - 1]) and (P.loc[j, 'Additional_Performance'] < l2[k])) and ((P.loc[j, 'POS_RES%'] >= BKT2T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT2T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l - 1, l2[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l - 1, l2[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l - 1, l2[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l2[k]) and ((P.loc[j, 'POS_RES%'] >= BKT2T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT2T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == "FORECLOSE") or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l - 1, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l - 1, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l - 1, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 7) and (l == 9):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif (P.loc[j, 'Additional_Performance'] >= l2[k]) and (P.loc[j, 'POS_RES%'] >= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 250
                                        elif ((P.loc[j, 'Additional_Performance'] > float(l2[k - 1])) and (P.loc[j, 'Additional_Performance'] <= l2[k])) and (P.loc[j, 'POS_RES%'] <= BKT2T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] > l2[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l2[k])) and ((P.loc[j, 'POS_RES%'] > BKT2T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT2T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT2.loc[l, l2[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT2.loc[l, l2[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT2.loc[l, l2[k]], A.loc[i, 'MOHAK'])

            # =============================================================================
            # BKT-3
            # =============================================================================

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 3:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 3:
                            for k in range(0, len(l3)):
                                for l in range(0, len(BKT3)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l3[k]) and (P.loc[j, 'POS_RES%'] <= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l3[k - 1]) and (P.loc[j, 'Additional_Performance'] < l3[k])) and (P.loc[j, 'POS_RES%'] <= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= int(l3[k])) and (P.loc[j, 'POS_RES%'] <= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l3[k]) and ((P.loc[j, 'POS_RES%'] >= BKT3T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT3T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l3[k]) and (P.loc[j, 'POS_RES%'] <= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l3[k - 1]) and (P.loc[j, 'Additional_Performance'] < l3[k])) and ((P.loc[j, 'POS_RES%'] >= BKT3T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT3T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l - 1, l3[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l - 1, l3[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l - 1, l3[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l - 1, l3[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l - 1, l3[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l3[k]) and ((P.loc[j, 'POS_RES%'] >= BKT3T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT3T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l - 1, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l - 1, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l - 1, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == "FORECLOSE") or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l - 1, l3[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 9):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] >= l3[k]) and (P.loc[j, 'POS_RES%'] >= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l == 7):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l3[k]) and (P.loc[j, 'POS_RES%'] >= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] > l3[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l3[k])) and (P.loc[j, 'POS_RES%'] <= BKT3T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] > l3[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l3[k])) and ((P.loc[j, 'POS_RES%'] > BKT3T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT3T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT3.loc[l, l3[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT3.loc[l, l3[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT3.loc[l, l3[k]], A.loc[i, 'MOHAK'])

            # =============================================================================
            # BKT-4
            # =============================================================================

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 4:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 4:
                            for k in range(0, len(l4)):
                                for l in range(0, len(BKT4)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l4[k]) and (P.loc[j, 'POS_RES%'] <= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l4[k - 1]) and (P.loc[j, 'Additional_Performance'] < l4[k])) and (P.loc[j, 'POS_RES%'] <= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= int(l4[k])) and (P.loc[j, 'POS_RES%'] <= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l4[k]) and ((P.loc[j, 'POS_RES%'] >= BKT4T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT4T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l4[k]) and (P.loc[j, 'POS_RES%'] <= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l4[k - 1]) and (P.loc[j, 'Additional_Performance'] < l4[k])) and ((P.loc[j, 'POS_RES%'] >= BKT4T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT4T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l - 1, l4[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l - 1, l4[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l - 1, l4[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l4[k]) and ((P.loc[j, 'POS_RES%'] >= BKT4T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT4T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l - 1, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l - 1, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l - 1, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == "FORECLOSE") or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l - 1, l4[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 9):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] >= l4[k]) and (P.loc[j, 'POS_RES%'] >= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] > l4[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l4[k])) and (P.loc[j, 'POS_RES%'] <= BKT4T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] > l4[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l4[k])) and ((P.loc[j, 'POS_RES%'] > BKT4T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT4T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT4.loc[l, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT4.loc[l, l4[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT4.loc[l, l4[k]], A.loc[i, 'MOHAK'])

            # =============================================================================
            # BKT-5
            # =============================================================================

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 5:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 5:
                            for k in range(0, len(l5)):
                                for l in range(0, len(BKT5)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l5[k]) and (P.loc[j, 'POS_RES%'] <= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l5[k - 1]) and (P.loc[j, 'Additional_Performance'] < l5[k])) and (P.loc[j, 'POS_RES%'] <= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= int(l5[k])) and (P.loc[j, 'POS_RES%'] <= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 0) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l5[k]) and ((P.loc[j, 'POS_RES%'] >= BKT5T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT5T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l5[k]) and (P.loc[j, 'POS_RES%'] <= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l5[k - 1]) and (P.loc[j, 'Additional_Performance'] < l5[k])) and ((P.loc[j, 'POS_RES%'] >= BKT5T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT5T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l - 1, l5[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l - 1, l5[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l - 1, l5[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l5[k]) and ((P.loc[j, 'POS_RES%'] >= BKT5T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT5T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l - 1, l4[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l - 1, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l - 1, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == "FORECLOSE") or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l - 1, l5[k]], A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 9):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] >= l5[k]) and (P.loc[j, 'POS_RES%'] >= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] > l5[k - 1])and (P.loc[j, 'Additional_Performance'] <= l5[k])) and (P.loc[j, 'POS_RES%'] <= BKT5T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] > l5[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l5[k])) and ((P.loc[j, 'POS_RES%'] > BKT5T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT5T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT5.loc[l, l5[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
                                                A.loc[i, 'percentage'] = str(15) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], str(15), A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT5.loc[l, l5[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT5.loc[l, l5[k]], A.loc[i, 'MOHAK'])

            # =============================================================================
            # BKT-6
            # =============================================================================

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 6:
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 6:
                            for k in range(0, len(l6)):
                                for l in range(0, len(BKT6)):
                                    if (k == 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] <= l6[k]) and (P.loc[j, 'POS_RES%'] <= BKT6T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = a
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l6[k - 1]) and (P.loc[j, 'Additional_Performance'] < l6[k])) and (P.loc[j, 'POS_RES%'] <= BKT6T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'Percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l1[k]) and (P.loc[j, 'POS_RES%'] <= BKT6T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l > 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] >= l6[k - 1]) and (P.loc[j, 'Additional_Performance'] < l6[k])) and ((P.loc[j, 'POS_RES%'] >= BKT6T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT6T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l - 1, l6[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l - 1, l6[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l - 1, l6[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'Percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                        elif (P.loc[j, 'Additional_Performance'] >= l6[k]) and ((P.loc[j, 'POS_RES%'] >= BKT6T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] < BKT6T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l - 1, l6[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l - 1, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l - 1, l6[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == "FORECLOSE") or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                    elif (k == 6) and (l == 6):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif (P.loc[j, 'Additional_Performance'] >= l6[k]) and (P.loc[j, 'POS_RES%'] >= BKT6T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l == 0):
                                        if A.loc[i, 'STATUS'] == 'RT':
                                            A.loc[i, 'MOHAK'] = 150
                                        elif ((P.loc[j, 'Additional_Performance'] > l6[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l6[k])) and (P.loc[j, 'POS_RES%'] <= BKT6T.loc[l, 'TARGET']):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k - 1]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k - 1]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                    elif (k > 0) and (l > 0):
                                        if ((P.loc[j, 'Additional_Performance'] > l6[k - 1]) and (P.loc[j, 'Additional_Performance'] <= l1[k])) and ((P.loc[j, 'POS_RES%'] > BKT6T.loc[l - 1, 'TARGET']) and (P.loc[j, 'POS_RES%'] <=BKT6T.loc[l, 'TARGET'])):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * BKT6.loc[l, l6[k]] / 100
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
                                                A.loc[i, 'percentage'] = str(20) + '%'
                                                A.loc[i, 'MOHAK'] = c
                                                print(A.loc[i, 'AGREEMENTID'], 20, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'percentage'] = str(BKT6.loc[l, l6[k]]) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], BKT6.loc[l, l6[k]], A.loc[i, 'MOHAK'])

            A.rename({'MOHAK': 'PAYOUT'}, axis=1, inplace=True)

            A.to_excel('media/IDFC_TW/FOS Salary/MASTER FILE IDFC_TW.xlsx', index=False)

            A.to_excel('media/IDFC_TW/Billing/Final_Billing_IDFC_TW.xlsx', index=False)

            F = pd.DataFrame(A.groupby('BKT')['PAYOUT'].sum()).reset_index()

            for i in range(0, len(F['PAYOUT'])):
                F.loc[i, 'PAYOUT'] = round(F.loc[i, 'PAYOUT'], 2)

            A['PAYOUT'].fillna(0, inplace=True)
            F.to_excel('media/IDFC_TW/Billing/BKT_Billing_IDFC_TW.xlsx', index=False)
            F2 = F.copy()

            Total_Payout = round(sum(A['PAYOUT']), 2)

        else:
            return HttpResponseRedirect(reverse('basic_app:IDFC_TW_MIS'))

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/Billing/Final_Billing_IDFC_TW.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_TW/Billing')
            AA = fs.open('BKT_Billing_IDFC_TW.xlsx')
            F2 = pd.read_excel(AA)
            Total_Payout = round(sum(F2['PAYOUT']), 2)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/Billing.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C1 = list(F2.columns)

    for j in range(0, len(F2[C1[0]])):
        row_data1 = list()
        for col in range(0, len(C1)):
            row_data1.append(str(F2.loc[j, C1[col]]))
        excel_data1.append(row_data1)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/Billing.html', {'Billing': excel_data1, 'columns': C1, 'Total_Payout': Total_Payout, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_HL_MIS(request):
    excel_data = []
    F1 = pd.DataFrame()

    if request.method == 'POST':
        Allocation1 = request.FILES['Allocation']
        Paidfile1 = request.FILES['Paid_File']
        A = pd.read_excel(Allocation1)
        B = pd.read_excel(Paidfile1)

        for i in range(0, len(A['AGREEMENTID'])):
            if pd.isnull(A['AGREEMENTID'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i, 'CUSTOMERNAME'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i, 'TC NAME'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i, 'TL'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i, 'FOS'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i, 'AREA'], str) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'BKT'], np.str) == False or pd.isnull(A['BKT'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'BKT DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'POS'], np.float64) == False or pd.isnull(A['POS'][i]) == True:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            elif isinstance(A.loc[i, 'EMI'], np.float64) == True and pd.isnull(A['EMI'][i]) == False:
                print('error', i)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            else:
                continue

        fs = FileSystemStorage(location='media/IDFC_HL/MIS')
        fs.save(Allocation1.name, Allocation1)
        fs.save(Paidfile1.name, Paidfile1)
        print(A.head())

        B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

        for i in range(0, len(A['AGREEMENTID'])):
            for k in range(0, len(B['AGREEMENTID'])):
                if (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and ((B.loc[k, 'AGAINST'] != 'FORECLOSE') and (B.loc[k, 'AGAINST'] != 'SETTLEMENT')):
                    for j in range(0, len(B1['AGREEMENTID'])):
                        if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
                            if (A.loc[i, 'BKT'] != 'BKT0') and (A.loc[i, 'BKT'] != 'BKT12') and (A.loc[i, 'BKT'] != 'BKT1') and (A.loc[i, 'BKT'] != 'BKT10'):
                                a = (int(A.loc[i, 'BKT'][-1]) + 1) * A.loc[i, 'EMI']
                                b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                                if (B1.loc[j, 'PAID AMOUNT'] >= a) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
                                    A.loc[i, 'STATUS'] = 'NM'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= b) and (B1.loc[j, 'PAID AMOUNT'] < a) and (B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'POS']):
                                    A.loc[i, 'STATUS'] = 'RB'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                            elif A.loc[i, 'BKT'] == 'BKT1':
                                b = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                                if (B1.loc[j, 'PAID AMOUNT'] >= b) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
                                    A.loc[i, 'STATUS'] = 'NM'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < b):
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                            elif (A.loc[i, 'BKT'] == 'BKT12') or (A.loc[i, 'BKT'] == 'BKT10'):
                                c = (int(A.loc[i, 'BKT'][-2:]) + 1) * A.loc[i, 'EMI']
                                d = A.loc[i, 'EMI'] + A.loc[i, 'EMI']
                                if (B1.loc[j, 'PAID AMOUNT'] >= c) or (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']):
                                    A.loc[i, 'STATUS'] = 'NM'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= d) and (B1.loc[j, 'PAID AMOUNT'] < c):
                                    A.loc[i, 'STATUS'] = 'RB'
                                elif (B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']) and (B1.loc[j, 'PAID AMOUNT'] < d):
                                    A.loc[i, 'STATUS'] = 'SB'
                                elif B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                            elif A.loc[i, 'BKT'] == 'BKT0':
                                if B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
                                    A.loc[i, 'STATUS'] = 'PART PAID'
                                else:
                                    A.loc[i, 'STATUS'] = 'SB'
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'FORECLOSE'):
                    A.loc[i, 'STATUS'] = 'FORECLOSE'
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'SETTLEMENT'):
                    A.loc[i, 'STATUS'] = 'SETTLEMENT'
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'LOAN CANCELED'):
                    A.loc[i, 'STATUS'] = 'LOAN CANCELED'

        A['STATUS'].fillna('FLOW', inplace=True)

        for i in range(0, len(A['AGREEMENTID'])):
            for j in range(0, len(B1['PAID AMOUNT'])):
                if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
                    A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']

        M = pd.DataFrame(A.groupby(['BKT', 'STATE'])['POS'].sum()).reset_index()

        M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)

        R = pd.DataFrame(A.groupby(['BKT', 'STATE'])['AGREEMENTID'].count()).reset_index()

        F = M.merge(R, how='outer')

        F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)

        R1 = pd.DataFrame(A.groupby(['BKT', 'STATE', 'STATUS'])['AGREEMENTID'].count()).reset_index()

        P = F.copy()

        P = P.iloc[:, :3]

        P['FLOW'] = np.nan
        P['SB'] = np.nan
        P['RB'] = np.nan
        P['NM'] = np.nan
        P['PART PAID'] = np.nan
        P['FORECLOSE'] = np.nan
        P['SETTLEMENT'] = np.nan
        P['LOAN CANCELED'] = np.nan

        COL = P.columns

        for i in range(0, len(R1['BKT'])):
            for j in range(0, len(P['FLOW'])):
                for k in range(0, len(COL)):
                    if ((R1.loc[i, ['BKT', 'STATE']] == P.loc[j, ['BKT', 'STATE']]).all()) and (R1.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']

        F = F.merge(P, how='outer')

        F.fillna(0, inplace=True)

        F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
                  'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES',
                  'LOAN CANCELED': 'LOAN_CANCELED_CASES'}, axis=1, inplace=True)

        R2 = pd.DataFrame(A.groupby(['BKT', 'STATE', 'STATUS'])['POS'].sum()).reset_index()

        for i in range(0, len(R2['BKT'])):
            for j in range(0, len(P['FLOW'])):
                for k in range(0, len(COL)):
                    if ((R2.loc[i, ['BKT', 'STATE']] == P.loc[j, ['BKT', 'STATE']]).all()) and (R2.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R2.loc[i, 'POS']

        F = F.merge(P, how='outer')

        F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
                  'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS', 'LOAN CANCELED': 'LOAN_CANCELED_POS'},
                 axis=1, inplace=True)

        F.fillna(0, inplace=True)

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'LOAN_CANCELED%'] = round((F.loc[i, 'LOAN_CANCELED_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)

        TP = pd.DataFrame(A.groupby(['BKT', 'STATE'])['TOTAL PAID'].sum()).reset_index()

        F = F.merge(TP, how='outer')

        for i in range(0, len(F['SB_POS'])):
            F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + F.loc[
                i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%'] + F.loc[i, 'LOAN_CANCELED%']
            F.loc[i, 'Additional_Performance'] = F.loc[i, 'RB_POS%'] + F.loc[i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%']

        F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
                  'SETTLEMENT_CASES': 'SC_CASES',
                  'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
                  'FORECLOSE_POS%': 'FC_POS%',
                  'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
                 inplace=True)

        for i in range(0,len(F['SB_POS'])):
            F.loc[i,'TOTAL_POS']=round(F.loc[i,'TOTAL_POS'],2)
            F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
            F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
            F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'], 2)
            F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'], 2)
            F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
            F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
            F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
            F.loc[i, 'Additional_Performance'] = round(F.loc[i, 'Additional_Performance'], 2)
            F.loc[i, 'POS_RES%'] = round(F.loc[i, 'POS_RES%'], 2)


        F.replace(0, np.nan, inplace=True)

        F.to_excel('media/IDFC_HL/MIS/IDFC_HL_MIS.xlsx', index=False)

        F.replace(np.nan, 0, inplace=True)

        F.to_excel('media/IDFC_HL/Billing/Performance_IDFC_HL.xlsx', index=False)
        F.to_excel('media/IDFC_HL/MIS/Performance_IDFC_HL.xlsx', index=False)

        for i in range(0, len(A['AGREEMENTID'])):
            s = 0
            for j in range(0, len(B['AGREEMENTID'])):
                if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and ((A.loc[i, 'STATUS'] == 'NM') or (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT')) and (B.loc[j, 'MODE'] != 'ECS'):
                    s = s + B.loc[j, 'PAID AMOUNT']
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and (A.loc[i, 'STATUS'] == 'SB') and (B.loc[j, 'MODE'] != 'ECS'):
                    s = s + B.loc[j, 'PAID AMOUNT']
                elif (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and (A.loc[i, 'STATUS'] == 'RB'):
                    s = s + B.loc[j, 'PAID AMOUNT']
            A.loc[i, 'Billing PAID AMT.'] = s

        for i in range(0, len(A['STATE'])):
            if A.loc[i, 'STATUS'] == 'SB':
                if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']:
                    A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']

        A.to_excel('media/IDFC_HL/Billing/MASTER_FILE_IDFC_HL.xlsx', index=False)

        A.to_excel('media/IDFC_HL/TC Performance/MASTER_FILE_IDFC_HL.xlsx', index=False)

        A.to_excel('media/IDFC_HL/MIS/MASTER_FILE_IDFC_HL.xlsx', index=False)

        A.to_excel('media/IDFC_HL/FOS Salary/MASTER_FILE_IDFC_HL.xlsx', index=False)

        F1 = F.copy()

        ## TL-Wise Performace

        M = pd.DataFrame(A.groupby(['BKT', 'TL'])['POS'].sum()).reset_index()

        M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)

        R = pd.DataFrame(A.groupby(['BKT', 'TL'])['AGREEMENTID'].count()).reset_index()

        F = M.merge(R, how='outer')

        F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)

        R1 = pd.DataFrame(A.groupby(['BKT', 'TL', 'STATUS'])['AGREEMENTID'].count()).reset_index()

        R1 = pd.DataFrame(A.groupby(['BKT', 'TL', 'STATUS'])['AGREEMENTID'].count()).reset_index()

        P = F.copy()

        P = P.iloc[:, :2]

        P['FLOW'] = np.nan
        P['SB'] = np.nan
        P['RB'] = np.nan
        P['NM'] = np.nan
        P['PART PAID'] = np.nan
        P['FORECLOSE'] = np.nan
        P['SETTLEMENT'] = np.nan
        P['LOAN CANCELED'] = np.nan

        COL = P.columns

        for i in range(0, len(R1['BKT'])):
            for j in range(0, len(P['BKT'])):
                for k in range(0, len(COL)):
                    if ((R1.loc[i, ['BKT', 'TL']] == P.loc[j, ['BKT', 'TL']]).all()) and (R1.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']

        F = F.merge(P, how='outer')

        F.fillna(0, inplace=True)

        F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
                  'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES',
                  'LOAN CANCELED': 'LOAN_CANCELED_CASES'}, axis=1, inplace=True)

        R2 = pd.DataFrame(A.groupby(['BKT', 'TL', 'STATUS'])['POS'].sum()).reset_index()

        for i in range(0, len(R2['BKT'])):
            for j in range(0, len(P['BKT'])):
                for k in range(0, len(COL)):
                    if ((R2.loc[i, ['BKT', 'TL']] == P.loc[j, ['BKT', 'TL']]).all()) and (R2.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R2.loc[i, 'POS']

        F = F.merge(P, how='outer')

        F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
                  'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS', 'LOAN CANCELED': 'LOAN_CANCELED_POS'},
                 axis=1, inplace=True)

        F.fillna(0, inplace=True)

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'LOAN_CANCELED%'] = round((F.loc[i, 'LOAN_CANCELED_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)

        TP = pd.DataFrame(A.groupby(['BKT', 'TL'])['TOTAL PAID'].sum()).reset_index()

        F = F.merge(TP, how='outer')

        for i in range(0, len(F['SB_POS'])):
            F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + F.loc[
                i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%'] + F.loc[i, 'LOAN_CANCELED%']

        for i in range(0, len(F['SB_CASES'])):
            F.loc[i, 'Additional_Performance'] = F.loc[i, 'RB_POS%'] + F.loc[i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%']

        F.replace(0, np.nan, inplace=True)

        F.to_excel(r'media/IDFC_HL/MIS/MIS TL-WISE.xlsx', index=False)


    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/MIS/Performance_IDFC_HL.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_HL/MIS')
            AA = fs.open('Performance_IDFC_HL.xlsx')
            F1 = pd.read_excel(AA)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C = list(F1.columns)

    for j in range(0, len(F1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(F1.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/upload_excel.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_HL_BILLING(request):
    excel_data1 = []
    F2 = pd.DataFrame()
    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/Billing/MASTER_FILE_IDFC_HL.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_HL/Billing')
            AA = fs.open('Performance_IDFC_HL.xlsx')
            AA1 = fs.open('MASTER_FILE_IDFC_HL.xlsx')
            AA2 = fs.open('BKT 0 Res.xlsx')
            AA3 = fs.open('BKT 1 Res.xlsx')
            AA4 = fs.open('BKT 1 Rollback.xlsx')
            AA5 = fs.open('BKT 2 Res.xlsx')
            AA6 = fs.open('BKT 2 Rollback.xlsx')
            AA7 = fs.open('BKT 3 Res.xlsx')
            AA8 = fs.open('BKT 3 Rollback.xlsx')
            AA9 = fs.open('BKT 4 Res.xlsx')
            AA10 = fs.open('BKT 4 Rollback.xlsx')
            AA11 = fs.open('BKT 5 Res.xlsx')
            AA12 = fs.open('BKT 5 Rollback.xlsx')
            AA13 = fs.open('BKT 6 Res.xlsx')
            AA14 = fs.open('BKT 6 Rollback.xlsx')
            AA15 = fs.open('BKT 7 Res.xlsx')
            AA16 = fs.open('BKT 7 Rollback.xlsx')
            AA17 = fs.open('BKT 8 Res.xlsx')
            AA18 = fs.open('BKT 8 Rollback.xlsx')
            AA19 = fs.open('BKT 9 Res.xlsx')
            AA20 = fs.open('BKT 9 Rollback.xlsx')
            AA21 = fs.open('BKT 10 Res.xlsx')
            AA22 = fs.open('BKT 10 Rollback.xlsx')
            AA23 = fs.open('BKT 11 Res.xlsx')
            AA24 = fs.open('BKT 11 Rollback.xlsx')
            AA25 = fs.open('BKT 12 Res.xlsx')
            AA26 = fs.open('BKT 12 Rollback.xlsx')
            AA27 = fs.open('BKT 13 Res.xlsx')
            AA28 = fs.open('BKT 13 Rollback.xlsx')


            A = pd.read_excel(AA1)
            P = pd.read_excel(AA)

            P0 = pd.read_excel(AA2)
            P1 = pd.read_excel(AA3)
            R1 = pd.read_excel(AA4)
            P2 = pd.read_excel(AA5)
            R2 = pd.read_excel(AA6)
            P3 = pd.read_excel(AA7)
            R3 = pd.read_excel(AA8)
            P4 = pd.read_excel(AA9)
            R4 = pd.read_excel(AA10)
            P5 = pd.read_excel(AA11)
            R5 = pd.read_excel(AA12)
            P6 = pd.read_excel(AA13)
            R6 = pd.read_excel(AA14)
            P7 = pd.read_excel(AA15)
            R7 = pd.read_excel(AA16)
            P8 = pd.read_excel(AA17)
            R8 = pd.read_excel(AA18)
            P9 = pd.read_excel(AA19)
            R9 = pd.read_excel(AA20)
            P10 = pd.read_excel(AA21)
            R10 = pd.read_excel(AA22)
            P11 = pd.read_excel(AA23)
            R11 = pd.read_excel(AA24)
            P12 = pd.read_excel(AA25)
            R12 = pd.read_excel(AA26)
            P13 = pd.read_excel(AA27)
            R13 = pd.read_excel(AA28)

            CAP = pd.DataFrame(
                {'BKT0': 5500, 'BKT1': 5500, 'BKT2': 5500, 'BKT3': 5500, 'BKT4': 5500, 'BKT5': 5500, 'BKT6': 5500, 'BKT7': 5500,
                 'BKT8': 5500, 'BKT9': 5500, 'BKT10': 5500, 'BKT11': 5500, 'BKT12': 5500, 'BKT13': 5500}, index=[0])
            RB_CAP = pd.DataFrame(
                {'BKT0': 5500, 'BKT1': 11000, 'BKT2': 11000, 'BKT3': 11000, 'BKT4': 11000, 'BKT5': 11000, 'BKT6': 11000,
                 'BKT7': 11000, 'BKT8': 11000, 'BKT9': 11000, 'BKT10': 11000, 'BKT11': 11000, 'BKT12': 11000, 'BKT13': 11000},
                index=[0])

            l0 = list(P0.columns)
            l1 = list(P1.columns)
            l2 = list(P2.columns)
            l3 = list(P3.columns)
            l4 = list(P4.columns)
            l5 = list(P5.columns)
            l6 = list(P6.columns)
            l7 = list(P7.columns)
            l8 = list(P8.columns)
            l9 = list(P9.columns)
            l10 = list(P10.columns)
            l11 = list(P11.columns)
            l12 = list(P12.columns)
            l13 = list(P13.columns)

            # BKT0

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT0':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT0':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l0)):
                                    if k == 0:
                                        if P.loc[j, 'POS_RES%'] <= l0[k]:
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                a = A.loc[i, 'Billing PAID AMT.'] * P0.loc[0, l0[k]] / 100
                                                if a > CAP.loc[0, 'BKT0']:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT0']
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = a
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                if b > 25000:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = 25000
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = b
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                    elif k == 4:
                                        if P.loc[j, 'POS_RES%'] >= l0[k]:
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * P0.loc[0, l0[k]] / 100
                                                if c > CAP.loc[0, 'BKT0']:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT0']
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = c
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                if d > 25000:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = 25000
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = d
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif P.loc[j, 'POS_RES%'] >= l0[k]:
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * P0.loc[0, l0[k]] / 100
                                                if c > CAP.loc[0, 'BKT0']:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT0']
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k]]) + '%'
                                                    A.loc[i, 'MOHAK'] = c
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                if d > 25000:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = 25000
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = d
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                    elif k > 0:
                                        if (P.loc[j, 'POS_RES%'] >= l0[k - 1]) and (P.loc[j, 'POS_RES%'] < l0[k]):
                                            if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                c = A.loc[i, 'Billing PAID AMT.'] * P0.loc[0, l0[k - 1]] / 100
                                                if c > CAP.loc[0, 'BKT0']:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k - 1]]) + '%'
                                                    A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT0']
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k - 1]], A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(P0.loc[0, l0[k - 1]]) + '%'
                                                    A.loc[i, 'MOHAK'] = c
                                                    print(A.loc[i, 'AGREEMENTID'], P0.loc[0, l0[k - 1]], A.loc[i, 'MOHAK'])
                                            elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                if d > 25000:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = 25000
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                    A.loc[i, 'MOHAK'] = d
                                                    print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                            else:
                                                A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                A.loc[i, 'MOHAK'] = 0
                                                print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])

            # BKT1

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT1':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT1':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l1)):
                                    for l in range(0, len(R1['Target'])):
                                        if (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l1[k - 1]) and (P.loc[j, 'POS_RES%'] < l1[k])) and ((P.loc[j, 'Additional_Performance'] >= R1.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R1.loc[l, 'Target'])):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k - 1]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (
                                                            A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 4):
                                            if ((P.loc[j, 'POS_RES%'] >= l1[k - 1]) and (P.loc[j, 'POS_RES%'] < l1[k])) and (P.loc[j, 'Additional_Performance'] >= R1.loc[l, 'Target']):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k - 1]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l1[k]) and (P.loc[j, 'Additional_Performance'] <= R1.loc[l, 'Target']):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if a > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 6) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] > l1[k]) and (P.loc[j, 'Additional_Performance'] <= R1.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (
                                                            A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l1[k]) and (P.loc[j, 'Additional_Performance'] <= R1.loc[l, 'Target']):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (
                                                            A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (
                                                            A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 6) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l1[k - 1]) and (P.loc[j, 'POS_RES%'] < l1[k])) and ((P.loc[j, 'Additional_Performance'] >= R1.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R1.loc[l, 'Target'])):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k - 1]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l1[k]) and ((P.loc[j, 'Additional_Performance'] >= R1.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R1.loc[l, 'Target'])):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 0) and (l > 0):
                                            if (P.loc[j, 'POS_RES%'] <= l1[k]) and ((P.loc[j, 'Additional_Performance'] >= R1.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R1.loc[l, 'Target'])):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l - 1, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l - 1, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l - 1, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 6) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l1[k]) and (P.loc[j, 'Additional_Performance'] >= R1.loc[l, 'Target']):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l1[k - 1]) and (P.loc[j, 'POS_RES%'] < l1[k])) and (P.loc[j, 'Additional_Performance'] <= R1.loc[l, 'Target']):
                                                if A.loc[i, 'STATUS'] == 'SB':
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT1']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P1.loc[l, l1[k - 1]] / 100
                                                    if (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = RB_CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    elif (a > RB_CAP.loc[0, 'BKT1']) and (A.loc[i, 'Billing PAID AMT.'] != A.loc[i, 'TOTAL PAID']):
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT1']
                                                        print(A.loc[i, 'AGREEMENTID'], P1.loc[l, l1[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P1.loc[l, l1[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])

            # BKT2

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT2':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT2':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l2)):
                                    for l in range(0, len(R2['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l2[k]) and (P.loc[j, 'Additional_Performance'] <= R2.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l, l2[k]] / 100
                                                    if a > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l2[k - 1]) and (P.loc[j, 'POS_RES%'] < l2[k])) and (P.loc[j, 'Additional_Performance'] <= R2.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l, l2[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l2[k]) and (P.loc[j, 'Additional_Performance'] <= R2.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l, l2[k]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l2[k - 1]) and (P.loc[j, 'POS_RES%'] < l2[k])) and ((P.loc[j, 'Additional_Performance'] >= R2.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R2.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l - 1, l2[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l2[k]) and ((P.loc[j, 'Additional_Performance'] >= R2.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R2.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l - 1, l2[k]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(2) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l2[k]) and (P.loc[j, 'Additional_Performance'] >= R2.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l, l2[k]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l2[k - 1]) and (P.loc[j, 'POS_RES%'] < l2[k])) and (P.loc[j, 'Additional_Performance'] <= R2.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l, l2[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l2[k - 1]) and (P.loc[j, 'POS_RES%'] < l2[k])) and ((P.loc[j, 'Additional_Performance'] >= R2.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R2.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P2.loc[l - 1, l2[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT2']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT2']
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P2.loc[l - 1, l2[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P2.loc[l - 1, l2[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT3

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT3':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT3':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l3)):
                                    for l in range(0, len(R3['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l3[k]) and (P.loc[j, 'Additional_Performance'] <= R3.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l, l3[k]] / 100
                                                    if a > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l3[k - 1]) and (P.loc[j, 'POS_RES%'] <= l3[k])) and (P.loc[j, 'Additional_Performance'] <= R3.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l, l3[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l3[k]) and (P.loc[j, 'Additional_Performance'] <= R3.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l, l3[k]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l3[k - 1]) and (P.loc[j, 'POS_RES%'] < l3[k])) and ((P.loc[j, 'Additional_Performance'] >= R3.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R3.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l - 1, l3[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l3[k]) and ((P.loc[j, 'Additional_Performance'] >= R3.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R3.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l - 1, l3[k]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l3[k]) and (P.loc[j, 'Additional_Performance'] >= R3.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l, l3[k]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l3[k - 1]) and (P.loc[j, 'POS_RES%'] < l3[k])) and (P.loc[j, 'Additional_Performance'] <= R3.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l, l3[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l3[k - 1]) and (P.loc[j, 'POS_RES%'] < l3[k])) and ((P.loc[j, 'Additional_Performance'] >= R3.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R3.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P3.loc[l - 1, l3[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT3']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT3']
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P3.loc[l - 1, l3[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P3.loc[l - 1, l3[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT4

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT4':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT4':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l4)):
                                    for l in range(0, len(R4['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l4[k]) and (P.loc[j, 'Additional_Performance'] <= R4.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l, l4[k]] / 100
                                                    if a > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l4[k - 1]) and (P.loc[j, 'POS_RES%'] < l4[k])) and (P.loc[j, 'Additional_Performance'] <= R4.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l, l4[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l4[k]) and (P.loc[j, 'Additional_Performance'] <= R4.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l, l4[k]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l4[k - 1]) and (P.loc[j, 'POS_RES%'] < l4[k])) and ((P.loc[j, 'Additional_Performance'] >= R4.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R4.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l - 1, l4[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l4[k]) and ((P.loc[j, 'Additional_Performance'] >= R4.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R4.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l - 1, l4[k]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l4[k]) and (P.loc[j, 'Additional_Performance'] >= R4.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l, l4[k]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l4[k - 1]) and (P.loc[j, 'POS_RES%'] < l4[k])) and (P.loc[j, 'Additional_Performance'] <= R4.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB' or A.loc[i, 'STATUS'] == 'RB' or A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l, l4[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l4[k - 1]) and (P.loc[j, 'POS_RES%'] < l4[k])) and ((P.loc[j, 'Additional_Performance'] >= R4.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R4.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P4.loc[l - 1, l4[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT4']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT4']
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P4.loc[l - 1, l4[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P4.loc[l - 1, l4[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT5

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT5':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT5':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l5)):
                                    for l in range(0, len(R5['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l5[k]) and (P.loc[j, 'Additional_Performance'] <= R5.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l, l5[k]] / 100
                                                    if a > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l5[k - 1]) and (P.loc[j, 'POS_RES%'] < l5[k])) and (P.loc[j, 'Additional_Performance'] <= R5.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l, l5[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l5[k]) and (P.loc[j, 'Additional_Performance'] <= R5.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l, l5[k]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l5[k - 1]) and (P.loc[j, 'POS_RES%'] < l5[k])) and ((P.loc[j, 'Additional_Performance'] >= R5.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R5.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l - 1, l5[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l5[k]) and ((P.loc[j, 'Additional_Performance'] >= R5.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R5.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l - 1, l5[k]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l5[k]) and (P.loc[j, 'Additional_Performance'] >= R5.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l, l5[k]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l5[k - 1]) and (P.loc[j, 'POS_RES%'] < l5[k])) and (P.loc[j, 'Additional_Performance'] <= R5.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l, l5[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l5[k - 1]) and (P.loc[j, 'POS_RES%'] < l5[k])) and ((P.loc[j, 'Additional_Performance'] >= R5.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R5.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P5.loc[l - 1, l5[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT5']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT5']
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P5.loc[l - 1, l5[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P5.loc[l - 1, l5[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT6

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT6':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT6':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l6)):
                                    for l in range(0, len(R6['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l6[k]) and (P.loc[j, 'Additional_Performance'] <= R6.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l, l6[k]] / 100
                                                    if a > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l6[k - 1]) and (P.loc[j, 'POS_RES%'] < l6[k])) and (P.loc[j, 'Additional_Performance'] <= R6.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l, l6[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l6[k]) and (P.loc[j, 'Additional_Performance'] <= R6.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l, l6[k]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l6[k - 1]) and (P.loc[j, 'POS_RES%'] < l6[k])) and ((P.loc[j, 'Additional_Performance'] >= R6.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R6.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l - 1, l6[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l6[k]) and ((P.loc[j, 'Additional_Performance'] >= R6.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R6.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l - 1, l6[k]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) or (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l6[k]) and (P.loc[j, 'Additional_Performance'] >= R6.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l, l6[k]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l6[k - 1]) and (P.loc[j, 'POS_RES%'] < l6[k])) and (P.loc[j, 'Additional_Performance'] <= R6.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l, l6[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l, l6[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l6[k - 1]) and (P.loc[j, 'POS_RES%'] < l6[k])) and ((P.loc[j, 'Additional_Performance'] >= R6.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R6.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P6.loc[l - 1, l6[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT6']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT6']
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P6.loc[l - 1, l6[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P6.loc[l - 1, l6[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT7

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT7':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT7':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l7)):
                                    for l in range(0, len(R7['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l7[k]) and (P.loc[j, 'Additional_Performance'] <= R7.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l, l7[k]] / 100
                                                    if a > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l7[k - 1]) and (P.loc[j, 'POS_RES%'] < l7[k])) and (P.loc[j, 'Additional_Performance'] <= R7.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l, l7[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l7[k]) and (P.loc[j, 'Additional_Performance'] <= R7.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l, l7[k]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l7[k - 1]) and (P.loc[j, 'POS_RES%'] < l7[k])) and ((P.loc[j, 'Additional_Performance'] >= R7.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R7.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l - 1, l7[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l7[k]) and ((P.loc[j, 'Additional_Performance'] >= R7.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R7.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l - 1, l7[k]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l7[k]) and P.loc[j, 'Additional_Performance'] >= \
                                                    R7.loc[l, 'Target']:
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l, l7[k]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l7[k - 1]) and (P.loc[j, 'POS_RES%'] < l7[k])) and (P.loc[j, 'Additional_Performance'] <= R7.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l, l7[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l7[k - 1]) and (P.loc[j, 'POS_RES%'] < l7[k])) and ((P.loc[j, 'Additional_Performance'] >= R7.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R7.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P7.loc[l - 1, l7[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT7']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT7']
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P7.loc[l - 1, l7[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P7.loc[l - 1, l7[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT8

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT8':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT8':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l8)):
                                    for l in range(0, len(R8['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l8[k]) and (P.loc[j, 'Additional_Performance'] <= R8.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l, l8[k]] / 100
                                                    if a > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l8[k - 1]) and (P.loc[j, 'POS_RES%'] < l8[k])) and (P.loc[j, 'Additional_Performance'] <= R8.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l, l8[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l8[k]) and (P.loc[j, 'Additional_Performance'] <= R8.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l, l8[k]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l8[k - 1]) and (P.loc[j, 'POS_RES%'] < l8[k])) and ((P.loc[j, 'Additional_Performance'] >= R8.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R8.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l - 1, l8[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l8[k]) and ((P.loc[j, 'Additional_Performance'] >= R8.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R8.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l - 1, l8[k]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l8[k]) and (P.loc[j, 'Additional_Performance'] >= R8.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l, l8[k]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l8[k - 1]) and (P.loc[j, 'POS_RES%'] < l8[k])) and (P.loc[j, 'Additional_Performance'] <= R8.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l, l8[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l8[k - 1]) and (P.loc[j, 'POS_RES%'] < l8[k])) and ((P.loc[j, 'Additional_Performance'] >= R8.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R8.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P8.loc[l - 1, l8[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT8']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT8']
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k - 1]],A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P8.loc[l - 1, l8[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P8.loc[l - 1, l8[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT9

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT9':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT9':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l9)):
                                    for l in range(0, len(R9['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l9[k]) and (P.loc[j, 'Additional_Performance'] <= R9.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k]] / 100
                                                    if a > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l9[k - 1]) and (P.loc[j, 'POS_RES%'] < l9[k])) and (P.loc[j, 'Additional_Performance'] <= R9.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l9[k]) and (P.loc[j, 'Additional_Performance'] <= R9.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l9[k - 1]) and (P.loc[j, 'POS_RES%'] < l9[k])) and ((P.loc[j, 'Additional_Performance'] >= R9.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] <= R9.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l - 1, l9[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l9[k]) and ((P.loc[j, 'Additional_Performance'] >= R9.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R9.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l - 1, l9[k]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l9[k]) and (P.loc[j, 'Additional_Performance'] >= R9.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (k == 4) and (l == 4):
                                                if (P.loc[j, 'POS_RES%'] >= l9[k]) and (
                                                        P.loc[j, 'Additional_Performance'] >= R9.loc[l, 'Target']):
                                                    if (A.loc[i, 'STATUS'] == 'SB' or A.loc[i, 'STATUS'] == 'RB' or A.loc[
                                                        i, 'STATUS'] == 'NM'):
                                                        c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k]] / 100
                                                        if c > CAP.loc[0, 'BKT9']:
                                                            A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                            A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                            print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                        else:
                                                            A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k]]) + '%'
                                                            A.loc[i, 'MOHAK'] = c
                                                            print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k]], A.loc[i, 'MOHAK'])
                                                    elif A.loc[i, 'STATUS'] == 'FORECLOSE' or A.loc[
                                                        i, 'STATUS'] == 'SETTLEMENT':
                                                        d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                        if d > 25000:
                                                            A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                            A.loc[i, 'MOHAK'] = 25000
                                                            print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                        else:
                                                            A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                            A.loc[i, 'MOHAK'] = d
                                                            print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                        A.loc[i, 'MOHAK'] = 0
                                                        print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l9[k - 1]) and (P.loc[j, 'POS_RES%'] < l9[k])) and (P.loc[j, 'Additional_Performance'] <= R9.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l, l9[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l, l9[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l9[k - 1]) and (P.loc[j, 'POS_RES%'] < l9[k])) and ((P.loc[j, 'Additional_Performance'] >= R9.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R9.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P9.loc[l - 1, l9[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT9']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT9']
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P9.loc[l - 1, l9[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P9.loc[l - 1, l9[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT10

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT10':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT10':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l10)):
                                    for l in range(0, len(R10['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l10[k]) and (P.loc[j, 'Additional_Performance'] <= R10.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l, l10[k]] / 100
                                                    if a > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l10[k - 1]) and (P.loc[j, 'POS_RES%'] < l10[k])) and (P.loc[j, 'Additional_Performance'] <= R10.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l, l10[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l10[k]) and (P.loc[j, 'Additional_Performance'] <= R10.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l, l10[k]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l10[k - 1]) and (P.loc[j, 'POS_RES%'] < l10[k])) and ((P.loc[j, 'Additional_Performance'] >= R10.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R10.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l - 1, l10[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l10[k]) and ((P.loc[j, 'Additional_Performance'] >= R10.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R10.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l - 1, l10[k]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l10[k]) and (P.loc[j, 'Additional_Performance'] >= R10.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l, l10[k]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l10[k - 1]) and (P.loc[j, 'POS_RES%'] < l10[k])) and (P.loc[j, 'Additional_Performance'] <= R10.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l, l10[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l10[k - 1]) and (P.loc[j, 'POS_RES%'] < l10[k])) and ((P.loc[j, 'Additional_Performance'] >= R10.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R10.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P10.loc[l - 1, l10[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT10']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT10']
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P10.loc[l - 1, l10[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P10.loc[l - 1, l10[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT11

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT11':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT11':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l11)):
                                    for l in range(0, len(R11['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l11[k]) and (P.loc[j, 'Additional_Performance'] <= R11.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l, l11[k]] / 100
                                                    if a > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l11[k - 1]) and (P.loc[j, 'POS_RES%'] < l11[k])) and (P.loc[j, 'Additional_Performance'] <= R11.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l, l11[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l11[k]) and (P.loc[j, 'Additional_Performance'] <= R11.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l, l11[k]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l11[k - 1]) and (P.loc[j, 'POS_RES%'] < l11[k])) and ((P.loc[j, 'Additional_Performance'] >= R11.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R11.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l - 1, l11[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l11[k]) and ((P.loc[j, 'Additional_Performance'] >= R11.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R11.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l - 1, l11[k]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l11[k]) and (P.loc[j, 'Additional_Performance'] >= R11.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l, l11[k]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l11[k - 1]) and (P.loc[j, 'POS_RES%'] < l11[k])) and (P.loc[j, 'Additional_Performance'] <= R11.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l, l11[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l, l11[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l11[k - 1]) and (P.loc[j, 'POS_RES%'] < l11[k])) and ((P.loc[j, 'Additional_Performance'] >= R11.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R11.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P11.loc[l - 1, l11[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT11']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT11']
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P11.loc[l - 1, l11[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P11.loc[l - 1, l11[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT12

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT12':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT12':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l12)):
                                    for l in range(0, len(R12['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l12[k]) and (P.loc[j, 'Additional_Performance'] <= R12.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l, l12[k]] / 100
                                                    if a > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l12[k - 1]) and (P.loc[j, 'POS_RES%'] < l12[k])) and (P.loc[j, 'Additional_Performance'] <= R12.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l, l12[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l12[k]) and (P.loc[j, 'Additional_Performance'] <= R12.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l, l12[k]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l12[k - 1]) and (P.loc[j, 'POS_RES%'] < l12[k])) and ((P.loc[j, 'Additional_Performance'] >= R12.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R12.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l - 1, l12[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif A.loc[i, 'STATUS'] == 'FORECLOSE' or A.loc[i, 'STATUS'] == 'SETTLEMENT':
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l12[k]) and ((P.loc[j, 'Additional_Performance'] >= R12.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R12.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l - 1, l12[k]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l12[k]) and (P.loc[j, 'Additional_Performance'] >= R12.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l, l12[k]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l12[k - 1]) and (P.loc[j, 'POS_RES%'] < l12[k])) and (P.loc[j, 'Additional_Performance'] <= R12.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l, l12[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l, l12[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l12[k - 1]) and (P.loc[j, 'POS_RES%'] < l12[k])) and ((P.loc[j, 'Additional_Performance'] >= R12.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R12.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P12.loc[l - 1, l12[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT12']
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P12.loc[l - 1, l12[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P12.loc[l - 1, l12[k - 1]],
                                                              A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
            # BKT13

            for j in range(0, len(P['BKT'])):
                if P.loc[j, 'BKT'] == 'BKT13':
                    for i in range(0, len(A['BKT'])):
                        if A.loc[i, 'BKT'] == 'BKT13':
                            if (P.loc[j, ['BKT', 'STATE']] == A.loc[i, ['BKT', 'STATE']]).all():
                                for k in range(0, len(l13)):
                                    for l in range(0, len(R13['Target'])):
                                        if (k == 0) and (l == 0):
                                            if (P.loc[j, 'POS_RES%'] <= l13[k]) and (P.loc[j, 'Additional_Performance'] <= R13.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    a = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l, l13[k]] / 100
                                                    if a > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = a
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    b = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if b > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = b
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l13[k - 1]) and (P.loc[j, 'POS_RES%'] < l13[k])) and (P.loc[j, 'Additional_Performance'] <= R13.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l, l13[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l13[k]) and (P.loc[j, 'Additional_Performance'] <= R13.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l, l13[k]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l13[k - 1]) and (P.loc[j, 'POS_RES%'] < l13[k])) and ((P.loc[j, 'Additional_Performance'] >= R13.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R13.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l - 1, l13[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                            elif (P.loc[j, 'POS_RES%'] >= l13[k]) and ((P.loc[j, 'Additional_Performance'] >= R13.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R13.loc[l, 'Target'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l - 1, l13[k]] / 100
                                                    if c > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k]], A.loc[i, 'MOHAK'])
                                                elif A.loc[i, 'STATUS'] == 'FORECLOSE' or A.loc[i, 'STATUS'] == 'SETTLEMENT':
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k == 4) and (l == 4):
                                            if (P.loc[j, 'POS_RES%'] >= l13[k]) and (P.loc[j, 'Additional_Performance'] >= R13.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l, l13[k]] / 100
                                                    if c > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l == 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l13[k - 1]) and (P.loc[j, 'POS_RES%'] < l13[k])) and (P.loc[j, 'Additional_Performance'] <= R13.loc[l, 'Target']):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l, l13[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT13']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])
                                        elif (k > 0) and (l > 0):
                                            if ((P.loc[j, 'POS_RES%'] >= l13[k - 1]) and (P.loc[j, 'POS_RES%'] < l13[k])) and ((P.loc[j, 'Additional_Performance'] >= R13.loc[l - 1, 'Target']) and (P.loc[j, 'Additional_Performance'] < R13.loc[l, 'Traget'])):
                                                if (A.loc[i, 'STATUS'] == 'SB') or (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
                                                    c = A.loc[i, 'Billing PAID AMT.'] * P13.loc[l - 1, l13[k - 1]] / 100
                                                    if c > CAP.loc[0, 'BKT12']:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = CAP.loc[0, 'BKT13']
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(P13.loc[l - 1, l13[k - 1]]) + '%'
                                                        A.loc[i, 'MOHAK'] = c
                                                        print(A.loc[i, 'AGREEMENTID'], P13.loc[l - 1, l13[k - 1]], A.loc[i, 'MOHAK'])
                                                elif (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT'):
                                                    d = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
                                                    if d > 25000:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = 25000
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                    else:
                                                        A.loc[i, 'PERCENTAGE'] = str(4) + '%'
                                                        A.loc[i, 'MOHAK'] = d
                                                        print(A.loc[i, 'AGREEMENTID'], 4, A.loc[i, 'MOHAK'])
                                                else:
                                                    A.loc[i, 'PERCENTAGE'] = str(0) + '%'
                                                    A.loc[i, 'MOHAK'] = 0
                                                    print(A.loc[i, 'AGREEMENTID'], 0, A.loc[i, 'MOHAK'])

            A.rename({'MOHAK': 'PAYOUT'}, axis=1, inplace=True)

            A.to_excel('media/IDFC_HL/FOS Salary/MASTER_FILE_IDFC_HL.xlsx', index=False)

            A.to_excel('media/IDFC_HL/Billing/Final_Billing_IDFC_HL.xlsx', index=False)

            F = pd.DataFrame(A.groupby('BKT')['PAYOUT'].sum()).reset_index()

            for i in range(0, len(F['PAYOUT'])):
                F.loc[i, 'PAYOUT'] = round(F.loc[i, 'PAYOUT'], 2)

            A['PAYOUT'].fillna(0, inplace=True)
            F.to_excel('media/IDFC_HL/Billing/BKT_Billing_IDFC_HL.xlsx', index=False)
            F2 = F.copy()

            Total_Payout = round(sum(A['PAYOUT']), 2)

        else:
            return HttpResponseRedirect(reverse('basic_app:IDFC_HL_MIS'))

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/Billing/Final_Billing_IDFC_HL.xlsx')):
            fs = FileSystemStorage(location='media/IDFC_HL/Billing')
            AA = fs.open('BKT_Billing_IDFC_HL.xlsx')
            F2 = pd.read_excel(AA)
            Total_Payout = round(sum(F2['PAYOUT']), 2)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/Billing.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C1 = list(F2.columns)

    for j in range(0, len(F2[C1[0]])):
        row_data1 = list()
        for col in range(0, len(C1)):
            row_data1.append(str(F2.loc[j, C1[col]]))
        excel_data1.append(row_data1)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/Billing.html', {'Billing': excel_data1, 'columns': C1, 'Total_Payout': Total_Payout, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

# def FULLERTON_OTR_MIS(request):
#     excel_data = []
#     excel_data11 = []
#     F1 = pd.DataFrame()
#     F11 = pd.DataFrame()
#     status = ''
#     status1 = ''
#     QQ2 = ''
#     QQ1 = ''
#     if request.method == 'POST':
#         Allocation1 = request.FILES['Allocation12']
#         Paidfile1 = request.FILES['Paid_File12']
#         A = pd.read_excel(Allocation1)
#         B = pd.read_excel(Paidfile1)
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if pd.isnull(A['AGREEMENTID'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html',
#                               {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i, 'CUSTOMERNAME'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html',
#                               {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i, 'TC NAME'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i, 'TL'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i, 'FOS'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i, 'AREA'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES'})
#             elif isinstance(A.loc[i, 'POS'], np.float64) == False or pd.isnull(A['POS'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES'})
#             elif isinstance(A.loc[i, 'EMI'], np.int64) == False or pd.isnull(A['EMI'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES'})
#             else:
#                 continue
#
#         fs = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#         fs.save(Allocation1.name, Allocation1)
#         fs.save(Paidfile1.name, Paidfile1)
#         print(A.head())
#
#         B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             for k in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (
#                         (B.loc[k, 'AGAINST'] != 'FORECLOSE') and (B.loc[k, 'AGAINST'] != 'SETTLEMENT')):
#                     for j in range(0, len(B1['AGREEMENTID'])):
#                         if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                             if B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                 A.loc[i, 'STATUS'] = 'PART PAID'
#                             elif B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']:
#                                 A.loc[i, 'STATUS'] = 'SETTLEMENT'
#                             elif B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']:
#                                 A.loc[i, 'STATUS'] = 'SB'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'FORECLOSE'):
#                     A.loc[i, 'STATUS'] = 'FORECLOSE'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'SETTLEMENT'):
#                     A.loc[i, 'STATUS'] = 'SETTLEMENT'
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if str(A.loc[i, 'STATUS']) == 'nan':
#                 A.loc[i, 'STATUS'] = 'FLOW'
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             for j in range(0, len(B1['PAID AMOUNT'])):
#                 if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                     A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']
#
#         M = pd.DataFrame(A.groupby(['PRODUCT'])['POS'].sum()).reset_index()
#
#         M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)
#
#         R = pd.DataFrame(A.groupby(['PRODUCT'])['AGREEMENTID'].count()).reset_index()
#
#         F = M.merge(R, how='outer')
#
#         F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)
#
#         R1 = pd.DataFrame(A.groupby(['PRODUCT', 'STATUS'])['AGREEMENTID'].count()).reset_index()
#
#         P = F.copy()
#
#         P.drop(['TOTAL_POS', 'TOTAL_CASES'], axis=1, inplace=True)
#
#         P['FLOW'] = np.nan
#         P['SB'] = np.nan
#         P['PART PAID'] = np.nan
#         P['FORECLOSE'] = np.nan
#         P['SETTLEMENT'] = np.nan
#
#         COL = P.columns
#
#         for i in range(0, len(R1['PRODUCT'])):
#             for j in range(0, len(P['FLOW'])):
#                 for k in range(0, len(COL)):
#                     if (R1.loc[i, 'PRODUCT'] == P.loc[j, 'PRODUCT']) and (R1.loc[i, 'STATUS'] == COL[k]):
#                         P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']
#
#         F = F.merge(P, how='outer')
#
#         F.fillna(0, inplace=True)
#
#         F.rename(
#             {'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'FORECLOSE': 'FORECLOSE_CASES', 'SETTLEMENT': 'SETTLEMENT_CASES',
#              'PART PAID': 'PART_PAID_CASES'}, axis=1, inplace=True)
#
#         R2 = pd.DataFrame(A.groupby(['PRODUCT', 'STATUS'])['POS'].sum()).reset_index()
#
#         for i in range(0, len(R2['PRODUCT'])):
#             for j in range(0, len(P['PRODUCT'])):
#                 for k in range(0, len(COL)):
#                     if (R2.loc[i, 'PRODUCT'] == P.loc[j, 'PRODUCT']) and (R2.loc[i, 'STATUS'] == COL[k]):
#                         P.loc[j, COL[k]] = R2.loc[i, 'POS']
#
#         F = F.merge(P, how='outer')
#
#         F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'SETTLEMENT': 'SETTLEMENT_POS',
#                   'PART PAID': 'PART_PAID_POS'}, axis=1, inplace=True)
#
#         F.fillna(0, inplace=True)
#
#         for i in range(0, len(F['FLOW_CASES'])):
#             F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#
#         TP = pd.DataFrame(A.groupby(['PRODUCT'])['TOTAL PAID'].sum()).reset_index()
#
#         F = F.merge(TP, how='outer')
#
#         for i in range(0, len(F['SB_POS'])):
#             F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#
#         F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
#                   'SETTLEMENT_CASES': 'SC_CASES',
#                   'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
#                   'FORECLOSE_POS%': 'FC_POS%',
#                   'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
#                  inplace=True)
#         for i in range(0, len(F['FLOW_CASES'])):
#             F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
#             F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
#             F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
#             F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
#             F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
#             F.loc[i, 'TOTAL_POS'] = round(F.loc[i, 'TOTAL_POS'], 2)
#
#         F.to_excel('media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx', index=False)
#
#         F1 = F.copy()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             s = 0
#             for j in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and (
#                         (A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (
#                         A.loc[i, 'STATUS'] == 'SB')) and (B.loc[j, 'MODE'] != 'ECS'):
#                     s = s + B.loc[j, 'PAID AMOUNT']
#             A.loc[i, 'Billing PAID AMT.'] = s
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if (A.loc[i, 'EMI'] > A.loc[i, 'TOTAL PAID']) and (A.loc[i, 'STATUS'] == 'SB'):
#                 A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
#
#         A['TOTAL PAID'].fillna(0, inplace=True)
#
#         A['Billing PAID AMT.'].fillna(0, inplace=True)
#
#         status1 = 'There is DataFrame of OTR'
#
#         A.to_excel('media/FULLERTON_OTR/Billing/MASTER_FILE_FULLERTON_OTR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_OTR/TC Performance/MASTER_FILE_FULLERTON_OTR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_OTR/FOS Salary/MASTER_FILE_FULLERTON_OTR.xlsx', index=False)
#
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#             AA = fs.open('MIS_FULLERTON_FR.xlsx')
#             F11 = pd.read_excel(AA)
#             status = 'There is a data Frame'
#         else:
#             QQ2 = 'Please Upload File for FULLERTON_FR'
#
#     elif request.method != 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx') and os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             fs11 = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#             AA = fs.open('MIS_FULLERTON_OTR.xlsx')
#             AA11 = fs11.open('MIS_FULLERTON_FR.xlsx')
#             F1 = pd.read_excel(AA)
#             F11 = pd.read_excel(AA11)
#             status = 'There is a data Frame'
#
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             AA = fs.open('MIS_FULLERTON_OTR.xlsx')
#             F1 = pd.read_excel(AA)
#             QQ2 = 'Please Upload File for FULLERTON_FR'
#
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#             AA = fs.open('MIS_FULLERTON_FR.xlsx')
#             F11 = pd.read_excel(AA)
#             QQ1 = 'Please Upload File for FULLERTON_OTR'
#             status = 'There is a data Frame'
#             status1 = 'There is no OTR data Frame'
#
#         else:
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#
#             QQ = 'Please Upload File for FULLERTON_FR'
#             QQ1 = 'Please Upload File for FULLERTON_OTR'
#             return render(request, 'FirstLevel/upload_excel.html',
#                           {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'OTR': QQ1, 'FR': QQ, 'Designation': Designation})
#
#     C = list(F1.columns)
#     C11 = list(F11.columns)
#     if status1 != 'There is no OTR data Frame':
#         for j in range(0, len(F1[C[0]])):
#             row_data = list()
#             for col in range(0, len(C)):
#                 row_data.append(str(F1.loc[j, C[col]]))
#             excel_data.append(row_data)
#     if status == 'There is a data Frame':
#         for j in range(0, len(F11[C11[0]])):
#             row_data11 = list()
#             for col in range(0, len(C11)):
#                 row_data11.append(str(F11.loc[j, C11[col]]))
#             excel_data11.append(row_data11)
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#
#     return render(request, 'FirstLevel/upload_excel.html', {'excel1': excel_data11, 'columns1': C11, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel': excel_data, 'columns': C, 'FR': QQ2, 'OTR': QQ1, 'Designation': Designation})

# def FULLERTON_OTR_BILLING(request):
#     Total_Payout = ''
#     final_dep = ''
#     final_process = ''
#     Total_Payout1 = ''
#     QQ = ''
#     QQ1 = ''
#     QQ2 = ''
#     line = ''
#     line2 = ''
#
#     if request.method == 'POST':
#         if os.path.exists(
#                 r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/MASTER_FILE_FULLERTON_OTR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_OTR/Billing')
#             fs1 = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             AA = fs.open('MASTER_FILE_FULLERTON_OTR.xlsx')
#             AA1 = fs1.open('MIS_FULLERTON_OTR.xlsx')
#             for i in range(1, 32, -1):
#                 if os.path.exists(
#                         r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/FULLERTON_OTR_PAID FILE_' + i + 'SEP21.xlsx'):
#                     AA122 = fs1.open('FULLERTON_OTR_PAID FILE_' + i + 'SEP21.xlsx')
#                     PAID_FILE = pd.read_excel(AA122)
#                 else:
#                     continue
#             A = pd.read_excel(AA)
#             P = pd.read_excel(AA1)
#
#             for i in range(0, len(A['PRODUCT'])):
#                 # PL-SAL
#                 if A.loc[i, 'PRODUCT'] == 'PL Sal':
#                     for j in range(0, len(P['PRODUCT'])):
#                         if (A.loc[i, 'PRODUCT'] == P.loc[j, 'PRODUCT']):
#                             if P.loc[j, 'POS_RES%'] < 55:
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 11 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(11) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(11), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 55) and (P.loc[j, 'POS_RES%'] < 65):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 13 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(13) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(13), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 65) and (P.loc[j, 'POS_RES%'] < 70):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(15) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(15), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 70) and (P.loc[j, 'POS_RES%'] < 75):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 17 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(17) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(17), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 75) and (P.loc[j, 'POS_RES%'] < 80):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 19 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(19) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(19), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 80) and (P.loc[j, 'POS_RES%'] < 85):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 21 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(21) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(21), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 85) and (P.loc[j, 'POS_RES%'] < 90):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 23 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(23) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(23), a, P.loc[j, 'PRODUCT'])
#                             elif P.loc[j, 'POS_RES%'] >= 90:
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 25 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(25) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(25), a, P.loc[j, 'PRODUCT'])
#                 # PL-SELF
#                 elif A.loc[i, 'PRODUCT'] == 'PL Self':
#                     for j in range(0, len(P['PRODUCT'])):
#                         if A.loc[i, 'PRODUCT'] == P.loc[j, 'PRODUCT']:
#                             if P.loc[j, 'POS_RES%'] < 55:
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 6 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(6) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(6), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 55) and (P.loc[j, 'POS_RES%'] < 65):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 8 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(8) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(8), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 65) and (P.loc[j, 'POS_RES%'] < 70):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 10 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(10) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(10), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 70) and (P.loc[j, 'POS_RES%'] < 75):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 12 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(12) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(12), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 75) and (P.loc[j, 'POS_RES%'] < 80):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 14 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(14) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(14), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 80) and (P.loc[j, 'POS_RES%'] < 85):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 16 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(16) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(16), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 85) and (P.loc[j, 'POS_RES%'] < 90):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 18 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(18) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(18), a, P.loc[j, 'PRODUCT'])
#                             elif (P.loc[j, 'POS_RES%'] >= 90):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 20 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(20) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'PRODUCT'], P.loc[j, 'POS_RES%'],
#                                           A.loc[i, 'Billing PAID AMT.'], str(20), a, P.loc[j, 'PRODUCT'])
#
#             FLOWLIST = A[A['STATUS'] == 'FLOW'].index
#
#             for i in range(0, len(FLOWLIST)):
#                 A.loc[FLOWLIST[i], 'MOHAK'] = 0
#
#             A[A['MOHAK'].isnull()]['STATUS'].value_counts()
#
#             for i in range(0, len(A['AGREEMENTID'])):
#                 if A.loc[i, 'STATUS'] == 'SETTLEMENT':
#                     for j in range(0, len(PAID_FILE['AGREEMENTID'])):
#                         if A.loc[i, 'AGREEMENTID'] == PAID_FILE.loc[j, 'AGREEMENTID']:
#                             wavier = 100 - round(PAID_FILE.loc[j, 'PAID AMOUNT'] / A.loc[i, 'POS'] * 100)
#                             if (A.loc[i, 'POS'] < 100000):
#                                 if wavier == 0:
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 18 / 100
#                                     if a >= 20000:
#                                         A.loc[i, 'MOHAK'] = 20000
#                                     elif a < 20000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(18) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(18),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 0) and (wavier <= 25):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
#                                     if a >= 15000:
#                                         A.loc[i, 'MOHAK'] = 15000
#                                     elif a < 15000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(15) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(15),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 25) and (wavier <= 50):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 12 / 100
#                                     if a >= 10000:
#                                         A.loc[i, 'MOHAK'] = 10000
#                                     elif a < 10000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(12) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(12),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                             elif (A.loc[i, 'POS'] >= 100000) and (A.loc[i, 'POS'] < 200000):
#                                 if wavier == 0:
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 21 / 100
#                                     if a >= 30000:
#                                         A.loc[i, 'MOHAK'] = 30000
#                                     elif a < 30000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(21) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(21),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 0) and (wavier <= 25):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 18 / 100
#                                     if a >= 25000:
#                                         A.loc[i, 'MOHAK'] = 25000
#                                     elif a < 25000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(18) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(18),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 25) and (wavier <= 50):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 15 / 100
#                                     if a >= 20000:
#                                         A.loc[i, 'MOHAK'] = 20000
#                                     elif a < 20000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(15) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(15),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                             elif (A.loc[i, 'POS'] >= 200000) and (A.loc[i, 'POS'] < 300000):
#                                 if wavier == 0:
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 25 / 100
#                                     if a >= 35000:
#                                         A.loc[i, 'MOHAK'] = 35000
#                                     elif a < 35000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(25) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(25),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 0) and (wavier <= 25):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 22 / 100
#                                     if a >= 30000:
#                                         A.loc[i, 'MOHAK'] = 30000
#                                     elif a < 30000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(22) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(22),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 25) and (wavier <= 50):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 19 / 100
#                                     if a >= 25000:
#                                         A.loc[i, 'MOHAK'] = 25000
#                                     elif a < 25000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(19) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(19),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                             elif (A.loc[i, 'POS'] >= 300000):
#                                 if wavier == 0:
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 30 / 100
#                                     if a >= 40000:
#                                         A.loc[i, 'MOHAK'] = 40000
#                                     elif a < 40000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(30) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(30),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 0) and (wavier <= 25):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 27 / 100
#                                     if a >= 35000:
#                                         A.loc[i, 'MOHAK'] = 35000
#                                     elif a < 35000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(27) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(27),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#                                 elif (wavier > 25) and (wavier <= 50):
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 24 / 100
#                                     if a >= 30000:
#                                         A.loc[i, 'MOHAK'] = 30000
#                                     elif a < 30000:
#                                         A.loc[i, 'MOHAK'] = a
#                                     A.loc[i, 'PERCENTAGE'] = str(24) + '%'
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'Billing PAID AMT.'], str(24),
#                                           A.loc[i, 'MOHAK'],
#                                           wavier)
#
#             A.rename({'MOHAK': 'PAYOUT'}, axis=1, inplace=True)
#
#             A['PAYOUT'].fillna(0, inplace=True)
#
#             A.to_excel(r'media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx', index=False)
#
#             Total_Payout1 = round(sum(A['PAYOUT']), 2)
#
#             line2 = 'Total Payout for OTR = '
#             QQ1 = 'Please click Billing button for FULLERTON_OTR'
#
#             if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/MASTER_FILE_FULLERTON_FR.xlsx'):
#                 fs2 = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # OTR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_FR.xlsx')  # OTR
#                 F2 = pd.read_excel(AA2)  # OTR
#                 Total_Payout = round(sum(F2['PAYOUT']), 2)  # OTR
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 line = 'Total Payout for FR = '
#             else:
#                 QQ = 'Please upload Allocation file for FULLERTON_FR'
#
#         else:
#             return HttpResponseRedirect(reverse('basic_app:FULLERTON_OTR_MIS'))
#
#     elif request.method != 'POST':
#         if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MASTER_FILE_FULLERTON_FR.xlsx') and os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx') and os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs2 = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # FR
#                 fs = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_FR.xlsx')  # FR
#                 AA3 = fs.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                 F2 = pd.read_excel(AA2)  # FR
#                 F3 = pd.read_excel(AA3)  # OTR
#                 line = 'Total Payout for FR = '
#                 line2 = 'Total Payout for OTR = '
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 Total_Payout = round(sum(F2['PAYOUT']), 2)  # FR
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2)  # OTR
#
#             elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                 AA3 = fs.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                 F3 = pd.read_excel(AA3)  # OTR
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2)  # OTR
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 line2 = 'Total Payout for OTR = '
#
#             elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx'):
#                 fs2 = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # OTR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_FR.xlsx')  # OTR
#                 F2 = pd.read_excel(AA2)  # OTR
#                 Total_Payout = round(sum(F2['PAYOUT']), 2)  # OTR
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 line = 'Total Payout for FR = '
#
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 return render(request, 'FirstLevel/Billing.html', {'OTR': QQ1, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs1 = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                 AA1 = fs1.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                 F3 = pd.read_excel(AA1)  # OTR
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2)  # OTR
#                 QQ = 'Please Upload Allocation File for FULLERTON_FR'
#                 QQ1 = 'Please click billing button for FULLERTON_OTR'
#                 line2 = 'Total Payout for OTR = '
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ = 'Please Upload Allocation File for FULLERTON_FR'
#                 QQ1 = 'Please click billing button for FULLERTON_OTR'
#                 return render(request, 'FirstLevel/Billing.html', {'FR': QQ, 'OTR': QQ1, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MASTER_FILE_FULLERTON_FR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx'):
#                 fs = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # FR
#                 AA3 = fs.open('PAYOUT_FULLERTON_FR.xlsx')  # FR
#                 F2 = pd.read_excel(AA3)  # OTR
#                 Total_Payout = round(sum(F2['PAYOUT']), 2)  # FR
#                 QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#                 QQ = 'Please click billing button for FULLERTON_FR'
#                 line = 'Total Payout for FR = '
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ = 'Please click billing button for FULLERTON_FR'
#                 QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#                 return render(request, 'FirstLevel/Billing.html', {'OTR': QQ1, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         else:
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#             QQ = 'Please Upload Allocation File for FULLERTON_FR'
#             QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#             return render(request, 'FirstLevel/Billing.html', {'OTR': QQ1, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#
#     return render(request, 'FirstLevel/Billing.html', {'Total_Payout12': Total_Payout, 'Total_Payout': Total_Payout1, 'FR': QQ, 'OTR': QQ1, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'com': line, 'com2': line2, 'Designation': Designation})

# def FULLERTON_FR_MIS(request):
#     excel_data = [] #OTR
#     excel_data11 = [] #FR
#     F1 = pd.DataFrame() #FR
#     F11 = pd.DataFrame() #OTR
#     status = ''
#     status1 = ''
#     C = ''
#     QQ1 = ''
#     if request.method == 'POST':
#         Allocation1 = request.FILES['Allocation']
#         Paidfile1 = request.FILES['Paid_File']
#         A = pd.read_excel(Allocation1)
#         B = pd.read_excel(Paidfile1)
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if pd.isnull(A['AGREEMENTID'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html',
#                               {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i, 'CUSTOMERNAME'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html',
#                               {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i, 'TC NAME'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i, 'TL'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i, 'FOS'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES'})
#             elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i, 'AREA'], str) == False:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES'})
#             elif isinstance(A.loc[i, 'POS'], np.float64) == False or pd.isnull(A['POS'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES'})
#             elif isinstance(A.loc[i, 'EMI'], np.int64) == False or pd.isnull(A['EMI'][i]) == True:
#                 print('error', i)
#                 return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES'})
#             else:
#                 continue
#
#         fs = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#         fs.save(Allocation1.name, Allocation1)
#         fs.save(Paidfile1.name, Paidfile1)
#         print(A.head())
#
#         B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             for k in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and ((B.loc[k, 'AGAINST'] != 'FORECLOSE') and (B.loc[k, 'AGAINST'] != 'SETTLEMENT')):
#                     for j in range(0, len(B1['AGREEMENTID'])):
#                         if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                             if B1.loc[j, 'PAID AMOUNT'] < A.loc[i, 'EMI']:
#                                 A.loc[i, 'STATUS'] = 'PART PAID'
#                             elif B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'POS']:
#                                 A.loc[i, 'STATUS'] = 'SETTLEMENT'
#                             elif B1.loc[j, 'PAID AMOUNT'] >= A.loc[i, 'EMI']:
#                                 A.loc[i, 'STATUS'] = 'SB'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'FORECLOSE'):
#                     A.loc[i, 'STATUS'] = 'FORECLOSE'
#                 elif (A.loc[i, 'AGREEMENTID'] == B.loc[k, 'AGREEMENTID']) and (B.loc[k, 'AGAINST'] == 'SETTLEMENT'):
#                     A.loc[i, 'STATUS'] = 'SETTLEMENT'
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if str(A.loc[i, 'STATUS']) == 'nan':
#                 A.loc[i, 'STATUS'] = 'FLOW'
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             for j in range(0, len(B1['PAID AMOUNT'])):
#                 if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
#                     A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']
#
#         M = pd.DataFrame(A.groupby(['COMPANY'])['POS'].sum()).reset_index()
#
#         M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)
#
#         R = pd.DataFrame(A.groupby(['COMPANY'])['AGREEMENTID'].count()).reset_index()
#
#         F = M.merge(R, how='outer')
#
#         F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)
#
#         R1 = pd.DataFrame(A.groupby(['COMPANY', 'STATUS'])['AGREEMENTID'].count()).reset_index()
#
#         P = F.copy()
#
#         P.drop(['TOTAL_POS', 'TOTAL_CASES'], axis=1, inplace=True)
#
#         P['FLOW'] = np.nan
#         P['SB'] = np.nan
#         P['PART PAID'] = np.nan
#         P['FORECLOSE'] = np.nan
#         P['SETTLEMENT'] = np.nan
#
#         COL = P.columns
#
#         for i in range(0, len(R1['COMPANY'])):
#             for j in range(0, len(P['FLOW'])):
#                 for k in range(0, len(COL)):
#                     if (R1.loc[i, 'COMPANY'] == P.loc[j, 'COMPANY']) and R1.loc[i, 'STATUS'] == COL[k]:
#                         P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']
#
#         F = F.merge(P, how='outer')
#
#         F.fillna(0, inplace=True)
#
#         F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'FORECLOSE': 'FORECLOSE_CASES', 'SETTLEMENT': 'SETTLEMENT_CASES',
#                   'PART PAID': 'PART_PAID_CASES'}, axis=1, inplace=True)
#
#         R2 = pd.DataFrame(A.groupby(['COMPANY', 'STATUS'])['POS'].sum()).reset_index()
#
#         for i in range(0, len(R2['COMPANY'])):
#             for j in range(0, len(P['COMPANY'])):
#                 for k in range(0, len(COL)):
#                     if (R2.loc[i, 'COMPANY'] == P.loc[j, 'COMPANY']) and R2.loc[i, 'STATUS'] == COL[k]:
#                         P.loc[j, COL[k]] = R2.loc[i, 'POS']
#
#         F = F.merge(P, how='outer')
#
#         F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'SETTLEMENT': 'SETTLEMENT_POS',
#                   'PART PAID': 'PART_PAID_POS'}, axis=1, inplace=True)
#
#         F.fillna(0, inplace=True)
#
#         for i in range(0, len(F['FLOW_CASES'])):
#             F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#             F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#
#         TP = pd.DataFrame(A.groupby(['COMPANY'])['TOTAL PAID'].sum()).reset_index()
#
#         F = F.merge(TP, how='outer')
#
#         for i in range(0, len(F['SB_POS'])):
#             F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#
#         F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
#                   'SETTLEMENT_CASES': 'SC_CASES',
#                   'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
#                   'FORECLOSE_POS%': 'FC_POS%',
#                   'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
#                  inplace=True)
#
#         for i in range(0,len(F['FLOW_CASES'])):
#             F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
#             F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
#             F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
#             F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
#             F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
#             F.loc[i, 'TOTAL_POS'] = round(F.loc[i, 'TOTAL_POS'], 2)
#
#         F.to_excel('media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx', index=False)
#
#         F1 = F.copy()
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             s = 0
#             for j in range(0, len(B['AGREEMENTID'])):
#                 if (A.loc[i, 'AGREEMENTID'] == B.loc[j, 'AGREEMENTID']) and ((A.loc[i, 'STATUS'] == 'FORECLOSE') or (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'SB')) and (B.loc[j, 'MODE'] != 'ECS'):
#                     s = s + B.loc[j, 'PAID AMOUNT']
#             A.loc[i, 'Billing PAID AMT.'] = s
#
#         for i in range(0, len(A['AGREEMENTID'])):
#             if (A.loc[i, 'EMI'] > A.loc[i, 'TOTAL PAID']) and (A.loc[i, 'STATUS'] == 'SB'):
#                 A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
#
#         A['TOTAL PAID'].fillna(0, inplace=True)
#
#         A['Billing PAID AMT.'].fillna(0, inplace=True)
#
#         A.to_excel('media/FULLERTON_FR/Billing/MASTER_FILE_FULLERTON_FR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_FR/TC Performance/MASTER_FILE_FULLERTON_FR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_FR/MIS/MASTER_FILE_FULLERTON_FR.xlsx', index=False)
#         A.to_excel('media/FULLERTON_FR/FOS Salary/MASTER_FILE_FULLERTON_FR.xlsx', index=False)
#
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_OTR.xlsx'):
#             True
#         else:
#             QQ1 = 'Please Upload File for FULLERTON_OTR'
#
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx') and os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx'):
#             fs11 = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             AA11 = fs11.open('MIS_FULLERTON_OTR.xlsx')
#             F11 = pd.read_excel(AA11)  # OTR
#             status = 'There is a data Frame'
#         else:
#             status = 'There is a data Frame'
#             status1 = 'There is no otr file'
#
#     elif request.method != 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MIS_FULLERTON_FR.xlsx') and os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#             fs11 = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             AA = fs.open('MIS_FULLERTON_FR.xlsx')
#             AA11 = fs11.open('MIS_FULLERTON_OTR.xlsx')
#             F1 = pd.read_excel(AA) #FR
#             F11 = pd.read_excel(AA11) #OTR
#             status = 'There is a data Frame'
#             status1 = 'There is otr file'
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MIS_FULLERTON_OTR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_OTR/MIS')
#             AA11 = fs.open('MIS_FULLERTON_OTR.xlsx')
#             F11 = pd.read_excel(AA11)
#             QQ = 'Please Upload File for FULLERTON_FR'
#             status1= 'There is otr file'
#         else:
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#
#             QQ = 'Please Upload File for FULLERTON_FR'
#             QQ1 = 'Please Upload File for FULLERTON_OTR'
#             return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'OTR': QQ1, 'FR': QQ, 'Designation': Designation})
#
#     if status1 != 'There is no otr file':
#         C = list(F11.columns) #OTR
#         for j in range(0, len(F11[C[0]])):
#             row_data11 = list()
#             for col in range(0, len(C)):
#                 row_data11.append(str(F11.loc[j, C[col]]))
#             excel_data.append(row_data11)
#     C11 = list(F1.columns)  # FR
#     if status == 'There is a data Frame':
#         for j in range(0, len(F1[C11[0]])):
#             row_data = list()
#             for col in range(0, len(C11)):
#                 row_data.append(str(F1.loc[j, C11[col]]))
#             excel_data11.append(row_data)
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#
#     return render(request, 'FirstLevel/upload_excel.html', {'excel1': excel_data11, 'columns1': C11, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel': excel_data, 'columns': C, 'OTR': QQ1, 'Designation': Designation})

# def FULLERTON_FR_BILLING(request):
#     Total_Payout = ''
#     Total_Payout1 = ''
#     line = ''
#     line2 = ''
#     QQ = ''
#     QQ1 = ''
#     if request.method == 'POST':
#         if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/MASTER_FILE_FULLERTON_FR.xlsx'):
#             fs = FileSystemStorage(location='media/FULLERTON_FR/Billing')
#             fs1 = FileSystemStorage(location='media/FULLERTON_FR/MIS')
#             AA = fs.open('MASTER_FILE_FULLERTON_FR.xlsx')
#             AA1 = fs1.open('MIS_FULLERTON_FR.xlsx')
#             for i in range(1, 32, -1):
#                 if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/FULLERTON_FR_PAID FILE_' + i + 'SEP21.xlsx'):
#                     AA122 = fs1.open('FULLERTON_FR_PAID FILE_' + i + 'SEP21.xlsx')
#                     PAID_FILE = pd.read_excel(AA122)
#                 else:
#                     continue
#             A = pd.read_excel(AA)
#             P = pd.read_excel(AA1)
#
#             for i in range(0, len(A['COMPANY'])):
#                 if A.loc[i, 'COMPANY'] == 'FULLERTON':
#                     for j in range(0, len(P['COMPANY'])):
#                         if A.loc[i, 'COMPANY'] == P.loc[j, 'COMPANY']:
#                             if P.loc[j, 'POS_RES%'] < 75:
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 4 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(4) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(4), a, P.loc[j, 'COMPANY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 75) and (P.loc[j, 'POS_RES%'] < 78):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 4.25 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(4.25) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(4.25), a, P.loc[j, 'COMPANY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 78) and (P.loc[j, 'POS_RES%'] < 80):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 4.5 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(4.5) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(4.5), a, P.loc[j, 'COMPANY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 80) and (P.loc[j, 'POS_RES%'] < 82):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 4.75 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(4.75) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(4.75), a, P.loc[j, 'COMPANY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 82) and (P.loc[j, 'POS_RES%'] < 84):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 5 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(5) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(5), a, P.loc[j, 'COMPNAY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 84) and (P.loc[j, 'POS_RES%'] < 86):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 5.25 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(5.25) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], A.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(5.25), a, P.loc[j, 'COMPNAY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 86) and (P.loc[j, 'POS_RES%'] < 88):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 5.5 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(5.5) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(5.5), a, P.loc[j, 'COMPNAY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 88) and (P.loc[j, 'POS_RES%'] < 90):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 5.75 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(5.75) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(5.75), a, P.loc[j, 'COMPNAY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 90) and (P.loc[j, 'POS_RES%'] < 92):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 6 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(6) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(6), a, P.loc[j, 'COMPNAY'])
#                             elif (P.loc[j, 'POS_RES%'] >= 92):
#                                 if A.loc[i, 'STATUS'] == 'SB':
#                                     a = A.loc[i, 'Billing PAID AMT.'] * 6.25 / 100
#                                     A.loc[i, 'PERCENTAGE'] = str(6.25) + '%'
#                                     A.loc[i, 'MOHAK'] = a
#                                     print(A.loc[i, 'AGREEMENTID'], A.loc[i, 'COMPANY'], P.loc[j, 'POS_RES%'], A.loc[i, 'Billing PAID AMT.'], str(6.25), a, P.loc[j, 'COMPANY'])
#
#             FLOWLIST = A[A['STATUS'] == 'FLOW'].index
#
#             for i in range(0, len(FLOWLIST)):
#                 A.loc[FLOWLIST[i], 'MOHAK'] = 0
#
#             A[A['MOHAK'].isnull()]['STATUS'].value_counts()
#
#             A.rename({'MOHAK': 'PAYOUT'}, axis=1, inplace=True)
#
#             A['PAYOUT'].fillna(0, inplace=True)
#
#             A.to_excel(r'media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx', index=False)
#
#             Total_Payout = round(sum(A['PAYOUT']), 2)
#             line = 'Total Payout for FR = '
#
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx'):
#                 if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                     fs2 = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                     AA2 = fs2.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                     F3 = pd.read_excel(AA2)  # OTR
#                     Total_Payout1 = round(sum(F3['PAYOUT']), 2)
#                     line2 = 'Total Payout for OTR = '# OTR
#                     QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                     QQ = 'Please click Billing button for FULLERTON_FR'
#                 else:
#                     QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                     QQ = 'Please click Billing button for FULLERTON_FR'
#             else:
#                 QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#
#         else:
#             return HttpResponseRedirect(reverse('basic_app:FULLERTON_OTR_MIS'))
#
#     elif request.method != 'POST':
#         if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MASTER_FILE_FULLERTON_FR.xlsx') and os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx') and os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs = FileSystemStorage(location='media/FULLERTON_FR/Billing') #FR
#                 fs2 = FileSystemStorage(location='media/FULLERTON_OTR/Billing') #OTR
#                 AA3 = fs.open('PAYOUT_FULLERTON_FR.xlsx') #FR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_OTR.xlsx') #OTR
#                 F2 = pd.read_excel(AA3) #FR
#                 F3 = pd.read_excel(AA2) #OTR
#                 Total_Payout = round(sum(F2['PAYOUT']), 2) #FR
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 line = 'Total Payout for FR = '
#                 line2 = 'Total Payout for OTR = '
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2) #OTR
#
#             elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs2 = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                 F3 = pd.read_excel(AA2)  # OTR
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2)  # OTR
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 line2 = 'Total Payout for OTR = '
#
#             elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx'):
#                 fs = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # OTR
#                 AA3 = fs.open('PAYOUT_FULLERTON_FR.xlsx')  # OTR
#                 F3 = pd.read_excel(AA3)  # OTR
#                 Total_Payout = round(sum(F3['PAYOUT']), 2)  # OTR
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 line = 'Total Payout for FR = '
#
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 return render(request, 'FirstLevel/Billing.html',
#                               {'OTR': QQ1, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/MIS/MASTER_FILE_FULLERTON_OTR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_OTR/Billing/PAYOUT_FULLERTON_OTR.xlsx'):
#                 fs2 = FileSystemStorage(location='media/FULLERTON_OTR/Billing')  # OTR
#                 AA2 = fs2.open('PAYOUT_FULLERTON_OTR.xlsx')  # OTR
#                 F3 = pd.read_excel(AA2)  # OTR
#                 Total_Payout1 = round(sum(F3['PAYOUT']), 2)  # OTR
#                 QQ = 'Please Upload Allocation File for FULLERTON_FR'
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 line2 = 'Total Payout for OTR = '
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ1 = 'Please click Billing button for FULLERTON_OTR'
#                 QQ = 'Please Upload Allocation File for FULLERTON_FR'
#                 return render(request, 'FirstLevel/Billing.html',
#                               {'OTR': QQ1, 'FR':QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         elif os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/MIS/MASTER_FILE_FULLERTON_FR.xlsx'):
#             if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/FULLERTON_FR/Billing/PAYOUT_FULLERTON_FR.xlsx'):
#                 fs = FileSystemStorage(location='media/FULLERTON_FR/Billing')  # OTR
#                 AA3 = fs.open('PAYOUT_FULLERTON_FR.xlsx')  # OTR
#                 F2 = pd.read_excel(AA3)  # OTR
#                 Total_Payout = round(sum(F2['PAYOUT']), 2)  # OTR
#                 QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 line = 'Total Payout for FR = '
#             else:
#                 final_dep = DEP()
#                 final_process = COMPANY_PROCESS()
#                 Designation = Employee_Designation()
#
#                 QQ1 = 'Please Upload Allocation File for FULLERTON_OTR'
#                 QQ = 'Please click Billing button for FULLERTON_FR'
#                 return render(request, 'FirstLevel/Billing.html',
#                               {'FR': QQ, "OTR": QQ1, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         else:
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#             QQ = 'Please Upload File for FULLERTON_FR'
#             QQ1 = 'Please Upload File for FULLERTON_OTR'
#             return render(request, 'FirstLevel/Billing.html', {'OTR': QQ1, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#
#     return render(request, 'FirstLevel/Billing.html', {'Total_Payout12': Total_Payout, 'Total_Payout': Total_Payout1, 'OTR': QQ1, 'com': line, 'com2' : line2, 'FR': QQ, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def FULLERTON_RECOVERY_MIS(request):
    excel_data = []
    F1 = pd.DataFrame()
    if request.method == 'POST':
        Allocation1 = request.FILES['Allocation']
        Paidfile1 = request.FILES['Paid_File']
        A = pd.read_excel(Allocation1)
        B = pd.read_excel(Paidfile1)

        for i in range(0, len(A['AGREEMENTID'])):
            if pd.isnull(A['AGREEMENTID'][i]) == True:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html',
                              {'error': 'AGREEMENTID DOES NOT TAKE NULL VALUES'})
            elif pd.isnull(A['CUSTOMERNAME'][i]) == True or isinstance(A.loc[i, 'CUSTOMERNAME'], str) == False:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html',
                              {'error': 'CUSTOMERNAME DOES NOT TAKE NULL VALUES'})
            elif pd.isnull(A['TC NAME'][i]) == True or isinstance(A.loc[i, 'TC NAME'], str) == False:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TC NAME DOES NOT TAKE NULL VALUES'})
            elif pd.isnull(A['TL'][i]) == True or isinstance(A.loc[i, 'TL'], str) == False:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'TL DOES NOT TAKE NULL VALUES'})
            elif pd.isnull(A['FOS'][i]) == True or isinstance(A.loc[i, 'FOS'], str) == False:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'FOS DOES NOT TAKE NULL VALUES'})
            elif pd.isnull(A['AREA'][i]) == True or isinstance(A.loc[i, 'AREA'], str) == False:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'AREA DOES NOT TAKE NULL VALUES'})
            elif isinstance(A.loc[i, 'POS'], np.float64) == False or pd.isnull(A['POS'][i]) == True:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'POS DOES NOT TAKE STR VALUES'})
            elif isinstance(A.loc[i, 'EMI'], np.int64) == False or pd.isnull(A['EMI'][i]) == True:
                print('error', i)
                return render(request, 'FirstLevel/upload_excel.html', {'error': 'EMI DOES NOT TAKE STR VALUES'})
            else:
                continue

        fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/MIS')
        fs.save(Allocation1.name, Allocation1)
        fs.save(Paidfile1.name, Paidfile1)
        print(A.head())

        dr = list(B[B['MODE'] == 'ECS'].index)

        B.drop(dr, axis=0, inplace=True)

        B = B.reset_index(drop=True)

        B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

        for i in range(0, len(A['AGREEMENTID'])):
            for j in range(0, len(B1['PAID AMOUNT'])):
                if A.loc[i, 'AGREEMENTID'] == B1.loc[j, 'AGREEMENTID']:
                    A.loc[i, 'TOTAL PAID'] = B1.loc[j, 'PAID AMOUNT']

        for i in range(0, len(A['AGREEMENTID'])):
            if A.loc[i, 'TOTAL PAID'] > 0:
                A.loc[i, 'STATUS'] = 'PAID'
            else:
                A.loc[i, 'STATUS'] = 'FLOW'

        M = pd.DataFrame(A.groupby(['PRODUCT', 'VINTAGE'])['POS'].sum()).reset_index()

        M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)

        R = pd.DataFrame(A.groupby(['PRODUCT', 'VINTAGE'])['AGREEMENTID'].count()).reset_index()

        F = M.merge(R, how='outer')

        F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)

        R1 = pd.DataFrame(A.groupby(['PRODUCT', 'VINTAGE', 'STATUS'])['AGREEMENTID'].count()).reset_index()

        P = F.copy()

        P.drop(['TOTAL_POS', 'TOTAL_CASES'], axis=1, inplace=True)

        P['FLOW'] = np.nan
        P['PAID'] = np.nan

        COL = P.columns

        for i in range(0, len(R1['PRODUCT'])):
            for j in range(0, len(P['FLOW'])):
                for k in range(0, len(COL)):
                    if ((R1.loc[i, ['PRODUCT', 'VINTAGE']] == P.loc[j, ['PRODUCT', 'VINTAGE']]).all()) and (R1.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']

        F = F.merge(P, how='outer')

        F.fillna(0, inplace=True)

        F.rename({'FLOW': 'FLOW_CASES', 'PAID': 'PAID_CASES'}, axis=1, inplace=True)

        R2 = pd.DataFrame(A.groupby(['PRODUCT', 'VINTAGE', 'STATUS'])['TOTAL PAID'].sum()).reset_index()

        for i in range(0, len(R2['PRODUCT'])):
            for j in range(0, len(P['PRODUCT'])):
                for k in range(0, len(COL)):
                    if ((R2.loc[i, ['PRODUCT', 'VINTAGE']] == P.loc[j, ['PRODUCT', 'VINTAGE']]).all()) and (R2.loc[i, 'STATUS'] == COL[k]):
                        P.loc[j, COL[k]] = R2.loc[i, 'TOTAL PAID']

        F = F.merge(P, how='outer')

        F.rename({'FLOW': 'FLOW_POS', 'PAID': 'PAID_POS'}, axis=1, inplace=True)

        F.fillna(0, inplace=True)

        for i in range(0, len(F['FLOW_CASES'])):
            F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i, 'PAID_POS%'] = round((F.loc[i, 'PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
            F.loc[i,'TOTAL_POS'] = round(F.loc[i,'TOTAL_POS'],2)

        F.rename({'PAID_POS%': 'PERFORMANCE', 'PAID_POS': 'MONEY_COLLECTION'}, axis=1, inplace=True)

        F.drop(['FLOW_POS%', 'FLOW_POS'], axis=1, inplace=True)

        F.to_excel('media/FULLERTON_RECOVERY/MIS/MIS_FULLERTON_RECOVERY.xlsx', index=False)

        F1 = F.copy()

        for i in range(0, len(F['PRODUCT'])):

            # PL-SAL

            if (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V1'):
                if F.loc[i, 'PERFORMANCE'] < 6:
                    F.loc[i, 'PAYOUT%'] = '16%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 16 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 6) and (F.loc[i, 'PERFORMANCE'] < 8):
                    F.loc[i, 'PAYOUT%'] = '17.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 17.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 8:
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V2'):
                if F.loc[i, 'PERFORMANCE'] < 5:
                    F.loc[i, 'PAYOUT%'] = '17.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 17.5 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 5) and (F.loc[i, 'PERFORMANCE'] < 6):
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 6:
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V3'):
                if F.loc[i, 'PERFORMANCE'] < 4:
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 4) and (F.loc[i, 'PERFORMANCE'] < 5):
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 5:
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V4'):
                if F.loc[i, 'PERFORMANCE'] < 3:
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 4) and (F.loc[i, 'PERFORMANCE'] < 5):
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 5:
                    F.loc[i, 'PAYOUT%'] = '27.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 27.5 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V5'):
                if F.loc[i, 'PERFORMANCE'] < 2:
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 2) and (F.loc[i, 'PERFORMANCE'] < 3):
                    F.loc[i, 'PAYOUT%'] = '27.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 27.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 3:
                    F.loc[i, 'PAYOUT%'] = '30%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 30 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Sal') and (F.loc[i, 'VINTAGE'] == 'V6'):
                if F.loc[i, 'PERFORMANCE'] < 1:
                    F.loc[i, 'PAYOUT%'] = '30%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 30 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 1) and (F.loc[i, 'PERFORMANCE'] < 2):
                    F.loc[i, 'PAYOUT%'] = '32.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 32.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 2:
                    F.loc[i, 'PAYOUT%'] = '35%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 35 / 100

            # PL-SELF

            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V1'):
                if F.loc[i, 'PERFORMANCE'] < 5:
                    F.loc[i, 'PAYOUT%'] = '16%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 16 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 5) and (F.loc[i, 'PERFORMANCE'] < 6):
                    F.loc[i, 'PAYOUT%'] = '17.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 17.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 6:
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V2'):
                if F.loc[i, 'PERFORMANCE'] < 4:
                    F.loc[i, 'PAYOUT%'] = '17.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 17.5 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 4) and (F.loc[i, 'PERFORMANCE'] < 5):
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 5:
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V3'):
                if F.loc[i, 'PERFORMANCE'] < 3:
                    F.loc[i, 'PAYOUT%'] = '20%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 20 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 3) and (F.loc[i, 'PERFORMANCE'] < 4):
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 4:
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V4'):
                if F.loc[i, 'PERFORMANCE'] < 2:
                    F.loc[i, 'PAYOUT%'] = '22.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 22.5 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 2) and (F.loc[i, 'PERFORMANCE'] < 3):
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 3:
                    F.loc[i, 'PAYOUT%'] = '27.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 27.5 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V5'):
                if F.loc[i, 'PERFORMANCE'] < 1:
                    F.loc[i, 'PAYOUT%'] = '25%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 25 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 1) and (F.loc[i, 'PERFORMANCE'] < 2):
                    F.loc[i, 'PAYOUT%'] = '27.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 27.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 2:
                    F.loc[i, 'PAYOUT%'] = '30%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 30 / 100
            elif (F.loc[i, 'PRODUCT'] == 'PL Self') and (F.loc[i, 'VINTAGE'] == 'V6'):
                if F.loc[i, 'PERFORMANCE'] < 1:
                    F.loc[i, 'PAYOUT%'] = '30%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 30 / 100
                elif (F.loc[i, 'PERFORMANCE'] >= 1) and (F.loc[i, 'PERFORMANCE'] < 1.5):
                    F.loc[i, 'PAYOUT%'] = '32.5%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 32.5 / 100
                elif F.loc[i, 'PERFORMANCE'] >= 1.5:
                    F.loc[i, 'PAYOUT%'] = '35%'
                    F.loc[i, 'PAYOUT'] = F.loc[i, 'MONEY_COLLECTION'] * 35 / 100

        A['TOTAL PAID'].fillna(0, inplace=True)

        F.to_excel('media/FULLERTON_RECOVERY/Billing/PAYOUT_FULLERTON_RECOVERY.xlsx', index=False)
        A.to_excel('media/FULLERTON_RECOVERY/TC Performance/MASTER_FILE_FULLERTON_RECOVERY.xlsx', index=False)
        A.to_excel('media/FULLERTON_RECOVERY/MIS/MASTER_FILE_FULLERTON_RECOVERY.xlsx', index=False)
        A.to_excel('media/FULLERTON_RECOVERY/FOS Salary/MASTER_FILE_FULLERTON_RECOVERY.xlsx', index=False)

        F.to_excel('media/FULLERTON_RECOVERY/MIS/MIS_FULLERTON_RECOVERY.xlsx', index=False)

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/MIS/MIS_FULLERTON_RECOVERY.xlsx')):
            fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/MIS')
            AA = fs.open('MIS_FULLERTON_RECOVERY.xlsx')
            F1 = pd.read_excel(AA)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C = list(F1.columns)

    for j in range(0, len(F1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(F1.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/upload_excel.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def FULLERTON_RECOVERY_BILLING(request):
    excel_data1 = []
    F2 = pd.DataFrame()
    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/Billing/PAYOUT_FULLERTON_RECOVERY.xlsx')):
            fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/Billing')
            AA = fs.open('PAYOUT_FULLERTON_RECOVERY.xlsx')
            A = pd.read_excel(AA)
            F2 = A.copy()
            Total_Payout = round(sum(A['PAYOUT']), 2)

        else:
            return HttpResponseRedirect(reverse('basic_app:FULLERTON_RECOVERY_MIS'))

    elif request.method != 'POST':
        final_dep = DEP()
        final_process = COMPANY_PROCESS()
        Designation = Employee_Designation()

        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/Billing/PAYOUT_FULLERTON_RECOVERY.xlsx')):
            fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/Billing')
            AA = fs.open('PAYOUT_FULLERTON_RECOVERY.xlsx')
            F2 = pd.read_excel(AA)
            Total_Payout = round(sum(F2['PAYOUT']), 2)

        else:
            return render(request, 'FirstLevel/Billing.html')

    C1 = list(F2.columns)

    for j in range(0, len(F2[C1[0]])):
        row_data1 = list()
        for col in range(0, len(C1)):
            row_data1.append(str(F2.loc[j, C1[col]]))
        excel_data1.append(row_data1)

    return render(request, 'FirstLevel/Billing.html', {'Billing': excel_data1, 'columns': C1, 'Total_Payout': Total_Payout, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def MASTER_SALARY_TW(request):
    excel_data = []
    excel_data1 = []
    excel_data123 = []
    excel_data1233 = []
    F = pd.DataFrame()
    FINAL_COPY = pd.DataFrame()
    FINAL_COPY1 = pd.DataFrame()
    FINAL_COPY12 = pd.DataFrame()
    LTTW = pd.DataFrame()
    IDFCHL = pd.DataFrame()
    a=0

    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')):
            # and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'))
            # fs = FileSystemStorage(location='media/L_T/MIS')
            fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/Employees')
            # fs3 = FileSystemStorage(location='media/IDFC_HL/MIS')
            # AA = fs.open('MASTER FILE L_T.xlsx')
            AA1 = fs1.open('MASTER FILE IDFC_TW.xlsx')
            E = fs2.open('Employee_Database.xlsx')
            for i in range(31, 0, -1):
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')):
                    AA122 = fs1.open('IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')
                    PAID_FILE_IDFC_TW = pd.read_excel(AA122)
                else:
                    continue
            # for i in range(31, 0, -1):
            #     if os.path.exists(
            #             '/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/L_T PAID FILE ' + str(i) + ' AUG 21.xlsx'):
            #         AA123 = fs.open('L_T PAID FILE ' + str(i) + ' AUG 21.xlsx')
            #         PAID_FILE_L_T = pd.read_excel(AA123)
            #     else:
            #         continue
            # for i in range(31, 0, -1):
            #     if os.path.exists(
            #             '/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/L_T Allocation ' + str(i) + ' AUG 21.xlsx'):
            #         AA124 = fs.open('L_T Allocation ' + str(i) + ' AUG 21.xlsx')
            #         LTTW = pd.read_excel(AA124)
            #     else:
            #         continue
            for i in range(31, 0, -1):
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/IDFC_TW ALLOCATION ' + str(i) + ' OCT 21.xlsx')):
                    AA125 = fs1.open('IDFC_TW ALLOCATION ' + str(i) + ' OCT 21.xlsx')
                    IDFCTW = pd.read_excel(AA125)
                else:
                    continue
            # for i in range(31, 0, -1):
            #     if os.path.exists(
            #             '/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/MIS/IDFC_ALLOCATION_' + str(i) + 'AUG21.xlsx'):
            #         AA126 = fs3.open('IDFC_ALLOCATION_' + str(i) + 'AUG21.xlsx')
            #         IDFCHL = pd.read_excel(AA126)
            #     else:
            #         continue
            # MASTER_FILE_L_T = pd.read_excel(AA)
            MASTER_FILE_IDFC_TW = pd.read_excel(AA1)
            A = pd.read_excel(E)

            # print('LT FILE')
            # print(LTTW.head(10))
            print('IDFC TW FILE')
            print(IDFCTW.head(10))
            # print('IDFC HL FILE')
            # print(IDFCHL.head(10))
            print('PAID FILE IDFC_TW')
            print(PAID_FILE_IDFC_TW.head(10))
            # print('PDIA FILE L_T')
            # print(PAID_FILE_L_T.head(10))


            # LTTW.drop('TOTAL COLLECTABLE', axis=1, inplace=True)

            # MASTER = pd.concat([IDFCHL, LTTW])
            MASTER = IDFCTW
            MASTER = MASTER.reset_index(drop=True)

            for i in range(0, len(MASTER['COMPANY'])):
                # if (MASTER.loc[i, 'COMPANY'] == 'HFC') or (MASTER.loc[i, 'COMPANY'] == 'SUVIDHA'):
                #     MASTER.loc[i, 'PROCESS'] = 'IDFC-HL'
                # elif MASTER.loc[i, 'COMPANY'] == 'L&T':
                #     MASTER.loc[i, 'PROCESS'] = 'TW'
                if MASTER.loc[i, 'COMPANY'] == 'IDFC - TW':
                    MASTER.loc[i, 'PROCESS'] = 'TW'

            MASTER_COUNT = pd.DataFrame(MASTER.groupby(['PROCESS', 'FOS'])['AGREEMENTID'].count()).reset_index()

            dr = []
            for i in range(0, len(MASTER_COUNT['FOS'])):
                if MASTER_COUNT.loc[i, 'FOS'] == 'NO FOS' or MASTER_COUNT.loc[i, 'FOS'] == 'LOW POS':
                    dr.append(i)

            MASTER_COUNT.drop(dr, axis=0, inplace=True)

            MASTER_COUNT = MASTER_COUNT.reset_index(drop=True)


            PAID_FILE_IDFC_TW.drop(['DATE','BOUNCING AMT.','AGAINST'],axis=1,inplace=True)
            # PAID_FILE_L_T.drop(['DATE','BOUNCING AMT.','AGAINST'],axis=1,inplace=True)

            MASTER_FILE_IDFC_TW.drop(['COMPANY','LAST MONTH','MOB','LOAN TYPE','BOUNCING REASONS','EMI CYCLE','TOTAL PAID','MOB','LOAN_AMT','ADDITIONAL NUMBER'],axis=1,inplace=True)

            # MASTER_FILE_L_T.drop(['BOUNCING REASONS','EMI CYCLE','LOAN AMT','ADDITIONAL NUMBER','TOTAL PAID','TOTAL COLLECTABLE','LAST MONTH','COMPANY','MOB'],axis=1,inplace=True)

            MASTER_FILE_IDFC_TW['PRODUCT']='IDFC-TW'
            # MASTER_FILE_L_T['PRODUCT']='L&T'

            # MASTER_FILE=pd.concat([MASTER_FILE_IDFC_TW,MASTER_FILE_L_T])
            MASTER_FILE = MASTER_FILE_IDFC_TW

            MASTER_FILE=MASTER_FILE.reset_index(drop=True)

            # MASTER_PAID_FILE=pd.concat([PAID_FILE_IDFC_TW,PAID_FILE_L_T])

            MASTER_PAID_FILE = PAID_FILE_IDFC_TW

            MASTER_PAID_FILE=MASTER_PAID_FILE.reset_index(drop=True)

            MASTER_PAID_FILE.rename({'PROCESS':'PRODUCT'},axis=1,inplace=True)

            MASTER_PAID_FILE['MODE'].unique()

            CASH=MASTER_PAID_FILE[MASTER_PAID_FILE['MODE']=='CASH']

            CASH.drop(['PRODUCT','CUSTOMERNAME','EMI','PAID AMOUNT','BKT','MODE'],axis=1,inplace=True)

            CASH.rename({'FOS':'FINAL PAID FOS'},axis=1,inplace=True)

            AA=pd.DataFrame(CASH.groupby(['AGREEMENTID'])['FINAL PAID FOS'].value_counts())

            AA.rename({'FINAL PAID FOS':'FOS'},axis=1,inplace=True)

            CASH=AA.reset_index()

            CASH.drop('FOS',axis=1,inplace=True)

            MASTER_FILE=MASTER_FILE.merge(CASH,how='left')

            for i in range(0,len(MASTER_FILE['AGREEMENTID'])):
                for j in range(0,len(MASTER_PAID_FILE['AGREEMENTID'])):
                    if type(MASTER_FILE.loc[i,'FINAL PAID FOS'])==np.float:
                        if MASTER_FILE.loc[i,'AGREEMENTID']==MASTER_PAID_FILE.loc[j,'AGREEMENTID']:
                            MASTER_FILE.loc[i,'FINAL PAID FOS']=MASTER_PAID_FILE.loc[j,'FOS']

            off=list(A[A['STAFF']=='OFFICE']['NAMES'])

            for i in range(0,len(MASTER_FILE['AGREEMENTID'])):
                for j in range(0,len(MASTER_PAID_FILE['AGREEMENTID'])):
                    if MASTER_FILE.loc[i,'AGREEMENTID']==MASTER_PAID_FILE.loc[j,'AGREEMENTID']:
                        if MASTER_PAID_FILE.loc[j,'FOS'] in off:
                            MASTER_FILE.loc[i,'FINAL PAID FOS']=MASTER_FILE.loc[i,'FOS']
                        else:
                            MASTER_FILE.loc[i,'FINAL PAID FOS']=MASTER_PAID_FILE.loc[j,'FOS']

            for i in range(0,len(MASTER_FILE['FINAL PAID FOS'])):
                if (type(MASTER_FILE.loc[i,'FINAL PAID FOS'])==np.float):
                    MASTER_FILE.loc[i,'FINAL PAID FOS']='--'

            for i in range(0,len(MASTER_FILE['FINAL PAID FOS'])):
                if MASTER_FILE.loc[i,'STATUS']=='PART PAID':
                    MASTER_FILE.loc[i,'FINAL PAID FOS']='--'

            MASTER_FILE[MASTER_FILE['FINAL PAID FOS']=='--']['STATUS'].unique()

            FINAL=MASTER_FILE.copy()

            FUNDING_LIST=list(FINAL[FINAL['FINAL PAID FOS']=='FUNDING']['STATUS'].index)

            FINAL.loc[FUNDING_LIST,'STATUS']='FLOW'

            FINAL.rename({'FOS':'ALLOCATED FOS'},axis=1,inplace=True)

            M=pd.DataFrame(FINAL.groupby(['PRODUCT', 'ALLOCATED FOS', 'BKT'])['POS'].sum()).reset_index()

            M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

            R=pd.DataFrame(FINAL.groupby(['PRODUCT', 'ALLOCATED FOS', 'BKT'])['AGREEMENTID'].count()).reset_index()

            F=M.merge(R,how='outer')

            F.rename({'AGREEMENTID' : 'TOTAL_CASES'},axis=1,inplace=True)

            R1=pd.DataFrame(FINAL.groupby(['PRODUCT','ALLOCATED FOS','BKT','STATUS'])['AGREEMENTID'].count()).reset_index()

            P=F.copy()

            P=P.iloc[:,:3]

            P['FLOW']=np.nan
            P['SB']=np.nan
            P['RB']=np.nan
            P['NM']=np.nan
            P['PART PAID']=np.nan
            P['FORECLOSE']=np.nan
            P['SETTLEMENT']=np.nan

            COL=P.columns
            for i in range(0,len(R1['PRODUCT'])):
                for j in range(0,len(P['PRODUCT'])):
                    for k in range(0,len(COL)):
                        if ((R1.loc[i,['PRODUCT','ALLOCATED FOS','BKT']]==P.loc[j,['PRODUCT','ALLOCATED FOS','BKT']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                            P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

            F=F.merge(P,how='outer')

            F.fillna(0,inplace=True)

            F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','RB':'RB_CASES','FORECLOSE':'FORECLOSE_CASES','SETTLEMENT':'SETTLEMENT_CASES','NM':'NM_CASES','PART PAID':'PART_PAID_CASES'},axis=1,inplace=True)

            R2=pd.DataFrame(FINAL.groupby(['PRODUCT','ALLOCATED FOS','BKT','STATUS'])['POS'].sum()).reset_index()

            for i in range(0,len(R2['PRODUCT'])):
                for j in range(0,len(P['PRODUCT'])):
                    for k in range(0,len(COL)):
                        if ((R2.loc[i,['PRODUCT','ALLOCATED FOS','BKT']]==P.loc[j,['PRODUCT','ALLOCATED FOS','BKT']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                            P.loc[j,COL[k]]=R2.loc[i,'POS']

            F=F.merge(P,how='outer')

            F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','RB':'RB_POS','FORECLOSE':'FORECLOSE_POS', 'NM':'NM_POS','SETTLEMENT':'SETTLEMENT_POS','PART PAID':'PART_PAID_POS'},axis=1,inplace=True)

            F.fillna(0,inplace=True)

            for i in range(0,len(F['FLOW_CASES'])):
                F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'RB_POS%']=round((F.loc[i,'RB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'FORECLOSE_POS%']=round((F.loc[i,'FORECLOSE_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'SETTLEMENT_POS%']=round((F.loc[i,'SETTLEMENT_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'NM_POS%']=round((F.loc[i,'NM_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)
                F.loc[i, 'TOTAL_POS'] = round(F.loc[i, 'TOTAL_POS'],2)
                F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'],2)
                F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'],2)
                F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'],2)
                F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'],2)
                F.loc[i, 'PART_PAID_POS'] = round(F.loc[i, 'PART_PAID_POS'],2)
                F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'],2)
                F.loc[i, 'FORECLOSE_POS'] = round(F.loc[i, 'FORECLOSE_POS'],2)
                F.loc[i, 'SETTLEMENT_POS'] = round(F.loc[i, 'SETTLEMENT_POS'],2)

            for i in range(0,len(F['NM_CASES'])):
                F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']+F.loc[i,'RB_POS%']+F.loc[i,'NM_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'SETTLEMENT_POS%']

            for i in range(0,len(F['NM_POS'])):
                F.loc[i,'Additional_Performance']=F.loc[i,'RB_POS%']+F.loc[i,'NM_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'SETTLEMENT_POS%']

            for i in range(0, len(F['FLOW_CASES'])):
                F.loc[i, 'PERFORMANCE'] = round(F.loc[i, 'PERFORMANCE'], 2)
                F.loc[i, 'Additional_Performance'] = round(F.loc[i, 'Additional_Performance'], 2)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Performance.xlsx',index=False)

            #
            # FINAL TABLE COPY CREATION
            #



            FINAL_COPY=FINAL.copy()

            for i in range(0,len(FINAL_COPY['FINAL PAID FOS'])):
                for j in range(0,len(A['NAMES'])):
                    if (FINAL_COPY.loc[i,'FINAL PAID FOS']==A.loc[j,'NAMES']) and (A.loc[j,'DESIGNATION']=='OFFICE'):
                        FINAL_COPY.loc[i,'FINAL PAID FOS']=FINAL_COPY.loc[i,'ALLOCATED FOS']
                    elif (FINAL_COPY.loc[i,'FINAL PAID FOS']==A.loc[j,'NAMES']) and (A.loc[j,'DESIGNATION']=='FIELD'):
                        FINAL_COPY.loc[i,'FINAL PAID FOS']=FINAL_COPY.loc[i,'FINAL PAID FOS']

            for i in range(0,len(FINAL_COPY['AGREEMENTID'])):
                if (FINAL_COPY.loc[i,'FINAL PAID FOS']=='FUNDING') or (FINAL_COPY.loc[i,'FINAL PAID FOS']=='NO FOS') or (FINAL_COPY.loc[i,'FINAL PAID FOS']=='--') or (FINAL_COPY.loc[i,'FINAL PAID FOS']=='Low Val'):
                    FINAL_COPY.loc[i,'PER PAID CASE']=0

            FINAL_COPY=FINAL_COPY.merge(A,left_on='FINAL PAID FOS',right_on='NAMES',how='left')

            FINAL_COPY.drop(['DEPARTMENT_ID','END_DATE','HIRE_DATE','PHONE_NUMBER','LOCATION_ID','SALARY','TYPE_OF_SALARY','MANAGEMENT_LEVEL','NAMES', 'DATE_OF_BIRTH'],axis=1,inplace=True)

            pick_up_case=[]
            for i in range(0,len(FINAL_COPY['AGREEMENTID'])):
                if FINAL_COPY.loc[i,'PER PAID CASE']!=0:
                    if FINAL_COPY.loc[i,'ALLOCATED FOS']!=FINAL_COPY.loc[i,'FINAL PAID FOS']:
                        pick_up_case.append(i)

            for i in range(0,len(pick_up_case)):
                if (FINAL_COPY.loc[pick_up_case[i],'STATUS']=='SB') or (FINAL_COPY.loc[pick_up_case[i],'STATUS']=='SETTLEMENT') or (FINAL_COPY.loc[pick_up_case[i],'STATUS']=='FORECLOSE') or (FINAL_COPY.loc[pick_up_case[i],'STATUS']=='NM') or (FINAL_COPY.loc[pick_up_case[i],'STATUS']=='RB'):
                    FINAL_COPY.loc[pick_up_case[i],'PER PAID CASE']=100

            l6=list(FINAL_COPY['PER PAID CASE'].unique())

            for i in range(0, len(l6)):
                if math.isnan(l6[i]):
                    a = i

            print(l6[a])

            l6.pop(a)

            blank4=[]
            for i in range(0,len(FINAL_COPY['BKT'])):
                if FINAL_COPY.loc[i,'PER PAID CASE'] not in l6:
                    blank4.append(i)

            # HL = MASTER_COUNT[MASTER_COUNT['PROCESS'] == 'IDFC-HL']
            TW = MASTER_COUNT[MASTER_COUNT['PROCESS'] == 'TW']

            # HL=HL.reset_index(drop=True)

            TW=TW.reset_index(drop=True)

            #BKT-1
            for i in range(0, len(F['ALLOCATED FOS'])):
                if F.loc[i, 'BKT'] == 1:
                    for j in range(0, len(blank4)):
                        if (FINAL_COPY.loc[blank4[j], 'BKT'] == 1):
                            if (F.loc[i, ['PRODUCT', 'ALLOCATED FOS']] == FINAL_COPY.loc[blank4[j], ['PRODUCT', 'ALLOCATED FOS']]).all():
                                if (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SETTLEMENT') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FORECLOSE'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0):
                                        if F.loc[i, 'PERFORMANCE'] < 70:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75) and (F.loc[i, 'PERFORMANCE'] < 80):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 80) and (F.loc[i, 'PERFORMANCE'] < 85):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 85) and (F.loc[i, 'PERFORMANCE'] < 90):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 90) and (F.loc[i, 'PERFORMANCE'] < 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'RB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'NM'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 1) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 2)):
                                        if F.loc[i, 'PERFORMANCE'] < 70:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75) and (F.loc[i, 'PERFORMANCE'] < 80):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 80) and (F.loc[i, 'PERFORMANCE'] < 85):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 85) and (F.loc[i, 'PERFORMANCE'] < 90):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 90) and (F.loc[i, 'PERFORMANCE'] < 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 2) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 3)):
                                        if F.loc[i, 'PERFORMANCE'] < 70:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50 * 2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75) and (F.loc[i, 'PERFORMANCE'] < 80):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75 * 2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 80) and (F.loc[i, 'PERFORMANCE'] < 85):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100 * 2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 85) and (F.loc[i, 'PERFORMANCE'] < 90):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125 * 2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 90) and (F.loc[i, 'PERFORMANCE'] < 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150 * 2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 95):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200 * 2
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'PART PAID') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FLOW'):
                                    FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0

            l=list(FINAL_COPY['PER PAID CASE'].unique())

            for i in range(0, len(l)):
                if math.isnan(l[i]):
                    a = i

            l.pop(a)

            blank4=[]
            for i in range(0,len(FINAL_COPY['BKT'])):
                if FINAL_COPY.loc[i,'PER PAID CASE'] not in l:
                    blank4.append(i)

            #BKT-2
            for i in range(0, len(F['ALLOCATED FOS'])):
                if F.loc[i, 'BKT'] == 2:
                    for j in range(0, len(blank4)):
                        if (FINAL_COPY.loc[blank4[j], 'BKT'] == 2) and (FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] != 0):
                            if (F.loc[i, ['PRODUCT', 'ALLOCATED FOS']] == FINAL_COPY.loc[blank4[j], ['PRODUCT', 'ALLOCATED FOS']]).all():
                                if (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SETTLEMENT') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FORECLOSE'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0):
                                        if F.loc[i, 'PERFORMANCE'] < 50:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'RB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'NM'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 1) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 2)):
                                        if F.loc[i, 'PERFORMANCE'] < 50:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 2) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 3)):
                                        if F.loc[i, 'PERFORMANCE'] < 50:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200*2
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 3) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 4)):
                                        if F.loc[i, 'PERFORMANCE'] < 50:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 50*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70) and (F.loc[i, 'PERFORMANCE'] < 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 75):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200*3
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'PART PAID') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FLOW'):
                                    FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0

            #BKT-3
            for i in range(0, len(F['ALLOCATED FOS'])):
                if F.loc[i, 'BKT'] == 3:
                    for j in range(0, len(blank4)):
                        if (FINAL_COPY.loc[blank4[j], 'BKT'] == 3) and (FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] != 0):
                            if (F.loc[i, ['PRODUCT', 'ALLOCATED FOS']] == FINAL_COPY.loc[blank4[j], ['PRODUCT', 'ALLOCATED FOS']]).all():
                                if (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'SETTLEMENT') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FORECLOSE'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0):
                                        if F.loc[i, 'PERFORMANCE'] <45:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 45) and (F.loc[i, 'PERFORMANCE'] < 50):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 175
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'RB') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'NM'):
                                    if (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 1) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 2)):
                                        if F.loc[i, 'PERFORMANCE'] <45:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 45) and (F.loc[i, 'PERFORMANCE'] < 50):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 175
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 2) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 3)):
                                        if F.loc[i, 'PERFORMANCE'] <45:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 45) and (F.loc[i, 'PERFORMANCE'] < 50):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 175*2
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200*2
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 3) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 4)):
                                        if F.loc[i, 'PERFORMANCE'] <45:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 45) and (F.loc[i, 'PERFORMANCE'] < 50):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 175*3
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200*3
                                    elif (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] != 0) and ((FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] >= 4) and (FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] /FINAL_COPY.loc[blank4[j], 'EMI'] < 5)):
                                        if F.loc[i, 'PERFORMANCE'] <45:
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                        elif (F.loc[i, 'PERFORMANCE'] >= 45) and (F.loc[i, 'PERFORMANCE'] < 50):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 75*4
                                        elif (F.loc[i, 'PERFORMANCE'] >= 50) and (F.loc[i, 'PERFORMANCE'] < 55):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 100*4
                                        elif (F.loc[i, 'PERFORMANCE'] >= 55) and (F.loc[i, 'PERFORMANCE'] < 60):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 125*4
                                        elif (F.loc[i, 'PERFORMANCE'] >= 60) and (F.loc[i, 'PERFORMANCE'] < 65):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 150*4
                                        elif (F.loc[i, 'PERFORMANCE'] >= 65) and (F.loc[i, 'PERFORMANCE'] < 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 175*4
                                        elif (F.loc[i, 'PERFORMANCE'] >= 70):
                                            FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 200*4
                                    elif FINAL_COPY.loc[blank4[j], 'Billing PAID AMT.'] == 0:
                                        FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0
                                elif (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'PART PAID') or (FINAL_COPY.loc[blank4[j], 'STATUS'] == 'FLOW'):
                                    FINAL_COPY.loc[blank4[j], 'PER PAID CASE'] = 0

            l=list(FINAL_COPY['PER PAID CASE'].unique())

            for i in range(0, len(l)):
                if math.isnan(l[i]):
                    a = i

            l.pop(a)

            blank=[]
            for i in range(0,len(FINAL_COPY['BKT'])):
                if FINAL_COPY.loc[i,'PER PAID CASE'] not in l:
                    blank.append(i)

            l=list(FINAL_COPY['PER PAID CASE'].unique())

            for i in range(0, len(l)):
                if math.isnan(l[i]):
                    a = i

            l.pop(a)

            blank=[]
            for i in range(0,len(FINAL_COPY['BKT'])):
                if FINAL_COPY.loc[i,'PER PAID CASE'] not in l:
                    blank.append(i)

            for i in range(0,len(blank)):
                if (FINAL_COPY.loc[blank[i],'BKT']!=1) and (FINAL_COPY.loc[blank[i],'BKT']!=3) and (FINAL_COPY.loc[blank[i],'BKT']!=2):
                    if FINAL_COPY.loc[blank[i],'Billing PAID AMT.']!=0:
                        FINAL_COPY.loc[blank[i],'PER PAID CASE']=100

            l2=list(FINAL_COPY['PER PAID CASE'].unique())

            for i in range(0, len(l2)):
                if math.isnan(l2[i]):
                    a = i

            l2.pop(a)

            blank=[]
            for i in range(0,len(FINAL_COPY['BKT'])):
                if FINAL_COPY.loc[i,'PER PAID CASE'] not in l2:
                    blank.append(i)

            for i in range(0,len(blank)):
                if FINAL_COPY.loc[blank[i],'Billing PAID AMT.']==0:
                    FINAL_COPY.loc[blank[i],'PER PAID CASE']=0

            dr=list(FINAL_COPY[FINAL_COPY['STAFF']=='OFFICE'].index)

            for i in range(0,len(dr)):
                FINAL_COPY.loc[dr[i],'PER PAID CASE']=0

            sys=list(FINAL_COPY[FINAL_COPY['FINAL PAID FOS']=='SYS. PAID'].index)

            for i in range(0,len(sys)):
                FINAL_COPY.loc[sys[i],'PER PAID CASE']=0

            sy=list(FINAL_COPY[FINAL_COPY['FINAL PAID FOS']=='PAID FILE'].index)

            for i in range(0,len(sy)):
                FINAL_COPY.loc[sy[i],'PER PAID CASE']=0

            FINAL_COPY.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE.xlsx',index=False)

            FINAL_COPY1 = pd.DataFrame(FINAL_COPY.groupby(['PRODUCT','FINAL PAID FOS'])['PER PAID CASE'].sum()).reset_index()

            li1=[]
            for i in range(0,len(FINAL_COPY1['PRODUCT'])):
                if (FINAL_COPY1.loc[i,'FINAL PAID FOS']=='NO FOS') or (FINAL_COPY1.loc[i,'FINAL PAID FOS']=='--') or (FINAL_COPY1.loc[i,'FINAL PAID FOS']=='FUNDING'):
                    li1.append(i)

            FINAL_COPY1.drop(li1,axis=0,inplace=True)

            FINAL_COPY1 = FINAL_COPY1.reset_index(drop=True)

            FINAL_COPY1 = FINAL_COPY1.merge(A, left_on='FINAL PAID FOS', right_on='NAMES', how='left')
            FINAL_COPY1.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY', 'TYPE_OF_SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'DATE_OF_BIRTH'], axis=1, inplace=True)

            FINAL_COPY1.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(PIVOT).xlsx', index=False)

            FF = pd.DataFrame(FINAL_COPY[FINAL_COPY['PRODUCT']=='IDFC-TW']).reset_index(drop=True)
            FF1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT']=='IDFC-TW']).reset_index(drop=True)

            FF.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE IDFC-TW.xlsx',index=False)
            FF1.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(PIVOT) IDFC-TW.xlsx',index=False)


            # FF2 = pd.DataFrame(FINAL_COPY[FINAL_COPY['PRODUCT']=='L&T']).reset_index(drop=True)
            # FF3 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT']=='L&T']).reset_index(drop=True)
            #
            # FF2.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE L&T.xlsx',index=False)
            # FF3.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(PIVOT) L&T.xlsx',index=False)

            for i in range(0,len(F['ALLOCATED FOS'])):
                F.loc[i,'TOTAL_FIX_SALARY']=F.loc[i,'TOTAL_CASES']*100

            for i in range(0,len(F['PRODUCT'])):
                for j in range(0,len(TW['PROCESS'])):
                    if F.loc[i,'ALLOCATED FOS']==TW.loc[j,'FOS']:
                        if TW.loc[j,'AGREEMENTID']>=50:
                            if (F.loc[i,'BKT']==1) or (F.loc[i,'BKT']==2) or (F.loc[i,'BKT']==3):
                                if F.loc[i,'Additional_Performance']<15:
                                    F.loc[i,'RB_INCENTIVE']=0
                                elif (F.loc[i,'Additional_Performance']>=15) and (F.loc[i,'Additional_Performance']<20):
                                    F.loc[i,'RB_INCENTIVE']=1500
                                elif (F.loc[i,'Additional_Performance']>=20) and (F.loc[i,'Additional_Performance']<25):
                                    F.loc[i,'RB_INCENTIVE']=3000
                                elif F.loc[i,'Additional_Performance']>=25:
                                    F.loc[i,'RB_INCENTIVE']=5000
                        else:
                            F.loc[i,'RB_INCENTIVE']=0

            F=F.merge(A,left_on='ALLOCATED FOS',right_on='NAMES',how='left')

            F.drop(['PHONE_NUMBER','DEPARTMENT_ID','END_DATE','HIRE_DATE','LOCATION_ID','SALARY','TYPE_OF_SALARY', 'MANAGEMENT_LEVEL','NAMES', 'DATE_OF_BIRTH'],axis=1,inplace=True)

            li2 = []
            for i in range(0, len(F['PRODUCT'])):
                if (F.loc[i, 'ALLOCATED FOS'] == 'NO FOS') or (F.loc[i, 'ALLOCATED FOS'] == '--') or (FINAL_COPY.loc[i, 'ALLOCATED FOS'] == 'FUNDING'):
                    li2.append(i)

            F.drop(li2, axis=0, inplace=True)

            F = F.reset_index(drop=True)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary).xlsx',index=False)

            FF4 = pd.DataFrame(F[F['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
            FF4.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx',index=False)

            # FF5 = pd.DataFrame(F[F['PRODUCT'] == 'L&T']).reset_index(drop=True)
            # FF5.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) L&T.xlsx',index=False)

            if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
            # and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'))
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()
                
                if (final_dep == 'TW') and (final_process == 'IDFC'):
                    FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
                    F = pd.DataFrame(F[F['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)

                # elif (final_dep == 'TW') and (final_process == 'L&T'):
                #     FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'L&T']).reset_index(drop=True)
                #     F = pd.DataFrame(F[F['PRODUCT'] == 'L&T']).reset_index(drop=True)

                fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
                F12 = pd.read_excel(AA123)

                # fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
                # AA1233 = fs1233.open('TC Performance L_T.xlsx')
                # F123 = pd.read_excel(AA1233)

            elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
                fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
                F12 = pd.read_excel(AA123)

                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                if (final_dep == 'TW') and (final_process == 'IDFC'):
                    FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
                    F = pd.DataFrame(F[F['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)

                # elif (final_dep == 'TW') and (final_process == 'L&T'):
                #     FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'L&T']).reset_index(drop=True)
                #     F = pd.DataFrame(F[F['PRODUCT'] == 'L&T']).reset_index(drop=True)

                C = list(FINAL_COPY1.columns)  # FOS_Incentive
                C11 = list(F.columns)  # FOS_Fixed
                C123 = list(F12.columns)  # IDFC-TC_Incentive

                for j in range(0, len(FINAL_COPY1[C[0]])):
                    row_data = list()
                    for col in range(0, len(C)):
                        row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
                    excel_data.append(row_data)

                for j in range(0, len(F[C11[0]])):
                    row_data1 = list()
                    for col in range(0, len(C11)):
                        row_data1.append(str(F.loc[j, C11[col]]))
                    excel_data1.append(row_data1)

                for j in range(0, len(F12[C123[0]])):
                    row_data22 = list()
                    for col1 in range(0, len(C123)):
                        row_data22.append(str(F12.loc[j, C123[col1]]))
                    excel_data123.append(row_data22)

                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()

                return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel123': excel_data123, 'columns123': C123, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

            # elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'):
            #
            #     # fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
            #     # AA1233 = fs1233.open('TC Performance L_T.xlsx')
            #     # F123 = pd.read_excel(AA1233)
            #
            #     final_dep = DEP()
            #     final_process = COMPANY_PROCESS()
            #     if (final_dep == 'TW') and (final_process == 'IDFC'):
            #         FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
            #         F = pd.DataFrame(F[F['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
            #
            #     # elif (final_dep == 'TW') and (final_process == 'L&T'):
            #     #     FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'L&T']).reset_index(drop=True)
            #     #     F = pd.DataFrame(F[F['PRODUCT'] == 'L&T']).reset_index(drop=True)
            #
            #     C = list(FINAL_COPY1.columns)  # FOS_Incentive
            #     C11 = list(F.columns)  # FOS_Fixed
            #     # C1233 = list(F123.columns)  # L_T-TC_Incentive
            #
            #     for j in range(0, len(FINAL_COPY1[C[0]])):
            #         row_data = list()
            #         for col in range(0, len(C)):
            #             row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
            #         excel_data.append(row_data)
            #
            #     for j in range(0, len(F[C11[0]])):
            #         row_data1 = list()
            #         for col in range(0, len(C11)):
            #             row_data1.append(str(F.loc[j, C11[col]]))
            #         excel_data1.append(row_data1)
            #
            #     # for j in range(0, len(F123[C1233[0]])):
            #     #     row_data223 = list()
            #     #     for col1 in range(0, len(C1233)):
            #     #         row_data223.append(str(F123.loc[j, C1233[col1]]))
            #     #     excel_data1233.append(row_data223)
            #
            #     final_dep = DEP()
            #     final_process = COMPANY_PROCESS()
            #     Designation = Employee_Designation()
            #
            #     return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel1233': excel_data1233, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # # 'columns1233': C1233

            else:
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                if (final_dep == 'TW') and (final_process == 'IDFC'):
                    FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)
                    F = pd.DataFrame(F[F['PRODUCT'] == 'IDFC-TW']).reset_index(drop=True)

                # elif (final_dep == 'TW') and (final_process == 'L&T'):
                #     FINAL_COPY1 = pd.DataFrame(FINAL_COPY1[FINAL_COPY1['PRODUCT'] == 'L&T']).reset_index(drop=True)
                #     F = pd.DataFrame(F[F['PRODUCT'] == 'L&T']).reset_index(drop=True)

                C = list(FINAL_COPY1.columns)  # FOS_Incentive
                C11 = list(F.columns)  # FOS_Fixed

                for j in range(0, len(FINAL_COPY1[C[0]])):
                    row_data = list()
                    for col in range(0, len(C)):
                        row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
                    excel_data.append(row_data)

                for j in range(0, len(F[C11[0]])):
                    row_data1 = list()
                    for col in range(0, len(C11)):
                        row_data1.append(str(F.loc[j, C11[col]]))
                    excel_data1.append(row_data1)

                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()

                return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')):
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/salary.html', {'Salary_Update': 'Please upload Allocation file for L&T-TW', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

        # elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'):
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     return render(request, 'FirstLevel/salary.html', {'Salary_Update': 'Please upload Allocation file for IDFC-TW', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/salary.html', {'Salary_Update': 'Upload for both', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    elif request.method != 'POST':
        if (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'))):
            # and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'))
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            if (final_dep == 'TW') and (final_process == 'IDFC'):
                fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
                AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
                FINAL_COPY1 = pd.read_excel(AA)
                F = pd.read_excel(AA2)
                fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
                F12 = pd.read_excel(AA123)
                # fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
                # AA1233 = fs1233.open('TC Performance L_T.xlsx')
                # F123 = pd.read_excel(AA1233)


            # elif (final_dep == 'TW') and (final_process == 'L&T'):
            #     fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            #     AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
            #     AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
            #     FINAL_COPY1 = pd.read_excel(AA)
            #     F = pd.read_excel(AA2)
            #     fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            #     AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
            #     F12 = pd.read_excel(AA123)
            #     fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
            #     AA1233 = fs1233.open('TC Performance L_T.xlsx')
            #     F123 = pd.read_excel(AA1233)
        # elif (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')) and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     if (final_dep == 'TW') and (final_process == 'IDFC'):
        #         fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
        #         AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
        #         AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
        #         FINAL_COPY1 = pd.read_excel(AA)
        #         F = pd.read_excel(AA2)
        #         fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
        #         AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
        #         F12 = pd.read_excel(AA123)
        #
        #     elif (final_dep == 'TW') and (final_process == 'L&T'):
        #         fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
        #         AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
        #         AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
        #         FINAL_COPY1 = pd.read_excel(AA)
        #         F = pd.read_excel(AA2)
        #         fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
        #         AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
        #
        #     F12 = pd.read_excel(AA123)
        #     C = list(FINAL_COPY1.columns)  # FOS_Incentive
        #     C11 = list(F.columns)  # FOS_Fixed
        #     C123 = list(F12.columns)  # IDFC-TC_Incentive
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     print(final_dep)
        #     print(final_process)
        #
        #     for j in range(0, len(FINAL_COPY1[C[0]])):
        #         row_data = list()
        #         for col in range(0, len(C)):
        #             row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
        #         excel_data.append(row_data)
        #
        #     for j in range(0, len(F[C11[0]])):
        #         row_data1 = list()
        #         for col in range(0, len(C11)):
        #             row_data1.append(str(F.loc[j, C11[col]]))
        #         excel_data1.append(row_data1)
        #
        #     for j in range(0, len(F12[C123[0]])):
        #         row_data22 = list()
        #         for col1 in range(0, len(C123)):
        #             row_data22.append(str(F12.loc[j, C123[col1]]))
        #         excel_data123.append(row_data22)
        #
        #     return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel123': excel_data123, 'columns123': C123, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        # elif (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')) and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx')):
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     if (final_dep == 'TW') and (final_process == 'IDFC'):
        #         fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
        #         AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
        #         AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
        #         FINAL_COPY1 = pd.read_excel(AA)
        #         F = pd.read_excel(AA2)
        #         fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
        #         AA1233 = fs1233.open('TC Performance L_T.xlsx')
        #         F123 = pd.read_excel(AA1233)
        #
        #     elif (final_dep == 'TW') and (final_process == 'L&T'):
        #         fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
        #         AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
        #         AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
        #         FINAL_COPY1 = pd.read_excel(AA)
        #         F = pd.read_excel(AA2)
        #         fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
        #         AA1233 = fs1233.open('TC Performance L_T.xlsx')
        #         F123 = pd.read_excel(AA1233)
        #
        #     C = list(FINAL_COPY1.columns)  # FOS_Incentive
        #     C11 = list(F.columns)  # FOS_Fixed
        #     C1233 = list(F123.columns)  # L_T-TC_Incentive
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     for j in range(0, len(FINAL_COPY1[C[0]])):
        #         row_data = list()
        #         for col in range(0, len(C)):
        #             row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
        #         excel_data.append(row_data)
        #
        #     for j in range(0, len(F[C11[0]])):
        #         row_data1 = list()
        #         for col in range(0, len(C11)):
        #             row_data1.append(str(F.loc[j, C11[col]]))
        #         excel_data1.append(row_data1)
        #
        #     for j in range(0, len(F123[C1233[0]])):
        #         row_data223 = list()
        #         for col1 in range(0, len(C1233)):
        #             row_data223.append(str(F123.loc[j, C1233[col1]]))
        #         excel_data1233.append(row_data223)
        #
        #     return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel1233': excel_data1233, 'columns1233': C1233, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        elif os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')):
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            if (final_dep == 'TW') and (final_process == 'IDFC'):
                fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
                AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
                FINAL_COPY1 = pd.read_excel(AA)
                F = pd.read_excel(AA2)

            # elif (final_dep == 'TW') and (final_process == 'L&T'):
            #     fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            #     AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
            #     AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
            #     FINAL_COPY1 = pd.read_excel(AA)
            #     F = pd.read_excel(AA2)

            C = list(FINAL_COPY1.columns)  # FOS_Incentive
            C11 = list(F.columns)  # FOS_FixedC = list(FINAL_COPY1.columns)#FOS_Incentive
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            for j in range(0, len(FINAL_COPY1[C[0]])):
                row_data = list()
                for col in range(0, len(C)):
                    row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
                excel_data.append(row_data)

            for j in range(0, len(F[C11[0]])):
                row_data1 = list()
                for col in range(0, len(C11)):
                    row_data1.append(str(F.loc[j, C11[col]]))
                excel_data1.append(row_data1)
            return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/MASTER FILE IDFC_TW.xlsx')):
            # and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/MASTER FILE L_T.xlsx'))
            if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
                # (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'))
                fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
                F12 = pd.read_excel(AA123)
                C123 = list(F12.columns)  # TC_Incentive
                for j in range(0, len(F12[C123[0]])):
                    row_data22 = list()
                    for col1 in range(0, len(C123)):
                        row_data22.append(str(F12.loc[j, C123[col1]]))
                    excel_data123.append(row_data22)
                # fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
                # AA1233 = fs1233.open('TC Performance L_T.xlsx')
                # F123 = pd.read_excel(AA1233)
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()

                # C1233 = list(F123.columns)  # L_T-TC_Incentive
                # for j in range(0, len(F123[C1233[0]])):
                #     row_data223 = list()
                #     for col1 in range(0, len(C1233)):
                #         row_data223.append(str(F123.loc[j, C1233[col1]]))
                #     excel_data1233.append(row_data223)
                return render(request, 'FirstLevel/salary.html', {'excel1233': excel_data1233, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel123': excel_data123, 'columns123': C123, 'Designation': Designation})
            # 'columns1233': C1233
            # elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'):
            #     fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
            #     AA1233 = fs1233.open('TC Performance L_T.xlsx')
            #     F123 = pd.read_excel(AA1233)
            #     final_dep = DEP()
            #     final_process = COMPANY_PROCESS()
            #     Designation = Employee_Designation()
            #
            #     C1233 = list(F123.columns)  # L_T-TC_Incentive
            #
            #     for j in range(0, len(F123[C1233[0]])):
            #         row_data223 = list()
            #         for col1 in range(0, len(C1233)):
            #             row_data223.append(str(F123.loc[j, C1233[col1]]))
            #         excel_data1233.append(row_data223)
            #     return render(request, 'FirstLevel/salary.html', {'excel1233': excel_data1233, 'columns1233': C1233, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'):
            #     fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            #     AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
            #     F12 = pd.read_excel(AA123)
            #     C123 = list(F12.columns)  # TC_Incentive
            #     final_dep = DEP()
            #     final_process = COMPANY_PROCESS()
            #     Designation = Employee_Designation()
            #
            #     for j in range(0, len(F12[C123[0]])):
            #         row_data22 = list()
            #         for col1 in range(0, len(C123)):
            #             row_data22.append(str(F12.loc[j, C123[col1]]))
            #         excel_data123.append(row_data22)
            #     return render(request, 'FirstLevel/salary.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel123': excel_data123, 'columns123': C123, 'Designation': Designation})
            else:
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()

                # if final_process == 'L&T':
                #     if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'):
                #         final_dep = DEP()
                #         final_process = COMPANY_PROCESS()
                #         Designation = Employee_Designation()
                #
                #         return render(request, 'FirstLevel/salary.html',
                #                       {'Salary_Update': 'Please click on salaries button for updated salaries', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
                #     else:
                #         return HttpResponseRedirect(reverse('basic_app:L_T_MIS'))
                if final_process == 'IDFC':
                    if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')):
                        final_dep = DEP()
                        final_process = COMPANY_PROCESS()
                        Designation = Employee_Designation()

                        return render(request, 'FirstLevel/salary.html',
                                      {'Salary_Update': 'Please refresh Salary data for TC & FOS', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
                    else:
                        return HttpResponseRedirect(reverse('basic_app:IDFC_TW_MIS'))
        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            # if (final_process == 'L&T') and (final_dep == 'TW'):
            #     return HttpResponseRedirect(reverse('basic_app:L_T_MIS'))
            # else:
            fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
            F12 = pd.read_excel(AA123)
            C123 = list(F12.columns)  # TC_Incentive
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            for j in range(0, len(F12[C123[0]])):
                row_data22 = list()
                for col1 in range(0, len(C123)):
                    row_data22.append(str(F12.loc[j, C123[col1]]))
                excel_data123.append(row_data22)
            return render(request, 'FirstLevel/salary.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process,'excel123': excel_data123, 'columns123': C123, 'Designation': Designation})
        # elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx'):
        #     final_dep = DEP()
        #     final_process = COMPANY_PROCESS()
        #     Designation = Employee_Designation()
        #
        #     if (final_process == 'IDFC') and (final_dep == 'TW'):
        #         return HttpResponseRedirect(reverse('basic_app:IDFC_TW_MIS'))
        #     else:
        #         fs1233 = FileSystemStorage(location='media/L_T/TC Incentive')
        #         AA1233 = fs1233.open('TC Performance L_T.xlsx')
        #         F123 = pd.read_excel(AA1233)
        #         final_dep = DEP()
        #         final_process = COMPANY_PROCESS()
        #         Designation = Employee_Designation()
        #         C1233 = list(F123.columns)  # L_T-TC_Incentive
        #
        #         for j in range(0, len(F123[C1233[0]])):
        #             row_data223 = list()
        #             for col1 in range(0, len(C1233)):
        #                 row_data223.append(str(F123.loc[j, C1233[col1]]))
        #             excel_data1233.append(row_data223)
        #         return render(request, 'FirstLevel/salary.html', {'excel1233': excel_data1233, 'columns1233': C1233, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            # if final_process == 'L&T':
            #     if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'):
            #         final_dep = DEP()
            #         final_process = COMPANY_PROCESS()
            #         Designation = Employee_Designation()
            #
            #         return render(request, 'FirstLevel/salary.html', {'Salary_Update': 'Please upload Allocation file for IDFC-TW', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            #     else:
            #         return HttpResponseRedirect(reverse('basic_app:L_T_MIS'))
            if final_process == 'IDFC':
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')):
                    final_dep = DEP()
                    final_process = COMPANY_PROCESS()
                    Designation = Employee_Designation()

                    return render(request, 'FirstLevel/salary.html', {'Salary_Update': 'Please refresh Salary data for TC & FOS', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
                else:
                    return HttpResponseRedirect(reverse('basic_app:IDFC_TW_MIS'))

    C = list(FINAL_COPY1.columns)  # FOS_Incentive
    C11 = list(F.columns)  # FOS_Fixed
    C123 = list(F12.columns)  # IDFC-TC_Incentive
    # C1233 = list(F123.columns)  # L_T-TC_Incentive

    for j in range(0, len(FINAL_COPY1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
        excel_data.append(row_data)

    for j in range(0, len(F[C11[0]])):
        row_data1 = list()
        for col in range(0, len(C11)):
            row_data1.append(str(F.loc[j, C11[col]]))
        excel_data1.append(row_data1)

    for j in range(0, len(F12[C123[0]])):
        row_data22 = list()
        for col1 in range(0, len(C123)):
            row_data22.append(str(F12.loc[j, C123[col1]]))
        excel_data123.append(row_data22)

    # for j in range(0, len(F123[C1233[0]])):
    #     row_data223 = list()
    #     for col1 in range(0, len(C1233)):
    #         row_data223.append(str(F123.loc[j, C1233[col1]]))
    #     excel_data1233.append(row_data223)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/salary.html',{'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel123': excel_data123, 'columns123': C123, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
# 'excel1233': excel_data1233, 'columns1233': C1233

def MASTER_SALARY_IDFC(request):
    excel_data = []
    excel_data1 = []
    excel_data2 = []
    FINAL_PAYOUT = pd.DataFrame()
    COMBINED_SALARY = pd.DataFrame()
    LTTW = pd.DataFrame()
    AA1 = pd.DataFrame()

    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/MIS/MASTER_FILE_IDFC_HL.xlsx')):
            # and (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')))
            # and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'))
            # fs = FileSystemStorage(location='media/L_T/MIS')
            # fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/Employees')
            fs3 = FileSystemStorage(location='media/IDFC_HL/MIS')

            A123 = fs3.open('MASTER_FILE_IDFC_HL.xlsx')
            A = pd.read_excel(A123)
            UNIQUE_NAME1 = fs2.open('Employee_Database.xlsx')
            UNIQUE_NAME=pd.read_excel(UNIQUE_NAME1)

            # for i in range(31, 0, -1):
            #     if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/MIS/IDFC_PAID FILE_'+ str(i) +'AUG21.xlsx')):
            #         A1234 = fs3.open('IDFC_PAID FILE_' + str(i) + 'AUG21.xlsx')
            #         PAID_FILE = pd.read_excel(A1234)

            # for i in range(31, 0, -1):
            #     if os.path.exists(
            #             '/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/L_T Allocation ' + str(i) + ' AUG 21.xlsx'):
            #         AA124 = fs.open('L_T Allocation ' + str(i) + ' AUG 21.xlsx')
            #         LTTW = pd.read_excel(AA124)
            #     else:
            #         continue
            # for i in range(31, 0, -1):
            #     if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/IDFC_TW/MIS/IDFC_TW ALLOCATION ' + str(i) + ' AUG 21.xlsx'):
            #         AA125 = fs1.open('IDFC_TW ALLOCATION ' + str(i) + ' AUG 21.xlsx')
            #         IDFCTW = pd.read_excel(AA125)
            #     else:
            #         continue
            # for i in range(31, 0, -1):
            #     if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/MIS/IDFC_ALLOCATION_' + str(i) + 'AUG21.xlsx'):
            #         AA126 = fs3.open('IDFC_ALLOCATION_' + str(i) + 'AUG21.xlsx')
            #         IDFCHL = pd.read_excel(AA126)
            #     else:
            #         continue
            #
            # print('LT FILE')
            # print(LTTW.head(10))
            # print('IDFC TW FILE')
            # print(IDFCTW.head(10))
            # print('IDFC HL FILE')
            # print(IDFCHL.head(10))
            # print('A')
            # print(UNIQUE_NAME.head(10))
            #
            # LTTW.drop('TOTAL COLLECTABLE', axis=1, inplace=True)
            #
            # MASTER = pd.concat([IDFCHL, LTTW])
            # MASTER = pd.concat([MASTER, IDFCTW])
            # MASTER = MASTER.reset_index(drop=True)

            # for i in range(0, len(MASTER['COMPANY'])):
            #     if (MASTER.loc[i, 'COMPANY'] == 'HFC') or (MASTER.loc[i, 'COMPANY'] == 'SUVIDHA'):
            #         MASTER.loc[i, 'PROCESS'] = 'IDFC-HL'
            #     elif MASTER.loc[i, 'COMPANY'] == 'L&T':
            #         MASTER.loc[i, 'PROCESS'] = 'TW'
            #     elif MASTER.loc[i, 'COMPANY'] == 'IDFC - TW':
            #         MASTER.loc[i, 'PROCESS'] = 'TW'
            #
            # MASTER_COUNT = pd.DataFrame(MASTER.groupby(['PROCESS', 'FOS'])['AGREEMENTID'].count()).reset_index()
            #
            # dr = []
            # for i in range(0, len(MASTER_COUNT['FOS'])):
            #     if MASTER_COUNT.loc[i, 'FOS'] == 'NO FOS' or MASTER_COUNT.loc[i, 'FOS'] == 'LOW POS':
            #         dr.append(i)
            #
            # MASTER_COUNT.drop(dr, axis=0, inplace=True)
            #
            # MASTER_COUNT = MASTER_COUNT.reset_index(drop=True)
            #
            # BKT1B = []
            # for i in range(0, len(PAID_FILE['PROCESS'])):
            #     if (PAID_FILE.loc[i, 'BKT'] == 1) and (PAID_FILE.loc[i, 'BOUNCING AMT.'] != 0) and (
            #             PAID_FILE.loc[i, 'MODE'] != 'CASH'):
            #         BKT1B.append(i)
            #
            # BKT1B
            #
            # PAID_FILE.drop(BKT1B, axis=0, inplace=True)
            #
            # PAID_FILE = PAID_FILE.reset_index(drop=True)
            #
            # BOU_AMT = pd.DataFrame(PAID_FILE.groupby(['FOS', 'BKT'])['BOUNCING AMT.'].sum()).reset_index()
            #
            # PAID_FILE = PAID_FILE[PAID_FILE['BOUNCING AMT.'] >= 200]
            #
            # BOU = pd.DataFrame(PAID_FILE.groupby(['FOS', 'BKT', 'AGREEMENTID'])['BOUNCING AMT.'].sum()).reset_index()
            #
            # d = []
            # for i in range(0, len(BOU['FOS'])):
            #     if BOU.loc[i, 'BOUNCING AMT.'] == 0:
            #         d.append(i)
            #
            # BOU.drop(d, axis=0, inplace=True)
            #
            # BOU = BOU.reset_index(drop=True)
            #
            # BOUNCING_CASE_COUNT = pd.DataFrame(BOU.groupby(['FOS', 'BKT'])['AGREEMENTID'].count()).reset_index()
            #
            # BOUNCING_CASE_COUNT.head()

            for i in range(0, len(A['AGREEMENTID'])):
                if A.loc[i, 'Billing PAID AMT.'] * 2 / 100 > 20000:
                    A.loc[i, 'FOS_PAYOUT'] = 20000
                else:
                    A.loc[i, 'FOS_PAYOUT'] = A.loc[i, 'Billing PAID AMT.'] * 2 / 100

            F = pd.DataFrame(A.groupby(['FOS'])['POS'].sum()).reset_index()

            R1 = pd.DataFrame(A.groupby(['FOS', 'STATUS'])['POS'].sum()).reset_index()

            R2 = pd.DataFrame(A.groupby(['FOS', 'STATUS'])['AGREEMENTID'].count()).reset_index()

            AA=pd.DataFrame(A.groupby(['FOS'])['AGREEMENTID'].count()).reset_index()

            F=F.merge(AA,how='outer')

            F=F.reset_index(drop=True)

            F.rename({'AGREEMENTID':'CASE_COUNT'},axis=1,inplace=True)

            # BOUNCING_CASE_COUNT.rename({'PROCESS': 'COMPANY'}, axis=1, inplace=True)

            # BOUNCING_CASE_COUNT['BKT'].unique()

            # for i in range(0, len(BOUNCING_CASE_COUNT['FOS'])):
            #     if BOUNCING_CASE_COUNT.loc[i, 'BKT'] == 0:
            #         BOUNCING_CASE_COUNT.loc[i, 'BKT'] = 'BKT0'
            #     elif BOUNCING_CASE_COUNT.loc[i, 'BKT'] == 1:
            #         BOUNCING_CASE_COUNT.loc[i, 'BKT'] = 'BKT1'
            #
            # BOUNCING_CASE_COUNT.head()

            # F = F.merge(BOUNCING_CASE_COUNT, how='outer')

            # F.rename({'AGREEMENTID': 'BOUNCING_CASE_COUNT'}, axis=1, inplace=True)

            # BOU_AMT.rename({'PROCESS': 'COMPANY'}, axis=1, inplace=True)

            # BOU_AMT['BKT'].unique()

            # for i in range(0, len(BOU_AMT['FOS'])):
            #     if BOU_AMT.loc[i, 'BKT'] == 0:
            #         BOU_AMT.loc[i, 'BKT'] = 'BKT0'
            #     elif BOU_AMT.loc[i, 'BKT'] == 1:
            #         BOU_AMT.loc[i, 'BKT'] = 'BKT1'
            #     elif BOU_AMT.loc[i, 'BKT'] == 6:
            #         BOU_AMT.loc[i, 'BKT'] = 'BKT6'

            # F = F.merge(BOU_AMT, how='left')

            P = F.copy()

            P = P.iloc[:, :1]

            P['SB'] = np.nan
            P['RB'] = np.nan
            P['NM'] = np.nan
            P['FORECLOSE'] = np.nan
            P['SETTLEMENT'] = np.nan

            COL = list(P.columns)

            for i in range(0, len(R1['FOS'])):
                for j in range(0, len(P['FOS'])):
                    for k in range(0, len(COL)):
                        if (R1.loc[i, 'FOS'] == P.loc[j, 'FOS']) and (R1.loc[i, 'STATUS'] == COL[k]):
                            P.loc[j, COL[k]] = R1.loc[i, 'POS']

            F = F.merge(P, how='outer')

            F.fillna(0, inplace=True)

            F.rename({'SB':'SB_POS','RB':'RB_POS','NM':'NM_POS','FORECLOSE':'FORECLOSE_POS','SETTLEMENT':'SETTLEMENT_POS'},axis=1,inplace=True)

            for i in range(0, len(R2['FOS'])):
                for j in range(0, len(P['FOS'])):
                    for k in range(0, len(COL)):
                        if (R2.loc[i, 'FOS'] == P.loc[j, 'FOS']) and (R2.loc[i, 'STATUS'] == COL[k]):
                            P.loc[j, COL[k]] = R2.loc[i, 'AGREEMENTID']

            F = F.merge(P, how='outer')

            F.fillna(0, inplace=True)

            F.rename({'POS': 'TOTAL POS'}, axis=1, inplace=True)

            F.rename({'SB': 'SB_COUNT', 'RB': 'RB_COUNT', 'NM': 'NM_COUNT', 'FORECLOSE': 'FORECLOSE_COUNT', 'SETTLEMENT': 'SETTLEMENT_COUNT'}, axis=1, inplace=True)

            for i in range(0, len(F['TOTAL POS'])):
                F.loc[i, 'POS'] = F.loc[i, 'SB_POS'] + F.loc[i, 'RB_POS'] + F.loc[i, 'NM_POS'] + F.loc[i, 'FORECLOSE_POS'] + F.loc[i, 'SETTLEMENT_POS']
                F.loc[i, 'TOTAL_PAID_COUNT'] = F.loc[i, 'SB_COUNT'] + F.loc[i, 'RB_COUNT'] + F.loc[i, 'NM_COUNT'] + F.loc[i, 'FORECLOSE_COUNT'] + F.loc[i, 'SETTLEMENT_COUNT']

            for i in range(0, len(F['FOS'])):
                F.loc[i, 'Performance'] = F.loc[i, 'POS'] / F.loc[i, 'TOTAL POS'] * 100

            F.fillna(0, inplace=True)

            PA = pd.DataFrame(A.groupby(['FOS'])['FOS_PAYOUT'].sum()).reset_index()

            F = F.merge(PA, how='outer')

            for i in range(0, len(F['FOS'])):
                F.loc[i, 'VISIT_PAYOUT'] = F.loc[i, 'CASE_COUNT'] * 100

            F['FINAL_PAYOUT'] = F['VISIT_PAYOUT'] + F['FOS_PAYOUT']

            # for i in range(0, len(A['AGREEMENTID'])):
            #     for j in range(0, len(F['FOS'])):
            #         if (A.loc[i, 'BKT'] == 'BKT0' and F.loc[j, 'BKT'] == 'BKT0'):
            #             if (A.loc[i, ['FOS', 'BKT']] == F.loc[j, ['FOS', 'BKT']]).all():
            #                 if (A.loc[i, 'STATUS'] == 'SB'):
            #                     if F.loc[j, 'Performance'] < 88:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 0 / 100
            #                     elif F.loc[j, 'Performance'] >= 88 and F.loc[j, 'Performance'] < 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 0.65 / 100
            #                     elif F.loc[j, 'Performance'] >= 90 and F.loc[j, 'Performance'] < 92:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 1 / 100
            #                     elif F.loc[j, 'Performance'] >= 92 and F.loc[j, 'Performance'] < 95:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 1.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 95:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(2) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 2 / 100
            #
            # for i in range(0, len(A['AGREEMENTID'])):
            #     for j in range(0, len(F['FOS'])):
            #         if (A.loc[i, 'BKT'] == 'BKT1') and (F.loc[j, 'BKT'] == 'BKT1'):
            #             if (A.loc[i, ['FOS', 'BKT']] == F.loc[j, ['FOS', 'BKT']]).all():
            #                 if (A.loc[i, 'STATUS'] != 'SETTLEMENT') and (A.loc[i, 'STATUS'] != 'FORECLOSE'):
            #                     if F.loc[j, 'Performance'] < 82:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 0 / 100
            #                     elif F.loc[j, 'Performance'] >= 82 and F.loc[j, 'Performance'] < 84:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 0.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 84 and F.loc[j, 'Performance'] < 86:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 1 / 100
            #                     elif F.loc[j, 'Performance'] >= 86 and F.loc[j, 'Performance'] < 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 1.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(2) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'Billing PAID AMT.'] * 2 / 100
            #
            # for i in range(0, len(A['AGREEMENTID'])):
            #     for j in range(0, len(F['FOS'])):
            #         if (A.loc[i, 'BKT'] == 'BKT1') and (F.loc[j, 'BKT'] == 'BKT1'):
            #             if (A.loc[i, ['FOS', 'BKT']] == F.loc[j, ['FOS', 'BKT']]).all():
            #                 if (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
            #                     if F.loc[j, 'RB+NM%'] < 22:
            #                         A.loc[i, 'RB PAYOUT'] = 0
            #                     elif F.loc[j, 'RB+NM%'] >= 22 and F.loc[j, 'RB+NM%'] < 24:
            #                         A.loc[i, 'RB PAYOUT'] = 250
            #                     elif F.loc[j, 'RB+NM%'] >= 24 and F.loc[j, 'RB+NM%'] < 28:
            #                         A.loc[i, 'RB PAYOUT'] = 400
            #                     elif F.loc[j, 'RB+NM%'] >= 28:
            #                         A.loc[i, 'RB PAYOUT'] = 500
            #
            # for i in range(0, len(F['FOS'])):
            #     if F.loc[i, 'BKT'] == 'BKT1':
            #         if (F.loc[i, 'RB+NM%'] < 10):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 'Deduction of 10%'
            #         elif (F.loc[i, 'RB+NM%'] >= 10) and (F.loc[i, 'RB+NM%'] < 15):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 'Deduction of 5%'
            #         elif ((F.loc[i, 'RB+NM%'] >= 15) and (F.loc[i, 'RB+NM%'] < 18)):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 0
            #         elif ((F.loc[i, 'RB+NM%'] >= 18) and (F.loc[i, 'RB+NM%'] < 22)):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 1000
            #         elif ((F.loc[i, 'RB+NM%'] >= 22) and (F.loc[i, 'RB+NM%'] < 24)):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 2000
            #         elif ((F.loc[i, 'RB+NM%'] >= 24) and (F.loc[i, 'RB+NM%'] < 30)):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 3000
            #         elif (F.loc[i, 'RB+NM%'] >= 30):
            #             F.loc[i, 'EXTRA INCENTIVE'] = 5000
            #
            # F[F['EXTRA INCENTIVE'] != 0]
            #
            # for i in range(0, len(F['BOUNCING_CASE_COUNT'])):
            #     F.loc[i, 'PENALTY_CHARGES'] = F.loc[i, 'BOUNCING_CASE_COUNT'] / F.loc[i, 'CASE_COUNT'] * 100
            #
            # for i in range(0, len(F['FOS'])):
            #     if F.loc[i, 'PENALTY_CHARGES'] >= 70:
            #         F.loc[i, 'PENALTY_PAYOUT'] = (F.loc[i, 'BOUNCING AMT.']) * (8 / 100)
            #     else:
            #         F.loc[i, 'PENALTY_PAYOUT'] = 0
            #
            # for i in range(0, len(A['PER PAID CASE'])):
            #     if (A.loc[i, 'STATUS'] == 'PART PAID') or (A.loc[i, 'STATUS'] == 'FLOW'):
            #         A.loc[i, 'FOS PERCENTAGE'] = str(0) + '%'
            #         A.loc[i, 'PER PAID CASE'] = 0
            #
            # for i in range(0, len(A['STATUS'])):
            #     if (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
            #         if A.loc[i, 'BKT'] == 'BKT0':
            #             if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']:
            #                 A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
            #             elif A.loc[i, 'Billing PAID AMT.'] < A.loc[i, 'EMI']:
            #                 A.loc[i, 'Billing PAID AMT.'] = 0
            #         elif A.loc[i, 'BKT'] == 'BKT1':
            #             if A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI'] * 2:
            #                 A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI'] * 2
            #             elif (A.loc[i, 'Billing PAID AMT.'] > A.loc[i, 'EMI']) and (
            #                     A.loc[i, 'Billing PAID AMT.'] < A.loc[i, 'EMI'] * 2):
            #                 A.loc[i, 'Billing PAID AMT.'] = A.loc[i, 'EMI']
            #             elif (A.loc[i, 'Billing PAID AMT.'] < A.loc[i, 'EMI']):
            #                 A.loc[i, 'Billing PAID AMT'] = 0
            #
            # for i in range(0, len(A['AGREEMENTID'])):
            #     for j in range(0, len(F['FOS'])):
            #         if (A.loc[i, 'BKT'] == 'BKT0' and F.loc[j, 'BKT'] == 'BKT0'):
            #             if (A.loc[i, ['FOS', 'BKT']] == F.loc[j, ['FOS', 'BKT']]).all():
            #                 if (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
            #                     if F.loc[j, 'Performance'] < 88:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'EMI'] * 0 / 100
            #                     elif F.loc[j, 'Performance'] >= 88 and F.loc[j, 'Performance'] < 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0.65) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'EMI'] * 0.65 / 100
            #                     elif F.loc[j, 'Performance'] >= 90 and F.loc[j, 'Performance'] < 92:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'EMI'] * 1 / 100
            #                     elif F.loc[j, 'Performance'] >= 92 and F.loc[j, 'Performance'] < 94:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'EMI'] * 1.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 94:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(2) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = A.loc[i, 'EMI'] * 2 / 100
            #
            # for i in range(0, len(A['AGREEMENTID'])):
            #     for j in range(0, len(F['FOS'])):
            #         if (A.loc[i, 'BKT'] == 'BKT1' and F.loc[j, 'BKT'] == 'BKT1'):
            #             if (A.loc[i, ['FOS', 'BKT']] == F.loc[j, ['FOS', 'BKT']]).all():
            #                 if (A.loc[i, 'STATUS'] == 'SETTLEMENT') or (A.loc[i, 'STATUS'] == 'FORECLOSE'):
            #                     if F.loc[j, 'Performance'] < 82:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = (A.loc[i, 'EMI'] * 2) * 0 / 100
            #                     elif F.loc[j, 'Performance'] >= 82 and F.loc[j, 'Performance'] < 84:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(0.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = (A.loc[i, 'EMI'] * 2) * 0.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 84 and F.loc[j, 'Performance'] < 86:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1) + '%'
            #                         A.loc[i, 'MOHAK'] = (A.loc[i, 'EMI'] * 2) * 1 / 100
            #                     elif F.loc[j, 'Performance'] >= 86 and F.loc[j, 'Performance'] < 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(1.5) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = (A.loc[i, 'EMI'] * 2) * 1.5 / 100
            #                     elif F.loc[j, 'Performance'] >= 90:
            #                         A.loc[i, 'FOS PERCENTAGE'] = str(2) + '%'
            #                         A.loc[i, 'PER PAID CASE'] = (A.loc[i, 'EMI'] * 2) * 2 / 100
            #
            # l1 = list(A[A['PER PAID CASE'].isnull()].index)
            #
            # for i in range(0, len(A['AGREEMENTID'])):
            #     if A.loc[i, 'STATUS'] == 'SB':
            #         if A.loc[i, 'PER PAID CASE'] > 500:
            #             A.loc[i, 'PER PAID CASE'] = 500
            #     elif (A.loc[i, 'STATUS'] == 'RB') or (A.loc[i, 'STATUS'] == 'NM'):
            #         if A.loc[i, 'PER PAID CASE'] > 1000:
            #             if A.loc[i, 'Billing PAID AMT.'] == A.loc[i, 'EMI']:
            #                 A.loc[i, 'PER PAID CASE'] = 500
            #             elif A.loc[i, 'Billing PAID AMT.'] >= (A.loc[i, 'EMI'] * 2):
            #                 A.loc[i, 'PER PAID CASE'] = 1000
            #
            # F.fillna(0, inplace=True)
            #
            # PPC = pd.DataFrame(A.groupby(['FOS', 'BKT'])['PER PAID CASE'].sum()).reset_index()
            #
            # PPC1 = pd.DataFrame(A.groupby(['FOS', 'BKT'])['RB PAYOUT'].sum()).reset_index()

            # COMBINED_SALARY = F.merge(PPC, left_on=['FOS', 'BKT'], right_on=['FOS', 'BKT'], how='left')
            #
            # COMBINED_SALARY = COMBINED_SALARY.merge(PPC1, left_on=['FOS', 'BKT'], right_on=['FOS', 'BKT'], how='left')
            #
            # COMBINED_SALARY = COMBINED_SALARY.reset_index(drop=True)
            #
            # COMBINED_SALARY.drop(['SB', 'RB', 'NM', 'FORECLOSE', 'SETTLEMENT', 'POS', 'RB+NM'], axis=1, inplace=True)
            #
            # COMBINED_SALARY.drop('BOUNCING_CASE_COUNT', axis=1, inplace=True)
            #
            # COMBINED_SALARY = COMBINED_SALARY.merge(UNIQUE_NAME, how='left', left_on='FOS', right_on='NAMES')
            #
            # COMBINED_SALARY.drop(
            #     ['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'TYPE_OF_SALARY', 'SALARY',
            #      'MANAGEMENT_LEVEL', 'NAMES', 'STAFF', 'DATE_OF_BIRTH'], axis=1, inplace=True)
            #
            # for i in range(0,len(COMBINED_SALARY['FOS'])):
            #     COMBINED_SALARY.loc[i,'TOTAL POS']=round(COMBINED_SALARY.loc[i,'TOTAL POS'],2)
            #     COMBINED_SALARY.loc[i,'Performance']=round(COMBINED_SALARY.loc[i,'Performance'],2)
            #     COMBINED_SALARY.loc[i,'RB+NM%']=round(COMBINED_SALARY.loc[i,'RB+NM%'],2)
            #     COMBINED_SALARY.loc[i,'PENALTY_CHARGES']=round(COMBINED_SALARY.loc[i,'PENALTY_CHARGES'],2)
            #     COMBINED_SALARY.loc[i,'PER PAID CASE']=round(COMBINED_SALARY.loc[i,'PER PAID CASE'],2)
            #
            # li1=[]
            # for i in range(0,len(COMBINED_SALARY['FOS'])):
            #     if (COMBINED_SALARY.loc[i,'FOS'] == '--') or (COMBINED_SALARY.loc[i,'FOS'] == 'FUNDING') or (COMBINED_SALARY.loc[i,'FOS'] == 'NO FOS'):
            #         li1.append(i)
            #
            # COMBINED_SALARY.drop(li1, axis=0, inplace=True)
            #
            # COMBINED_SALARY=COMBINED_SALARY.reset_index(drop=True)
            #
            # COMBINED_SALARY.drop(['BOUNCING AMT.','EXTRA INCENTIVE','PENALTY_CHARGES', 'PENALTY_PAYOUT'], axis=1, inplace=True)
            #
            # COMBINED_SALARY.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/FOS Salary/BKT-WISE PAYOUT.xlsx', index=False)
            #
            # IDFCHL = MASTER_COUNT[MASTER_COUNT['PROCESS'] == 'IDFC-HL']
            #
            # IDFCHL = IDFCHL.reset_index(drop=True)
            #
            # TW = MASTER_COUNT[MASTER_COUNT['PROCESS'] == 'TW']
            #
            # TW = TW.reset_index(drop=True)
            #
            # FINAL_PAYOUT = pd.DataFrame(COMBINED_SALARY.groupby(['FOS', 'PROCESS', 'DEPARTMENT'])['PER PAID CASE', 'RB PAYOUT'].sum()).reset_index()
            #
            # for i in range(0, len(FINAL_PAYOUT['FOS'])):
            #     for j in range(0, len(IDFCHL['FOS'])):
            #         if (FINAL_PAYOUT.loc[i, 'FOS'] == IDFCHL.loc[j, 'FOS']) and (
            #                 (FINAL_PAYOUT.loc[i, 'DEPARTMENT'] == 'HL') and (FINAL_PAYOUT.loc[i, 'PROCESS'] == 'IDFC')):
            #             if (IDFCHL.loc[j, 'AGREEMENTID'] >= 35) and (IDFCHL.loc[j, 'AGREEMENTID'] < 40):
            #                 FINAL_PAYOUT.loc[i, 'FIXED SALARY'] = 13000
            #             elif IDFCHL.loc[j, 'AGREEMENTID'] >= 40:
            #                 FINAL_PAYOUT.loc[i, 'FIXED SALARY'] = 15000
            #             elif MASTER_COUNT.loc[j, 'AGREEMENTID'] < 35:
            #                 FINAL_PAYOUT.loc[i, 'FIXED SALARY'] = round((13000 / 35) * IDFCHL.loc[j, 'AGREEMENTID'], 0)
            #         elif FINAL_PAYOUT.loc[i, 'DEPARTMENT'] == 'TW':
            #             FINAL_PAYOUT.loc[i, 'FIXED SALARY'] = 0
            #
            # FINAL_PAYOUT.drop(['PROCESS', 'DEPARTMENT'], axis=1, inplace=True)
            #
            # FINAL_PAYOUT = FINAL_PAYOUT.merge(UNIQUE_NAME, how='left', left_on='FOS', right_on='NAMES')
            #
            # FINAL_PAYOUT.drop(
            #     ['NAMES', 'MANAGEMENT_LEVEL', 'PROCESS', 'DEPARTMENT', 'TYPE_OF_SALARY', 'SALARY', 'END_DATE',
            #      'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'DEPARTMENT_ID', 'DATE_OF_BIRTH'], axis=1, inplace=True)
            #
            # FINAL_PAYOUT.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/FOS Salary/FINAL PAYOUT IDFC-HL.xlsx', index=False)
            #
            # AA456 = fs3.open('MIS TL-WISE.xlsx')
            # AA = pd.read_excel(AA456)
            #
            # for i in range(0, len(AA['TL'])):
            #     if AA.loc[i, 'BKT'] == 'BKT1':
            #         if AA.loc[i, 'PERFORMANCE'] < 84:
            #             AA.loc[i, 'INCENTIVE'] = 0
            #         elif (AA.loc[i, 'PERFORMANCE'] >= 84) and (AA.loc[i, 'PERFORMANCE'] < 86):
            #             AA.loc[i, 'INCENTIVE'] = 3000
            #         elif (AA.loc[i, 'PERFORMANCE'] >= 86) and (AA.loc[i, 'PERFORMANCE'] < 90):
            #             AA.loc[i, 'INCENTIVE'] = 6000
            #         elif AA.loc[i, 'PERFORMANCE'] >= 90:
            #             AA.loc[i, 'INCENTIVE'] = 12000
            #     if AA.loc[i, 'BKT'] == 'BKT0':
            #         if AA.loc[i, 'PERFORMANCE'] < 90:
            #             AA.loc[i, 'INCENTIVE'] = 0
            #         elif (AA.loc[i, 'PERFORMANCE'] >= 90) and (AA.loc[i, 'PERFORMANCE'] < 92):
            #             AA.loc[i, 'INCENTIVE'] = 5000
            #         elif (AA.loc[i, 'PERFORMANCE'] >= 92) and (AA.loc[i, 'PERFORMANCE'] < 95):
            #             AA.loc[i, 'INCENTIVE'] = 8000
            #         elif AA.loc[i, 'PERFORMANCE'] >= 95:
            #             AA.loc[i, 'INCENTIVE'] = 24000
            # for i in range(0, len(AA['TL'])):
            #     if AA.loc[i, 'BKT'] == 'BKT1':
            #         if AA.loc[i, 'Additional_Performance'] < 22:
            #             AA.loc[i, 'RB_INCENTIVE'] = 0
            #         elif (AA.loc[i, 'Additional_Performance'] >= 22) and (AA.loc[i, 'Additional_Performance'] < 24):
            #             AA.loc[i, 'RB_INCENTIVE'] = 3000
            #         elif (AA.loc[i, 'Additional_Performance'] >= 24) and (AA.loc[i, 'Additional_Performance'] < 28):
            #             AA.loc[i, 'RB_INCENTIVE'] = 5000
            #         elif AA.loc[i, 'Additional_Performance'] >= 28:
            #             AA.loc[i, 'RB_INCENTIVE'] = 10000

            # AA.fillna(0, inplace=True)

            F = F.merge(UNIQUE_NAME, how='left', left_on='FOS', right_on='NAMES')

            AA.drop(['NAMES', 'MANAGEMENT_LEVEL', 'PROCESS', 'DEPARTMENT', 'TYPE_OF_SALARY', 'SALARY', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'DEPARTMENT_ID', 'DATE_OF_BIRTH'], axis=1, inplace=True)

            F.drop(['DEPARTMENT_ID','END_DATE','HIRE_DATE','PHONE_NUMBER','LOCATION_ID','TYPE_OF_SALARY','SALARY','MANAGEMENT_LEVEL','NAMES','STAFF'],axis=1,inplace=True)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/FOS Salary/FINAL PAYOUT IDFC-HL.xlsx', index=False)

        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/salary.html', {'Salary_Update':'Please Refresh Salary for IDFC-HL', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/MASTER_FILE_IDFC_HL.xlsx')):
            # if os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_HL/FOS Salary/FINAL INCENTIVE IDFC-HL(TL).xlsx'):
            fs = FileSystemStorage(location='media/IDFC_HL/FOS Salary')
            AA12 = fs.open('FINAL INCENTIVE IDFC-HL(TL).xlsx')
            AA22 = fs.open('FINAL PAYOUT IDFC-HL.xlsx')
            AA32 = fs.open('BKT-WISE PAYOUT.xlsx')
            AA = pd.read_excel(AA12)
            FINAL_PAYOUT = pd.read_excel(AA22)
            COMBINED_SALARY = pd.read_excel(AA32)
            # else:
            #     final_dep = DEP()
            #     final_process = COMPANY_PROCESS()
            #     Designation = Employee_Designation()
            #
            #     return render(request, 'FirstLevel/salary.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        else:
            return HttpResponseRedirect(reverse('basic_app:IDFC_HL_MIS'))

    C = list(FINAL_PAYOUT.columns)
    C11 = list(AA.columns)
    C12 = list(COMBINED_SALARY.columns)

    for j in range(0, len(FINAL_PAYOUT[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(FINAL_PAYOUT.loc[j, C[col]]))
        excel_data.append(row_data)

    for j in range(0, len(AA[C11[0]])):
        row_data1 = list()
        for col in range(0, len(C11)):
            row_data1.append(str(AA.loc[j, C11[col]]))
        excel_data1.append(row_data1)

    for j in range(0, len(COMBINED_SALARY[C12[0]])):
        row_data2 = list()
        for col in range(0, len(C12)):
            row_data2.append(str(COMBINED_SALARY.loc[j, C12[col]]))
        excel_data2.append(row_data2)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel1': excel_data1, 'excel2': excel_data2, 'columns2': C12, 'columns': C, 'columns1': C11, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def MASTER_SALARY_FULLERTON(request):
    excel_data = []
    excel_data1 = []
    excel_data2 = []
    FINAL_PAYOUT = pd.DataFrame()
    COMBINED_SALARY = pd.DataFrame()
    LTTW = pd.DataFrame()
    AA1 = pd.DataFrame()

    if request.method == 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/MASTER_FILE_FULLERTON_RECOVERY.xlsx')):
            fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
            fs1 = FileSystemStorage(location='media/FULLERTON_RECOVERY/Billing')
            fs2 = FileSystemStorage(location='media/Employees')
            fs3 = FileSystemStorage(location='media/FULLERTON_RECOVERY/MIS')

            A123 = fs.open('MASTER_FILE_FULLERTON_RECOVERY.xlsx')
            A1 = fs1.open('PAYOUT_FULLERTON_RECOVERY.xlsx')
            A = pd.read_excel(A123)
            C = pd.read_excel(A1)
            UNIQUE_NAME1 = fs2.open('Employee_Database.xlsx')
            UNIQUE_NAME=pd.read_excel(UNIQUE_NAME1)

            for i in range(31, 0, -1):
                if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/MIS/FULLERTON_RECOVERY_PAID FILE_'+ str(i) +'OCT21.xlsx')):
                    A1234 = fs3.open('FULLERTON_RECOVERY_PAID FILE_' + str(i) + 'OCT21.xlsx')
                    B = pd.read_excel(A1234)

            COLLECTION = C['MONEY_COLLECTION'].sum()

            COLLECTION

            U = UNIQUE_NAME.copy()

            dr = list(B[B['MODE'] == 'ECS'].index)

            B.drop(dr, axis=0, inplace=True)

            B = B.reset_index(drop=True)

            B.shape

            B.head()

            B.groupby(['AGREEMENTID', 'FOS'])['FOS'].count()

            B1 = pd.DataFrame(B.groupby(['AGREEMENTID', 'FOS'])['MODE'].count()).reset_index()

            B1.shape

            B1

            B1.drop('MODE', axis=1, inplace=True)

            B1.rename({'FOS': 'FINAL PAID FOS'}, axis=1, inplace=True)

            B1.head(1)

            A.head(1)

            A = A.merge(B1, how='outer')

            A.head()

            A[A['STATUS'] == 'FLOW']['FINAL PAID FOS'].unique()

            A['FINAL PAID FOS'].fillna('--', inplace=True)

            A['FINAL PAID FOS'].unique()

            UN = list(U[U['DESIGNATION'] == 'OFFICE']['NAMES'])

            for i in range(0, len(A['AGREEMENTID'])):
                if (A.loc[i, 'FOS'] in UN) and (A.loc[i, 'FINAL PAID FOS'] in UN):
                    A.loc[i, 'FOS'] = 'NITIN JAIN'
                    A.loc[i, 'FINAL PAID FOS'] = 'NITIN JAIN'
                elif A.loc[i, 'FINAL PAID FOS'] in UN:
                    A.loc[i, 'FINAL PAID FOS'] = 'NITIN JAIN'
                elif A.loc[i, 'FOS'] in UN:
                    A.loc[i, 'FOS'] = 'NITIN JAIN'

            for i in range(0, len(A['AGREEMENTID'])):
                if A.loc[i, 'FINAL PAID FOS'] == 'NO FOS':
                    A.loc[i, 'FINAL PAID FOS'] = 'NITIN JAIN'

            A.head()

            A['FINAL PAID FOS'].unique()

            A['FOS'].unique()

            A.head()

            M = pd.DataFrame(A.groupby(['FOS'])['POS'].sum()).reset_index()

            M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)

            R = pd.DataFrame(A.groupby(['FOS'])['AGREEMENTID'].count()).reset_index()

            F = M.merge(R, how='outer')

            F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)

            R1 = pd.DataFrame(A.groupby(['FOS', 'STATUS'])['AGREEMENTID'].count()).reset_index()

            P = F.copy()

            P.drop(['TOTAL_POS', 'TOTAL_CASES'], axis=1, inplace=True)

            P['FLOW'] = np.nan
            P['PAID'] = np.nan

            COL = P.columns

            R1.head()

            for i in range(0, len(R1['FOS'])):
                for j in range(0, len(P['FLOW'])):
                    for k in range(0, len(COL)):
                        if (R1.loc[i, 'FOS'] == P.loc[j, 'FOS']) and R1.loc[i, 'STATUS'] == COL[k]:
                            P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']

            P.head()

            F = F.merge(P, how='outer')

            F.head()

            F.fillna(0, inplace=True)

            F.rename({'FLOW': 'FLOW_CASES', 'PAID': 'PAID_CASES'}, axis=1, inplace=True)

            F.head()

            R2 = pd.DataFrame(A.groupby(['FINAL PAID FOS', 'STATUS'])['TOTAL PAID'].sum()).reset_index()

            R2

            dr = []
            for i in range(0, len(R2['FINAL PAID FOS'])):
                if (R2.loc[i, 'FINAL PAID FOS'] == '--') or (R2.loc[i, 'FINAL PAID FOS'] == 'NO FOS'):
                    dr.append(i)

            R2.drop(dr, axis=0, inplace=True)

            R2 = R2.reset_index(drop=True)

            R2.rename({'FINAL PAID FOS': 'FOS'}, axis=1, inplace=True)

            R2

            P.head()

            COL

            for i in range(0, len(P['FOS'])):
                for j in range(0, len(R2['FOS'])):
                    for k in range(0, len(COL)):
                        if (R2.loc[j, 'FOS'] == P.loc[i, 'FOS']) and (R2.loc[j, 'STATUS'] == COL[k]):
                            P.loc[i, 'TOTAL_PAID'] = R2.loc[j, 'TOTAL PAID']

            P

            F = F.merge(P, how='outer')

            F.rename({'FLOW': 'FLOW_POS', 'TOTAL_PAID': 'PAID_POS'}, axis=1, inplace=True)

            F.fillna(0, inplace=True)

            F.drop('FLOW_POS', axis=1, inplace=True)

            F.head()

            F.rename({'PAID_POS': 'MONEY_COLLECTION'}, axis=1, inplace=True)

            F.head()

            F

            F['FIXED_PAYOUT'] = F['TOTAL_CASES'] * 100

            F.head()

            for i in range(0, len(F['FOS'])):
                if F.loc[i, 'MONEY_COLLECTION'] < 500000:
                    F.loc[i, 'INCENTIVE%'] = '6%'
                    F.loc[i, 'INCENTIVE'] = F.loc[i, 'MONEY_COLLECTION'] * 6 / 100
                elif F.loc[i, 'MONEY_COLLECTION'] >= 500000:
                    F.loc[i, 'INCENTIVE%'] = '7%'
                    F.loc[i, 'INCENTIVE'] = F.loc[i, 'MONEY_COLLECTION'] * 7 / 100

            for i in range(0, len(F['FOS'])):
                if F.loc[i, 'FOS'] == 'NITIN JAIN':
                    if COLLECTION >= 1000000:
                        F.loc[i, 'INCENTIVE%'] = '2%'
                        F.loc[i, 'INCENTIVE'] = F.loc[i, 'MONEY_COLLECTION'] * 2 / 100
                        F.loc[i, 'FIXED_PAYOUT'] = 0
                    else:
                        F.loc[i, 'INCENTIVE%'] = '0%'
                        F.loc[i, 'INCENTIVE'] = 0
                        F.loc[i, 'FIXED_PAYOUT'] = 0

            F

            F['TOTAL_SALARY'] = F['FIXED_PAYOUT'] + F['INCENTIVE']

            F.head()

            F

            dr = list(F[F['FOS'] == 'NO FOS'].index)

            dr

            F.drop(dr, axis=0, inplace=True)

            F

            F.reset_index(drop=True)

            F = F.merge(UNIQUE_NAME, left_on='FOS', right_on='NAMES', how='left')

            F.columns

            F.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'TYPE_OF_SALARY', 'SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'STAFF', 'DATE_OF_BIRTH'], axis=1, inplace=True)

            F

            F['TOTAL_POS'] = round(F['TOTAL_POS'],2)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx', index=False)

            FINAL_PAYOUT = F.copy()

        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/salary.html', {'Salary_Update':'Please upload Allocation file for FULLERTON_RECOVERY', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/MASTER_FILE_FULLERTON_RECOVERY.xlsx')):
            if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')):
                fs = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                AA12 = fs.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                FINAL_PAYOUT = pd.read_excel(AA12)
            else:
                final_dep = DEP()
                final_process = COMPANY_PROCESS()
                Designation = Employee_Designation()

                return render(request, 'FirstLevel/salary.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
        else:
            return HttpResponseRedirect(reverse('basic_app:FULLERTON_RECOVERY_MIS'))

    C = list(FINAL_PAYOUT.columns)

    for j in range(0, len(FINAL_PAYOUT[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(FINAL_PAYOUT.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def BAJAJ_MIS(request):
    excel_data = []
    F1 = pd.DataFrame()
    if request.method == 'POST':
        Allocation1 = request.FILES['Allocation']
        Paidfile1 = request.FILES['Paid_File']
        A = pd.read_excel(Allocation1)
        B = pd.read_excel(Paidfile1)

        fs = FileSystemStorage(location='media/BAJAJ-CD/MIS')
        fs.save(Allocation1.name, Allocation1)
        fs.save(Paidfile1.name, Paidfile1)


        fs2 = FileSystemStorage(location='media/Employees')
        E = fs2.open('Employee_Database.xlsx')
        print(A.head())

        B1 = pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

        B2 = pd.DataFrame(B.groupby(['AGREEMENTID', 'TC'])['PAID AMOUNT'].count()).reset_index()

        ECS = pd.DataFrame(B.groupby(['AGREEMENTID', 'MODE'])['PAID AMOUNT'].sum()).reset_index()

        ECS = ECS[ECS['MODE'] == 'ECS']

        ECS.rename({'PAID AMOUNT': 'ECS'}, axis=1, inplace=True)

        B1 = B1.merge(ECS, how='left')

        B1.drop('MODE', axis=1, inplace=True)

        B1.fillna(0, inplace=True)

        B1['FINAL PAID AMOUNT'] = B1['PAID AMOUNT'] - B1['ECS']

        B2.drop('PAID AMOUNT', axis=1, inplace=True)

        B2.rename({'TC': 'PAID TC', 'AGREEMENTID': 'LOAN_NUMBER'}, axis=1, inplace=True)

        B1.drop(['PAID AMOUNT', 'ECS'], axis=1, inplace=True)

        B1.rename({'FINAL PAID AMOUNT': 'PAID AMOUNT'}, axis=1, inplace=True)

        B1.rename({'AGREEMENTID': 'LOAN_NUMBER'}, axis=1, inplace=True)

        A = A.merge(B2, how='left')

        A = A.merge(B1, how='left')

        for i in range(0, len(A['LOAN_NUMBER'])):
            if str(A.loc[i, 'PAID AMOUNT']) == 'nan':
                A.loc[i, 'MOHAK STATUS'] = 'UNPAID'
            elif str(A.loc[i, 'PAID AMOUNT']) != 'nan':
                A.loc[i, 'MOHAK STATUS'] = 'PAID'

        A['MOHAK STATUS'].unique()

        for i in range(0, len(A['PAID AMOUNT'])):
            if A.loc[i, 'MOHAK STATUS'] == 'UNPAID':
                A.loc[i, 'PAID AMOUNT'] = 0

        A['PAID TC'].fillna('--', inplace=True)

        A.rename({'MOHAK STATUS': 'STATUS'}, axis=1, inplace=True)

        A.to_excel(r'media/BAJAJ-CD/MIS/MASTER_FILE_BAJAJ.xlsx', index=False)

        MIS = pd.DataFrame(A.groupby(['TC NAME'])['POS'].sum().reset_index())

        dr = []
        for i in range(0, len(MIS['TC NAME'])):
            if MIS.loc[i, 'TC NAME'] == 'NO TC':
                dr.append(i)

        MIS.drop(dr, axis=0, inplace=True)

        MIS = MIS.reset_index(drop=True)

        for i in range(0, len(A['LOAN_NUMBER'])):
            if A.loc[i, 'STATUS'] == 'PAID':
                if A.loc[i, 'PAID TC'] != 'SYS. PAID':
                    if A.loc[i, 'TC NAME'] != A.loc[i, 'PAID TC']:
                        print("ACTUAL TC-", A.loc[i, 'TC NAME'], "PAID TC-", A.loc[i, 'PAID TC'])

        P = pd.DataFrame(A.groupby(['PAID TC'])['PAID AMOUNT'].sum().reset_index())

        MIS = MIS.merge(P, left_on='TC NAME', right_on='PAID TC', how='left')

        MIS.drop(['PAID TC'], axis=1, inplace=True)

        MIS['PERFORMANCE'] = MIS['PAID AMOUNT'] / MIS['POS'] * 100

        for i in range(0, len(MIS['TC NAME'])):
            if (MIS.loc[i, 'PAID AMOUNT'] >= 150000) and (MIS.loc[i, 'PAID AMOUNT'] < 200000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 1500
            elif (MIS.loc[i, 'PAID AMOUNT'] >= 200000) and (MIS.loc[i, 'PAID AMOUNT'] < 250000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 2500
            elif (MIS.loc[i, 'PAID AMOUNT'] >= 250000) and (MIS.loc[i, 'PAID AMOUNT'] < 300000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 4000
            elif (MIS.loc[i, 'PAID AMOUNT'] >= 300000) and (MIS.loc[i, 'PAID AMOUNT'] < 350000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 7000
            elif (MIS.loc[i, 'PAID AMOUNT'] >= 350000) and (MIS.loc[i, 'PAID AMOUNT'] < 400000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 10000
            elif (MIS.loc[i, 'PAID AMOUNT'] >= 400000):
                MIS.loc[i, 'FLAT INCENTIVE'] = 12000
            else:
                MIS.loc[i, 'FLAT INCENTIVE'] = 0

        SS = pd.DataFrame(A.groupby(['LOAN_STATUS', 'BUCKET'])['POS', 'PAID AMOUNT'].sum()).reset_index()

        for i in range(0, len(SS['LOAN_STATUS'])):
            if (SS.loc[i, 'LOAN_STATUS'] == 'EXPIRE') & (SS.loc[i, 'BUCKET'] == 3):
                SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                SS.loc[i, 'PAYOUT PERCENTAGE'] = '18%'
                SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 18 / 100
            elif (SS.loc[i, 'LOAN_STATUS'] == 'EXPIRE') & (SS.loc[i, 'BUCKET'] == 2):
                SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                SS.loc[i, 'PAYOUT PERCENTAGE'] = '18%'
                SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 18 / 100
            elif (SS.loc[i, 'LOAN_STATUS'] == 'ACTIVE') & (SS.loc[i, 'BUCKET'] == 3):
                if (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 7:
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '12%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 12 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 7) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 8):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '13%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 13 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 8) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 9):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '14%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 14 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 9) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 10):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '15%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 15 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 10) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 11):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '16%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 16 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 11) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 12):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '17%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 17 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 12):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '18%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 18 / 100
            elif (SS.loc[i, 'LOAN_STATUS'] == 'ACTIVE') & (SS.loc[i, 'BUCKET'] == 4):
                if (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 1:
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '13%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 13 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 1) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 2):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '15%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 15 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 2) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 3):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '17%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 17 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 3) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 4):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '18%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 18 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 4) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 5):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '19%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 19 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 1) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 2):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '20%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 20 / 100
            elif (SS.loc[i, 'LOAN_STATUS'] == 'ACTIVE') & ((SS.loc[i, 'BUCKET'] == 5) or (SS.loc[i, 'BUCKET'] == 6)):
                if (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 <= 1:
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '14%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 14 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 1) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 2):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '16%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 16 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 2) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 3):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '17%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 17 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 3) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 4):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '18%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 18 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 4) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 5):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '20%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 20 / 100
                elif ((SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 > 1) and (
                        (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100 < 2):
                    SS.loc[i, 'PERFORMANCE'] = (SS.loc[i, 'PAID AMOUNT'] / SS.loc[i, 'POS']) * 100
                    SS.loc[i, 'PAYOUT PERCENTAGE'] = '21%'
                    SS.loc[i, 'PAYOUT'] = SS.loc[i, 'PAID AMOUNT'] * 21 / 100

        A = pd.read_excel(E)

        MIS = MIS.merge(A, left_on='TC NAME', right_on='NAMES', how='left')

        MIS.columns

        MIS.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY', 'NAMES', 'DATE_OF_BIRTH'], axis=1,
                 inplace=True)

        for i in range(0,len(MIS['PERFORMANCE'])):
            MIS.loc[i,'PERFORMANCE']=round(MIS.loc[i,'PERFORMANCE'],2)

        for i in range(0,len(SS['PERFORMANCE'])):
            SS.loc[i,'PERFORMANCE']=round(SS.loc[i,'PERFORMANCE'],2)

        MIS.to_excel(r'media/BAJAJ-CD/MIS/BAJAJ TC-WISE MIS.xlsx', index=False)

        SS.to_excel(r'media/BAJAJ-CD/Billing/BAJAJ PAYOUT.xlsx', index=False)

        SS1=SS.copy()

        SS1.drop(["PAYOUT PERCENTAGE","PAYOUT"],axis=1,inplace=True)

        SS1.to_excel(r'media/BAJAJ-CD/MIS/BAJAJ_PERFORMANCE.xlsx', index=False)

    elif request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/BAJAJ-CD/MIS/BAJAJ_PERFORMANCE.xlsx')):
            fs = FileSystemStorage(location='media/BAJAJ-CD/MIS')
            AA = fs.open('BAJAJ_PERFORMANCE.xlsx')
            SS1 = pd.read_excel(AA)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C = list(SS1.columns)

    for j in range(0, len(SS1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(SS1.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/upload_excel.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def BAJAJ_BILLING(request):
    excel_data=[]
    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/BAJAJ-CD/Billing/BAJAJ PAYOUT.xlsx')):
            fs = FileSystemStorage(location='media/BAJAJ-CD/Billing')
            AA = fs.open('BAJAJ PAYOUT.xlsx')
            F1 = pd.read_excel(AA)
            F1.fillna(0,inplace=True)
            Total_Payout = round(sum(F1['PAYOUT']), 2)
        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/upload_excel.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

    C = list(F1.columns)

    for j in range(0, len(F1[C[0]])):
        row_data = list()
        for col in range(0,len(C)):
            row_data.append(str(F1.loc[j,C[col]]))
        excel_data.append(row_data)
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/Billing.html', {'Billing': excel_data, 'columns': C, 'Total_Payout': Total_Payout,'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def BAJAJ_SALARY(request):
    excel_data=[]
    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/BAJAJ-CD/MIS/BAJAJ TC-WISE MIS.xlsx')):
            fs = FileSystemStorage(location='media/BAJAJ-CD/MIS')
            AA = fs.open('BAJAJ TC-WISE MIS.xlsx')
            FINAL_COPY1 = pd.read_excel(AA)
        else:
            return HttpResponseRedirect(reverse('basic_app:BAJAJ_MIS'))

    C = list(FINAL_COPY1.columns)

    for j in range(0, len(FINAL_COPY1[C[0]])):
        row_data = list()
        for col in range(0, len(C)):
            row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
        excel_data.append(row_data)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/salary.html', {'excel12334': excel_data, 'columns12334': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_TW_SALARY_TC(request):
    excel_data = []
    excel_data1 = []
    excel_data123 = []
    F12 = pd.DataFrame()
    a = 0

    if request.method == 'POST':
        if (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx'))):
            for i in range(31, 0, -1):
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')):
                    fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
                    AA122 = fs1.open('IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')
                    PAID_FILE_IDFC_TW = pd.read_excel(AA122)
                else:
                    continue

            fs1 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            fs2 = FileSystemStorage(location='media/Employees')
            AA1 = fs1.open('MASTER FILE IDFC_TW.xlsx')
            E = fs2.open('Employee_Database.xlsx')

            A = pd.read_excel(AA1)

            A.head()

            FUNDING_LIST=list(PAID_FILE_IDFC_TW[PAID_FILE_IDFC_TW['FOS']=='FUNDING']['AGREEMENTID'])

            for i in range(0,len(A['AGREEMENTID'])):
                for j in range(0,len(FUNDING_LIST)):
                    if A.loc[i,'AGREEMENTID']==FUNDING_LIST[j]:
                        A.loc[i,'STATUS']='FLOW'


            F1 = pd.DataFrame(A.groupby(['TC NAME', 'BKT'])['POS'].sum()).reset_index()
            F2 = pd.DataFrame(A.groupby(['TL', 'BKT'])['POS'].sum()).reset_index()

            F1.head()

            F2.head()

            F = F1.copy()
            F3 = F2.copy()

            R1 = pd.DataFrame(A.groupby(['TC NAME', 'BKT', 'STATUS'])['POS'].sum()).reset_index()
            R2 = pd.DataFrame(A.groupby(['TL', 'BKT', 'STATUS'])['POS'].sum()).reset_index()

            R1.head()

            R2.head()

            P = F.copy()
            P2 = F3.copy()

            P.head()

            P2

            P = P.iloc[:, :2]
            P2 = P2.iloc[:, :2]

            P['SB'] = np.nan
            P['RB'] = np.nan
            P['NM'] = np.nan
            P['FORECLOSE'] = np.nan
            P['SETTLEMENT'] = np.nan
            P['MONEY COLLECTION'] = np.nan
            P2['SB'] = np.nan
            P2['RB'] = np.nan
            P2['NM'] = np.nan
            P2['FORECLOSE'] = np.nan
            P2['SETTLEMENT'] = np.nan

            COL = list(P.columns)
            COL1 = list(P2.columns)

            for i in range(0, len(R1['TC NAME'])):
                for j in range(0, len(P['TC NAME'])):
                    for k in range(0, len(COL)):
                        if ((R1.loc[i, ['TC NAME', 'BKT']] == P.loc[j, ['TC NAME', 'BKT']]).all()) and R1.loc[i, 'STATUS'] == COL[k]:
                            P.loc[j, COL[k]] = R1.loc[i, 'POS']
            for i in range(0, len(R2['TL'])):
                for j in range(0, len(P2['TL'])):
                    for k in range(0, len(COL1)):
                        if ((R2.loc[i, ['TL', 'BKT']] == P2.loc[j, ['TL', 'BKT']]).all()) and R2.loc[i, 'STATUS'] == \
                                COL1[k]:
                            P2.loc[j, COL1[k]] = R2.loc[i, 'POS']

            R5 = pd.DataFrame(A.groupby(['TC NAME', 'BKT'])['Billing PAID AMT.'].sum()).reset_index()

            R5.head()

            R5.rename({'Billing PAID AMT.': 'MONEY COLLECTION'}, axis=1, inplace=True)

            R5

            P.head()

            COL

            for i in range(0, len(R5['TC NAME'])):
                for j in range(0, len(P['TC NAME'])):
                    for k in range(0, len(COL)):
                        if ((R5.loc[i, ['TC NAME', 'BKT']] == P.loc[j, ['TC NAME', 'BKT']]).all()):
                            P.loc[j, 'MONEY COLLECTION'] = R5.loc[i, 'MONEY COLLECTION']

            F.head()

            F3.head()

            P

            F = F.merge(P, how='outer')

            F3 = F3.merge(P2, how='outer')

            F.fillna(0, inplace=True)
            F3.fillna(0, inplace=True)

            F3.head()

            F.head()

            F.rename({'POS': 'TOTAL POS'}, axis=1, inplace=True)
            F3.rename({'POS': 'TOTAL POS'}, axis=1, inplace=True)

            for i in range(0, len(F['TOTAL POS'])):
                F.loc[i, 'POS'] = F.loc[i, 'SB'] + F.loc[i, 'RB'] + F.loc[i, 'NM'] + F.loc[i, 'FORECLOSE'] + F.loc[
                    i, 'SETTLEMENT']
                F.loc[i, 'RB_POS'] = F.loc[i, 'RB'] + F.loc[i, 'NM'] + F.loc[i, 'SETTLEMENT'] + F.loc[i, 'FORECLOSE']
                F.loc[i, 'Performance'] = F.loc[i, 'POS'] / F.loc[i, 'TOTAL POS'] * 100
                F.loc[i, 'RB_Performance'] = F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL POS'] * 100
            for i in range(0, len(F3['TOTAL POS'])):
                F3.loc[i, 'POS'] = F3.loc[i, 'SB'] + F3.loc[i, 'RB'] + F3.loc[i, 'NM'] + F3.loc[i, 'FORECLOSE'] + \
                                   F3.loc[i, 'SETTLEMENT']
                F3.loc[i, 'RB_POS'] = F3.loc[i, 'RB'] + F3.loc[i, 'NM'] + F3.loc[i, 'SETTLEMENT'] + F3.loc[
                    i, 'FORECLOSE']
                F3.loc[i, 'Performance'] = F3.loc[i, 'POS'] / F3.loc[i, 'TOTAL POS'] * 100
                F3.loc[i, 'RB_Performance'] = F3.loc[i, 'RB_POS'] / F3.loc[i, 'TOTAL POS'] * 100

            F3 = F3[F3['BKT'] == 1]

            F.head()

            F3.head()

            F = F.reset_index(drop=True)
            F3 = F3.reset_index(drop=True)

            F.head()

            BKT3_MONEY_COLLECTION = pd.DataFrame(F.groupby(['TC NAME'])['MONEY COLLECTION'].sum()).reset_index()

            BKT3_MONEY_COLLECTION

            F3.head()

            for i in range(0, len(F['TC NAME'])):
                if F.loc[i, 'BKT'] == 1:
                    if F.loc[i, 'Performance'] < 80:
                        F.loc[i, 'PAYOUT'] = 0
                    elif F.loc[i, 'Performance'] >= 80 and F.loc[i, 'Performance'] < 85:
                        F.loc[i, 'PAYOUT'] = 2000
                    elif F.loc[i, 'Performance'] >= 85 and F.loc[i, 'Performance'] < 88:
                        F.loc[i, 'PAYOUT'] = 3000
                    elif F.loc[i, 'Performance'] >= 88 and F.loc[i, 'Performance'] < 90:
                        F.loc[i, 'PAYOUT'] = 4000
                    elif F.loc[i, 'Performance'] >= 90:
                        F.loc[i, 'PAYOUT'] = 5000
                # elif F.loc[i, 'BKT'] == 2:
                #     if F.loc[i, 'Performance'] < 70:
                #         F.loc[i, 'PAYOUT'] = 0
                #     elif F.loc[i, 'Performance'] >= 75 and F.loc[i, 'Performance'] < 80:
                #         F.loc[i, 'PAYOUT'] = 2000
                #     elif F.loc[i, 'Performance'] >= 80 and F.loc[i, 'Performance'] < 85:
                #         F.loc[i, 'PAYOUT'] = 4000
                #     elif F.loc[i, 'Performance'] >= 85 and F.loc[i, 'Performance'] < 90:
                #         F.loc[i, 'PAYOUT'] = 5000
                #     elif F.loc[i, 'Performance'] >= 90:
                #         F.loc[i, 'PAYOUT'] = 7000

            for i in range(0, len(F['TC NAME'])):
                if F.loc[i, 'BKT'] == 1:
                    # (F.loc[i, 'BKT'] == 2):
                    if F.loc[i, 'RB_Performance'] < 15:
                        F.loc[i, 'RB_PAYOUT'] = 0
                    elif F.loc[i, 'RB_Performance'] >= 15 and F.loc[i, 'RB_Performance'] < 20:
                        F.loc[i, 'RB_PAYOUT'] = 1500
                    elif F.loc[i, 'RB_Performance'] >= 20 and F.loc[i, 'RB_Performance'] < 25:
                        F.loc[i, 'RB_PAYOUT'] = 3000
                    elif F.loc[i, 'RB_Performance'] >= 25:
                        F.loc[i, 'RB_PAYOUT'] = 5000

            for i in range(0, len(F3['TL'])):
                if F3.loc[i, 'BKT'] == 1:
                    if F3.loc[i, 'Performance'] < 80:
                        F3.loc[i, 'PAYOUT'] = 0
                    elif F3.loc[i, 'Performance'] >= 80 and F3.loc[i, 'Performance'] < 85:
                        F3.loc[i, 'PAYOUT'] = 2000
                    elif F3.loc[i, 'Performance'] >= 85 and F3.loc[i, 'Performance'] < 88:
                        F3.loc[i, 'PAYOUT'] = 3000
                    elif F3.loc[i, 'Performance'] >= 88 and F3.loc[i, 'Performance'] < 90:
                        F3.loc[i, 'PAYOUT'] = 4000
                    elif F3.loc[i, 'Performance'] >= 90:
                        F3.loc[i, 'PAYOUT'] = 5000
                if F3.loc[i, 'BKT'] == 1:
                    if F3.loc[i, 'RB_Performance'] < 15:
                        F3.loc[i, 'RB_PAYOUT'] = 0
                    elif F3.loc[i, 'RB_Performance'] >= 15 and F3.loc[i, 'RB_Performance'] < 20:
                        F3.loc[i, 'RB_PAYOUT'] = 2000
                    elif F3.loc[i, 'RB_Performance'] >= 20 and F3.loc[i, 'RB_Performance'] < 25:
                        F3.loc[i, 'RB_PAYOUT'] = 4000
                    elif F3.loc[i, 'RB_Performance'] >= 25:
                        F3.loc[i, 'RB_PAYOUT'] = 6000

            for i in range(0, len(BKT3_MONEY_COLLECTION)):
                if BKT3_MONEY_COLLECTION.loc[i, 'TC NAME'] == 'VISHAL PAL':
                    if BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] < 300000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 0
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 300000 and BKT3_MONEY_COLLECTION.loc[
                        i, 'MONEY COLLECTION'] < 400000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 1000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 400000 and BKT3_MONEY_COLLECTION.loc[
                        i, 'MONEY COLLECTION'] < 500000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 2000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 500000 and BKT3_MONEY_COLLECTION.loc[
                        i, 'MONEY COLLECTION'] < 600000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 3000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 600000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 5000

            BKT3_MONEY_COLLECTION.head()

            F.head()

            F3.head()

            F3.rename({'TL': 'TC NAME'}, axis=1, inplace=True)

            F = pd.concat([F, F3])

            F

            BKT3_MONEY_COLLECTION

            F = pd.concat([F, BKT3_MONEY_COLLECTION])

            F.fillna(0, inplace=True)

            F

            A = pd.read_excel(E)

            F = F.merge(A, left_on='TC NAME', right_on='NAMES', how='left')

            F.columns

            F.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY', 'TYPE_OF_SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'DATE_OF_BIRTH'], axis=1, inplace=True)

            for i in range(0,len(F['Performance'])):
                F.loc[i,'Performance'] = round(F.loc[i,'Performance'], 2)
                F.loc[i,'TOTAL POS'] = round(F.loc[i,'TOTAL POS'], 2)
                F.loc[i,'SB'] = round(F.loc[i,'SB'], 2)
                F.loc[i,'NM'] = round(F.loc[i,'NM'], 2)
                F.loc[i,'RB'] = round(F.loc[i,'RB'], 2)
                F.loc[i,'FORECLOSE'] = round(F.loc[i,'FORECLOSE'], 2)
                F.loc[i,'MONEY COLLECTION'] = round(F.loc[i,'MONEY COLLECTION'], 2)
                F.loc[i,'POS'] = round(F.loc[i,'POS'], 2)
                F.loc[i,'RB_POS'] = round(F.loc[i,'RB_POS'], 2)
                F.loc[i,'RB_Performance'] = round(F.loc[i,'RB_Performance'], 2)
                F.loc[i, 'SETTLEMENT'] = round(F.loc[i, 'SETTLEMENT'], 2)

            li=[]
            for i in range(0,len(F['Performance'])):
                if (F.loc[i,'TC NAME']=='KARAN PAL') or (F.loc[i,'TC NAME']=='NO TC') or (F.loc[i,'TC NAME']=='ANKUR'):
                    li.append(i)

            F.drop(li,axis=0,inplace=True)

            F = F.reset_index(drop=True)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx',
                       index=False)

            F12 = F.copy()

            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
            AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            FINAL_COPY1 = pd.read_excel(AA)
            F = pd.read_excel(AA2)

            C = list(FINAL_COPY1.columns)  # FOS_Incentive
            C11 = list(F.columns)  # FOS_Fixed
            C123 = list(F12.columns)  # TC_Incentive

            for j in range(0, len(FINAL_COPY1[C[0]])):
                row_data = list()
                for col in range(0, len(C)):
                    row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
                excel_data.append(row_data)

            for j in range(0, len(F[C11[0]])):
                row_data1 = list()
                for col in range(0, len(C11)):
                    row_data1.append(str(F.loc[j, C11[col]]))
                excel_data1.append(row_data1)

            for j in range(0, len(F12[C123[0]])):
                row_data22 = list()
                for col1 in range(0, len(C123)):
                    row_data22.append(str(F12.loc[j, C123[col1]]))
                excel_data123.append(row_data22)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()
            return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel123': excel_data123, 'columns123': C123, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/MASTER FILE IDFC_TW.xlsx')):
            for i in range(31, 0, -1):
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')):
                    fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
                    AA122 = fs1.open('IDFC_TW PAID FILE ' + str(i) + ' OCT 21.xlsx')
                    PAID_FILE_IDFC_TW = pd.read_excel(AA122)
                else:
                    continue

            fs1 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')

            fs2 = FileSystemStorage(location='media/Employees')

            AA1 = fs1.open('MASTER FILE IDFC_TW.xlsx')

            E = fs2.open('Employee_Database.xlsx')

            A = pd.read_excel(AA1)

            A.head()

            FUNDING_LIST = list(PAID_FILE_IDFC_TW[PAID_FILE_IDFC_TW['FOS'] == 'FUNDING']['AGREEMENTID'])

            for i in range(0, len(A['AGREEMENTID'])):

                for j in range(0, len(FUNDING_LIST)):

                    if A.loc[i, 'AGREEMENTID'] == FUNDING_LIST[j]:
                        A.loc[i, 'STATUS'] = 'FLOW'

            F1 = pd.DataFrame(A.groupby(['TC NAME', 'BKT'])['POS'].sum()).reset_index()

            F2 = pd.DataFrame(A.groupby(['TL', 'BKT'])['POS'].sum()).reset_index()

            F1.head()

            F2.head()

            F = F1.copy()

            F3 = F2.copy()

            R1 = pd.DataFrame(A.groupby(['TC NAME', 'BKT', 'STATUS'])['POS'].sum()).reset_index()

            R2 = pd.DataFrame(A.groupby(['TL', 'BKT', 'STATUS'])['POS'].sum()).reset_index()

            R1.head()

            R2.head()

            P = F.copy()

            P2 = F3.copy()

            P.head()

            P2

            P = P.iloc[:, :2]

            P2 = P2.iloc[:, :2]

            P['SB'] = np.nan

            P['RB'] = np.nan

            P['NM'] = np.nan

            P['FORECLOSE'] = np.nan

            P['SETTLEMENT'] = np.nan

            P['MONEY COLLECTION'] = np.nan

            P2['SB'] = np.nan

            P2['RB'] = np.nan

            P2['NM'] = np.nan

            P2['FORECLOSE'] = np.nan

            P2['SETTLEMENT'] = np.nan

            COL = list(P.columns)

            COL1 = list(P2.columns)

            for i in range(0, len(R1['TC NAME'])):

                for j in range(0, len(P['TC NAME'])):

                    for k in range(0, len(COL)):

                        if ((R1.loc[i, ['TC NAME', 'BKT']] == P.loc[j, ['TC NAME', 'BKT']]).all()) and R1.loc[i, 'STATUS'] == COL[k]:
                            P.loc[j, COL[k]] = R1.loc[i, 'POS']

            for i in range(0, len(R2['TL'])):
                for j in range(0, len(P2['TL'])):
                    for k in range(0, len(COL1)):
                        if ((R2.loc[i, ['TL', 'BKT']] == P2.loc[j, ['TL', 'BKT']]).all()) and R2.loc[i, 'STATUS'] == COL1[k]:
                            P2.loc[j, COL1[k]] = R2.loc[i, 'POS']

            R5 = pd.DataFrame(A.groupby(['TC NAME', 'BKT'])['Billing PAID AMT.'].sum()).reset_index()

            R5.head()

            R5.rename({'Billing PAID AMT.': 'MONEY COLLECTION'}, axis=1, inplace=True)

            R5

            P.head()

            COL

            for i in range(0, len(R5['TC NAME'])):

                for j in range(0, len(P['TC NAME'])):

                    for k in range(0, len(COL)):

                        if ((R5.loc[i, ['TC NAME', 'BKT']] == P.loc[j, ['TC NAME', 'BKT']]).all()):
                            P.loc[j, 'MONEY COLLECTION'] = R5.loc[i, 'MONEY COLLECTION']

            F.head()

            F3.head()

            P

            F = F.merge(P, how='outer')

            F3 = F3.merge(P2, how='outer')

            F.fillna(0, inplace=True)

            F3.fillna(0, inplace=True)

            F3.head()

            F.head()

            F.rename({'POS': 'TOTAL POS'}, axis=1, inplace=True)

            F3.rename({'POS': 'TOTAL POS'}, axis=1, inplace=True)

            for i in range(0, len(F['TOTAL POS'])):
                F.loc[i, 'POS'] = F.loc[i, 'SB'] + F.loc[i, 'RB'] + F.loc[i, 'NM'] + F.loc[i, 'FORECLOSE'] + F.loc[

                    i, 'SETTLEMENT']

                F.loc[i, 'RB_POS'] = F.loc[i, 'RB'] + F.loc[i, 'NM'] + F.loc[i, 'SETTLEMENT'] + F.loc[
                    i, 'FORECLOSE']

                F.loc[i, 'Performance'] = F.loc[i, 'POS'] / F.loc[i, 'TOTAL POS'] * 100

                F.loc[i, 'RB_Performance'] = F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL POS'] * 100

            for i in range(0, len(F3['TOTAL POS'])):
                F3.loc[i, 'POS'] = F3.loc[i, 'SB'] + F3.loc[i, 'RB'] + F3.loc[i, 'NM'] + F3.loc[i, 'FORECLOSE'] + F3.loc[i, 'SETTLEMENT']

            F3.loc[i, 'RB_POS'] = F3.loc[i, 'RB'] + F3.loc[i, 'NM'] + F3.loc[i, 'SETTLEMENT'] + F3.loc[i, 'FORECLOSE']

            F3.loc[i, 'Performance'] = F3.loc[i, 'POS'] / F3.loc[i, 'TOTAL POS'] * 100

            F3.loc[i, 'RB_Performance'] = F3.loc[i, 'RB_POS'] / F3.loc[i, 'TOTAL POS'] * 100

            F3 = F3[F3['BKT'] == 1]

            F.head()

            F3.head()

            F['Performance'] = round(F['Performance'], 2)

            F['RB_Performance'] = round(F['RB_Performance'], 2)

            F3['Performance'] = round(F3['Performance'], 2)

            F3['RB_Performance'] = round(F3['RB_Performance'], 2)

            F = F.reset_index(drop=True)

            F3 = F3.reset_index(drop=True)

            F.head()

            BKT3_MONEY_COLLECTION = pd.DataFrame(F.groupby(['TC NAME'])['MONEY COLLECTION'].sum()).reset_index()

            BKT3_MONEY_COLLECTION

            F3.head()

            for i in range(0, len(F['TC NAME'])):
                if F.loc[i, 'BKT'] == 1:
                    if F.loc[i, 'Performance'] < 80:
                        F.loc[i, 'PAYOUT'] = 0
                    elif F.loc[i, 'Performance'] >= 80 and F.loc[i, 'Performance'] < 85:
                        F.loc[i, 'PAYOUT'] = 2000
                    elif F.loc[i, 'Performance'] >= 85 and F.loc[i, 'Performance'] < 88:
                        F.loc[i, 'PAYOUT'] = 3000
                    elif F.loc[i, 'Performance'] >= 88 and F.loc[i, 'Performance'] < 90:
                        F.loc[i, 'PAYOUT'] = 4000
                    elif F.loc[i, 'Performance'] >= 90:
                        F.loc[i, 'PAYOUT'] = 5000
                # elif F.loc[i, 'BKT'] == 2:
                #     if F.loc[i, 'Performance'] < 70:
                #         F.loc[i, 'PAYOUT'] = 0
                #     elif F.loc[i, 'Performance'] >= 75 and F.loc[i, 'Performance'] < 80:
                #         F.loc[i, 'PAYOUT'] = 2000
                #     elif F.loc[i, 'Performance'] >= 80 and F.loc[i, 'Performance'] < 85:
                #         F.loc[i, 'PAYOUT'] = 4000
                #     elif F.loc[i, 'Performance'] >= 85 and F.loc[i, 'Performance'] < 90:
                #         F.loc[i, 'PAYOUT'] = 5000
                #     elif F.loc[i, 'Performance'] >= 90:
                #         F.loc[i, 'PAYOUT'] = 7000
            for i in range(0, len(F['TC NAME'])):
                if F.loc[i, 'BKT'] == 1:
                    # (F.loc[i, 'BKT'] == 2):
                    if F.loc[i, 'RB_Performance'] < 15:
                        F.loc[i, 'RB_PAYOUT'] = 0
                    elif F.loc[i, 'RB_Performance'] >= 15 and F.loc[i, 'RB_Performance'] < 20:
                        F.loc[i, 'RB_PAYOUT'] = 1500
                    elif F.loc[i, 'RB_Performance'] >= 20 and F.loc[i, 'RB_Performance'] < 25:
                        F.loc[i, 'RB_PAYOUT'] = 3000
                    elif F.loc[i, 'RB_Performance'] >= 25:
                        F.loc[i, 'RB_PAYOUT'] = 5000
            for i in range(0, len(F3['TL'])):
                if F3.loc[i, 'BKT'] == 1:
                    if F3.loc[i, 'Performance'] < 80:
                        F3.loc[i, 'PAYOUT'] = 0
                    elif F3.loc[i, 'Performance'] >= 80 and F3.loc[i, 'Performance'] < 85:
                        F3.loc[i, 'PAYOUT'] = 2000
                    elif F3.loc[i, 'Performance'] >= 85 and F3.loc[i, 'Performance'] < 88:
                        F3.loc[i, 'PAYOUT'] = 3000
                    elif F3.loc[i, 'Performance'] >= 88 and F3.loc[i, 'Performance'] < 90:
                        F3.loc[i, 'PAYOUT'] = 4000
                    elif F3.loc[i, 'Performance'] >= 90:
                        F3.loc[i, 'PAYOUT'] = 5000
                if F3.loc[i, 'BKT'] == 1:
                    if F3.loc[i, 'RB_Performance'] < 15:
                        F3.loc[i, 'RB_PAYOUT'] = 0
                    elif F3.loc[i, 'RB_Performance'] >= 15 and F3.loc[i, 'RB_Performance'] < 20:
                        F3.loc[i, 'RB_PAYOUT'] = 2000
                    elif F3.loc[i, 'RB_Performance'] >= 20 and F3.loc[i, 'RB_Performance'] < 25:
                        F3.loc[i, 'RB_PAYOUT'] = 4000
                    elif F3.loc[i, 'RB_Performance'] >= 25:
                        F3.loc[i, 'RB_PAYOUT'] = 6000

            for i in range(0, len(BKT3_MONEY_COLLECTION)):
                if BKT3_MONEY_COLLECTION.loc[i, 'TC NAME'] == 'VISHAL PAL':
                    if BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] < 300000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 0
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 300000 and BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] < 400000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 1000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 400000 and BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] < 500000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 2000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 500000 and BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] < 600000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 3000
                    elif BKT3_MONEY_COLLECTION.loc[i, 'MONEY COLLECTION'] >= 600000:
                        BKT3_MONEY_COLLECTION.loc[i, 'PAYOUT'] = 5000

            BKT3_MONEY_COLLECTION.head()

            F.head()

            F3.head()

            F3.rename({'TL': 'TC NAME'}, axis=1, inplace=True)

            F = pd.concat([F, F3])

            F

            BKT3_MONEY_COLLECTION

            F = pd.concat([F, BKT3_MONEY_COLLECTION])

            F.fillna(0, inplace=True)

            F

            A = pd.read_excel(E)

            F = F.merge(A, left_on='TC NAME', right_on='NAMES', how='left')

            F.columns

            F.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY', 'TYPE_OF_SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'DATE_OF_BIRTH'], axis=1, inplace=True)

            for i in range(0, len(F['Performance'])):
                F.loc[i, 'Performance'] = round(F.loc[i, 'Performance'], 2)
                F.loc[i, 'TOTAL POS'] = round(F.loc[i, 'TOTAL POS'], 2)
                F.loc[i, 'SB'] = round(F.loc[i, 'SB'], 2)
                F.loc[i, 'NM'] = round(F.loc[i, 'NM'], 2)
                F.loc[i, 'RB'] = round(F.loc[i, 'RB'], 2)
                F.loc[i, 'FORECLOSE'] = round(F.loc[i, 'FORECLOSE'], 2)
                F.loc[i, 'MONEY COLLECTION'] = round(F.loc[i, 'MONEY COLLECTION'], 2)
                F.loc[i, 'POS'] = round(F.loc[i, 'POS'], 2)
                F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'], 2)
                F.loc[i, 'RB_Performance'] = round(F.loc[i, 'RB_Performance'], 2)
                F.loc[i, 'SETTLEMENT'] = round(F.loc[i, 'SETTLEMENT'], 2)

            li = []
            for i in range(0, len(F['Performance'])):
                if (F.loc[i, 'TC NAME'] == 'KARAN PAL') or (F.loc[i, 'TC NAME'] == 'NO TC') or (F.loc[i, 'TC NAME'] == 'ANKUR'):
                    li.append(i)

            F.drop(li, axis=0, inplace=True)

            F = F.reset_index(drop=True)

            F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx', index=False)

            F12 = F.copy()


    elif request.method != 'POST':
        if (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'))):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
            AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            FINAL_COPY1 = pd.read_excel(AA)
            F = pd.read_excel(AA2)
            fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA123 = fs123.open('IDFC_TW TC Incentive.xlsx')
            F12 = pd.read_excel(AA123)

        elif os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            AA = fs.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
            AA2 = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            FINAL_COPY1 = pd.read_excel(AA)
            F = pd.read_excel(AA2)
            C = list(FINAL_COPY1.columns)  # FOS_Incentive
            C11 = list(F.columns)  # FOS_Fixed
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            for j in range(0, len(FINAL_COPY1[C[0]])):
                row_data = list()
                for col in range(0, len(C)):
                    row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
                excel_data.append(row_data)

            for j in range(0, len(F[C11[0]])):
                row_data1 = list()
                for col in range(0, len(C11)):
                    row_data1.append(str(F.loc[j, C11[col]]))
                excel_data1.append(row_data1)

            return render(request, 'FirstLevel/salary.html',
                          {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'Designation': Designation})

        else:
            return HttpResponseRedirect(reverse('basic_app:IDFC_TW_MIS'))

    C123 = list(F12.columns)  # TC_Incentive

    for j in range(0, len(F12[C123[0]])):
        row_data22 = list()
        for col1 in range(0, len(C123)):
            row_data22.append(str(F12.loc[j, C123[col1]]))
        excel_data123.append(row_data22)

    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/salary.html', {'excel123': excel_data123, 'columns123': C123, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

# def L_T_TW_SALARY_TC(request):
#     excel_data = []
#     excel_data1 = []
#     excel_data123 = []
#     excel_data12334 = []
#     F12 = pd.DataFrame()
#     a = 0
#
#     if request.method == 'POST':
#         if (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx')) and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')):
#
#             for i in range(31, 0, -1):
#                 if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/L_T PAID FILE ' + str(i) + ' AUG 21.xlsx'):
#                     fs1 = FileSystemStorage(location='media/L_T/MIS')
#                     AA122 = fs1.open('L_T PAID FILE ' + str(i) + ' AUG 21.xlsx')
#                     PAID_FILE_L_T = pd.read_excel(AA122)
#                 else:
#                     continue
#
#             fs1 = FileSystemStorage(location='media/L_T/TC Incentive')
#             fs2 = FileSystemStorage(location='media/Employees')
#             AA1 = fs1.open('MASTER FILE L_T.xlsx')
#             E = fs2.open('Employee_Database.xlsx')
#
#             A = pd.read_excel(AA1)
#             EE1 = pd.read_excel(E)
#
#             A.head()
#
#             FUNDING_LIST=list(PAID_FILE_L_T[PAID_FILE_L_T['FOS']=='FUNDING']['AGREEMENTID'])
#
#             for i in range(0,len(A['AGREEMENTID'])):
#                 for j in range(0,len(FUNDING_LIST)):
#                     if A.loc[i,'AGREEMENTID']==FUNDING_LIST[j]:
#                         A.loc[i,'STATUS']='FLOW'
#
#             M = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['POS'].sum()).reset_index()
#
#             M
#
#             M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)
#
#             R = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['AGREEMENTID'].count()).reset_index()
#
#             F = M.merge(R, how='outer')
#
#             F.head()
#
#             F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)
#
#             R1 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME', 'STATUS'])['AGREEMENTID'].count()).reset_index()
#
#             R1.head()
#
#             P = F.copy()
#
#             P = P.iloc[:, :3]
#
#             P.head()
#
#             P['FLOW'] = np.nan
#             P['SB'] = np.nan
#             P['RB'] = np.nan
#             P['NM'] = np.nan
#             P['PART PAID'] = np.nan
#             P['FORECLOSE'] = np.nan
#             P['SETTLEMENT'] = np.nan
#
#             P.head()
#
#             R1.head()
#
#             COL = P.columns
#
#             for i in range(0, len(R1['COMPANY'])):
#                 for j in range(0, len(P['COMPANY'])):
#                     for k in range(0, len(COL)):
#                         if (
#                         (R1.loc[i, ['COMPANY', 'BKT', 'TC NAME']] == P.loc[j, ['COMPANY', 'BKT', 'TC NAME']]).all()) and \
#                                 R1.loc[i, 'STATUS'] == COL[k]:
#                             P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']
#
#             P
#
#             F = F.merge(P, how='outer')
#
#             F.head()
#
#             F.fillna(0, inplace=True)
#
#             F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
#                       'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES'}, axis=1,
#                      inplace=True)
#
#             R2 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME', 'STATUS'])['POS'].sum()).reset_index()
#
#             for i in range(0, len(R2['COMPANY'])):
#                 for j in range(0, len(P['COMPANY'])):
#                     for k in range(0, len(COL)):
#                         if (
#                         (R2.loc[i, ['COMPANY', 'BKT', 'TC NAME']] == P.loc[j, ['COMPANY', 'BKT', 'TC NAME']]).all()) and \
#                                 R2.loc[i, 'STATUS'] == COL[k]:
#                             P.loc[j, COL[k]] = R2.loc[i, 'POS']
#
#             F = F.merge(P, how='outer')
#
#             F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
#                       'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS'}, axis=1, inplace=True)
#
#             F.fillna(0, inplace=True)
#
#             for i in range(0, len(F['FLOW_CASES'])):
#                 F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#
#             TP = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['TOTAL PAID'].sum()).reset_index()
#
#             F = F.merge(TP, how='outer')
#
#             for i in range(0, len(F['SB_POS'])):
#                 F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + \
#                                           F.loc[i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#
#             F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
#                       'SETTLEMENT_CASES': 'SC_CASES',
#                       'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
#                       'FORECLOSE_POS%': 'FC_POS%',
#                       'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
#                      inplace=True)
#
#             F
#
#             for i in range(0, len(F['COMPANY'])):
#                 if F.loc[i, 'POS_RES%'] < 60:
#                     F.loc[i, 'INCENTIVE'] = 0
#                 elif (F.loc[i, 'POS_RES%'] >= 60) and (F.loc[i, 'POS_RES%'] < 65):
#                     F.loc[i, 'INCENTIVE'] = 1000
#                 elif (F.loc[i, 'POS_RES%'] >= 65) and (F.loc[i, 'POS_RES%'] < 70):
#                     F.loc[i, 'INCENTIVE'] = 1500
#                 elif (F.loc[i, 'POS_RES%'] >= 70) and (F.loc[i, 'POS_RES%'] < 75):
#                     F.loc[i, 'INCENTIVE'] = 2000
#                 elif F.loc[i, 'POS_RES%'] >= 75:
#                     F.loc[i, 'INCENTIVE'] = 4000
#
#             F.head()
#
#             for i in range(0,len(F['COMPANY'])):
#                 F.loc[i,'TOTAL_POS'] = round(F.loc[i,'TOTAL_POS'],2)
#                 F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
#                 F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
#                 F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'], 2)
#                 F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'], 2)
#                 F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
#                 F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
#                 F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
#
#             F = F.merge(EE1, left_on='TC NAME', right_on='NAMES', how='left')
#
#             F.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY',
#                              'TYPE_OF_SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'DATE_OF_BIRTH'], axis=1,
#                             inplace=True)
#
#             F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx', index=False)
#
#             F12 = F.copy()
#
#             fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
#             AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
#             AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
#             FINAL_COPY1 = pd.read_excel(AA)
#             F = pd.read_excel(AA2)
#
#             C = list(FINAL_COPY1.columns)  # FOS_Incentive
#             C11 = list(F.columns)  # FOS_Fixed
#             C12334 = list(F12.columns)  # TC_Incentive
#
#             for j in range(0, len(FINAL_COPY1[C[0]])):
#                 row_data = list()
#                 for col in range(0, len(C)):
#                     row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
#                 excel_data.append(row_data)
#
#             for j in range(0, len(F[C11[0]])):
#                 row_data1 = list()
#                 for col in range(0, len(C11)):
#                     row_data1.append(str(F.loc[j, C11[col]]))
#                 excel_data1.append(row_data1)
#
#             for j in range(0, len(F12[C12334[0]])):
#                 row_data22 = list()
#                 for col1 in range(0, len(C12334)):
#                     row_data22.append(str(F12.loc[j, C12334[col1]]))
#                 excel_data12334.append(row_data22)
#
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#             return render(request, 'FirstLevel/salary.html', {'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'excel12334': excel_data12334, 'columns12334': C12334, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
#
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/MASTER FILE L_T.xlsx'):
#             for i in range(31, 0, -1):
#                 if os.path.exists('/Users/mohaksehgal/Website_Deployment/media/L_T/MIS/L_T PAID FILE ' + str(i) + ' AUG 21.xlsx'):
#                     fs1 = FileSystemStorage(location='media/L_T/MIS')
#                     AA122 = fs1.open('L_T PAID FILE ' + str(i) + ' AUG 21.xlsx')
#                     PAID_FILE_L_T = pd.read_excel(AA122)
#                 else:
#                     continue
#
#             fs1 = FileSystemStorage(location='media/L_T/TC Incentive')
#             fs2 = FileSystemStorage(location='media/Employees')
#             AA1 = fs1.open('MASTER FILE L_T.xlsx')
#             E = fs2.open('Employee_Database.xlsx')
#
#             A = pd.read_excel(AA1)
#             EE1 = pd.read_excel(E)
#
#             A.head()
#
#             FUNDING_LIST = list(PAID_FILE_L_T[PAID_FILE_L_T['FOS'] == 'FUNDING']['AGREEMENTID'])
#
#             for i in range(0, len(A['AGREEMENTID'])):
#                 for j in range(0, len(FUNDING_LIST)):
#                     if A.loc[i, 'AGREEMENTID'] == FUNDING_LIST[j]:
#                         A.loc[i, 'STATUS'] = 'FLOW'
#
#             M = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['POS'].sum()).reset_index()
#
#             M
#
#             M.rename({'POS': 'TOTAL_POS'}, axis=1, inplace=True)
#
#             R = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['AGREEMENTID'].count()).reset_index()
#
#             F = M.merge(R, how='outer')
#
#             F.head()
#
#             F.rename({'AGREEMENTID': 'TOTAL_CASES'}, axis=1, inplace=True)
#
#             R1 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME', 'STATUS'])['AGREEMENTID'].count()).reset_index()
#
#             R1.head()
#
#             P = F.copy()
#
#             P = P.iloc[:, :3]
#
#             P.head()
#
#             P['FLOW'] = np.nan
#             P['SB'] = np.nan
#             P['RB'] = np.nan
#             P['NM'] = np.nan
#             P['PART PAID'] = np.nan
#             P['FORECLOSE'] = np.nan
#             P['SETTLEMENT'] = np.nan
#
#             P.head()
#
#             R1.head()
#
#             COL = P.columns
#
#             for i in range(0, len(R1['COMPANY'])):
#                 for j in range(0, len(P['COMPANY'])):
#                     for k in range(0, len(COL)):
#                         if (
#                                 (R1.loc[i, ['COMPANY', 'BKT', 'TC NAME']] == P.loc[
#                                     j, ['COMPANY', 'BKT', 'TC NAME']]).all()) and \
#                                 R1.loc[i, 'STATUS'] == COL[k]:
#                             P.loc[j, COL[k]] = R1.loc[i, 'AGREEMENTID']
#
#             P
#
#             F = F.merge(P, how='outer')
#
#             F.head()
#
#             F.fillna(0, inplace=True)
#
#             F.rename({'FLOW': 'FLOW_CASES', 'SB': 'SB_CASES', 'RB': 'RB_CASES', 'FORECLOSE': 'FORECLOSE_CASES',
#                       'SETTLEMENT': 'SETTLEMENT_CASES', 'NM': 'NM_CASES', 'PART PAID': 'PART_PAID_CASES'}, axis=1,
#                      inplace=True)
#
#             R2 = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME', 'STATUS'])['POS'].sum()).reset_index()
#
#             for i in range(0, len(R2['COMPANY'])):
#                 for j in range(0, len(P['COMPANY'])):
#                     for k in range(0, len(COL)):
#                         if (
#                                 (R2.loc[i, ['COMPANY', 'BKT', 'TC NAME']] == P.loc[
#                                     j, ['COMPANY', 'BKT', 'TC NAME']]).all()) and \
#                                 R2.loc[i, 'STATUS'] == COL[k]:
#                             P.loc[j, COL[k]] = R2.loc[i, 'POS']
#
#             F = F.merge(P, how='outer')
#
#             F.rename({'FLOW': 'FLOW_POS', 'SB': 'SB_POS', 'RB': 'RB_POS', 'FORECLOSE': 'FORECLOSE_POS', 'NM': 'NM_POS',
#                       'SETTLEMENT': 'SETTLEMENT_POS', 'PART PAID': 'PART_PAID_POS'}, axis=1, inplace=True)
#
#             F.fillna(0, inplace=True)
#
#             for i in range(0, len(F['FLOW_CASES'])):
#                 F.loc[i, 'FLOW_POS%'] = round((F.loc[i, 'FLOW_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'SB_POS%'] = round((F.loc[i, 'SB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'RB_POS%'] = round((F.loc[i, 'RB_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'FORECLOSE_POS%'] = round((F.loc[i, 'FORECLOSE_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'SETTLEMENT_POS%'] = round((F.loc[i, 'SETTLEMENT_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'NM_POS%'] = round((F.loc[i, 'NM_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#                 F.loc[i, 'PART_PAID_POS%'] = round((F.loc[i, 'PART_PAID_POS'] / F.loc[i, 'TOTAL_POS']) * 100, 2)
#
#             TP = pd.DataFrame(A.groupby(['COMPANY', 'BKT', 'TC NAME'])['TOTAL PAID'].sum()).reset_index()
#
#             F = F.merge(TP, how='outer')
#
#             for i in range(0, len(F['SB_POS'])):
#                 F.loc[i, 'PERFORMANCE'] = F.loc[i, 'SB_POS%'] + F.loc[i, 'RB_POS%'] + F.loc[i, 'FORECLOSE_POS%'] + \
#                                           F.loc[i, 'NM_POS%'] + F.loc[i, 'SETTLEMENT_POS%']
#
#             F.rename({'TOTAL_CASES': 'COUNT', 'PART_PAID_CASES': 'PP_CASES', 'FORECLOSE_CASES': 'FC_CASES',
#                       'SETTLEMENT_CASES': 'SC_CASES',
#                       'PART_PAID_POS': 'PP_POS', 'FORECLOSE_POS': 'FC_POS', 'SETTLEMENT_POS': 'SC_POS',
#                       'FORECLOSE_POS%': 'FC_POS%',
#                       'SETTLEMENT_POS%': 'SC_POS%', 'PART_PAID_POS%': 'PP_POS%', 'PERFORMANCE': 'POS_RES%'}, axis=1,
#                      inplace=True)
#
#             F
#
#             for i in range(0, len(F['COMPANY'])):
#                 if F.loc[i, 'POS_RES%'] < 60:
#                     F.loc[i, 'INCENTIVE'] = 0
#                 elif (F.loc[i, 'POS_RES%'] >= 60) and (F.loc[i, 'POS_RES%'] < 65):
#                     F.loc[i, 'INCENTIVE'] = 1000
#                 elif (F.loc[i, 'POS_RES%'] >= 65) and (F.loc[i, 'POS_RES%'] < 70):
#                     F.loc[i, 'INCENTIVE'] = 1500
#                 elif (F.loc[i, 'POS_RES%'] >= 70) and (F.loc[i, 'POS_RES%'] < 75):
#                     F.loc[i, 'INCENTIVE'] = 2000
#                 elif F.loc[i, 'POS_RES%'] >= 75:
#                     F.loc[i, 'INCENTIVE'] = 4000
#
#             F.head()
#
#             for i in range(0,len(F['COMPANY'])):
#                 F.loc[i,'TOTAL_POS'] = round(F.loc[i,'TOTAL_POS'],2)
#                 F.loc[i, 'FLOW_POS'] = round(F.loc[i, 'FLOW_POS'], 2)
#                 F.loc[i, 'SB_POS'] = round(F.loc[i, 'SB_POS'], 2)
#                 F.loc[i, 'RB_POS'] = round(F.loc[i, 'RB_POS'], 2)
#                 F.loc[i, 'NM_POS'] = round(F.loc[i, 'NM_POS'], 2)
#                 F.loc[i, 'PP_POS'] = round(F.loc[i, 'PP_POS'], 2)
#                 F.loc[i, 'FC_POS'] = round(F.loc[i, 'FC_POS'], 2)
#                 F.loc[i, 'SC_POS'] = round(F.loc[i, 'SC_POS'], 2)
#
#             F = F.merge(EE1, left_on='TC NAME', right_on='NAMES', how='left')
#
#             F.drop(['DEPARTMENT_ID', 'END_DATE', 'HIRE_DATE', 'PHONE_NUMBER', 'LOCATION_ID', 'SALARY',
#                     'TYPE_OF_SALARY', 'MANAGEMENT_LEVEL', 'NAMES', 'DATE_OF_BIRTH'], axis=1,
#                    inplace=True)
#
#             F.to_excel(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx',
#                        index=False)
#
#             F12 = F.copy()
#
#
#     elif request.method != 'POST':
#         if (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx')) and (os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/L_T/TC Incentive/TC Performance L_T.xlsx')):
#             fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
#             AA = fs.open('PER PAID CASE(PIVOT) L&T.xlsx')
#             AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
#             FINAL_COPY1 = pd.read_excel(AA)
#             F = pd.read_excel(AA2)
#             fs123 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
#             AA123 = fs123.open('TC Performance L_T.xlsx')
#             F12 = pd.read_excel(AA123)
#
#         elif os.path.exists(r'/Users/mohaksehgal/Website_Deployment/media/COMBINED SALARY OF L_T AND IDFC TW/Per PAID CASE.xlsx'):
#             fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
#             AA = fs.open('PER PAID CASE(PIVOT L&T.xlsx')
#             AA2 = fs.open('PER PAID CASE(Including Fixed Salary) L&T.xlsx')
#             FINAL_COPY1 = pd.read_excel(AA)
#             F = pd.read_excel(AA2)
#             C = list(FINAL_COPY1.columns)  # FOS_Incentive
#             C11 = list(F.columns)  # FOS_Fixed
#             final_dep = DEP()
#             final_process = COMPANY_PROCESS()
#             Designation = Employee_Designation()
#
#             for j in range(0, len(FINAL_COPY1[C[0]])):
#                 row_data = list()
#                 for col in range(0, len(C)):
#                     row_data.append(str(FINAL_COPY1.loc[j, C[col]]))
#                 excel_data.append(row_data)
#
#             for j in range(0, len(F[C11[0]])):
#                 row_data1 = list()
#                 for col in range(0, len(C11)):
#                     row_data1.append(str(F.loc[j, C11[col]]))
#                 excel_data1.append(row_data1)
#
#             return render(request, 'FirstLevel/salary.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'excel': excel_data, 'excel2': excel_data1, 'columns': C, 'columns2': C11, 'Designation': Designation})
#
#         else:
#             return HttpResponseRedirect(reverse('basic_app:L_T_MIS'))
#
#
#     C12334 = list(F12.columns)  # TC_Incentive
#
#     for j in range(0, len(F12[C12334[0]])):
#         row_data22 = list()
#         for col1 in range(0, len(C12334)):
#             row_data22.append(str(F12.loc[j, C12334[col1]]))
#         excel_data12334.append(row_data22)
#
#     final_dep = DEP()
#     final_process = COMPANY_PROCESS()
#     Designation = Employee_Designation()
#
#     return render(request, 'FirstLevel/salary.html', {'excel12334': excel_data12334, 'columns12334': C12334, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_TW_TL_ANALYSIS(request):
    excel_data = []
    excel_data1 = []
    excel_data2 = []
    AA = pd.DataFrame()
    AA1 = pd.DataFrame()
    AA2 = pd.DataFrame()
    a = 0

    if request.method != 'POST':
        if (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx'))):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            AA = pd.read_excel(AA)
            AA1 = pd.read_excel(AA1)
            AA2 = pd.read_excel(AA2)

            AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            C = list(AA.columns)
            C1 = list(AA1.columns)
            C2 = list(AA2.columns)

            for j in range(0, len(AA[C[0]])):
                row_data = list()
                for col1 in range(0, len(C)):
                    row_data.append(str(AA.loc[j, C[col1]]))
                excel_data.append(row_data)

            for j in range(0, len(AA1[C1[0]])):
                row_data1 = list()
                for col1 in range(0, len(C1)):
                    row_data1.append(str(AA1.loc[j, C1[col1]]))
                excel_data1.append(row_data1)

            for j in range(0, len(AA2[C2[0]])):
                row_data2 = list()
                for col1 in range(0, len(C2)):
                    row_data2.append(str(AA2.loc[j, C2[col1]]))
                excel_data2.append(row_data2)

        elif (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'))):
            # fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            # AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            AA = pd.read_excel(AA)
            AA1 = pd.read_excel(AA1)
            AA2 = pd.read_excel(AA2)

            # AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            # C = list(AA.columns)
            C1 = list(AA1.columns)
            C2 = list(AA2.columns)

            # for j in range(0, len(AA[C[0]])):
            #     row_data = list()
            #     for col1 in range(0, len(C)):
            #         row_data.append(str(AA.loc[j, C[col1]]))
            #     excel_data.append(row_data)

            for j in range(0, len(AA1[C1[0]])):
                row_data1 = list()
                for col1 in range(0, len(C1)):
                    row_data1.append(str(AA1.loc[j, C1[col1]]))
                excel_data1.append(row_data1)

            for j in range(0, len(AA2[C2[0]])):
                row_data2 = list()
                for col1 in range(0, len(C2)):
                    row_data2.append(str(AA2.loc[j, C2[col1]]))
                excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'excel1': excel_data1, 'columns1': C1, 'excel2': excel_data2, 'columns2': C2, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel': excel_data, 'columns': C

        elif (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx'))):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            # fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            # AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            AA = pd.read_excel(AA)
            AA1 = pd.read_excel(AA1)
            # AA2 = pd.read_excel(AA2)

            AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            # AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            C = list(AA.columns)
            C1 = list(AA1.columns)
            # C2 = list(AA2.columns)

            for j in range(0, len(AA[C[0]])):
                row_data = list()
                for col1 in range(0, len(C)):
                    row_data.append(str(AA.loc[j, C[col1]]))
                excel_data.append(row_data)

            for j in range(0, len(AA1[C1[0]])):
                row_data1 = list()
                for col1 in range(0, len(C1)):
                    row_data1.append(str(AA1.loc[j, C1[col1]]))
                excel_data1.append(row_data1)

            # for j in range(0, len(AA2[C2[0]])):
            #     row_data2 = list()
            #     for col1 in range(0, len(C2)):
            #         row_data2.append(str(AA2.loc[j, C2[col1]]))
            #     excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'excel': excel_data, 'columns': C, 'excel1': excel_data1, 'columns1': C1, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel2': excel_data2, 'columns2': C2

        elif (os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx'))) and (os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx'))):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            # fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            # AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            AA = pd.read_excel(AA)
            # AA1 = pd.read_excel(AA1)
            AA2 = pd.read_excel(AA2)

            AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            C = list(AA.columns)
            # C1 = list(AA1.columns)
            C2 = list(AA2.columns)

            for j in range(0, len(AA[C[0]])):
                row_data = list()
                for col1 in range(0, len(C)):
                    row_data.append(str(AA.loc[j, C[col1]]))
                excel_data.append(row_data)

            # for j in range(0, len(AA1[C1[0]])):
            #     row_data1 = list()
            #     for col1 in range(0, len(C1)):
            #         row_data1.append(str(AA1.loc[j, C1[col1]]))
            #     excel_data1.append(row_data1)

            for j in range(0, len(AA2[C2[0]])):
                row_data2 = list()
                for col1 in range(0, len(C2)):
                    row_data2.append(str(AA2.loc[j, C2[col1]]))
                excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'excel': excel_data, 'columns': C, 'excel2': excel_data2, 'columns2': C2, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel1': excel_data1, 'columns1': C1

        elif os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')):
            fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            # fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            # fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            # AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            # AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            AA = pd.read_excel(AA)
            # AA1 = pd.read_excel(AA1)
            # AA2 = pd.read_excel(AA2)

            AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            # AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            C = list(AA.columns)
            # C1 = list(AA1.columns)
            # C2 = list(AA2.columns)

            for j in range(0, len(AA[C[0]])):
                row_data = list()
                for col1 in range(0, len(C)):
                    row_data.append(str(AA.loc[j, C[col1]]))
                excel_data.append(row_data)

            # for j in range(0, len(AA1[C1[0]])):
            #     row_data1 = list()
            #     for col1 in range(0, len(C1)):
            #         row_data1.append(str(AA1.loc[j, C1[col1]]))
            #     excel_data1.append(row_data1)
            #
            # for j in range(0, len(AA2[C2[0]])):
            #     row_data2 = list()
            #     for col1 in range(0, len(C2)):
            #         row_data2.append(str(AA2.loc[j, C2[col1]]))
            #     excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html', {'excel': excel_data, 'columns': C, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel1': excel_data1, 'columns1': C1, 'excel2': excel_data2, 'columns2': C2

        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
            # fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            # fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            # AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            # AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            # AA = pd.read_excel(AA)
            # AA1 = pd.read_excel(AA1)
            AA2 = pd.read_excel(AA2)

            # AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            # C = list(AA.columns)
            # C1 = list(AA1.columns)
            C2 = list(AA2.columns)

            # for j in range(0, len(AA[C[0]])):
            #     row_data = list()
            #     for col1 in range(0, len(C)):
            #         row_data.append(str(AA.loc[j, C[col1]]))
            #     excel_data.append(row_data)
            #
            # for j in range(0, len(AA1[C1[0]])):
            #     row_data1 = list()
            #     for col1 in range(0, len(C1)):
            #         row_data1.append(str(AA1.loc[j, C1[col1]]))
            #     excel_data1.append(row_data1)

            for j in range(0, len(AA2[C2[0]])):
                row_data2 = list()
                for col1 in range(0, len(C2)):
                    row_data2.append(str(AA2.loc[j, C2[col1]]))
                excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'excel2': excel_data2, 'columns2': C2, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel': excel_data, 'columns': C, 'excel1': excel_data1, 'columns1': C1,

        elif os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/MIS/Performance_IDFC_TW.xlsx')):
            # fs = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
            fs1 = FileSystemStorage(location='media/IDFC_TW/MIS')
            # fs2 = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
            # AA = fs.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
            AA1 = fs1.open('Performance_IDFC_TW.xlsx')
            # AA2 = fs2.open('IDFC_TW TC Incentive.xlsx')
            # AA = pd.read_excel(AA)
            AA1 = pd.read_excel(AA1)
            # AA2 = pd.read_excel(AA2)

            # AA.drop(['EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT', 'TOTAL_FIX_SALARY', 'RB_INCENTIVE', 'Unnamed: 0'], axis=1, inplace=True)

            # AA2.drop(['PAYOUT', 'RB_PAYOUT', 'Unnamed: 0', 'EMPLOYEE_ID', 'MANAGER_ID', 'DESIGNATION', 'STAFF', 'EMPLOYEE_STATUS', 'PROCESS', 'DEPARTMENT'], axis=1, inplace=True)

            # C = list(AA.columns)
            C1 = list(AA1.columns)
            # C2 = list(AA2.columns)

            # for j in range(0, len(AA[C[0]])):
            #     row_data = list()
            #     for col1 in range(0, len(C)):
            #         row_data.append(str(AA.loc[j, C[col1]]))
            #     excel_data.append(row_data)

            for j in range(0, len(AA1[C1[0]])):
                row_data1 = list()
                for col1 in range(0, len(C1)):
                    row_data1.append(str(AA1.loc[j, C1[col1]]))
                excel_data1.append(row_data1)

            # for j in range(0, len(AA2[C2[0]])):
            #     row_data2 = list()
            #     for col1 in range(0, len(C2)):
            #         row_data2.append(str(AA2.loc[j, C2[col1]]))
            #     excel_data2.append(row_data2)

            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'excel1': excel_data1, 'columns1': C1, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})
            # 'excel': excel_data, 'columns': C 'excel2': excel_data2, 'columns2': C2

        else:
            final_dep = DEP()
            final_process = COMPANY_PROCESS()
            Designation = Employee_Designation()

            return render(request, 'FirstLevel/analysis.html',{'Status':'Please Upload Allocation & Paid file for Analysis', 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation':Designation})


    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    return render(request, 'FirstLevel/analysis.html',{'excel': excel_data, 'columns': C, 'excel1': excel_data1, 'columns1': C1, 'excel2': excel_data2, 'columns2': C2, 'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation})

def IDFC_TW_TL_SALARY(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()
    TL_SALARY = SALARY()

    return render(request, 'FirstLevel/salary.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'TL_SALARY': TL_SALARY})

def IDFC_TW_EMPLOYEES(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()
    excel_data=[]

    if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
        fs = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')
        AA = fs.open('Employee_Database.xlsx')
        AA = pd.read_excel(AA)

        A2 = AA[((AA['DESIGNATION'] == 'FOS') | (AA['DESIGNATION'] == 'TC')) & (AA['PROCESS'] == 'IDFC') & (AA['DEPARTMENT'] == 'TW') & (AA['EMPLOYEE_STATUS']=='ACTIVE')]

        A3 = A2[['NAMES','EMPLOYEE_ID','MANAGER_ID','DESIGNATION','STAFF','EMPLOYEE_STATUS','PROCESS','DEPARTMENT','TYPE_OF_SALARY','SALARY','PHONE_NUMBER','HIRE_DATE']]

        A3 = A3.reset_index(drop=True)

        C = list(A3.columns)

        print(C)

        print(A3.loc[0,C[1]])

        for j in range(0, len(A3[C[0]])):
            row_data = list()
            for col in range(0, len(C)):
                row_data.append(str(A3.loc[j, C[col]]))
            excel_data.append(row_data)

        return render(request, 'FirstLevel/employee_views.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'excel': excel_data, 'columns': C})

def BAJAJ_CD_EMPLOYEES(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()
    excel_data=[]

    if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
        fs = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')
        AA = fs.open('Employee_Database.xlsx')
        AA = pd.read_excel(AA)

        A2 = AA[((AA['DESIGNATION'] == 'FOS') | (AA['DESIGNATION'] == 'TC')) & (AA['PROCESS'] == 'BAJAJ') & (AA['DEPARTMENT'] == 'CD') & (AA['EMPLOYEE_STATUS']=='ACTIVE')]

        A3 = A2[['NAMES','EMPLOYEE_ID','MANAGER_ID','DESIGNATION','STAFF','EMPLOYEE_STATUS','PROCESS','DEPARTMENT','TYPE_OF_SALARY','SALARY','PHONE_NUMBER','HIRE_DATE']]

        A3 = A3.reset_index(drop=True)

        C = list(A3.columns)

        print(C)

        print(A3.loc[0,C[1]])

        for j in range(0, len(A3[C[0]])):
            row_data = list()
            for col in range(0, len(C)):
                row_data.append(str(A3.loc[j, C[col]]))
            excel_data.append(row_data)

        return render(request, 'FirstLevel/employee_views.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'excel': excel_data, 'columns': C})

def IDFC_HL_EMPLOYEES(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()
    excel_data=[]

    if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
        fs = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')
        AA = fs.open('Employee_Database.xlsx')
        AA = pd.read_excel(AA)

        A2 = AA[((AA['DESIGNATION'] == 'FOS') | (AA['DESIGNATION'] == 'TC')) & (AA['PROCESS'] == 'IDFC') & (AA['DEPARTMENT'] == 'HL') & (AA['EMPLOYEE_STATUS']=='ACTIVE')]

        A3 = A2[['NAMES','EMPLOYEE_ID','MANAGER_ID','DESIGNATION','STAFF','EMPLOYEE_STATUS','PROCESS','DEPARTMENT','TYPE_OF_SALARY','SALARY','PHONE_NUMBER','HIRE_DATE']]

        A3 = A3.reset_index(drop=True)

        C = list(A3.columns)

        print(C)

        print(A3.loc[0,C[1]])

        for j in range(0, len(A3[C[0]])):
            row_data = list()
            for col in range(0, len(C)):
                row_data.append(str(A3.loc[j, C[col]]))
            excel_data.append(row_data)

        return render(request, 'FirstLevel/employee_views.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'excel': excel_data, 'columns': C})

def FULLERTON_RECOVERY_EMPLOYEES(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()
    excel_data=[]

    if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
        fs = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')
        AA = fs.open('Employee_Database.xlsx')
        AA = pd.read_excel(AA)

        A2 = AA[((AA['DESIGNATION'] == 'FOS') | (AA['DESIGNATION'] == 'TC')) & (AA['PROCESS'] == 'FULLERTON') & (AA['DEPARTMENT'] == 'RECOVERY') & (AA['EMPLOYEE_STATUS']=='ACTIVE')]

        A3 = A2[['NAMES','EMPLOYEE_ID','MANAGER_ID','DESIGNATION','STAFF','EMPLOYEE_STATUS','PROCESS','DEPARTMENT','TYPE_OF_SALARY','SALARY','PHONE_NUMBER','HIRE_DATE']]

        A3 = A3.reset_index(drop=True)

        C = list(A3.columns)

        print(C)

        print(A3.loc[0,C[1]])

        for j in range(0, len(A3[C[0]])):
            row_data = list()
            for col in range(0, len(C)):
                row_data.append(str(A3.loc[j, C[col]]))
            excel_data.append(row_data)

        return render(request, 'FirstLevel/employee_views.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'excel': excel_data, 'columns': C})

def IDFC_TW_ANALYSIS(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/TC Incentive/IDFC_TW TC Incentive.xlsx')):
            if os.path.exists(os.path.join(BASE_DIR, 'media/COMBINED SALARY OF L_T AND IDFC TW/PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')):
                if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_TW/Billing/Final_Billing_IDFC_TW.xlsx')):
                    if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
                        fs = FileSystemStorage(location='media/IDFC_TW/TC Incentive')
                        fs1 = FileSystemStorage(location='media/COMBINED SALARY OF L_T AND IDFC TW')
                        fs2 = FileSystemStorage(location='media/IDFC_TW/Billing')
                        fs3 = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')

                        AA = fs.open('IDFC_TW TC Incentive.xlsx')
                        AA2 = fs1.open('PER PAID CASE(Including Fixed Salary) IDFC-TW.xlsx')
                        AA3 = fs1.open('PER PAID CASE(PIVOT) IDFC-TW.xlsx')
                        AA4 = fs2.open('BKT_Billing_IDFC_TW.xlsx')
                        AA5 = fs3.open('Employee_Database.xlsx')

                        AA1 = pd.read_excel(AA)
                        AA2 = pd.read_excel(AA2)
                        AA3 = pd.read_excel(AA3)
                        AA4 = pd.read_excel(AA4)
                        AA5 = pd.read_excel(AA5)

                        AA5 = AA5[(AA5['DESIGNATION'] != 'FOS') & (AA5['PROCESS'] == 'IDFC') & (AA5['DEPARTMENT'] == 'TW') & (AA5['EMPLOYEE_STATUS'] == 'ACTIVE')]

                        AA5 = AA5.reset_index(drop=True)

                        AA1['TC COSTING'] = AA1['PAYOUT']+AA1['RB_PAYOUT']
                        AA2['FOS COSTING'] = AA2['TOTAL_FIX_SALARY'] + AA2['RB_INCENTIVE']

                        TC_INCENTIVE = AA1['TC COSTING'].sum()
                        FIXED_COSTING_FOS = AA2['FOS COSTING'].sum()
                        INCENTIVE_COSTING_FOS = AA3['PER PAID CASE'].sum()
                        TOTAL_BILLING = AA4['PAYOUT'].sum()
                        FIXED_COSTING_OFFICE = AA5['SALARY'].sum()
                        TOTAL_FOS_COSTING = FIXED_COSTING_OFFICE + INCENTIVE_COSTING_FOS
                        FINAL_COSTING = TC_INCENTIVE + FIXED_COSTING_FOS + INCENTIVE_COSTING_FOS + FIXED_COSTING_OFFICE
                        P_L_IDFC_TW = TOTAL_BILLING-FINAL_COSTING
                        P_L_IDFC_TW_PERCENTAGE = round((P_L_IDFC_TW/TOTAL_BILLING)*100,2)

                        return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'TC_INCENTIVE': TC_INCENTIVE, 'FIXED_COSTING_FOS': FIXED_COSTING_FOS, 'INCENTIVE_COSTING_FOS': INCENTIVE_COSTING_FOS, 'TOTAL_BILLING': TOTAL_BILLING, 'FIXED_COSTING_OFFICE': FIXED_COSTING_OFFICE, 'FINAL_COSTING': FINAL_COSTING, 'P_L_IDFC_TW': P_L_IDFC_TW, 'TOTAL_FOS_COSTING': TOTAL_FOS_COSTING, 'P_L_IDFC_TW_PERCENTAGE': P_L_IDFC_TW_PERCENTAGE})
                else:
                    return render(request, 'FirstLevel/analysis.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh Billing Data'})
            else:
                return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh FOS Salary Data'})
        else:
            return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh TC and FOS Salary Data'})

def FULLERTON_RECOVERY_ANALYSIS(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/FOS Salary/FOS_SALARY_FULLERTON_RECOVERY.xlsx')):
            if os.path.exists(os.path.join(BASE_DIR, 'media/FULLERTON_RECOVERY/BILLING/PAYOUT_FULLERTON_RECOVERY.xlsx')):
                if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
                    fs1 = FileSystemStorage(location='media/FULLERTON_RECOVERY/FOS Salary')
                    fs2 = FileSystemStorage(location='media/FULLERTON_RECOVERY/Billing')
                    fs3 = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')

                    AA1 = fs1.open('FOS_SALARY_FULLERTON_RECOVERY.xlsx')
                    AA2 = fs2.open('PAYOUT_FULLERTON_RECOVERY.xlsx')
                    AA3 = fs3.open('Employee_Database.xlsx')

                    AA1 = pd.read_excel(AA1)
                    AA2 = pd.read_excel(AA2)
                    AA3 = pd.read_excel(AA3)

                    AA3 = AA3[(AA3['PROCESS'] == 'FULLERTON') & (AA3['DEPARTMENT'] == 'RECOVERY') & (AA3['EMPLOYEE_STATUS'] == 'ACTIVE')]

                    FIXED_COSTING_FOS = AA1['FIXED_PAYOUT'].sum()
                    INCENTIVE_COSTING_FOS = AA1['INCENTIVE'].sum()
                    TOTAL_FOS_COSTING = FIXED_COSTING_FOS + INCENTIVE_COSTING_FOS
                    FIXED_COSTING_OFFICE = AA3['SALARY'].sum()
                    TOTAL_BILLING = AA2['PAYOUT'].sum()

                    FINAL_COSTING = FIXED_COSTING_FOS + INCENTIVE_COSTING_FOS + FIXED_COSTING_OFFICE
                    P_L_FULLERTON_RECOVERY = round(TOTAL_BILLING-FINAL_COSTING,2)
                    P_L_FULLERTON_RECOVERY_PERCENTAGE = round((P_L_FULLERTON_RECOVERY/TOTAL_BILLING)*100,2)

                    return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'FIXED_COSTING_FOS': FIXED_COSTING_FOS, 'INCENTIVE_COSTING_FOS': INCENTIVE_COSTING_FOS, 'TOTAL_BILLING': TOTAL_BILLING, 'FIXED_COSTING_OFFICE': FIXED_COSTING_OFFICE, 'FINAL_COSTING': FINAL_COSTING, 'P_L_FULLERTON_RECOVERY': P_L_FULLERTON_RECOVERY, 'TOTAL_FOS_COSTING': TOTAL_FOS_COSTING, 'P_L_FULLERTON_RECOVERY_PERCENTAGE': P_L_FULLERTON_RECOVERY_PERCENTAGE})
            else:
                return render(request, 'FirstLevel/analysis.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh Billing Data'})
        else:
            return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh FOS Salary Data'})

def BAJAJ_CD_ANALYSIS(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/BAJAJ-CD/MIS/BAJAJ TC-WISE MIS.xlsx')):
            if os.path.exists(os.path.join(BASE_DIR, 'media/BAJAJ-CD/Billing/BAJAJ PAYOUT.xlsx')):
                if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
                    fs = FileSystemStorage(location='media/BAJAJ-CD/MIS')
                    fs2 = FileSystemStorage(location='media/BAJAJ-CD/Billing')
                    fs3 = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')

                    AA1 = fs.open('BAJAJ TC-WISE MIS.xlsx')
                    AA2 = fs2.open('BAJAJ PAYOUT.xlsx')
                    AA3 = fs3.open('Employee_Database.xlsx')

                    AA1 = pd.read_excel(AA1)
                    AA2 = pd.read_excel(AA2)
                    AA3 = pd.read_excel(AA3)

                    AA3 = AA3[(AA3['DESIGNATION'] != 'FOS') & (AA3['PROCESS'] == 'BAJAJ') & (AA3['DEPARTMENT'] == 'CD') & (AA3['EMPLOYEE_STATUS'] == 'ACTIVE')]

                    AA3 = AA3.reset_index(drop=True)

                    TC_INCENTIVE = AA1['FLAT INCENTIVE'].sum()
                    TOTAL_BILLING = AA2['PAYOUT'].sum()
                    FIXED_COSTING_OFFICE = AA3['SALARY'].sum()
                    FINAL_COSTING = FIXED_COSTING_OFFICE + TC_INCENTIVE
                    P_L_BAJAJ_CD = round(TOTAL_BILLING-FINAL_COSTING,2)
                    P_L_BAJAJ_CD_PERCENTAGE = round((P_L_BAJAJ_CD/TOTAL_BILLING)*100,2)

                    return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'TC_INCENTIVE': TC_INCENTIVE, 'TOTAL_BILLING': TOTAL_BILLING, 'FIXED_COSTING_OFFICE': FIXED_COSTING_OFFICE, 'FINAL_COSTING': FINAL_COSTING, 'P_L_BAJAJ_CD': P_L_BAJAJ_CD, 'P_L_BAJAJ_CD_PERCENTAGE': P_L_BAJAJ_CD_PERCENTAGE})
            else:
                return render(request, 'FirstLevel/analysis.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh Billing Data'})
        else:
            return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh TC and FOS Salary Data'})

def IDFC_HL_ANALYSIS(request):
    final_dep = DEP()
    final_process = COMPANY_PROCESS()
    Designation = Employee_Designation()

    if request.method != 'POST':
        if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/FOS Salary/FINAL PAYOUT IDFC-HL.xlsx')):
            if os.path.exists(os.path.join(BASE_DIR, 'media/IDFC_HL/Billing/BKT_Billing_IDFC_HL.xlsx')):
                if os.path.exists(os.path.join(BASE_DIR, 'media/Employees/Employee_Database.xlsx')):
                    fs1 = FileSystemStorage(location='media/IDFC_HL/FOS Salary')
                    fs2 = FileSystemStorage(location='media/IDFC_HL/Billing')
                    fs3 = FileSystemStorage(location='/Users/mohaksehgal/Website_Deployment/media/Employees')

                    AA1 = fs1.open('FINAL PAYOUT IDFC-HL.xlsx')
                    AA2 = fs2.open('BKT_Billing_IDFC_HL.xlsx')
                    AA3 = fs3.open('Employee_Database.xlsx')

                    AA1 = pd.read_excel(AA1)
                    AA2 = pd.read_excel(AA2)
                    AA3 = pd.read_excel(AA3)

                    AA3 = AA3[(AA3['DESIGNATION'] != 'FOS') & (AA3['PROCESS'] == 'IDFC') & (AA3['DEPARTMENT'] == 'HL') & (AA3['EMPLOYEE_STATUS'] == 'ACTIVE')]

                    AA3 = AA3.reset_index(drop=True)

                    AA1['FOS COSTING'] = AA1['FIXED SALARY'] + AA1['RB PAYOUT']

                    FIXED_COSTING_FOS = AA1['FOS COSTING'].sum()
                    INCENTIVE_COSTING_FOS = round(AA1['PER PAID CASE'].sum(),2)
                    TOTAL_BILLING = AA2['PAYOUT'].sum()
                    FIXED_COSTING_OFFICE = AA3['SALARY'].sum()
                    TOTAL_FOS_COSTING = FIXED_COSTING_FOS + INCENTIVE_COSTING_FOS
                    FINAL_COSTING = FIXED_COSTING_FOS + INCENTIVE_COSTING_FOS + FIXED_COSTING_OFFICE
                    P_L_IDFC_HL = TOTAL_BILLING-FINAL_COSTING
                    P_L_IDFC_HL_PERCENTAGE = round((P_L_IDFC_HL/TOTAL_BILLING)*100,2)

                    return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'FIXED_COSTING_FOS': FIXED_COSTING_FOS, 'INCENTIVE_COSTING_FOS': INCENTIVE_COSTING_FOS, 'TOTAL_BILLING': TOTAL_BILLING, 'FIXED_COSTING_OFFICE': FIXED_COSTING_OFFICE, 'FINAL_COSTING': FINAL_COSTING, 'P_L_IDFC_HL': P_L_IDFC_HL, 'TOTAL_FOS_COSTING': TOTAL_FOS_COSTING, 'P_L_IDFC_HL_PERCENTAGE': P_L_IDFC_HL_PERCENTAGE})
            else:
                return render(request, 'FirstLevel/analysis.html',{'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh Billing Data'})
        else:
            return render(request, 'FirstLevel/analysis.html', {'DEPARTMENT': final_dep, 'PROCESS': final_process, 'Designation': Designation, 'STATUS': 'Please Refresh FOS Salary Data'})