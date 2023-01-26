from django.contrib import admin

from electronics.models import Product, Company


@admin.action(description='Обнулить задолженность')
def cancel_debt(self, request, queryset):
    queryset.update(debt=0.00)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('hierarchy', 'title', 'country',
                    'city', 'provider', 'debt')
    list_filter =('city', )
    actions = [cancel_debt]

