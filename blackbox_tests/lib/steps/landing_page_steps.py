import time

from behave import *
from hamcrest import assert_that, is_in, equal_to

from blackbox_tests.lib.page_objects.landing_page import LandingPage
from blackbox_tests.lib.utils.constants import Constants

use_step_matcher("re")


@when("user open landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.landing_page = LandingPage(context)
    time.sleep(3)


@then("user should be able to see landing page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert_that(context.landing_page.landing_page_title.text, equal_to(Constants.TITLE))


@step('the navigation bar should include the following "(?P<column>.+)"')
def step_impl(context, column):
    """
    :type context: behave.runner.Context
    :type column: str
    """
    # context.columns = [context.landing_page.hotels_column.text,
    #                    context.landing_page.flights_column.text,
    #                    context.landing_page.tours_column.text,
    #                    context.landing_page.cars_column.text]
    # for point in context.columns:
    #     point = point.text
    assert_that(context.landing_page.hotels_column.text, equal_to(column))
