from django.contrib import admin

from .models import *


admin.site.register((Loan,Bank,Candidate,LoanEnquiry))