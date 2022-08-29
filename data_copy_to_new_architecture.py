# import lettings
# import profiles
# import oc_lettings_site

"""WARNING: DO NOT RUN THIS SCRIPT (it has already be done)
Some datas will be doubled, this is probably not what you want.
If you go for it anyway, uncomment the code and run it in a django shell:

$ ./manage.py shell < data_copy_to_new_architecture.py

"""

print(
    "This script is not expected to be run twice, you should not do it.\n"
    "If for some reason you have to run it, read it's docstring first, and \n"
    "manually uncomment it's content."
    )

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

# old_profiles = oc_lettings_site.models.OldProfile.objects.all()
# for profile in old_profiles:
#     print(profile.id, profile.favorite_city, profile.user_id)
#     new_profile = profiles.models.Profile(
#         id=profile.id,
#         favorite_city=profile.favorite_city,
#         user_id=profile.user_id
#     )
#     print("new profile :", new_profile.id, new_profile.favorite_city, new_profile.user_id)
#     new_profile.save()

# print("Script executed: copied old architecture's database tables to new database tables")
