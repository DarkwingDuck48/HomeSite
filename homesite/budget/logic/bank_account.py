from budget.forms import BankAccountForm
from budget.models import BankAccount


def save_bank_account(form: BankAccountForm, user):
    bank_account: BankAccount = form.save(commit=False)
    bank_account.owned_by = user
    bank_account.save()
