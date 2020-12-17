# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def updated_damages(damages):
  updated_damages = []
  conversion = {"M": 1000000, "B": 1000000000}

  for item in damages:
    if item == "Damages not recorded":
      updated_damages.append(item)
    elif item[-1] == "M":
      updated_damages.append(float(item.strip("M"))*conversion["M"])
    elif item[-1] == "B":
      updated_damages.append(float(item.strip("B"))*conversion["B"])
  return updated_damages

updated_damages = updated_damages(damages)
# print(updated_damages)


# write your construct hurricane dictionary function here:
def hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes_by_name = {}

  for i in range(len(names)):
    hurricanes_by_name[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages[i], "Deaths": deaths[i]}
  return hurricanes_by_name

hurricanes_by_name = hurricanes_by_name(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(hurricanes_by_name)


# write your construct hurricane by year dictionary function here:
def hurricanes_by_year(hurricanes_by_name):
  hurricanes_by_year = {}

  for i in years:
    hurricanes_by_year[i] = [cane for cane in hurricanes_by_name.values() if cane["Year"] == i]
  return hurricanes_by_year

hurricanes_by_year = hurricanes_by_year(hurricanes_by_name)
# print(hurricanes_by_year)


# write your count affected areas function here:
def count_of_affected_areas(hurricanes_by_name):
  count_of_affected_areas = {}

  for area in areas_affected:
    for sub in area:
      if sub not in count_of_affected_areas:
        count_of_affected_areas[sub] = 0
      elif sub in count_of_affected_areas:
        count_of_affected_areas[sub] += 1
  return count_of_affected_areas

count_of_affected_areas = count_of_affected_areas(hurricanes_by_name)
# print(count_of_affected_areas)


# write your find most affected area function here:
def worst_hit_area(count_of_affected_areas):
  max_area = "SS"
  max_area_count = 0

  for x, y in count_of_affected_areas.items():
    if y > max_area_count:
      max_area = x
      max_area_count = y
  return{max_area: max_area_count}

worst_area = worst_hit_area(count_of_affected_areas)
# print(worst_area)


# write your greatest number of deaths function here:
def deadliest_cane(hurricanes_by_name):
  max_mortality_cane = "GG"
  max_mortality = 0

  for x, y in hurricanes_by_name.items():
    if y["Deaths"] > max_mortality:
      max_mortality_cane = x
      max_mortality = y["Deaths"]
  return {max_mortality_cane: max_mortality}

deadliest_cane = deadliest_cane(hurricanes_by_name)
# print(deadliest_cane)


# write your catgeorize by mortality function here:
def hurricanes_by_mortality(hurricanes_by_name):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

  hurricanes_by_mortality[0] = [x for x in hurricanes_by_name.values() if x["Deaths"] == 0]
  hurricanes_by_mortality[1] = [x for x in hurricanes_by_name.values() if 0 < x["Deaths"] <= 100]
  hurricanes_by_mortality[2] = [x for x in hurricanes_by_name.values() if 100 < x["Deaths"] <= 500]
  hurricanes_by_mortality[3] = [x for x in hurricanes_by_name.values() if 500 < x["Deaths"] <= 1000]
  hurricanes_by_mortality[4] = [x for x in hurricanes_by_name.values() if 1000 < x["Deaths"] <= 10000]
  hurricanes_by_mortality[5] = [x for x in hurricanes_by_name.values() if x["Deaths"] > 10000]

  return hurricanes_by_mortality

hurricanes_by_mortality = hurricanes_by_mortality(hurricanes_by_name)
# print(hurricanes_by_mortality)


# write your greatest damage function here:
def damage(hurricanes_by_name):
  max_damage_cane = 'Cuba I'
  max_damage = 0

  for x, y in hurricanes_by_name.items():
    if y["Damage"] == "Damages not recorded":
      continue
    elif y["Damage"] > max_damage:
      max_damage_cane = x
      max_damage = y["Damage"]

  return {max_damage_cane: max_damage}

hurricane_by_damage = damage(hurricanes_by_name)
# print(hurricane_by_damage)


# write your categorize by damage function here:
def hurricane_damage_rating(hurricanes_by_name):
  damage_scale = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for x, y in hurricanes_by_name.items():
    if y["Damage"] == "Damages not recorded":
      continue
    elif y["Damage"] == 0:
      damage_scale[0].append(x)
    elif 0 < y["Damage"] <= 100000000:
      damage_scale[1].append(x)
    elif 100000000 < y["Damage"] <= 1000000000:
      damage_scale[2].append(x)
    elif 1000000000 < y["Damage"] <= 10000000000:
      damage_scale[3].append(x)
    elif 10000000000 < y["Damage"] <= 50000000000:
      damage_scale[4].append(x)
    elif y["Damage"] > 50000000000:
      damage_scale[5].append(x)

  return damage_scale

damage_scale = hurricane_damage_rating(hurricanes_by_name)
# print(damage_scale)

# THE END!!!
