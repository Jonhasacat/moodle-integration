import os
from dotenv import load_dotenv
from app.helpers.moodle import moodle_api

load_dotenv()

moodle_api.URL = os.environ.get('MOODLE_URL')
moodle_api.KEY = os.environ.get('MOODLE_API_KEY')


class MoodleHelper:
    @classmethod
    def get_all_courses(cls):
        return moodle_api.call('core_course_get_courses')

