from behave import *
from features.actions.search_actions import SearchActions

@given(u'I got navigated to Home Page')
def step_impl(context):
    context.search_act = SearchActions(context.driver)
    expected_text = "Your Store"
    assert expected_text == context.driver.title



@when(u'I enter valid product into the Search box field')
def step_impl(context):
    product = "HP"
    context.search_act.search_product(product=product)


@when(u'I click on Search button')
def step_impl(context):
    context.search_act.click_search()


@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    product = "HP"
    context.search_act.verify_search_result(product=product)

@when(u'I enter invalid product into the Search box field')
def step_impl(context):
    product = "YAKULT"
    context.search_act.search_product(product=product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    context.search_act.verify_proper_message_for_non_existing_product()

@when(u'I dont enter anything into Search box field')
def step_impl(context):
    product = ""
    context.search_act.search_product(product=product)
