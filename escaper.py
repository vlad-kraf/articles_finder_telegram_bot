def escaping(string):
    characters = ('_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!')
    print("".join(["\\" + char if char in characters else char for char in string]))


string = """

Паляниця - центр благодійності в Дубліні, де можна отримати одяг, іграшки та речі першої необхідності БЕЗКОШТОВНО. При вході в магазин перевіряють, коли ви прибули, тому треба мати документ, який підтверджує дату прибуття  - 44 Clarendon Street, D2, Dublin https://goo.gl/maps/kBapwRtvxhhhiu4h6 
ЛімерикSacred Heart Catholic Church
(061) 315 812, https://maps.app.goo.gl/bvim45rFfHSKmRLr7 
До 17:00 в будні, на вихідним - під час служіння. 


"""


escaping(string)