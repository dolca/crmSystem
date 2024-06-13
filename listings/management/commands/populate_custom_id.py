from django.core.management.base import BaseCommand
from leads.models import IndustrialSpaceLead

class Command(BaseCommand):
    help = 'Populate custom_id for existing IndustrialSpaceLead instances'

    def handle(self, *args, **kwargs):
        leads = IndustrialSpaceLead.objects.all()
        for lead in leads:
            transaction_type = lead.transaction_type
            first_letter = transaction_type[0].upper()
            if first_letter == 'Î':
                first_letter = 'I'
            lead.custom_id = f"{first_letter}SI-{lead.id}"
            lead.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated custom_id for all IndustrialSpaceLead instances'))
