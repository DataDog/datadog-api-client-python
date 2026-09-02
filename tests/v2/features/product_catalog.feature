@endpoint(product-catalog) @endpoint(product-catalog-v2)
Feature: Product Catalog
  Look up the Datadog SKUs that are generally available, together with the
  public list prices, allotments, and tiered pricing that apply to them on a
  given date.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "ProductCatalog" API
    And operation "ListProductCatalogSKUs" enabled
    And new "ListProductCatalogSKUs" request

  @generated @skip @team:DataDog/red-zone-product-catalog
  Scenario: List SKUs returns "Bad Request - version is missing or invalid, or as_of_date is malformed or in the future" response
    Given request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request - version is missing or invalid, or as_of_date is malformed or in the future

  @generated @skip @team:DataDog/red-zone-product-catalog
  Scenario: List SKUs returns "Not Found - the requested catalog version is not supported" response
    Given request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found - the requested catalog version is not supported

  @generated @skip @team:DataDog/red-zone-product-catalog
  Scenario: List SKUs returns "OK" response
    Given request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
