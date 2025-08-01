import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from app.models import Commodity

class Command(BaseCommand):
    help = 'Import commodity data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('data/commodity.csv', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['data/commodity.csv']

        
        
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                commodities_to_create = []
                
                with transaction.atomic():
                    for row in reader:
                        # Convert field names from CSV headers to model field names
                        commodity_data = {}
                        for csv_field, value in row.items():
                            # Convert CSV header to model field name
                            model_field = csv_field.lower().replace(',_', '_').replace(' ', '_')
                            
                            # Handle the year field
                            if csv_field == 'Year':
                                commodity_data['year'] = int(value) if value else None
                            else:
                                # Handle float fields
                                if value and value.strip():
                                    try:
                                        commodity_data[model_field] = float(value)
                                    except ValueError:
                                        commodity_data[model_field] = None
                                else:
                                    commodity_data[model_field] = None
                        
                        commodity = Commodity(**commodity_data)
                        commodities_to_create.append(commodity)
                    
                    # Bulk create all commodities
                    Commodity.objects.bulk_create(commodities_to_create, ignore_conflicts=True)
                        
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully imported commodities from {csv_file_path}')
                )
                
        except FileNotFoundError:
            self.stderr.write(
                self.style.ERROR(f'File "{csv_file_path}" not found.')
            )
        except Exception as e:
            self.stderr.write(
                self.style.ERROR(f'Error importing data: {str(e)}')
            )
