from typing import Type

from django.forms import formset_factory, BaseFormSet
from django.http import HttpResponse
from django.shortcuts import render

from treasures.forms import TreasureForm


def treasureform_view(request):
    TreasureFormSet = formset_factory(TreasureForm, extra=2)
    treasure_formset = TreasureFormSet()
    context = {
        'treasure_formset': treasure_formset
    }
    return render(request, 'treasures/treasure_submit.html', context)
