from django import forms
from django.forms import ModelForm
from .models import BasicInformation, OperatingYears



#this is basically your html
#this is what your maids will use to decorate the rooms

class BasicInformationForm(ModelForm):
    finance_review = forms.CharField(max_length=255, label="Proposed project for financing review:")
    operating_company = forms.CharField(max_length=255, label="Operating Company")
    parent_company = forms.CharField(max_length=255, label="Parent Company")
    business_owners = forms.CharField(max_length=255, label="Business Owners", help_text="(Separate business owners with commas)")
    locations = forms.CharField(max_length=255, label="Locations", help_text="(Separate locations with commas)")
    primary_business_address = forms.CharField(max_length=255, label="Primary Business Address")
    proposed_loan_needs = forms.CharField(max_length=255, label="Proposed Loan Needs:")
    list_of_report_outcomes = forms.CharField(max_length=2000, label="Package Includes:", help_text="(Separate items with commas)", widget=forms.Textarea(attrs={
        'style': 'vertical-align: top',
        "rows":5, "cols":20
    }))
    class Meta:
        model = BasicInformation
        fields = ('finance_review','operating_company', 'parent_company', 'business_owners', 'locations', 'primary_business_address','proposed_loan_needs','list_of_report_outcomes')
        

class OperatingYearsForm1(ModelForm):
    state = forms.CharField(max_length=200, label="Which state does your company operate out of?")
    num_of_locations = forms.CharField(max_length=200, label="Please type number of locations for year 1")
    food_cost = forms.CharField(max_length=200, label="Enter total food cost for year 1")
    labor_cost = forms.CharField(max_length=200, label="Enter total labor cost for year 1")
    admin_and_general = forms.CharField(max_length=200, label="Enter total administration and general cost for year 1")
    rands_marketing = forms.CharField(max_length=200, label="Enter total royal/sales marketing cost for year 1")
    facilities = forms.CharField(max_length=200, label="Enter total facilities cost for year 1")
    property_tax = forms.CharField(max_length=200, label="Enter total property tax cost for year 1")
    insurance = forms.CharField(max_length=200, label="Enter total insurance costs for year 1")
    reserve = forms.CharField(max_length=200, label="Enter total reserve cost for year 1")    
    class Meta:
        model = OperatingYears
        fields = ['state','num_of_locations', 'total_sales', 'food_cost', 'labor_cost','admin_and_general','rands_marketing', 'facilities', 'property_tax','insurance','reserve']

class OperatingYearsForm2(ModelForm):
    num_of_locations = forms.CharField(max_length=200, label="Please type number of locations for year 2")
    food_cost = forms.CharField(max_length=200, label="Enter total food cost for year 2")
    labor_cost = forms.CharField(max_length=200, label="Enter total labor cost for year 2")
    admin_and_general = forms.CharField(max_length=200, label="Enter total administration and general cost for year 2")
    rands_marketing = forms.CharField(max_length=200, label="Enter total royal/sales marketing cost for year 2")
    facilities = forms.CharField(max_length=200, label="Enter total facilities cost for year 2")
    property_tax = forms.CharField(max_length=200, label="Enter total property tax cost for year 2")
    insurance = forms.CharField(max_length=200, label="Enter total insurance costs for year 2")
    reserve = forms.CharField(max_length=200, label="Enter total reserve cost for year 2")    
    class Meta:
        model = OperatingYears
        fields = ['num_of_locations', 'total_sales', 'food_cost', 'labor_cost','admin_and_general','rands_marketing', 'facilities', 'property_tax','insurance','reserve']

class OperatingYearsForm3(ModelForm):
    num_of_locations = forms.CharField(max_length=200, label="Please type number of locations for year 3")
    food_cost = forms.CharField(max_length=200, label="Enter total food cost for year 3")
    labor_cost = forms.CharField(max_length=200, label="Enter total labor cost for year 3")
    admin_and_general = forms.CharField(max_length=200, label="Enter total administration and general cost for year 3")
    rands_marketing = forms.CharField(max_length=200, label="Enter total royal/sales marketing cost for year 3")
    facilities = forms.CharField(max_length=200, label="Enter total facilities cost for year 3")
    property_tax = forms.CharField(max_length=200, label="Enter total property tax cost for year 3")
    insurance = forms.CharField(max_length=200, label="Enter total insurance costs for year 3")
    reserve = forms.CharField(max_length=200, label="Enter total reserve cost for year 3")    
    class Meta:
        model = OperatingYears
        fields = ['num_of_locations', 'total_sales', 'food_cost', 'labor_cost','admin_and_general','rands_marketing', 'facilities', 'property_tax','insurance','reserve']
        

# class TaxYearsForm(ModelForm):
#     date_of_statement = forms.CharField(max_length=200)
#     marketable_securities = forms.CharField(max_length=200)
#     cash_from_sales = forms.CharField(max_length=200)
#     gross_cash_income = forms.CharField(max_length=200)
#     cash_operating_expenses = forms.CharField(max_length=200)
#     other_income = forms.CharField(max_length=200)
#     net_cash_after_operations = forms.CharField(max_length=200)
#     m1_net_deductions = forms.CharField(max_length=200)
#     m2_net_deductions = forms.CharField(max_length=200)
#     ending_cash_position = forms.CharField(max_length=200)
#     depreciation = forms.CharField(max_length=200)
#     amortization = forms.CharField(max_length=200)
#     interest = forms.CharField(max_length=200)
#     nre = forms.CharField(max_length=200)
#     owners_management_fees = forms.CharField(max_length=200)
#     cash_flow = forms.CharField(max_length=200)
#     operational_cash = forms.CharField(max_length=200)
#     available_cash = forms.CharField(max_length=200)
#     new_debt_services = forms.CharField(max_length=200)
#     surplus = forms.CharField(max_length=200)
#     coverage_ratio = forms.CharField(max_length=200)
#     financial_footnotes = forms.CharField(max_length=200)
#     class Meta:
#         model = TaxYears
#         fields = ['date_of_statement','marketable_securities', 'cash_from_sales', 'gross_cash_income', 'cash_operating_expenses','other_income', 'net_cash_after_operations', 'm1_net_deductions', 'm2_net_deductions','ending_cash_position','depreciation',
#                   'amortization','interest','nre','owners_management_fees','cash_flow','operational_cash','available_cash','new_debt_services','surplus','coverage_ratio','financial_footnotes']    


    


# class YearThree(forms.Form):
#     area = forms.CharField(label="What state does your business operate out of", max_length=200)
#     numOfLocations = forms.CharField(label="Please type number of locations for year 3", max_length=200)
#     totalSales = forms.CharField(label="Total sales for year 3", max_length=200)
#     foodCost = forms.CharField(label="Food Cost", max_length=200)
#     laborCost = forms.CharField(label="Labor Cost", max_length=200)
#     adminAndGeneral = forms.CharField(label="Administrative & General Costs", max_length=200)
#     randsMarketing = forms.CharField(label="Royalty/Sales Marketing Costs", max_length=200)
#     incomeBeforeFixExpense = forms.CharField(label="Income Before Fix Expense", max_length=200)
#     propertyTax = forms.CharField(label="Property Tax", max_length=200)
#     insurance = forms.CharField(label="Insurance", max_length=200)
#     reserve = forms.CharField(label="Reserve", max_length=200)
