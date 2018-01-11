# -*- coding: utf-8 -*-
"""An advanced related items widget for Plone."""

from plone.app.z3cform.widget import RelatedItemsWidget as BaseWidget
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.schema.interfaces import IField


class RelatedItemsWidget(BaseWidget):
    """An advanced related items widget for Plone."""


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def RelatedItemsFieldWidget(field, request, extra=None):
    """An advanced related items widget for Plone."""
    if extra is not None:
        request = extra
    return FieldWidget(field, RelatedItemsWidget(request))
