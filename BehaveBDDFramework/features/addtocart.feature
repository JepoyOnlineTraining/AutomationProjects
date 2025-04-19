Feature: Add Product to Cart

  @done
  Scenario: Add Product to Cart using Product Add Cart Button
    Given I got navigated to Home Page
      When I click iphone add to cart button
      Then Cart will be updated

 @done
  Scenario: Add Product to Cart by going to product
    Given I got navigated to Home Page
      When I select iphone product
       And Enter unit and click add to cart button
      Then Cart will be updated with expected unit count