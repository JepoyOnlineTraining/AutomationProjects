from behave import *


@given(u'I navigate to Register Page')
def step_impl(context):
    print("Inside Step")


@when(u'I enter mandatory fields')
def step_impl(context):
    print("Inside Step")

@when(u'I click on Continue button')
def step_impl(context):
    print("Inside Step")


@then(u'Account should get created')
def step_impl(context):
    print("Inside Step")

@when(u'I enter all fields')
def step_impl(context):
    print("Inside Step")


@when(u'I enter details into all fields except email filed')
def step_impl(context):
    print("Inside Step")


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    print("Inside Step")


@then(u'Proper warning message informing about duplicate account should be display')
def step_impl(context):
    print("Inside Step")


@when(u'I dont enter anything into the fields')
def step_impl(context):
    print("Inside Step")


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    print("Inside Step")