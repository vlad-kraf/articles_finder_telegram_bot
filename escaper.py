def escaping(string):
    characters = ('_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!')
    print("".join(["\\" + char if char in characters else char for char in string]))


string = """

Державні ресурси
Багато корисної інформації є на ірландських державних сайтах. Радимо їх читати, дещо, навіть, перекладено українською мовою.
Головний державний сайт https://www.gov.ie/en/campaigns/bc537-irelands-response-to-the-situation-in-ukraine/
Інформація для громадян, резидентів та біженців https://www.citizensinformation.ie/en/moving_country/asylum_seekers_and_refugees/the_asylum_process_in_ireland/coming_to_ireland_from_ukraine.html
Сайт іміграційної служби https://www.irishimmigration.ie/faqs-for-ukraine-nationals-and-residents-of-ukraine/
Сайт ради біженців https://www.irishrefugeecouncil.ie/ukraine-information-note?fbclid=IwAR1m2kXRTluWYSlCCz2fdWErzAH9wrJ6c7jhAzy7Xe7r98tOkO5giMXH-aA
Посольство України в Ірландії  https://ireland.mfa.gov.ua/ 
Сайт Українського Кризового Центру. На ньому вже є безліч інформації для приїжджих до Ірландії, включаючи як, що і де купити, посилання на групи в WhatsApp і канали в Telegram, де ви можете безпосередньо зв'язатися з іншими людьми, які приїхали з України – www.iamukrainian.ie 


"""


escaping(string)