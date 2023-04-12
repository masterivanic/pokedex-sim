import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import PokedexCreature

class Command(BaseCommand):
    """
    Create PokedexCreature instances from CSV file
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file_path",
            type=str,
            nargs="?",
            default=os.path.join(settings.BASE_DIR, "csv-data/pokemon.csv"),
        )

    def handle(self, *args, **options):
        csv_file_path = options.get("csv_file_path", None)
        if csv_file_path and csv_file_path.endswith(".csv"):
            with open(csv_file_path, newline="") as csvfile:
                reader = csv.reader(csvfile)
                next(reader, None)

                creatures = [
                    PokedexCreature(
                        name=row[1],
                        type_1=row[2],
                        type_2=row[3],
                        total=int(row[4]),
                        hp=int(row[5]),
                        attack=int(row[6]),
                        defense=int(row[7]),
                        sp_atk=int(row[8]),
                        sp_def=int(row[9]),
                        speed=int(row[10]),
                        generation=int(row[11]),
                        legendary=(row[12] == "True"),
                    )
                    for row in reader
                ]

                PokedexCreature.objects.bulk_create(
                    creatures,
                    batch_size=100,
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Nb of creatures imported to the database: "
                        f"{len(creatures)}."
                    )
                )
        else:
            self.stderr.write(self.style.ERROR("This is not a CSV file."))