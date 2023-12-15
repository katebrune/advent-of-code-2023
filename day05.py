import re
import functools

"""
Part 1
"""
with open("./data/day05.txt", "r") as f:
    seeds = []
    maps = {}
    cur = ""
    for line in f:
        line = line.strip()
        if not len(line):
            continue
        if re.match('seeds:', line):
            seeds = list(
                map(lambda s: int(s), line.replace("seeds: ", "").split(" ")))
        elif re.match('seed-to-soil map:', line):
            cur = "seed-to-soil"
            maps[cur] = []
        elif re.match('soil-to-fertilizer map:', line):
            cur = "soil-to-fertilizer"
            maps[cur] = []
        elif re.match('fertilizer-to-water map:', line):
            cur = 'fertilizer-to-water'
            maps[cur] = []
        elif re.match('water-to-light map:', line):
            cur = 'water-to-light'
            maps[cur] = []
        elif re.match("light-to-temperature map:", line):
            cur = 'light-to-temperature'
            maps[cur] = []
        elif re.match("temperature-to-humidity map:", line):
            cur = 'temperature-to-humidity'
            maps[cur] = []
        elif re.match("humidity-to-location map:", line):
            cur = 'humidity-to-location'
            maps[cur] = []
        else:
            line = list(map(lambda s: int(s), line.split(' ')))
            obj = {
                "source_range": tuple((line[1], line[1] + line[2])),
                "target": line[0]
            }
            maps[cur].append(obj)
    locations = []
    for seed in seeds:
        soil = None
        fertilizer = None
        water = None
        light = None
        temperature = None
        humidity = None
        location = None
        for obj in maps['seed-to-soil']:
            if seed >= obj["source_range"][0] and seed <= obj["source_range"][1]:
                soil = obj["target"] + ((obj["source_range"][1] -
                                        obj["source_range"][0]) - (obj["source_range"][1] - seed))
        if soil is None:
            soil = seed
        for obj in maps['soil-to-fertilizer']:
            if soil >= obj["source_range"][0] and soil <= obj["source_range"][1]:
                fertilizer = obj["target"] + ((obj["source_range"][1] -
                                              obj["source_range"][0]) - (obj["source_range"][1] - soil))
        if fertilizer is None:
            fertilizer = soil
        for obj in maps['fertilizer-to-water']:
            if fertilizer >= obj["source_range"][0] and fertilizer <= obj["source_range"][1]:
                water = obj["target"] + ((obj["source_range"][1] -
                                          obj["source_range"][0]) - (obj["source_range"][1] - fertilizer))
        if water is None:
            water = fertilizer
        for obj in maps['water-to-light']:
            if water >= obj["source_range"][0] and water <= obj["source_range"][1]:
                light = obj["target"] + ((obj["source_range"][1] -
                                          obj["source_range"][0]) - (obj["source_range"][1] - water))
        if light is None:
            light = water
        for obj in maps['light-to-temperature']:
            if light >= obj["source_range"][0] and light <= obj["source_range"][1]:
                temperature = obj["target"] + ((obj["source_range"][1] -
                                                obj["source_range"][0]) - (obj["source_range"][1] - light))
        if temperature is None:
            temperature = light
        for obj in maps['temperature-to-humidity']:
            if temperature >= obj["source_range"][0] and temperature <= obj["source_range"][1]:
                humidity = obj["target"] + ((obj["source_range"][1] -
                                             obj["source_range"][0]) - (obj["source_range"][1] - temperature))
        if humidity is None:
            humidity = temperature
        for obj in maps['humidity-to-location']:
            if humidity >= obj["source_range"][0] and humidity <= obj["source_range"][1]:
                location = obj["target"] + ((obj["source_range"][1] -
                                             obj["source_range"][0]) - (obj["source_range"][1] - humidity))
        if location is None:
            location = humidity
        locations.append(location)
    lowest_location = functools.reduce(
        lambda a, b: a if a < b else b, locations)
    print(lowest_location)
