# # favorite_languages = {
# #     "jen": "python",
# #     "sarah":"c",
# #     "edward": "ruby",
# #     "phil":"python",
# # }
# # language = favorite_languages['sarah'].title()
# # print(f'sarahs favorite language is {language}')

# # # for favorite_language in  favorite_languages:
# # #     print(f'Their favorite language is {favorite_languages}')

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "ruby",
#     "phil": "python",
# }

# language = favorite_languages['sarah'].title()
# print(f"sarah's favorite language is {language}")

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}'")

# #Using get() to Access Values
# alien_o = {'color':'green','speed':'slow'}
# point_value = alien_o.get('points','no point value assigned')
# print(point_value)

# Governor = {'first_name':'Blanch', 
#             'Last_name':'Bumeh',
#             'age':"19",
#             'city':'Yaounde'
#             }
# print("first_name:",Governor["first_name"])
# for key, value in Governor.items():
#     print(f"{key.replace('_', ' ').title()}: {value}")

# # for Governor in Governor:
# #     print(Governor.title())

# Favorite_num = {"Blanche": "1",
#                 "Jude": "2",
#                 "Joules": "3",
#                 "Adama": "4",
#                 "Adamou": "5"
#                 }
# for key, value in Favorite_num.items():
#     print(f"{key.replace('_', ' ').title()}: {value}")
# print(f"Blanche favorite numer is:, Favorite_num["Blanche]")

#page 138

#User inputs and while loops
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your name? "
name = input(prompt) 
print(name)

#using int



