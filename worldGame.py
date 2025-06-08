import random
import time
from playsound import playsound

# lists
countries = ["Afghanistan","Albania","American Samoa","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi",
    "Cabo Verde (Cape Verde)","Cambodia","Cameroon","Canada","Cayman Islands","Central African Republic","Chad","Chile","China","Colombia","Comoros","Democratic Republic of the Congo","Republic of the Congo","Costa Rica","Cote di Ivoire","Croatia","Cuba","Curacao","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor (Timor-Leste)","Ecuador","Egypt","El Salvador","Equatorial Guinea",
    "Eritrea","Estonia","Eswatini (Swaziland)","Ethiopia","Faroe Islands","Fiji","Finland","France","French Guiana","French Polynesia","Gabon","The Gambia","Gaza Strip","Georgia","Germany","Ghana","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq",
    "Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","North Korea","South Korea","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon",
    "Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Caledonia","New Zealand","Nicaragua","Niger",
    "Nigeria","North Macedonia","Northern Mariana Islands","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone",
    "Singapore","Sint Maarten","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka","Sudan","South Sudan","Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","United States Virgin Islands",
    "Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","West Bank","Yemen","Zambia","Zimbabwe"]

genders = ["Male", "Female","Other"]
fNames = ["Sarah","Maria","Jannah","Isabella","Emma","Olivia","Catalina","Alma","Valentina","Sophia","Mia","Ava","Amelia","Eve","Lily","Charlotte","Alice","Laura","Julia","Luiza","Chloe","Aria","Zoey","Isidora","Josefa","Agustina","Julieta","Florencia","Amanda","Trinidad","Mariana","Luciana","Gabriela","Victoria","Samatha","Abigail","Ashley","Camila","Martina","Elena","Luna","Hannah","Leni","Myra","Fatima","Ananya","Diya","Kiara","Aadya","Renata","Jimena","Natalia","Romina","Regina","Antonella","Rafaela","Valeria","Paula","Carla","Daniela"]
mNames = ["Liam","Noah","Oliver","Elijah","James","William","Benjamin","Lucas","Henry","Alexander","Jackson","Sebastian","Aiden","Matthew","Samuel","David","Joseph","John","Wyatt","Daniel","Carter","Julian","Luke","Pedro","Mohammed","Ahmed","Omar","Adam","Ibrahim","Khalid","Youssef","Abdullah","Valentino","Bruno","Francisco","Felipe","Lorenzo","Miguel","Enzo","Facundo","Luciano","Gaspar","Santiago","Thiago","Jeronimo","Gael","Dylan","Jaydan","Maximiliano","Jonas","Finn","Felix","Sid","Advik","Diego","Joaquin","Salvador","Hugo","Manuel","Charles"]
lastNames = ["Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Lee","Perez","Harris","Robinson","Walker","Young","Allen","King","Flores","Adams","Nelson","Torres","Nguyen","Green","Baker","Rivera","Campbell","Carter","Turner","Diaz","Cruz","Reyes","Cook","Rogers","Ortiz","Gutierrez","Morales","Morris","Collins","Cooper","Ramos","Kim","Reed","Bailey","Richardson","Watson","Mendoza","Ruiz","Mendoza","Hughes","Gray","Chavez","Watson","Price","Ross","Jimenez","Sanders","Alvarez","Castillo"]

# prompts
goodPrompts = [
    "{name} wants to celebrate a tradition festival in {country}", "{name} wants to eat {country}'s food", "{name} is competing in tradition dance competition in {country}", "{name} is particating in ancient healing ritual in {country} for emotional damage", "{name} is going to a concert in {country}",
    "{name} is going to join a religious order in {country}", "{name} is going to see a nation landmark in {country}", "{name} is climblin through the exotic mountains in {country}", "{name} is swimming in the sought after water of {country}", "{name} is treking the rainforest of {country}",
    "{name} is witnessing wildlife in thier homeland of {country}", "{name} is viewing the beautiful waterfalls in {country}", "{name} is going to the beaches in {country}", "{name} is stargazing in {country}", "{name} is experiencing the unique weather in {country}",
    "{name} is visiting the ancient ruins in {country}", "{name} is exploring the medieval towns of {country}", "{name} is exploring an old castle in {country}", "{name} is safe in a fortess in {country}", "{name} is amazed with the artitecture in {country}",
    "{name} is taking a real history lesson in {country}", "{name} is rewalking old forgotten paths in {country}", "{name} is visiting an UNESCO world heritage site in {country}", "{name} is taking a guided tour in {country}", "{name} is in a stellar museum in {country}",
    "{name} is following ancient scrolls in {country}", "{name} is riding a hot air ballon in {country}", "{name} is sking in {country}", "{name} is scuba diving in {country}", "{name} is dune bugging in {country}",
    "{name} is river rafting in {country}", "{name} is zipling in {country}", "{name} is leading a safari in {country}", "{name} is hiking in {country}", "{name} is deep inside a cave in {country} looking for diamonds",
    "{name} is sand boarding in {country}", "{name} is stepping out of there confort zone after smelling the air in {country}", "{name} has become more wordly in {country}", "{name} has become more patient in {country}", "{name} has become more creative in {country}",
    "{name} has discovered new interest in {country}", "{name} has finally a friend in {country}", "{name} has strongly identified with {country}", "{name} has soften his heart in {country}", "{name} is no longer anti-social after visiting {country}",
    "{name} taking a short course in {country}", "{name} wants to learn a new language in {country}", "{name} is attending a workshop in {country}", "{name} is visiting a college in {country}", "{name} is volunteering in {country}",
    "{name} is on a field trip in {country}", "{name} is settling economic affairs in {country}", "{name} is visiting a scientific laboratory in {country}", "{name} is visiting family in {country}", "{name} is going to a friends wedding in {country}",
    "{name} is going to a comedy show in {country}", "{name} is going to settle diplomatic matters in {country}", "{name} is see what {country} is about", "{name} is going to a retreat in {country}", "{name} is finding solitude in {country}",
    "{name} is doing a digital detox in {country}", "{name} is escaping the hustle culture in {country}", "{name} is visiting sacred sites in {country}", "{name} is taking piligrimage in {country}", "{name} is relaxing in a hot spring in {country}",
    "{name} is doing nothing in {country}", "{name} is fast asleep under the stars in {country}", "{name} is relaxing in {country}", "{name}is visitng an art gallery in {country}", "{name} is going to street art expo in {country}",
    "{name} is going to the theather in {country}", "{name} is taking photos in {country}", "{name} collecting rare souvenirs in {country}", "{name} is riding a train in {country}", "{name} is taking a boat ride in {country}",
    "{name} is going on a cruise in {country}", "{name} is going on a road trip in {country}", "{name} is going on a bike ride in {country}", "{name} is going to party in {country}", "{name} is going to a festival in {country}",
    "{name} is going to a parade in {country}", "{name} is going to a fair in {country}", "{name} is going to a carnival in {country}", "{name} is going to celebrate life in {country}", "{name} is going to {country} just beacuse they can",
    "{name} is learning to cook a traditional dish in {country}", "{name} is painting a landscape in {country}", "{name} is making new friends at a local market in {country}", "{name} is attending a music festival in {country}", "{name} is taking a scenic train ride across {country}",
    "{name} is participating in a local sports event in {country}", "{name} is enjoying a sunrise hike in {country}", "{name} is writing poetry inspired by {country}", "{name} is learning traditional crafts in {country}", "{name} is joining a community celebration in {country}",
    "{name} is photographing ancient architecture in {country}", "{name} is studying indigenous art forms in {country}", "{name} is tasting award-winning wines in {country}", "{name} is participating in a traditional tea ceremony in {country}", "{name} is learning folk dances from locals in {country}",
    "{name} is exploring hidden caves in {country}", "{name} is participating in a spiritual retreat in {country}", "{name} is observing rare astronomical events in {country}", "{name} is visiting a chocolate factory in {country}", "{name} is joining a cooking class in {country}",
    "{name} is taking a hot air balloon ride over {country}", "{name} is joining an archaeological dig in {country}", "{name} is visiting an organic farm in {country}", "{name} is attending a traditional wedding in {country}", "{name} is watching artisans create traditional crafts in {country}",
    "{name} is learning about sustainable practices in {country}", "{name} is walking through flower fields in {country}", "{name} is sampling street food in {country}", "{name} is tracking wildlife with a local guide in {country}", "{name} is helping with a community garden project in {country}",
    "{name} is exploring underwater reefs in {country}", "{name} is watching a traditional theatrical performance in {country}", "{name} is visiting a butterfly sanctuary in {country}", "{name} is learning traditional fishing techniques in {country}", "{name} is attending a film festival in {country}",
    "{name} is exploring ancient libraries in {country}", "{name} is listening to local folk music in {country}", "{name} is participating in a local harvest festival in {country}", "{name} is learning traditional weaving in {country}", "{name} is studying medicinal plants with locals in {country}",
    "{name} is collecting seashells on the beaches of {country}", "{name} is riding horses through the countryside of {country}", "{name} is attending a literature festival in {country}", "{name} is watching migratory birds in {country}", "{name} is learning about local legends in {country}",
    "{name} is participating in a traditional soap making workshop in {country}", "{name} is visiting a flower market in {country}", "{name} is star-gazing in a dark sky reserve in {country}", "{name} is joining a bamboo rafting adventure in {country}", "{name} is visiting a tea plantation in {country}",
    "{name} is learning traditional pottery in {country}", "{name} is watching a puppet show in {country}", "{name} is participating in a lantern festival in {country}", "{name} is exploring botanical gardens in {country}", "{name} is attending a classical music concert in {country}",
    "{name} is learning about sustainable architecture in {country}", "{name} is taking a culinary tour in {country}", "{name} is visiting a traditional paper making workshop in {country}", "{name} is joining a bird watching expedition in {country}", "{name} is participating in a traditional boat race in {country}",
    "{name} is observing local artisans at work in {country}", "{name} is taking a photography workshop in {country}", "{name} is watching a traditional dance performance in {country}", "{name} is exploring local markets in {country}", "{name} is participating in a wine tasting tour in {country}",
    "{name} is learning about traditional medicine in {country}", "{name} is visiting ancient monasteries in {country}", "{name} is attending a poetry reading in {country}", "{name} is exploring coral reefs in {country}", "{name} is visiting a traditional textile mill in {country}",
    "{name} is learning calligraphy in {country}", "{name} is watching a meteor shower in {country}", "{name} is exploring historic neighborhoods in {country}", "{name} is learning about sustainable fishing in {country}", "{name} is attending a cheese making workshop in {country}",
    "{name} is visiting a butterfly farm in {country}", "{name} is taking a permaculture workshop in {country}", "{name} is exploring abandoned castles in {country}", "{name} is attending a honey harvesting festival in {country}", "{name} is watching glass blowers at work in {country}",
    "{name} is visiting a traditional family home in {country}", "{name} is learning about local conservation efforts in {country}", "{name} is attending a cultural exchange program in {country}", "{name} is exploring ancient forest trails in {country}", "{name} is participating in a traditional bread making class in {country}",
    "{name} is visiting a local artist's studio in {country}", "{name} is learning traditional musical instruments in {country}", "{name} is attending a storytelling festival in {country}", "{name} is exploring historic lighthouses in {country}", "{name} is learning about sustainable energy solutions in {country}",
    "{name} is visiting a traditional fishing village in {country}", "{name} is attending a flower arrangement workshop in {country}", "{name} is exploring historic bridges in {country}", "{name} is learning about local coffee production in {country}", "{name} is attending a traditional healing ceremony in {country}",
    "{name} is exploring glacier caves in {country}", "{name} is visiting a traditional farm in {country}", "{name} is learning about local textile traditions in {country}", "{name} is attending a chocolate making workshop in {country}", "{name} is exploring ancient irrigation systems in {country}",
    "{name} is watching traditional gold panning in {country}", "{name} is visiting a local perfumery in {country}", "{name} is learning about ancient astronomy in {country}", "{name} is attending a traditional music festival in {country}", "{name} is exploring hidden waterfalls in {country}",
    "{name} is visiting a local pottery studio in {country}", "{name} is learning about traditional boat building in {country}", "{name} is attending a traditional food festival in {country}", "{name} is exploring ancient trade routes in {country}", "{name} is watching traditional blacksmiths at work in {country}",
    "{name} is visiting a local spice market in {country}", "{name} is learning about traditional beekeeping in {country}", "{name} is attending an underwater concert in {country}", "{name} is participating in a zero-gravity experience in {country}", "{name} is researching bioluminescent organisms in {country}",
    "{name} is documenting endangered languages in {country}", "{name} is sampling molecular gastronomy in {country}", "{name} is learning ancient fire-making techniques in {country}", "{name} is staying in an ice hotel in {country}", "{name} is foraging for rare edible plants in {country}",
    "{name} is participating in a silent retreat in {country}", "{name} is learning to make traditional musical instruments in {country}", "{name} is studying ancient star maps in {country}", "{name} is attending a holographic art exhibition in {country}", "{name} is participating in extreme weather chasing in {country}",
    "{name} is creating land art in the desert of {country}", "{name} is learning traditional perfume making in {country}", "{name} is staying in a treehouse village in {country}", "{name} is studying ancient mathematics systems in {country}", "{name} is learning the art of fermentation in {country}",
    "{name} is observing a total solar eclipse in {country}", "{name} is documenting oral storytelling traditions in {country}"
]
                
badPrompts = [
    "{name} is fleeing war in {country}", "{name} is seeking asylum escaping {country}", "{name} is escaping genocide in {country}", "{name} is avoiding military service in {country}", "{name} is escaping escalading terrorist aggression in {country}",
    "{name} is fleeing from a gang in {country}", "{name} is scared of the political collapse in {country}", "{name} is hiding from thier abusive partner in {country}", "{name} is hiding from the {country} government", "{name} is avoiding military service in {country}",
    "{name} has been deported to {country}", "{name} has been exiled to {country}", "{name} is seeking fair trial in {country}", "{name} is avoiding jail time in {country}", "{name} is seeking a fair trial in {country}",
    "{name} is recieving witness protection in {country}", "{name} has loss thier citizenship in {country}", "{name} has been forced to relocate {country}", "{name} is being religiously persecuted in {country}", "{name} is being sexually persecuted in {country}",
    "{name} is being politically persecuted in {country}", "{name} is escaping poverty in {country}", "{name} is desperately searching for working in {country}", "{name} is leaving a hyberinflated {country}", "{name}'s business has failed in {country}",
    "{name} has been displaced in {country}", "{name} has been scammed in {country}", "{name} has been tricked into a bad contract in {country}", "{name} has fallen into debt in {country}", "{name} is in need of medical attention in {country}",
    "{name} has been diagosted of a chronic diease in {country}", "{name} is escaping a deadly diasese in {country}", "{name} is seeking mental health help in {country}", "{name} is seeking clean water in {country}", "{name} is hungry and seeking food in {country}",
    "{name} is seeking justice after neglected in {country}", "{name} was a victim of medical abuse in {country}", "{name} is going inland due to rising shores levels in {country}", "{name} is evacuating to a wild fire in {country}", "{name} has been displaced due to a natural diaster in {country}",
    "{name} has been a victim of a large earthquake in {country}", "{name} is fleeing the aftermath of a nuclear diaster in {country}", "{name} is avoiding an oil spill in {country}", "{name} has escaped an refugee camp in {country}", "{name} has been seperated from thier family in {country}",
    "{name} is going to a funeral in {country}", "{name} is visited an imprisioned friend in {country}", "{name} is looking for a missing friend in {country}", "{name} is undocumented in {country}", "{name} is legal stranded in {country}",
    "{name} was trafficated in {country}", "{name} was sexually abused in {country}", "{name} was physically abused in {country}", "{name} was emotionally abused in {country}", "{name} was promised a job in {country} but it was a scam",
    "{name} was promised a better life in {country} but it was a scam", "{name} was promised a better future in {country} but it was a scam", "{name} was promised a better education in {country} but it was a scam", "{name} was promised a better health care in {country} but it was a scam", "{name} was promised a visa in {country} but it was a scam",
    "{name} is being oppressed in {country}", "{name} is being discriminated in {country}", "{name} is being racially profiled in {country}", "{name} is being harassed in {country}", "{name} is being bullied in {country}",
    "{name} is being stalked in {country}", "{name} is being threatened in {country}", "{name} is being extorted in {country}", "{name} is being blackmailed in {country}", "{name} is lonely in {country}",
    "{name} is depressed in {country}", "{name} is anxious in {country}", "{name} is stressed in {country}", "{name} is overwhelmed in {country}", "{name} is homesick in {country}",
    "{name} is culture shocked in {country}", "{name} is feeling lost in {country}", "{name} is feeling isolated in {country}", "{name} is feeling disconnected in {country}", "{name} is feeling out of place in {country}",
    "{name} is feeling like a stranger in {country}", "{name} is feeling like an outsider in {country}", "{name} is feeling like a foreigner in {country}", "{name} is feeling like a tourist in {country}", "{name} is feeling like a refugee in {country}",
    "{name} is feeling brain washed in {country}", "{name} is feeling like a victim in {country}", "{name} is feeling like an unworthy survivor in {country}", "{name} is feeling like a failure in {country}", "{name} is feeling like a burden in {country}",
    "{name} is feeling like a liability in {country}", "{name} is feeling like a problem in {country}", "{name} is feeling like a nuisance in {country}", "{name} is forced to stop studying in {country}", "{name} is forced to stop working in {country}",
    "{name} is forced to stop living in {country}", "{name} is forced to stop dreaming in {country}", "{name} is forced to stop hoping in {country}", "{name} is forced to stop believing in {country}", "{name} is forced to stop loving in {country}",
    "{name} is forced to stop caring in {country}", "{name} is forced to stop being in {country}", "home for {name} is no longer {country}", "{name} is no longer welcome in {country}", "{name} is no longer safe in {country}",
    "{name} is no longer free in {country}", "{name} is no longer happy in {country}", "{name} is no longer healthy in {country}", "{name} is culturally displaced in {country}", "{name} is economically displaced in {country}",
    "{name} is socially displaced in {country}", "{name} is emotionally displaced in {country}", "{name} is spiritually displaced in {country}", "{name} is physically displaced in {country}", "{name} is mentally displaced in {country}",
    "{name} is existentially displaced in {country}", "{name} is displaced in {country}", "{name} is hiding thier true self in {country}", "{name} is hiding thier true identity in {country}", "{name} is hiding thier true feelings in {country}",
    "{name} is hiding thier true thoughts in {country}", "{name} is hiding thier true intentions in {country}", "{name} is hiding thier true desires in {country}", "{name} is hiding thier true needs in {country}", "{name} is hiding thier true wants in {country}",
    "{name} is hiding thier true dreams in {country}", "{name} is hiding thier true hopes in {country}", "{name} is hiding thier true beliefs in {country}", "{name} is hiding thier true values in {country}", "{name} is hiding thier true morals in {country}",
    "{name} is hiding thier true ethics in {country}", "{name} is hiding thier true principles in {country}", "{name} is hiding thier true standards in {country}", "{name} is hiding thier true expectations in {country}", "{name} is hiding thier true reality in {country}",
    "{name} is hiding thier true perception in {country}", "{name} is only travelling to {country} to escape thier problems at home", "{name} is only travelling to {country} to avoid facing thier issues", "{name} is only travelling to {country} to run away from thier responsibilities", "{name} is only travelling to {country} to avoid dealing with thier emotions",
    "{name} is only travelling to {country} to avoid confronting thier fears", "{name} is only travelling to {country} to avoid facing thier past", "{name} is only travelling to {country} to avoid dealing with thier future", "{name} is only travelling to {country} to avoid facing thier present", "{name} is only travelling to {country} to avoid dealing with thier reality",
    "{name} is only travelling to {country} to avoid facing thier truth", "{name} is only travelling to {country} to avoid dealing with thier authenticity", "{name} is only travelling to {country} to avoid facing thier integrity", "{name} is only travelling to {country} to avoid dealing with thier honesty", "{name} is only travelling to {country} to avoid facing thier vulnerability",
    "{name} is only travelling to {country} to avoid dealing with thier shame", "{name} is only travelling to {country} to avoid facing thier guilt", "{name} is only travelling to {country} to avoid dealing with thier regret", "{name} is only travelling to {country} to avoid facing thier grief", "{name} is only travelling to {country} to avoid dealing with thier loss",
    "{name} is only travelling to {country} to avoid facing thier trauma", "{name} is only travelling to {country} to avoid dealing with thier pain", "{name} is only travelling to {country} to avoid facing thier suffering", "{name} is only travelling to {country} to avoid dealing with thier challenges", "{name} is only travelling to {country} to avoid facing thier obstacles",
    "{name} is only travelling to {country} to avoid dealing with thier difficulties", "{name} is only travelling to {country} to avoid facing thier struggles", "{name} is only travelling to {country} to avoid dealing with thier hardships", "{name} is only travelling to {country} to avoid facing thier adversities", "{name} is only travelling to {country} to avoid dealing with thier conflicts",
    "{name} is only travelling to {country} to avoid facing thier crises", "{name} is only travelling to {country} to avoid dealing with thier emergencies", "{name} is only travelling to {country} to avoid facing thier disasters", "{name} is only travelling to {country} to avoid dealing with thier catastrophes", "{name} is only travelling to {country} to avoid facing thier tragedies",
    "{name} is only travelling to {country} to avoid dealing with thier misfortunes", "{name} is only travelling to {country} to avoid facing thier failures", "{name} is only travelling to {country} since they have no home", "{name} is struggling to find shelter in {country}", "{name} is facing language barriers in {country}",
    "{name} is caught in a bureaucratic nightmare in {country}", "{name} is stranded due to a transportation strike in {country}", "{name} is dealing with a lost passport in {country}", "{name} is facing unexpected medical expenses in {country}", "{name} is caught in a severe storm in {country}",
    "{name} is experiencing culture shock in {country}", "{name} is struggling with homesickness in {country}", "{name} is facing discrimination as a foreigner in {country}", "{name} is being followed by suspicious people in {country}", "{name} is trapped in a legal dispute in {country}",
    "{name} is unable to access their bank account in {country}", "{name} is living in a temporary shelter in {country}", "{name} is suffering from food poisoning in {country}", "{name} is harassed by corrupt officials in {country}", "{name} is separated from their travel group in {country}",
    "{name} is stuck with expired documentation in {country}", "{name} is struggling with extreme weather conditions in {country}", "{name} is facing hostility from locals in {country}", "{name} is lost in an unfamiliar city in {country}", "{name} is robbed of their belongings in {country}",
    "{name} is unable to find medication in {country}", "{name} is mistaken for someone else by authorities in {country}", "{name} is having difficulty communicating in {country}", "{name} is being overcharged for basic services in {country}", "{name} is caught in political unrest in {country}",
    "{name} is suffering from altitude sickness in {country}", "{name} is struggling with local customs in {country}", "{name} is fighting for their rights in {country}", "{name} is caught in a false accusation in {country}", "{name} is having trouble finding safe drinking water in {country}",
    "{name} is facing unexpected travel restrictions in {country}", "{name} is living in fear of violence in {country}", "{name} is experiencing prejudice in {country}", "{name} is caught in seasonal flooding in {country}", "{name} is suffering from insect-borne illness in {country}",
    "{name} is being monitored by authorities in {country}", "{name} is struggling with inadequate healthcare in {country}", "{name} is caught in an area with high crime rates in {country}", "{name} is facing eviction from temporary housing in {country}", "{name} is struggling with unreliable public transportation in {country}",
    "{name} is fleeing from a stalker in {country}", "{name} is suffering from sleep deprivation in {country}", "{name} is being pressured to leave {country}", "{name} is caught in a region with food shortages in {country}", "{name} is living in unsanitary conditions in {country}",
    "{name} is experiencing panic attacks in {country}", "{name} is falsely accused of theft in {country}", "{name} is targeted for being a foreigner in {country}", "{name} is facing unexpected border closures in {country}", "{name} is having trouble adapting to local dietary restrictions in {country}",
    "{name} is fleeing from a dangerous relationship in {country}", "{name} is suffering from heat exhaustion in {country}", "{name} is caught in a public transportation strike in {country}", "{name} is unable to find affordable housing in {country}", "{name} is experiencing technology withdrawal in {country}",
    "{name} is struggling with unfamiliar social norms in {country}", "{name} is suffering from hypothermia in {country}", "{name} is facing religious intolerance in {country}", "{name} is caught in a region with water shortages in {country}", "{name} is struggling with excessive noise pollution in {country}",
    "{name} is living in fear of deportation in {country}", "{name} is being denied basic services in {country}", "{name} is caught in an area with air pollution in {country}", "{name} is suffering from seasonal allergies in {country}", "{name} is being exploited by local businesses in {country}",
    "{name} is struggling with digital censorship in {country}", "{name} is facing gender discrimination in {country}", "{name} is caught in a region with frequent power outages in {country}", "{name} is suffering from sunburn and dehydration in {country}", "{name} is unable to access necessary medication in {country}",
    "{name} is struggling with slow internet connectivity in {country}", "{name} is caught in a tourist scam in {country}", "{name} is experiencing sensory overload in {country}", "{name} is facing age discrimination in {country}", "{name} is living without reliable electricity in {country}",
    "{name} is suffering from chronic fatigue in {country}", "{name} is being stalked by someone in {country}", "{name} is struggling with jet lag in {country}", "{name} is caught in a region with insect infestations in {country}", "{name} is being harassed online while in {country}",
    "{name} is facing unexpected banking issues in {country}", "{name} is living with constant anxiety in {country}", "{name} is suffering from chronic back pain in {country}", "{name} is unable to find work despite qualifications in {country}", "{name} is struggling with local business practices in {country}",
    "{name} is caught in a region with frequent earthquakes in {country}", "{name} is being followed by debt collectors in {country}", "{name} is facing difficulties with local authorities in {country}", "{name} is living in fear of natural disasters in {country}", "{name} is suffering from a mysterious illness in {country}",
    "{name} is unable to access their online accounts in {country}", "{name} is struggling with local education systems in {country}", "{name} is caught in a region with dangerous wildlife in {country}", "{name} is being charged excessive fees as a foreigner in {country}", "{name} is facing housing discrimination in {country}",
    "{name} is living with untreated dental pain in {country}", "{name} is suffering from technology addiction in {country}", "{name} is unable to find child care services in {country}", "{name} is struggling with unreliable postal services in {country}", "{name} is caught in a region with high radiation levels in {country}",
    "{name} is being denied access to legal representation in {country}", "{name} is facing unexpected tax issues in {country}", "{name} is living with untreated vision problems in {country}", "{name} is suffering from malnutrition in {country}", "{name} is unable to find adequate wheelchair accessibility in {country}",
    "{name} is struggling with frequent miscommunications in {country}", "{name} is caught in a region with ongoing land disputes in {country}", "{name} is being denied access to public facilities in {country}", "{name} is facing unexpected inheritance issues in {country}", "{name} is living with undiagnosed hearing loss in {country}",
    "{name} is suffering from technology-related stress in {country}", "{name} is unable to find support for learning disabilities in {country}", "{name} is struggling with online censorship in {country}", "{name} is caught in a region with dangerous road conditions in {country}", "{name} is experiencing phantom smells and tastes in {country}",
    "{name} is caught in a time zone confusion in {country}", "{name} is struggling with doppelgänger accusations in {country}", "{name} is experiencing digital identity theft in {country}", "{name} is suffering from unexplained recurring dreams about {country}", "{name} is dealing with an unusual allergic reaction to local flora in {country}",
    "{name} is facing accusations of being a foreign spy in {country}", "{name} is caught in a bureaucratic loop requiring impossible documents in {country}", "{name} is experiencing technology that mysteriously fails only in {country}", "{name} is suffering from location-specific insomnia in {country}", "{name} is dealing with a bizarre local superstition targeted at them in {country}",
    "{name} is facing unexpected legal consequences for a harmless gesture in {country}", "{name} is experiencing unexplained déjà vu episodes in {country}", "{name} is struggling with a mysterious object that follows them throughout {country}", "{name} is dealing with a culturally specific phobia triggered only in {country}", "{name} is experiencing strange temporal distortions while in {country}",
    "{name} is facing consequences for violating an obscure local taboo in {country}", "{name} is being mistaken for a local celebrity in {country}", "{name} is experiencing phantom radio signals only they can hear in {country}", "{name} is struggling with a peculiar form of reverse culture shock in {country}"
]

# VARS # 
intro = ['L','O','A','D','I','N','G','!']
age = random.randint(18, 100)
day = 0
visited = []
unvisited = countries.copy()
prompt = ""
go = True
victory_sound = random.choice(['soundeffects/good/pablo.mp3','soundeffects/good/rat-dance-music.mp3','soundeffects/good/mundian-to-bach-ke.mp3'])
lastPrompts = ["Oof you lost"]
numList = [-1 , 0 , 1]
weights = [.005,.275,.72]
country = random.choice(countries)
gender = random.choice(genders)
if gender == 'Female':
    name = random.choice(fNames)
elif gender == 'Male':
    name = random.choice(mNames)
else:
    name = random.choice(mNames + fNames)
name += " " + random.choice(lastNames)

# functions #
def getPrompt():
    promptType = random.choices(numList,weights = weights,k=1)[0]
    if promptType == 1:
        prompt = random.choice(goodPrompts).format(name=name,country=country)
    elif promptType == 0:
        prompt = random.choice(badPrompts).format(name=name,country=country)
    else:
        prompt = random.choice(lastPrompts)
    return prompt

# start of game
playsound('soundeffects/good/pedro-song.mp3',block=False)
for i in range(8):
    print(' '*i,intro[i],' ')
    time.sleep(0.33)

print("\nWelcome to the World Game!\n")
print("Your goal is to travel the entire world while surviving\n")
print("Disclaimer: All name, situations, or concidences are entirly incidental and non-intented.\nProceed at your own risk!\n")
print("Your Country:",country,"\tName: ",name,"\tGender: ",gender,"\tAge: ",age)
while go == True:
    print("\nDay: ",day)
    if day > 0:
        country = random.choice(countries)
    if visited:
        country = random.choice(unvisited)
    visited.append(country)
    unvisited.remove(country)
    print("You are in",country)
    prompt = getPrompt()
    if prompt in lastPrompts:
        go = False
        print("You made it to:",len(visited)/len(countries),"%")
        print("Countries left:",len(unvisited))
        break
    time.sleep(1)
    print("\n",prompt,"\n")
    nextDay = input(" Enter 'n' to continue to... ")
    if nextDay.lower() == 'n':
        day += 1
        playsound('soundeffects/good/correct.mp3',block=False)
    else:
        while nextDay.lower() != 'n':
            nextDay = input(" Enter 'n' to continue to... ")
        day += 1
        playsound('soundeffects/good/correct.mp3',block=False)
    if len(visited) == len(countries):
        playsound(victory_sound,block=False)
        print("Congratulations You have visited all countries! Surviving the all the things of the world!")
        go = False