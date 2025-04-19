from behave import *
from features.actions.add_to_cart_actions import AddToCartActions


@when(u'I click iphone add to cart button')
def step_impl(context):
    context.add_to_cart_act = AddToCartActions(context.driver)
    context.add_to_cart_act.click_product_cart_button()


@then(u'Cart will be updated')
def step_impl(context):
    context.add_to_cart_act.verify_product_added()


@when(u'I select iphone product')
def step_impl(context):
    context.add_to_cart_act = AddToCartActions(context.driver)
    context.add_to_cart_act.select_iphone()


@when(u'Enter unit and click add to cart button')
def step_impl(context):
    context.add_to_cart_act.add_multiple_product()


@then(u'Cart will be updated with expected unit count')
def step_impl(context):
    context.add_to_cart_act.verify_multiple_product_added()
