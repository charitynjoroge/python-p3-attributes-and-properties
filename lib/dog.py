#!/usr/bin/env python3
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name="", breed=""):
        self.name = name
        self.breed = breed

        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")

        approved_breeds = ["Pug", "Labrador", "German Shepherd", "Golden Retriever"]
        if breed not in approved_breeds:
            print("Breed must be in list of approved breeds.")

