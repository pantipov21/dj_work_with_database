import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

import slug

class Command(BaseCommand):
	def add_arguments(self, parser):
		pass

	def handle(self, *args, **options):
		with open('phones.csv', 'r') as file:
		    phones = list(csv.DictReader(file, delimiter=';'))
		    print(phones)

		for phone in phones:
			# TODO: Добавьте сохранение модели
			p = Phone(
				name = phone.get('name'),
				image = phone.get('image'),
				price = phone.get('price'),
				release_date = phone.get('release_date'),
				lte_exists = phone.get('lte_exists'),
				slug = slug.slug(phone.get('name'))
			)
			p.save()