
import asyncio 

# import banner requests

from django.core.management import base

from scraper.models import Section, Instructor
# from scraper.models.Department import Department

def parse_all_sections(json):
    """ Stuff """

def parse_courses(json):
    """ Iterates through all of the sections """

def parse_section(json, instructor: Instructor):
    """ Parses each individual section
        Requires an instructor
    """


    section = Section(id=468298201931, subject="CSCE", course_num=121, section_num=501,
                      term_code=201931, min_credits=4, instructor=instructor,
                      max_enrollment=50, current_enrollment=50)
    section.save()

def parse_meeting(json, section: Section):
    """ Parses the section json for the meeting data
        Requires a section model due to Meetings' foreignkey Section attribute
    """

class Command(base.BaseCommand):
    "Iterates through all of the courses and loads them into the database"
    def handle(self, *args, **kwargs):
        pass
