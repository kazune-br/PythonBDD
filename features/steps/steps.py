from behave import *
from vending_machine import *


@given(u'the vending machine')
def step_impl(context):
    context.vending_machine = VendingMachine()


@when(u'the customer inserts 100 yen into the machine')
def step_impl(context):
    context.vending_machine.insert_money(100)


@then(u'the amount of money in the machine should be 100 yen')
def step_impl(context):
    assert (100 == context.vending_machine.amount_of_money)


@then("the amount of money in the machine should be 200 yen")
def step_impl(context):
    assert (200 == context.vending_machine.amount_of_money)


@when(u'the customer inserts 1 yen into the machine')
def step_impl(context):
    context.vending_machine.insert_money(1)


@then(u'the amount of money in the machine should be 0 yen')
def step_impl(context):
    assert (0 == context.vending_machine.amount_of_money)


@when("the customer inserts {input_money:d} yen into the machine")
def step_impl(context, input_money):
    context.vending_machine.insert_money(input_money)


@then("the amount of money in the machine should be {total_money:d} yen")
def step_impl(context, total_money):
    assert (total_money == context.vending_machine.amount_of_money)