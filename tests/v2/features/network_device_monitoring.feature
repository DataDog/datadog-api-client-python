@endpoint(network-device-monitoring) @endpoint(network-device-monitoring-v2)
Feature: Network Device Monitoring
  The Network Device Monitoring API allows you to fetch devices and
  interfaces and their attributes. See the [Network Device Monitoring
  page](https://docs.datadoghq.com/network_monitoring/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "NetworkDeviceMonitoring" API

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the device details returns "Not Found" response
    Given new "GetDevice" request
    And request contains "device_id" parameter with value "unknown_device_id"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the device details returns "OK" response
    Given new "GetDevice" request
    And request contains "device_id" parameter with value "default_device"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "device"
    And the response "data.id" is equal to "default_device"
    And the response "data.attributes.description" is equal to "a device monitored with NDM"
    And the response "data.attributes.device_type" is equal to "other"
    And the response "data.attributes.ip_address" is equal to "1.2.3.4"
    And the response "data.attributes.location" is equal to "paris"
    And the response "data.attributes.model" is equal to "xx-123"
    And the response "data.attributes.name" is equal to "example device"
    And the response "data.attributes.os_name" is equal to "example OS"
    And the response "data.attributes.os_version" is equal to "1.0.2"
    And the response "data.attributes.ping_status" is equal to "unmonitored"
    And the response "data.attributes.product_name" is equal to "example device"
    And the response "data.attributes.serial_number" is equal to "X12345"
    And the response "data.attributes.status" is equal to "ok"
    And the response "data.attributes.sys_object_id" is equal to "1.3.6.1.4.1.99999"
    And the response "data.attributes.tags" is equal to ["device_ip:1.2.3.4","device_id:default_device"]

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the list of devices returns "Bad Request" response
    Given new "ListDevices" request
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the list of devices returns "OK" response
    Given new "ListDevices" request
    And request contains "page[size]" parameter with value 1
    And request contains "page[number]" parameter with value 0
    And request contains "filter[tag]" parameter with value "device_namespace:default"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "device"
    And the response "data[0].id" is equal to "default:1.2.3.4"
    And the response "data[0].attributes.description" is equal to "a device monitored with NDM"
    And the response "data[0].attributes.device_type" is equal to "other"
    And the response "data[0].attributes.ip_address" is equal to "1.2.3.4"
    And the response "data[0].attributes.location" is equal to "paris"
    And the response "data[0].attributes.model" is equal to "xx-123"
    And the response "data[0].attributes.name" is equal to "example device"
    And the response "data[0].attributes.os_name" is equal to "example OS"
    And the response "data[0].attributes.os_version" is equal to "1.0.2"
    And the response "data[0].attributes.ping_status" is equal to "unmonitored"
    And the response "data[0].attributes.product_name" is equal to "example device"
    And the response "data[0].attributes.serial_number" is equal to "X12345"
    And the response "data[0].attributes.status" is equal to "ok"
    And the response "data[0].attributes.sys_object_id" is equal to "1.3.6.1.4.1.99999"
    And the response "data[0].attributes.tags" is equal to ["device_ip:1.2.3.4","device_id:default:1.2.3.4"]
    And the response "data[0].attributes.interface_statuses.up" is equal to 2
    And the response "data[0].attributes.interface_statuses.warning" is equal to 4
    And the response "data[0].attributes.interface_statuses.down" is equal to 13
    And the response "meta.page.total_filtered_count" is equal to 1

  @generated @skip @team:DataDog/network-device-monitoring @with-pagination
  Scenario: Get the list of devices returns "OK" response with pagination
    Given new "ListDevices" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the list of interfaces of the device returns "OK" response
    Given new "GetInterfaces" request
    And request contains "device_id" parameter with value "default:1.2.3.4"
    And request contains "get_ip_addresses" parameter with value true
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "interface"
    And the response "data[0].id" is equal to "default:1.2.3.4:99"
    And the response "data[0].attributes.name" is equal to "if99"
    And the response "data[0].attributes.description" is equal to "a network interface"
    And the response "data[0].attributes.mac_address" is equal to "00:00:00:00:00:00"
    And the response "data[0].attributes.ip_addresses" is equal to ["1.1.1.1","1.1.1.2"]
    And the response "data[0].attributes.alias" is equal to "interface_99"
    And the response "data[0].attributes.index" is equal to 99
    And the response "data[0].attributes.status" is equal to "up"
    And the response "data[1].type" is equal to "interface"
    And the response "data[1].id" is equal to "default:1.2.3.4:999"
    And the response "data[1].attributes.name" is equal to "if999"
    And the response "data[1].attributes.description" is equal to "another network interface"
    And the response "data[1].attributes.mac_address" is equal to "99:99:99:99:99:99"
    And the response "data[1].attributes.alias" is equal to "interface_999"
    And the response "data[1].attributes.index" is equal to 999
    And the response "data[1].attributes.status" is equal to "down"

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the list of tags for a device returns "Not Found" response
    Given new "ListDeviceUserTags" request
    And request contains "device_id" parameter with value "unknown_device_id"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Get the list of tags for a device returns "OK" response
    Given new "ListDeviceUserTags" request
    And request contains "device_id" parameter with value "default_device"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "default_device"
    And the response "data.type" is equal to "tags"
    And the response "data.attributes.tags[0]" is equal to "tag:test"
    And the response "data.attributes.tags[1]" is equal to "tag:testbis"

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: List tags for an interface returns "Not Found" response
    Given new "ListInterfaceUserTags" request
    And request contains "interface_id" parameter with value "unknown_interface_id"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: List tags for an interface returns "OK" response
    Given new "ListInterfaceUserTags" request
    And request contains "interface_id" parameter with value "example:1.2.3.4:1"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "example:1.2.3.4:1"
    And the response "data.type" is equal to "tags"
    And the response "data.attributes.tags[0]" is equal to "tag:test"
    And the response "data.attributes.tags[1]" is equal to "tag:testbis"

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Update the tags for a device returns "Not Found" response
    Given new "UpdateDeviceUserTags" request
    And request contains "device_id" parameter with value "unknown_device_id"
    And body with value {"data": {"attributes": {"tags": ["tag:test", "tag:testbis"]}, "id": "unknown_device_id", "type":"tags"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Update the tags for a device returns "OK" response
    Given new "UpdateDeviceUserTags" request
    And request contains "device_id" parameter with value "default_device"
    And body with value {"data": {"attributes": {"tags": ["tag:test", "tag:testbis"]}, "id": "default_device", "type":"tags"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "default_device"
    And the response "data.type" is equal to "tags"
    And the response "data.attributes.tags[0]" is equal to "tag:test"
    And the response "data.attributes.tags[1]" is equal to "tag:testbis"

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Update the tags for an interface returns "Not Found" response
    Given new "UpdateInterfaceUserTags" request
    And request contains "interface_id" parameter with value "unknown_interface_id"
    And body with value {"data": {"attributes": {"tags": ["tag:test", "tag:testbis"]}, "id": "unknown_interface_id", "type":"tags"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/network-device-monitoring
  Scenario: Update the tags for an interface returns "OK" response
    Given new "UpdateInterfaceUserTags" request
    And request contains "interface_id" parameter with value "example:1.2.3.4:1"
    And body with value {"data": {"attributes": {"tags": ["tag:test", "tag:testbis"]}, "id": "example:1.2.3.4:1", "type":"tags"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "example:1.2.3.4:1"
    And the response "data.type" is equal to "tags"
    And the response "data.attributes.tags[0]" is equal to "tag:test"
    And the response "data.attributes.tags[1]" is equal to "tag:testbis"
