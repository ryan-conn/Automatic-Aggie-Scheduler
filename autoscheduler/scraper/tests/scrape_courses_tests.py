import json

import django.test

from pathlib import Path

from scraper.management.commands.scrape_courses import parse_section
from scraper.models import Section, Meeting, Instructor

def load_json_file(path: str):
    """ Loads a json file given a path """
    base_path = Path(__file__).parent
    file_path = (base_path / path).resolve()

    data = None
    with open(file_path) as json_file:
        data = json.load(json_file)

        json_file.close()

    return data

class ScrapeCoursesTests(django.test.TestCase):
    """ Tests scrape_courses """
    def setUp(self):
        self.section_json = load_json_file("../tests/data/section_input.json")

    def test_parse_section_does_save_model(self):
        """ Tests if parse sections saves the model to the databse correctly
            Does so by calling parse_section on the section_input, and queries for a
        """

        # Arrange
        subject = "CSCE"
        course_num = 121
        section_num = 501
        term_code = 201931
        min_credits = 4
        max_enroll = curr_enroll = 50
        section_id = int('468298' + str(term_code))

        # Section model requires an Instructor
        fake_instructor = Instructor(id=123, email_address="a@b.com", name="Fake")
        fake_instructor.save()

        # Act
        parse_section(self.section_json, fake_instructor)

        # Assert
        Section.objects.get(id=section_id, subject=subject, course_num=course_num,
                            section_num=section_num, term_code=term_code,
                            current_enrollment=curr_enroll, max_enrollment=max_enroll,
                            instructor=fake_instructor)
        assert True
        # If the query failed then the section doesn't exist, and thus the section
        # model wasn't saved correctly
