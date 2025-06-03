import random
import time

# Data lists
COUNTRIES = [
    "Afghanistan", "Albania", "American Samoa", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde (Cape Verde)", "Cambodia", "Cameroon", "Canada", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo", "Costa Rica", "Cote di Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini (Swaziland)", "Ethiopia", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "Gabon", "The Gambia", "Gaza Strip", "Georgia", "Germany", "Ghana", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
    "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
    "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Caledonia", "New Zealand", "Nicaragua", "Niger",
    "Nigeria", "North Macedonia", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
    "Singapore", "Sint Maarten", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", "South Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Virgin Islands",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "West Bank", "Yemen", "Zambia", "Zimbabwe"
]
GENDERS = ["Male", "Female", "Other"]
F_NAMES = ["Sarah", "Maria", "Jannah", "Isabella", "Emma", "Olivia", "Catalina", "Alma", "Valentina", "Sophia", "Mia", "Ava", "Amelia", "Eve", "Lily", "Charlotte", "Alice", "Laura", "Julia", "Luiza", "Chloe", "Aria", "Zoey", "Isidora", "Josefa", "Agustina", "Julieta", "Florencia", "Amanda", "Trinidad", "Mariana", "Luciana", "Gabriela", "Victoria", "Samatha", "Abigail", "Ashley", "Camila", "Martina", "Elena", "Luna", "Hannah", "Leni", "Myra", "Fatima", "Ananya", "Diya", "Kiara", "Aadya", "Renata", "Jimena", "Natalia", "Romina", "Regina", "Antonella", "Rafaela", "Valeria", "Paula", "Carla", "Daniela"]
M_NAMES = ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander", "Jackson", "Sebastian", "Aiden", "Matthew", "Samuel", "David", "Joseph", "John", "Wyatt", "Daniel", "Carter", "Julian", "Luke", "Pedro", "Mohammed", "Ahmed", "Omar", "Adam", "Ibrahim", "Khalid", "Youssef", "Abdullah", "Valentino", "Bruno", "Francisco", "Felipe", "Lorenzo", "Miguel", "Enzo", "Facundo", "Luciano", "Gaspar", "Santiago", "Thiago", "Jeronimo", "Gael", "Dylan", "Jaydan", "Maximiliano", "Jonas", "Finn", "Felix", "Sid", "Advik", "Diego", "Joaquin", "Salvador", "Hugo", "Manuel", "Charles"]
LAST_NAMES = ["Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Lee", "Perez", "Harris", "Robinson", "Walker", "Young", "Allen", "King", "Flores", "Adams", "Nelson", "Torres", "Nguyen", "Green", "Baker", "Rivera", "Campbell", "Carter", "Turner", "Diaz", "Cruz", "Reyes", "Cook", "Rogers", "Ortiz", "Gutierrez", "Morales", "Morris", "Collins", "Cooper", "Ramos", "Kim", "Reed", "Bailey", "Richardson", "Watson", "Mendoza", "Ruiz", "Mendoza", "Hughes", "Gray", "Chavez", "Watson", "Price", "Ross", "Jimenez", "Sanders", "Alvarez", "Castillo"]

# Prompt templates (use {name} and {country})
GOOD_PROMPTS = [
    "{name} wants to celebrate a tradition festival in {country}",
    "{name} wants to eat {country}'s food",
    "{name} is competing in tradition dance competition in {country}",
    "{name} is particating in ancient healing ritual in {country} for emotional damage",
    "{name} is going to a concert in {country}",
    "{name} is going to join a religious order in {country}",
    "{name} is going to see a nation landmark in {country}",
    "{name} is climblin through the exotic mountains in {country}",
    "{name} is swimming in the sought after water of {country}",
    "{name} is treking the rainforest of {country}",
    "{name} is witnessing wildlife in thier homeland of {country}",
    "{name} is viewing the beautiful waterfalls in {country}",
    "{name} is going to the beaches in {country}",
    "{name} is stargazing in {country}",
    "{name} is experiencing the unique weather in {country}",
    "{name} is visiting the ancient ruins in {country}",
    "{name} is exploring the medieval towns of {country}",
    "{name} is exploring an old castle in {country}",
    "{name} is safe in a fortess in {country}",
    "{name} is amazed with the artitecture in {country}",
    "{name} is taking a real history lesson in {country}",
    "{name} is rewalking old forgotten paths in {country}",
    "{name} is visiting an UNESCO world heritage site in {country}",
    "{name} is taking a guided tour in {country}",
    "{name} is in a stellar museum in {country}",
    "{name} is following ancient scrolls in {country}",
    "{name} is riding a hot air ballon in {country}",
    "{name} is sking in {country}",
    "{name} is scuba diving in {country}",
    "{name} is dune bugging in {country}",
    "{name} is river rafting in {country}",
    "{name} is zipling in {country}",
    "{name} is leading a safari in {country}",
    "{name} is hiking in {country}",
    "{name} is deep inside a cave in {country} looking for diamonds",
    "{name} is sand boarding in {country}",
    "{name} is stepping out of there confort zone after smelling the air in {country}",
    "{name} has become more wordly in {country}",
    "{name} has become more patient in {country}",
    "{name} has become more creative in {country}",
    "{name} has discovered new interest in {country}",
    "{name} has finally a friend in {country}",
    "{name} has strongly identified with {country}",
    "{name} has soften his heart in {country}",
    "{name} is no longer anti-social after visiting {country}",
    "{name} taking a short course in {country}",
    "{name} wants to learn a new language in {country}",
    "{name} is attending a workshop in {country}",
    "{name} is visiting a college in {country}",
    "{name} is volunteering in {country}",
    "{name} is on a field trip in {country}",
    "{name} is settling economic affairs in {country}",
    "{name} is visiting a scientific laboratory in {country}",
    "{name} is visiting family in {country}",
    "{name} is going to a friends wedding in {country}",
    "{name} is going to a comedy show in {country}",
    "{name} is going to settle diplomatic matters in {country}",
    "{name} is see what {country} is about",
    "{name} is going to a retreat in {country}",
    "{name} is finding solitude in {country}",
    "{name} is doing a digital detox in {country}",
    "{name} is escaping the hustle culture in {country}",
    "{name} is visiting sacred sites in {country}",
    "{name} is taking piligrimage in {country}",
    "{name} is relaxing in a hot spring in {country}",
    "{name} is doing nothing in {country}",
    "{name} is fast asleep under the stars in {country}",
    "{name} is relaxing in {country}",
    "{name}is visitng an art gallery in {country}",
    "{name} is going to street art expo in {country}",
    "{name} is going to the theather in {country}",
    "{name} is taking photos in {country}",
    "{name} collecting rare souvenirs in {country}",
    "{name} is riding a train in {country}",
    "{name} is taking a boat ride in {country}",
    "{name} is going on a cruise in {country}",
    "{name} is going on a road trip in {country}",
    "{name} is going on a bike ride in {country}",
    "{name} is going to party in {country}",
    "{name} is going to a festival in {country}",
    "{name} is going to a parade in {country}",
    "{name} is going to a fair in {country}",
    "{name} is going to a carnival in {country}",
    "{name} is going to celebrate life in {country}",
    "{name} is going to {country} just beacuse they can"
]
BAD_PROMPTS = [
    "{name} is fleeing war in {country}",
    "{name} is seeking asylum escaping {country}",
    "{name} is escaping genocide in {country}",
    "{name} is avoiding military service in {country}",
    "{name} is escaping escalading terrorist aggression in {country}",
    "{name} is fleeing from a gang in {country}",
    "{name} is scared of the political collapse in {country}",
    "{name} is hiding from thier abusive partner in {country}",
    "{name} is hiding from the {country} government",
    "{name} is avoiding military service in {country}",
    "{name} has been deported to {country}",
    "{name} has been exiled to {country}",
    "{name} is seeking fair trial in {country}",
    "{name} is avoiding jail time in {country}",
    "{name} is seeking a fair trial in {country}",
    "{name} is recieving witness protection in {country}",
    "{name} has loss thier citizenship in {country}",
    "{name} has been forced to relocate {country}",
    "{name} is being religiously persecuted in {country}",
    "{name} is being sexually persecuted in {country}",
    "{name} is being politically persecuted in {country}",
    "{name} is escaping poverty in {country}",
    "{name} is desperately searching for working in {country}",
    "{name} is leaving a hyberinflated {country}",
    "{name}'s business has failed in {country}",
    "{name} has been displaced in {country}",
    "{name} has been scammed in {country}",
    "{name} has been tricked into a bad contract in {country}",
    "{name} has fallen into debt in {country}",
    "{name} is in need of medical attention in {country}",
    "{name} has been diagosted of a chronic diease in {country}",
    "{name} is escaping a deadly diasese in {country}",
    "{name} is seeking mental health help in {country}",
    "{name} is seeking clean water in {country}",
    "{name} is hungry and seeking food in {country}",
    "{name} is seeking justice after neglected in {country}",
    "{name} was a victim of medical abuse in {country}",
    "{name} is going inland due to rising shores levels in {country}",
    "{name} is evacuating to a wild fire in {country}",
    "{name} has been displaced due to a natural diaster in {country}",
    "{name} has been a victim of a large earthquake in {country}",
    "{name} is fleeing the aftermath of a nuclear diaster in {country}",
    "{name} is avoiding an oil spill in {country}",
    "{name} has escaped an refugee camp in {country}",
    "{name} has been seperated from thier family in {country}",
    "{name} is going to a funeral in {country}",
    "{name} is visited an imprisioned friend in {country}",
    "{name} is looking for a missing friend in {country}",
    "{name} is undocumented in {country}",
    "{name} is legal stranded in {country}",
    "{name} was trafficated in {country}",
    "{name} was sexually abused in {country}",
    "{name} was physically abused in {country}",
    "{name} was emotionally abused in {country}",
    "{name} was promised a job in {country} but it was a scam",
    "{name} was promised a better life in {country} but it was a scam",
    "{name} was promised a better future in {country} but it was a scam",
    "{name} was promised a better education in {country} but it was a scam",
    "{name} was promised a better health care in {country} but it was a scam",
    "{name} was promised a visa in {country} but it was a scam",
    "{name} is being oppressed in {country}",
    "{name} is being discriminated in {country}",
    "{name} is being racially profiled in {country}",
    "{name} is being harassed in {country}",
    "{name} is being bullied in {country}",
    "{name} is being stalked in {country}",
    "{name} is being threatened in {country}",
    "{name} is being extorted in {country}",
    "{name} is being blackmailed in {country}",
    "{name} is lonely in {country}",
    "{name} is depressed in {country}",
    "{name} is anxious in {country}",
    "{name} is stressed in {country}",
    "{name} is overwhelmed in {country}",
    "{name} is homesick in {country}",
    "{name} is culture shocked in {country}",
    "{name} is feeling lost in {country}",
    "{name} is feeling isolated in {country}",
    "{name} is feeling disconnected in {country}",
    "{name} is feeling out of place in {country}",
    "{name} is feeling like a stranger in {country}",
    "{name} is feeling like an outsider in {country}",
    "{name} is feeling like a foreigner in {country}",
    "{name} is feeling like a tourist in {country}",
    "{name} is feeling like a refugee in {country}",
    "{name} is feeling brain washed in {country}",
    "{name} is feeling like a victim in {country}",
    "{name} is feeling like an unworthy survivor in {country}",
    "{name} is feeling like a failure in {country}",
    "{name} is feeling like a burden in {country}",
    "{name} is feeling like a liability in {country}",
    "{name} is feeling like a problem in {country}",
    "{name} is feeling like a nuisance in {country}",
    "{name} is forced to stop studying in {country}",
    "{name} is forced to stop working in {country}",
    "{name} is forced to stop living in {country}",
    "{name} is forced to stop dreaming in {country}",
    "{name} is forced to stop hoping in {country}",
    "{name} is forced to stop believing in {country}",
    "{name} is forced to stop loving in {country}",
    "{name} is forced to stop caring in {country}",
    "{name} is forced to stop being in {country}",
    "home for {name} is no longer {country}",
    "{name} is no longer welcome in {country}",
    "{name} is no longer safe in {country}",
    "{name} is no longer free in {country}",
    "{name} is no longer happy in {country}",
    "{name} is no longer healthy in {country}",
    "{name} is culturally displaced in {country}",
    "{name} is economically displaced in {country}",
    "{name} is socially displaced in {country}",
    "{name} is emotionally displaced in {country}",
    "{name} is spiritually displaced in {country}",
    "{name} is physically displaced in {country}",
    "{name} is mentally displaced in {country}",
    "{name} is existentially displaced in {country}",
    "{name} is displaced in {country}",
    "{name} is hiding thier true self in {country}",
    "{name} is hiding thier true identity in {country}",
    "{name} is hiding thier true feelings in {country}",
    "{name} is hiding thier true thoughts in {country}",
    "{name} is hiding thier true intentions in {country}",
    "{name} is hiding thier true desires in {country}",
    "{name} is hiding thier true needs in {country}",
    "{name} is hiding thier true wants in {country}",
    "{name} is hiding thier true dreams in {country}",
    "{name} is hiding thier true hopes in {country}",
    "{name} is hiding thier true beliefs in {country}",
    "{name} is hiding thier true values in {country}",
    "{name} is hiding thier true morals in {country}",
    "{name} is hiding thier true ethics in {country}",
    "{name} is hiding thier true principles in {country}",
    "{name} is hiding thier true standards in {country}",
    "{name} is hiding thier true expectations in {country}",
    "{name} is hiding thier true reality in {country}",
    "{name} is hiding thier true perception in {country}",
    "{name} is only travelling to {country} to escape thier problems at home",
    "{name} is only travelling to {country} to avoid facing thier issues",
    "{name} is only travelling to {country} to run away from thier responsibilities",
    "{name} is only travelling to {country} to avoid dealing with thier emotions",
    "{name} is only travelling to {country} to avoid confronting thier fears",
    "{name} is only travelling to {country} to avoid facing thier past",
    "{name} is only travelling to {country} to avoid dealing with thier future",
    "{name} is only travelling to {country} to avoid facing thier present",
    "{name} is only travelling to {country} to avoid dealing with thier reality",
    "{name} is only travelling to {country} to avoid facing thier truth",
    "{name} is only travelling to {country} to avoid dealing with thier authenticity",
    "{name} is only travelling to {country} to avoid facing thier integrity",
    "{name} is only travelling to {country} to avoid dealing with thier honesty",
    "{name} is only travelling to {country} to avoid facing thier vulnerability",
    "{name} is only travelling to {country} to avoid dealing with thier shame",
    "{name} is only travelling to {country} to avoid facing thier guilt",
    "{name} is only travelling to {country} to avoid dealing with thier regret",
    "{name} is only travelling to {country} to avoid facing thier grief",
    "{name} is only travelling to {country} to avoid dealing with thier loss",
    "{name} is only travelling to {country} to avoid facing thier trauma",
    "{name} is only travelling to {country} to avoid dealing with thier pain",
    "{name} is only travelling to {country} to avoid facing thier suffering",
    "{name} is only travelling to {country} to avoid dealing with thier challenges",
    "{name} is only travelling to {country} to avoid facing thier obstacles",
    "{name} is only travelling to {country} to avoid dealing with thier difficulties",
    "{name} is only travelling to {country} to avoid facing thier struggles",
    "{name} is only travelling to {country} to avoid dealing with thier hardships",
    "{name} is only travelling to {country} to avoid facing thier adversities",
    "{name} is only travelling to {country} to avoid dealing with thier conflicts",
    "{name} is only travelling to {country} to avoid facing thier crises",
    "{name} is only travelling to {country} to avoid dealing with thier emergencies",
    "{name} is only travelling to {country} to avoid facing thier disasters",
    "{name} is only travelling to {country} to avoid dealing with thier catastrophes",
    "{name} is only travelling to {country} to avoid facing thier tragedies",
    "{name} is only travelling to {country} to avoid dealing with thier misfortunes",
    "{name} is only travelling to {country} to avoid facing thier failures",
    "{name} is only travelling to {country} since they have no home"
]
LAST_PROMPTS = ["Oof you lost"]

PROMPT_TYPES = [1, 0, -1]
PROMPT_WEIGHTS = [0.72, 0.275, 0.005]  # [good, bad, last]

# Utility functions
def generate_name():
    gender = random.choice(GENDERS)
    if gender == 'Female':
        first = random.choice(F_NAMES)
    elif gender == 'Male':
        first = random.choice(M_NAMES)
    else:
        first = random.choice(F_NAMES + M_NAMES)
    last = random.choice(LAST_NAMES)
    return f"{first} {last}", gender

def get_prompt(name, country):
    prompt_type = random.choices(PROMPT_TYPES, weights=PROMPT_WEIGHTS, k=1)[0]
    if prompt_type == 1:
        prompt = random.choice(GOOD_PROMPTS).format(name=name, country=country)
    elif prompt_type == 0:
        prompt = random.choice(BAD_PROMPTS).format(name=name, country=country)
    else:
        prompt = random.choice(LAST_PROMPTS)
    return prompt, prompt_type

def loading_screen():
    intro = ['L','O','A','D','I','N','G','!']
    for i, char in enumerate(intro):
        print(' ' * i, char, ' ')
        time.sleep(0.25)

def main():
    loading_screen()
    print("\nWelcome to the World Game!\n")
    print("Your goal is to travel the entire world while surviving\n")
    print("Disclaimer: All name, situations, or concidences are entirly incidental and non-intented.\nProceed at your own risk!\n")

    name, gender = generate_name()
    age = random.randint(18, 100)
    countries = COUNTRIES.copy()
    random.shuffle(countries)
    visited = []
    unvisited = countries.copy()
    day = 0
    go = True

    print(f"Your Country: {countries[0]}\tName: {name}\tGender: {gender}\tAge: {age}")

    while go and unvisited:
        print(f"\nDay: {day}")
        country = unvisited.pop(0)
        visited.append(country)
        print(f"You are in {country}")
        prompt, prompt_type = get_prompt(name, country)
        if prompt_type == -1:
            go = False
            percent = (len(visited) / len(COUNTRIES)) * 100
            print(f"You made it to: {percent:.2f}%")
            print(f"Countries left: {len(unvisited)}")
            break
        time.sleep(1.5)
        print(f"\n{prompt}\n")
        while True:
            next_day = input(" Enter 'n' to continue to...")
            if next_day.lower() == 'n':
                day += 1
                break
        if not unvisited:
            print("Congratulations! You have visited all countries! Surviving all the things of the world!")
            go = False

if __name__ == "__main__":
    main()