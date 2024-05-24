#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="", job=""):
        self.name = name.title()
        self.job = job

        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")

        approved_jobs = ["Sales", "ITC", "Manager", "Developer"]
        if job not in approved_jobs:
            print("Job must be in list of approved jobs.")

