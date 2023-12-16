import re
import functools
from enum import Enum
from itertools import chain

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

"""
Part 2
"""
seed_ranges = []
with open("./data/day05.txt", "r") as f:
    for line in f:
        line = line.strip()
        if re.match('seeds:', line):
            temp_seeds = list(
                map(lambda s: int(s), line.replace('seeds: ', '').split(' ')))
            for i in range(len(temp_seeds)):
                if i % 2 != 0:
                    continue
                seed_ranges.append(
                    range(temp_seeds[i], temp_seeds[i] + temp_seeds[i+1]))
        else:
            break


class Maps(Enum):
    SEED_TO_SOIL = 1,
    SOIL_TO_FERTILIZER = 2,
    FERTILIZER_TO_WATER = 3
    WATER_TO_LIGHT = 4
    LIGHT_TO_TEMPERATURE = 5
    TEMPERATURE_TO_HUMIDITY = 6
    HUMIDITY_TO_LOCATION = 7


maps = {}
with open("./data/day05.txt", "r") as f:
    cur = None
    for line in f:
        line = line.strip()
        if not len(line):
            continue
        if re.match('seeds:', line):
            continue
        elif re.match('seed-to-soil map:', line):
            cur = Maps.SEED_TO_SOIL
            maps[cur] = []
        elif re.match('soil-to-fertilizer map:', line):
            cur = Maps.SOIL_TO_FERTILIZER
            maps[cur] = []
        elif re.match('fertilizer-to-water map:', line):
            cur = Maps.FERTILIZER_TO_WATER
            maps[cur] = []
        elif re.match('water-to-light map:', line):
            cur = Maps.WATER_TO_LIGHT
            maps[cur] = []
        elif re.match('light-to-temperature map:', line):
            cur = Maps.LIGHT_TO_TEMPERATURE
            maps[cur] = []
        elif re.match('temperature-to-humidity map:', line):
            cur = Maps.TEMPERATURE_TO_HUMIDITY
            maps[cur] = []
        elif re.match('humidity-to-location map:', line):
            cur = Maps.HUMIDITY_TO_LOCATION
            maps[cur] = []
        else:
            line = list(map(lambda s: int(s), line.split(' ')))
            maps[cur].append({
                "source_start": line[1],
                "target_start": line[0],
                "source_range": range(line[1], line[1] + line[2]),
            })


def transform_range(s, t, r):
    if s > t:
        diff = s - t
        return range(r.start - diff, r.stop - diff)
    elif t > s:
        diff = t - s
        return range(r.start + diff, r.stop + diff)
    else:
        return r


def get_ranges(input_ranges, maps):
    output_ranges = []
    for r in input_ranges:
        for i, m in enumerate(maps):
            intersection = range(max(r.start, m["source_range"].start), min(
                r.stop, m["source_range"].stop)) or None
            if not intersection:
                if i == len(maps) - 1:
                    output_ranges.append(r)
            elif intersection == r:
                output_ranges.append(transform_range(
                    m["source_start"], m["target_start"], intersection))
                break
            else:
                t_range = transform_range(
                    m["source_start"], m["target_start"], intersection)
                output_ranges.append(t_range)
                if intersection.start == r.start:
                    diff = range(intersection.stop, r.stop)
                    input_ranges.append(diff)
                elif intersection.stop == r.stop:
                    diff = range(r.start, intersection.start)
                    input_ranges.append(diff)
                else:
                    diff_l = range(r.start, intersection.start)
                    diff_r = range(intersection.stop, r.stop)
                    input_ranges.append(diff_l)
                    input_ranges.append(diff_r)
                break
    return output_ranges


soil_ranges = get_ranges(
    list(set(seed_ranges)), maps[Maps.SEED_TO_SOIL])
fertilizer_ranges = get_ranges(
    list(set(soil_ranges)), maps[Maps.SOIL_TO_FERTILIZER])
water_ranges = get_ranges(
    list(set(fertilizer_ranges)), maps[Maps.FERTILIZER_TO_WATER])
light_ranges = get_ranges(
    list(set(water_ranges)), maps[Maps.WATER_TO_LIGHT])
temperature_ranges = get_ranges(
    list(set(light_ranges)), maps[Maps.LIGHT_TO_TEMPERATURE])
humidity_ranges = get_ranges(
    list(set(temperature_ranges)), maps[Maps.TEMPERATURE_TO_HUMIDITY])
location_ranges = get_ranges(
    list(set(humidity_ranges)), maps[Maps.HUMIDITY_TO_LOCATION])
lowest_range = functools.reduce(
    lambda a, b: a if a.start < b.start else b, location_ranges)
lowest_location = lowest_range.start
print(lowest_location)
