Feature: VendingMachine

  Scenario: Check an insertion of money into the vending machine
    Given the vending machine
    When the customer inserts 100 yen into the machine
    Then the amount of money in the machine should be 100 yen

  Scenario: Check additional insertions of money into the vending machine
    Given the vending machine
    When the customer inserts 100 yen into the machine
    And the customer inserts 100 yen into the machine
    Then the amount of money in the machine should be 200 yen

  Scenario Outline: Check the valid money
    Given the vending machine
    When the customer inserts <input_money> yen into the machine
    Then the amount of money in the machine should be <total_money> yen
    Examples:
      | input_money | total_money |
      | 1           | 0           |
      | 5           | 5           |
      | 10          | 10          |
      | 50          | 50          |
      | 100         | 100         |
      | 500         | 500         |
      | 1000        | 1000        |
      | 2000        | 0           |
      | 5000        | 0           |
      | 10000       | 0           |
