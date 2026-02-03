@endpoint(oci-integration) @endpoint(oci-integration-v2)
Feature: OCI Integration
  Auto-generated tag OCI Integration

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OCIIntegration" API

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Create tenancy config returns "Created" response
    Given operation "CreateTenancyConfig" enabled
    And new "CreateTenancyConfig" request
    And body with value {"data": {"attributes": {"auth_credentials": {"fingerprint": "", "private_key": "----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----"}, "config_version": null, "cost_collection_enabled": true, "dd_compartment_id": "ocid.compartment.test", "dd_stack_id": "ocid.stack.test", "home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["service_1", "service_1"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["service_1", "service_1"]}, "regions_config": {"available": ["us-ashburn-1", "us-phoenix-1"], "disabled": ["us-phoenix-1"], "enabled": ["us-ashburn-1"]}, "resource_collection_enabled": true, "user_ocid": "ocid.user.test"}, "id": "ocid.tenancy.test", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Delete tenancy config returns "No Content" response
    Given new "DeleteTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Get tenancy config returns "OK" response
    Given new "GetTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Get tenancy configs returns "OK" response
    Given operation "GetTenancyConfigs" enabled
    And new "GetTenancyConfigs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: List tenancy products returns "OK" response
    Given new "ListTenancyProducts" request
    And request contains "productKeys" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Update tenancy config returns "OK" response
    Given new "UpdateTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"auth_credentials": {"fingerprint": "", "private_key": "----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCdvSMmlfLyeD4M\nQsA3WlrWBqKdWa5eVV3/uODyqT3wWMEMIJHcG3/quNs8nh9xrK1/JkQT2qoKEHqR\nC5k59jN6Vp8em8ARJthMgam9K37ELt+IQ/G8ySTSuqZG8T4cHp/cs3fAclNqttOl\nYnGr4RbVAgMBAAECggEAGZNLGbyCUbIRTW6Kh4d8ZVC+eZtJMqGmGJ3KfVaW8Pjn\nQGWfSuJCEe2o2Y8G3phlidFauICnZ44enXA17Rhi+I/whnr7FIyQk2bR7rv+1Uhc\nmOJygWX5eFFMsledgVAdIAl9Luk2nykx7Un3g6rtbl/Vs+5k4m7ITLFMpCHzsJLU\nnm8kBzDOqY2JUkMd08nL88KL6QywWtal05UESzQpNFXd0e5kxYfexeMCsLsWP0mc\nquMLRbn7NuBjCbe9VU2kmIvcfDDaWjurT7d5m1OXx1cc8p6P4PFZTVyCjdhiWOr3\nLQXZ4/vdZNR3zgEHypRoM6D9Yq99LWUOUEMrdiSLQQKBgQDQkh7C1OtAXnpy7F6R\nW+/I3zBHici2p7A57UT7VECQ1IVGg37/uus83DkuOtdZ33JmHLAVrwLFJvUlbyjx\nl6dc/1ms40L5HFdLgaVtd4k0rSPFeOSDr6evz0lX4yBuzlP0fEh+o3XHW7mwe2G+\nrWCULF/Uqza66fjbCSKMNgLIXQKBgQDBm9nZg/s4S0THWCFNWcB1tXBG0p/sH5eY\nPC1H/VmTEINIixStrS4ufczf31X8rcoSjSbO7+vZDTTATdk7OLn1I2uGFVYl8M59\n86BYT2Hi7cwp7YVzOc/cJigVeBAqSRW/iYYyWBEUTiW1gbkV0sRWwhPp67m+c0sP\nXpY/iEZA2QKBgB1w8tynt4l/jKNaUEMOijt9ndALWATIiOy0XG9pxi9rgGCiwTOS\nDBCsOXoYHjv2eayGUijNaoOv6xzcoxfvQ1WySdNIxTRq1ru20kYwgHKqGgmO9hrM\nmcwMY5r/WZ2qjFlPjeAqbL62aPDLidGjoaVo2iIoBPK/gjxQ/5f0MS4N/YQ0zWoYBueSQ0DGs\n-----END PRIVATE KEY-----"}, "cost_collection_enabled": true, "home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["service_1", "service_1"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["service_1", "service_1"]}, "regions_config": {"available": ["us-ashburn-1", "us-phoenix-1"], "disabled": ["us-phoenix-1"], "enabled": ["us-ashburn-1"]}, "resource_collection_enabled": true, "user_ocid": "ocid.user.test"}, "id": "ocid.tenancy.test", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 200 OK
