import lettings
import oc_lettings_site


# old_addresses = oc_lettings_site.models.Address.objects.all()

# for address in old_addresses:
#     new = lettings.models.Address(
#         number=address.number,
#         street=address.street,
#         city=address.city,
#         state=address.state,
#         zip_code=address.zip_code,
#         country_iso_code=address.country_iso_code
#         )
#     new.save()

# old_lettings = oc_lettings_site.models.Letting.objects.all()

# for letting in old_lettings:
#     new_adress = lettings.models.Address.objects.get(id=letting.id)
#     new = lettings.models.Letting(
#         title=letting.title,
#         address=new_adress,
#     )
#     new.save()

print("Script executed: copied old architecture's database tables to new database tables")
