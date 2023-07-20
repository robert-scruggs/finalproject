from django.shortcuts import render, redirect
from financialStatements import *
from financialFlashReports import *
from .forms import BasicInformationForm, OperatingYearsForm1, OperatingYearsForm2, OperatingYearsForm3
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import * 
from django.core.files.base import ContentFile
import io
from django.http import HttpResponse
from itertools import groupby
from operator import attrgetter





# Create your views here.
#basically methods that link up to the forms.py module and return instances of the html created
#in forms

#think of these mfs as people who prepare the rooms
#like a specific maid to tend to a room 
#that maid knows how to do specific things that i have already taught them

#comes from forms.py 
@login_required
def basicInformation(request):
    form = BasicInformationForm()
    
    if request.method == "POST":
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            #this will be the signed in users id
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.save()
        return redirect("/yearOne/")
    
    return render(request, "firstPage.html", {"form":form})

@login_required
def yearOne(request):
    form = OperatingYearsForm1()
    if request.method == "POST":
        form = OperatingYearsForm1(request.POST)
        
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.save()
            form.user = request.user.id
            #extra values that need to be saved
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[0]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
            # idk = OperatingYears.objects.filter(user_id=form.user).all()[:3]
            # for data in idk:
            #     print(data.property_tax)
        return redirect("/yearTwo/")
    

    return render(request, 'secondPage.html', {"form" : form})

@login_required
def yearTwo(request):
    form = OperatingYearsForm2()

    if request.method == "POST":
        form = OperatingYearsForm2(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
            #
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[1]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
        return redirect("/yearThree/")

    return render(request, 'thirdPage.html', {"form" : form})

@login_required
def yearThree(request):
    form = OperatingYearsForm3()

    
    if request.method == "POST":
        form = OperatingYearsForm3(request.POST)
        if form.is_valid():
            my_object = form.save(commit=False)
            my_object.user = request.user
            my_object.save()
            form.user = request.user.id
            form.save()
            total_cost_of_goods_sold_value = int(form.cleaned_data['food_cost']) + int(form.cleaned_data['labor_cost'])
            total_other_operative_expense_value = int(form.cleaned_data['admin_and_general']) + int(form.cleaned_data['rands_marketing']) + int(form.cleaned_data['facilities'])
            total_operative_expense_value = total_cost_of_goods_sold_value + total_other_operative_expense_value
            income_before_fix_expense_value = int(form.cleaned_data['total_sales']) - total_operative_expense_value
            total_fix_expense_value = int(form.cleaned_data['property_tax']) + int(form.cleaned_data['insurance']) + int(form.cleaned_data['reserve'])
            net_income_value = income_before_fix_expense_value - total_fix_expense_value
            #this is getting the first row of operating years for the specific user
            tcogsDB = OperatingYears.objects.filter(user_id = form.user).all()[2]
            tcogsDB.total_cost_of_goods_sold = total_cost_of_goods_sold_value
            tcogsDB.total_other_operative_expenses = total_other_operative_expense_value
            tcogsDB.total_operative_expenses = total_operative_expense_value
            tcogsDB.income_before_fix_expense = income_before_fix_expense_value
            tcogsDB.total_fix_expenses = total_fix_expense_value
            tcogsDB.net_income_before_interest_and_tax = net_income_value
            #saves extra data to database
            tcogsDB.save()
            print(total_cost_of_goods_sold_value, total_other_operative_expense_value, total_operative_expense_value, income_before_fix_expense_value,total_fix_expense_value,net_income_value)
        return redirect("/personalFinancialStatementFiles/")

    return render(request, 'fourthPage.html', {"form" : form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/basicInformation/")
        else:
            print("wrong information")
            
    # context = {'form':form}
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            form.save()
            if user is not None:
                login(request, user)
                return redirect("/basicInformation")
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "register.html", context)

@login_required    
def logoutUser(request):
    logout(request)
    return redirect("/login")

incomeTaxReturnFilesList = []
businessID = [0]
@login_required
def incomeTaxReturnFiles(request):
    user = request.user
    ffr = FinancialFlashReport.objects.filter(user_id=user)
    businessID[0] = businessID[0] + 1

    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        businessName = request.POST.get('businessName')
        address = request.POST.get('address')
        owners = request.POST.get('owners')
        yearsInBusiness = request.POST.get('yearsInBusiness')
        locations = request.POST.get('locations')
        nre = request.POST.getlist('nre')
        ownersManagementFees = request.POST.getlist('ownersManagementFees')

        print(uploaded_files)

        for file, nre ,ownersFee in zip(uploaded_files, nre, ownersManagementFees):
            incomeTaxReturnFilesList.append(uploaded_files)
            file_contents = io.BytesIO(file.read())
            new_file = FinancialFlashReport(user=user,business_id=businessID[0])
            new_file.file.save(file.name, ContentFile(file_contents.getvalue()))
            new_file.company_name = businessName
            new_file.address = address
            new_file.owner_name = owners
            new_file.years_in_current_business = yearsInBusiness
            new_file.current_business_structure = locations
            new_file.nre = nre
            new_file.owners_management_fees = ownersFee
            new_file.save()
            print(file)
        
    context = {
        'ffr':ffr
    }

    return render(request, 'uploadIncomeTaxReturns.html',context)

def restart(request):
    FinancialFlashReport.objects.all(user_id=request.user).delete()
    PersonalFinancialStatement.objects.all(user_id=request.user).delete()
    OperatingYears.objects.all(user_id=request.user).delete()
    BasicInformation.objects.all(user_id=request.user).delete()

    return HttpResponse("all deleted")


personalFinancialStatementFilesList = []
@login_required
def personalFinancialStatementFiles(request):
    user = request.user
    pfs = PersonalFinancialStatement.objects.filter(user_id=user) 
    
    if request.method == 'POST':
        uploaded_files = request.FILES.getlist('files')
        for file in uploaded_files:
            personalFinancialStatementFilesList.append(file)
            file_contents = io.BytesIO(file.read())
            new_file = PersonalFinancialStatement(user=user)
            new_file.file.save(file.name, ContentFile(file_contents.getvalue()))
            new_file.save()

        for person in pfs:
            file = person.file
            person.cash_on_hand = getCashOnHand(file)
            person.savings_account = getSavingsAccount(file)
            person.cash = getCash(file)
            person.marketable_securities = getMarketableSecurities(file)
            person.total_liquid_assets = getTotalLiquidAssets(file)
            person.primary_residence = getPrimaryResidence(file)
            person.ira_401k = getIRA(file)
            person.life_insurance = getLifeInsurance(file)
            person.notes_receivable = getNotesReceivable(file)
            person.business_values = getBusinessValues(file)
            person.automobiles = getAutomobiles(file)
            person.personal_property = getPersonalProperty(file)
            person.total_other_assets = getTotalOtherAssets(file)
            person.total_assets = getTotalAssets(file)
            person.total_re_mortgage = getTotalREMortgage(file)
            person.accounts_payable = getAccountsPayable(file)
            person.notes_payable = getNotesPayable(file)
            person.installment_accounts_auto = getInstallmentAccountsAuto(file)
            person.installment_accounts_other = getInstallmentAccountsOther(file)
            person.installment_accounts = getInstallmentAccounts(file)
            person.total_liabilities = getTotalLiabilities(file)
            person.net_worth = getNetWorth(file)
            person.grand_total = getAbsoluteTotal(file)
            person.save()
    context = {
        'pfs':pfs
    }
    return render(request, 'uploadFinancialStatements.html', context)
 

@login_required
def finalReport(request):
    #resets businessID back to zero since it will be used globally, yes i know its bad code but i must continue i fear
    businessID[0] = 0
    user = request.user
    finalReport = FinancialFlashReport.objects.filter(user_id=user)
    bi = BasicInformation.objects.filter(user_id=user)
    oy1 = OperatingYears.objects.filter(user_id=user)
    pfs = PersonalFinancialStatement.objects.filter(user_id=user)
    items = FinancialFlashReport.objects.filter(user_id=user).filter(consolidated=0).order_by('business_id')
    max_id = finalReport.latest('business_id').business_id
    grouped_items = groupby(items, key=attrgetter('business_id'))
    ffr = [{'business_id': key, 'items': list(group)} for key, group in grouped_items]
    
    # #these names are confusing as hell but keep up please
    # for id in range(max_id + 1):
    #     files = finalReport.filter(business_id=id)

    #     for currUser in files:
    #         currFile = currUser.file
    #         currUser.cash_from_sales = financialFlashReports.getCashFromSales(currFile)
    #         currUser.gross_cash_income = financialFlashReports.getGrossCashIncome(currFile)
    #         currUser.cash_operating_expenses = financialFlashReports.getCashOperatingExpenses(currFile)
    #         currUser.other_income = financialFlashReports.getOtherIncomeExpenses(currFile)
    #         currUser.net_cash_after_operations = financialFlashReports.getNetCashAfterOperations(currFile)
    #         currUser.m1_net_deductions = financialFlashReports.getM1Deductions(currFile)
    #         currUser.m2_net_deductions = financialFlashReports.getM2Deductions(currFile)
    #         currUser.ending_cash_position = financialFlashReports.getEndingCashPosition(currFile)
    #         currUser.depreciation = financialFlashReports.getDepreciation(currFile)
    #         currUser.amortization = financialFlashReports.getAmortization(currFile)
    #         currUser.interest = financialFlashReports.getInterest(currFile)
    #         currUser.cash_flow = financialFlashReports.getCashFlow(currFile)
    #         currUser.operational_cash = financialFlashReports.getCashFlow(currFile)
    #         currUser.available_cash = financialFlashReports.getCashFlow(currFile)
    #         currUser.new_debt_services = 0
    #         currUser.surplus = financialFlashReports.getCashFlow(currFile)
    #         currUser.coverage_ratio = 0
    #         currUser.financial_footnotes = "empty"
    #         currUser.date_of_statement = financialFlashReports.getStatementDate(currFile)
    #         currUser.consolidated = 0
    #         currUser.save()
    
    # #consolidated
    first_value = FinancialFlashReport.objects.filter(user_id=user).values_list('business_id', flat=True).first()
    if first_value is not None:
        queryset = FinancialFlashReport.objects.filter(business_id=first_value)
        for x in queryset:
            secondSet = FinancialFlashReport.objects.filter(date_of_statement=x.date_of_statement)
            
            # excludedFields = ['user','file','company_name','address','owner_name','years_in_current_business','current_business_structure','date_of_statement', 'id', 'business_id', 'financial_footnotes']
            # fields = FinancialFlashReport._meta.get_fields()
            # column_names = [field.name for field in fields if field.name not in excludedFields]
            cash_from_sales = 0
            gross_cash_income = 0
            cash_operating_expenses = 0
            other_income = 0
            net_cash_after_operations = 0
            m1_net_deductions = 0
            m2_net_deductions = 0
            ending_cash_position = 0
            depreciation = 0
            amortization = 0
            interest = 0
            nre = 0
            owners_management_fees = 0
            cash_flow = 0
            address = ""
            for x in secondSet:
                try:
                    cash_from_sales = x.cash_from_sales + cash_from_sales
                    gross_cash_income = x.gross_cash_income + gross_cash_income
                    cash_operating_expenses = x.cash_operating_expenses + cash_operating_expenses
                    other_income = x.other_income + other_income
                    net_cash_after_operations = x.net_cash_after_operations + net_cash_after_operations
                    m1_net_deductions = x.m1_net_deductions + m1_net_deductions
                    m2_net_deductions = x.m2_net_deductions + m2_net_deductions
                    ending_cash_position = x.ending_cash_position + ending_cash_position
                    depreciation = x.depreciation + depreciation
                    amortization = x.amortization + amortization
                    interest = x.interest + interest
                    nre = x.nre + nre
                    owners_management_fees = x.owners_management_fees + owners_management_fees
                    cash_flow = x.cash_flow + cash_flow
                    address = x.address 
                    company_name = x.company_name
                    operational_cash= x.operational_cash
                    current_business_structure= x.current_business_structure + ", " + x.current_business_structure
                except:
                    pass        
            newFile = FinancialFlashReport(user=user,
                                            company_name=company_name,
                                            owner_name= x.owner_name,
                                            address=address,
                                            years_in_current_business= x.years_in_current_business,
                                            current_business_structure= current_business_structure,
                                            date_of_statement= x.date_of_statement,
                                            cash_from_sales= cash_from_sales,
                                            gross_cash_income= gross_cash_income,
                                            cash_operating_expenses= cash_operating_expenses,
                                            other_income= other_income,
                                            net_cash_after_operations= net_cash_after_operations,
                                            m1_net_deductions= m1_net_deductions,
                                            m2_net_deductions= m2_net_deductions,
                                            ending_cash_position= ending_cash_position,
                                            depreciation= depreciation,
                                            amortization= amortization,
                                            interest= interest,
                                            nre= nre,
                                            owners_management_fees= owners_management_fees,
                                            cash_flow= cash_flow,
                                            operational_cash= operational_cash,
                                            consolidated= 1
                                            )
            newFile.save()

    consolidated = FinancialFlashReport.objects.filter(consolidated=1)

    business_structure_split = consolidated[0].current_business_structure.split(", ")
    
    context = {
        'bi': bi,
        'oy1': oy1,
        'pfs': pfs,
        'finalReport': finalReport,
        'ffr': ffr,
        'state': oy1[0].state,
        'consolidated': consolidated,
        "business_structure_split": business_structure_split,
    }
    
    return render(request, 'practiceReport.html', context)
