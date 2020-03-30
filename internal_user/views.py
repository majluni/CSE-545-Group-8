from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import FundDepositForm, IssueChequeForm, CustomerForm
from django.conf import settings

customers = [
    {
        'customerName': 'James Karen',
        'customerId': 1,
        'accountId': 1,
        'accountType': 'Savings'
    },
    {
        'customerName': 'Jane Doe',
        'customerId': 2,
        'accountId': 2,
        'accountType': 'Checking'
    }
]

def initFundDeposit(request):
    return render(request, 'init_fund_deposit.html')

def depositTemplate(request):
    form = FundDepositForm(initial={'customerName': request.POST['customerName'],
                                    'customerId': request.POST['customerId'],
                                    'accountId': request.POST['accountId'],
                                    'accountType': request.POST['accountType']
    })
    return render(request, 'depositFund.html', {'form':form})

def depositFund(request):
    if request.method == 'POST':
        form = FundDepositForm(request.POST)
        if form.is_valid():
            depositAmount = form.cleaned_data.get('depositAmount')
            ## backend code goes here
            messages.success(request, f'Amount deposited successfully {depositAmount}')
            return redirect('./initFundDeposit')

def initIssueCheque(request):
    context = {'context_page' : 'issue_cheque'}
    return render(request, 'init_issue_cheque.html', context)

def issueChequeTemplate(request):
    form = IssueChequeForm(initial={'customerName': request.POST['customerName'],
                                    'customerId': request.POST['customerId'],
                                    'accountId': request.POST['accountId'],
                                    'accountType': request.POST['accountType']
    })
    return render(request, 'issueCheque.html', {'form':form})

def issueCheque(request):
    if request.method == 'POST':
        form = IssueChequeForm(request.POST)
        if form.is_valid():
            chequeAmount = form.cleaned_data.get('chequeAmount')
            ## backend code goes here
            messages.success(request, f'Cheque Issued successfully {chequeAmount}')
            return redirect('./initIssueCheque')

def searchCustomer(request):
    context = {
        'customers' : customers,
        'customerSearchString' : request.POST['customerSearchString']
    }
    if request.POST['context_page']=='deposit':
        return render(request, 'init_fund_deposit.html', context)
    elif request.POST['context_page']=='issue_cheque':
        return render(request, 'init_issue_cheque.html', context)
    elif request.POST['context_page']=='view_customer':
        return render(request, 'init_view_customer.html', context)
    elif request.POST['context_page']=='modify_customer':
        return render(request, 'init_modify_customer.html', context)
    elif request.POST['context_page']=='delete_customer':
        return render(request, 'delete_customer_account.html', context)

def initViewCustomer(request):
    context = {'context_page' : 'view_customer'}
    return render(request, 'init_view_customer.html', context)

def viewCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(initial={'customerName': request.POST['customerName'],
                                    'customerId': request.POST['customerId'],
                                    'accountId': request.POST['accountId'],
                                    'accountType': request.POST['accountType']
        })
        ##Get all customer realted data from database and populate form
        return render(request, 'view_customer.html', {'form':form})

def createCustomer(request):
    return render(request, 'create_customer_account.html')

def initModifyCustomer(request):
    context = {'context_page' : 'modify_customer'}
    return render(request, 'init_modify_customer.html', context)

def modifyCustomerTemplate(request):
    if request.method == 'POST':
        print('inside')
        # populate all customer related data here in the form
        form = CustomerForm(initial={'customerName': request.POST['customerName'],
                                    'customerId': request.POST['customerId'],
                                    'accountId': request.POST['accountId'],
                                    'accountType': request.POST['accountType']
        })
        return render(request, 'modify_customer_template.html',{'form':form})

def modifyCustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        #backend code goes here, save modified form data to db
        return redirect('./initModifyCustomer')

def deleteCustomer(request):
    context = {'context_page' : 'delete_customer'}
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            ## backend code goes here. Code to delete/close customer account
            messages.success(request, f'Customer account deleted successfully')
            return redirect(settings.BASE_URL+'/user_home/home')
        else:
            messages.error(request, f'Failed to delete customer account')
            return redirect(settings.BASE_URL+'/user_home/home')
    else:
        form = CustomerForm()
        return render(request, 'delete_customer_account.html', context)
