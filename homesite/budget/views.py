from django.shortcuts import get_object_or_404, render

from .models import Account, Operation

# Create your views here.
def accounts(request):
    accounts = Account.objects.all()
    context = {
        "accounts": accounts
    }
    return render(request, "budget/accounts.html", context)

def detail_account(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    operations = Operation.objects.all().filter(account = account_id)
    return render(request, "budget/account_detail.html", {"account_id": account_id, "operations": operations})