"""Logic for dashboard data query"""

from datetime import date
from typing import Any
from django.db.models import Sum
import budget.logic.queries as queries

__all__ = ["homepage_data"]

def homepage_data(dashboard_date: date|None = None) -> dict[str, Any]:
    """Retrive data from database to generate budget homepage

    Args:
        period (Period): Dashboard period

    Returns:
        dict[str, Any]: context for template
    """
    period = queries.get_period(dashboard_date)
    operations_credit, operations_debit = queries.get_operations_by_period_and_category_sum(period)
    sum_by_credit = operations_credit.aggregate(Sum("spend_by_category", default=0))
    sum_by_debit = operations_debit.aggregate(Sum("get_by_category", default=0))
    context = {
        "operations_credit": operations_credit,
        "operations_debit": operations_debit,
        "spend_all_category": sum_by_credit,
        "get_all_category": sum_by_debit,
        "rest_of_money": sum_by_debit["get_by_category__sum"] - sum_by_credit["spend_by_category__sum"],
        "period_today": period,
    }
    return context