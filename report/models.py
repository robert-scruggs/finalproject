from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import DefaultStorage

# Create your models here.

class BasicInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    finance_review = models.CharField(max_length=200)
    operating_company = models.CharField(max_length=200)
    parent_company = models.CharField( max_length=200)
    business_owners = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)
    primary_business_address = models.CharField(max_length=200)
    proposed_loan_needs = models.CharField(max_length=200)
    list_of_report_outcomes = models.TextField(max_length=40000)
 
class OperatingYears(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    state = models.CharField(max_length=200)
    num_of_locations = models.IntegerField()
    total_sales = models.IntegerField()
    food_cost = models.IntegerField()
    labor_cost = models.IntegerField()
    total_cost_of_goods_sold = models.IntegerField(default=0)
    admin_and_general = models.IntegerField()
    rands_marketing = models.IntegerField()
    facilities = models.IntegerField()
    total_other_operative_expenses = models.IntegerField(default=0)
    total_operative_expenses = models.IntegerField(default=0)
    income_before_fix_expense = models.IntegerField(default=0)
    property_tax = models.IntegerField()
    insurance = models.IntegerField()
    reserve = models.IntegerField()
    total_fix_expenses = models.IntegerField(default=0)
    net_income_before_interest_and_tax = models.IntegerField(default=0)
    percentages = models.IntegerField(default=0)


class PersonalFinancialStatement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    file = models.FileField(storage=DefaultStorage(), unique=False)
    cash_on_hand = models.IntegerField(null=True)
    savings_account = models.IntegerField(null=True)
    cash = models.IntegerField(null=True)
    marketable_securities = models.IntegerField(null=True)
    total_liquid_assets = models.IntegerField(null=True)
    primary_residence = models.IntegerField(null=True)
    ira_401k = models.IntegerField(null=True)
    life_insurance = models.IntegerField(null=True)
    notes_receivable = models.IntegerField(null=True)
    business_values = models.IntegerField(null=True)
    automobiles = models.IntegerField(null=True)
    personal_property = models.IntegerField(null=True)
    total_other_assets = models.IntegerField(null=True)
    total_assets = models.IntegerField(null=True)
    total_re_mortgage = models.IntegerField(null=True)
    accounts_payable = models.IntegerField(null=True)
    notes_payable = models.IntegerField(null=True)
    installment_accounts_auto = models.IntegerField(null=True)
    installment_accounts_other = models.IntegerField(null=True)
    installment_accounts = models.IntegerField(null=True)
    total_liabilities = models.IntegerField(null=True)
    net_worth = models.IntegerField(null=True)
    grand_total = models.IntegerField(null=True)

class FinancialFlashReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file = models.FileField(storage=DefaultStorage(), unique=False)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    years_in_current_business = models.CharField(max_length=255)
    current_business_structure = models.CharField(max_length=255)
    date_of_statement = models.CharField(max_length=255)
    cash_from_sales = models.IntegerField(null=True)
    gross_cash_income = models.IntegerField(null=True)
    cash_operating_expenses = models.IntegerField(null=True)
    other_income = models.IntegerField(null=True)
    net_cash_after_operations = models.IntegerField(null=True)
    m1_net_deductions = models.IntegerField(null=True)
    m2_net_deductions = models.IntegerField(null=True)
    ending_cash_position = models.IntegerField(null=True)
    depreciation = models.IntegerField(null=True)
    amortization = models.IntegerField(null=True)
    interest = models.IntegerField(null=True)
    nre = models.IntegerField(null=True)
    owners_management_fees = models.IntegerField(null=True)
    cash_flow = models.IntegerField(null=True)
    operational_cash = models.IntegerField(null=True)
    available_cash = models.IntegerField(null=True)
    new_debt_services = models.IntegerField(null=True)
    surplus = models.IntegerField(null=True)
    coverage_ratio = models.IntegerField(null=True)
    financial_footnotes = models.CharField(max_length=10000)
    business_id = models.IntegerField(null=True)
    consolidated = models.BooleanField(null=True)
    
    def __str__(self):
        return f"MyModel(company_name={self.company_name}, address={self.address}, owner_name={self.owner_name}, years_in_current_business={self.years_in_current_business}, current_business_structure={self.current_business_structure}, date_of_statement={self.date_of_statement}, cash_from_sales={self.cash_from_sales}, gross_cash_income={self.gross_cash_income}, cash_operating_expenses={self.cash_operating_expenses}, other_income={self.other_income}, net_cash_after_operations={self.net_cash_after_operations}, m1_net_deductions={self.m1_net_deductions}, m2_net_deductions={self.m2_net_deductions}, ending_cash_position={self.ending_cash_position}, depreciation={self.depreciation}, amortization={self.amortization}, interest={self.interest}, nre={self.nre}, owners_management_fees={self.owners_management_fees}, cash_flow={self.cash_flow}, operational_cash={self.operational_cash}, available_cash={self.available_cash}, new_debt_services={self.new_debt_services}, surplus={self.surplus}, coverage_ratio={self.coverage_ratio}, financial_footnotes={self.financial_footnotes}, business_id={self.business_id})"
 


    