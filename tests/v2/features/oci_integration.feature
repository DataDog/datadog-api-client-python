@endpoint(oci-integration) @endpoint(oci-integration-v2)
Feature: OCI Integration
  Configure your Datadog-OCI integration directly through the Datadog API.
  For more information, see the [OCI integration page](https://docs.datadogh
  q.com/integrations/oracle_cloud_infrastructure/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "OCIIntegration" API

  @team:DataDog/emerging-cloud-integrations
  Scenario: Create tenancy config returns "Bad Request" response
    Given new "CreateTenancyConfig" request
    And body with value {"data": {"attributes": {"auth_credentials": {"fingerprint": "a7:b5:54:f2:da:a2:d7:b0:ed:f4:79:47:93:64:12:b1", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEv\n-----END PRIVATE KEY-----\n"}, "config_version": 2, "home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["oacnativeproduction"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["oci_compute"]}, "resource_collection_enabled": true, "user_ocid": "ocid1.user.test"}, "id": "ocid1.tenancy.dummy_value", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Create tenancy config returns "Conflict" response
    Given new "CreateTenancyConfig" request
    And body with value {"data": {"attributes": {"auth_credentials": {"fingerprint": "a7:b5:54:f2:da:a2:d7:b0:ed:f4:79:47:93:64:12:b1", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmMo2jwJXWTt0y\nk+X6biZycflZSwOAP/iNeAZPTWwhYxj9pxDvd5OfiIe+o/7eupk/3q+fRsSaztPn\nJwI/JnbQz5IT5miLi/apIozg870FFxjrgRxSGjo7BNH0dLKITc5nLDLBnOEzxR2Y\nk9+0dFaiNlcodFULlg75trqbILRSc6jn9Tp9G8C5e9cj+LYQuUu2JwIqhCJqcNcU\nt+lRL5odBJhZ85KlugKyUg6LN3VQIdOpTtPBMXYA1oBgDCbe5Rw5yzgnd0KtSFf3\nGOmLfR95gQshLfbGavLOTh9ioaOj/2hT9HrsEe1VWgX3m1WibqKiPc4OA4BGGToN\n9tzN/t89AgMBAAECggEAVFKD4JherXwX6Ih3f6cRZLGFBJP1s8VBM225LdUnTo07\n6b4w7n6p7KBV1xjXwGPGS0yNqG88YxsbEkWNc0Ltt6YJBIW7d0nNHSVFewDPX1zH\nrP01xEZAUx9v8uqehl+LoHchTXBuJlkVWgt0zdbU+bo+YG0dlSJOeM4IQZrHQqlQ\ne4PNk73rot9NSqiKQFXUroaoVPTkUHb3idpLX60K3MgIBoAm4DpJ6cMItb4hyHv5\npNZhHQbr9Eciz2tj+OhQTYKCrAd0gJgl0tC+6L3kzkmiYE3ceGphqWfI9bX52Y96\nwpgAtYi6o8wTykgRLabLc6vSQ9RegWEh7P8iSAvAlQKBgQDX5wJhYeWDdG4uPqLC\nX3EtnR3y5zYgOd7cVtMr1DIvXa4I8PSIOC4Wnb/5A1S03dJ2e8GJ/qSbl5R2fsDr\nXhjIm/KeBPI9p2dVZM8fPoWppR3SgDaHY5qxAED111DnEZuTMl5BO87QZXurTSiF\nfbGsWaVqdVieRAQ3b5DEkC9TSwKBgQDFEFgui7iyPhQaQafsjnVbWyrWF821xjTG\nb6Bo4FO97c9pw/tbkpfM+dcOU4SsZL8HjwGBUhUsDsVOX7m/sWRjZqNM5t/VR+52\n9ygIPEjNyh0b3aARgn8AQ8n+RZvl1Z2A32KCO3MFzhpVKnv2sdSc1TNHQkuJH/rq\neUAm3El6lwKBgQCK8w+jIOAXRB2NAZ66PbaXRqD5rTg2cUguwmpRsNVDiqTw+DJI\nYO+4enoMhspDROeofWlHqGzD/j/8KwN59ys4ILV6YXCNoWltmd17HD/luHCDAyUU\n6VOrSqCEF7jnnXtktmvWy+kEUevPiW7kyspIQ8GjzDXmVZvpGZIwDyOGFQKBgGtS\nl3PiDFimjnQuRbIDc86pPA8VL6dLpvpbWNVFNtY9abSEU6RvldTATGs0+RCaXZ9U\nNtGjTnyMHtCsOZE4nx+zikQbiNOzNR/9QwQZMN1Csc+3R7HBjEEsqhmc92aYjArf\nndqnXeFPee/gD1svRkeTpTWt2U146UJBfrqrRilJAoGAQp7FtEtps5I9xK92AVpD\nHj2p1JNKzLCRtWQ8j4jthKqR0iTQ9SwQyjiAvcKc7HdMaG11gmr5XbmKAzelVC+f\no9kEwoumo8yHVn5Ztp4F2cxaD6+MzSJ/I6WesPyePUD7sPeorXByg1UNOXyzqDub\n/aU4/sNo2f8epM9l7QGiCtY=\n-----END PRIVATE KEY-----"}, "config_version": 2, "home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["oacnativeproduction"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["oci_compute"]}, "resource_collection_enabled": true, "user_ocid": "ocid1.user.test"}, "id": "ocid1.tenancy.dummy_value", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/emerging-cloud-integrations
  Scenario: Create tenancy config returns "Created" response
    Given new "CreateTenancyConfig" request
    And body with value {"data": {"attributes": {"auth_credentials": {"fingerprint": "a7:b5:54:f2:da:a2:d7:b0:ed:f4:79:47:93:64:12:b1", "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmMo2jwJXWTt0y\nk+X6biZycflZSwOAP/iNeAZPTWwhYxj9pxDvd5OfiIe+o/7eupk/3q+fRsSaztPn\nJwI/JnbQz5IT5miLi/apIozg870FFxjrgRxSGjo7BNH0dLKITc5nLDLBnOEzxR2Y\nk9+0dFaiNlcodFULlg75trqbILRSc6jn9Tp9G8C5e9cj+LYQuUu2JwIqhCJqcNcU\nt+lRL5odBJhZ85KlugKyUg6LN3VQIdOpTtPBMXYA1oBgDCbe5Rw5yzgnd0KtSFf3\nGOmLfR95gQshLfbGavLOTh9ioaOj/2hT9HrsEe1VWgX3m1WibqKiPc4OA4BGGToN\n9tzN/t89AgMBAAECggEAVFKD4JherXwX6Ih3f6cRZLGFBJP1s8VBM225LdUnTo07\n6b4w7n6p7KBV1xjXwGPGS0yNqG88YxsbEkWNc0Ltt6YJBIW7d0nNHSVFewDPX1zH\nrP01xEZAUx9v8uqehl+LoHchTXBuJlkVWgt0zdbU+bo+YG0dlSJOeM4IQZrHQqlQ\ne4PNk73rot9NSqiKQFXUroaoVPTkUHb3idpLX60K3MgIBoAm4DpJ6cMItb4hyHv5\npNZhHQbr9Eciz2tj+OhQTYKCrAd0gJgl0tC+6L3kzkmiYE3ceGphqWfI9bX52Y96\nwpgAtYi6o8wTykgRLabLc6vSQ9RegWEh7P8iSAvAlQKBgQDX5wJhYeWDdG4uPqLC\nX3EtnR3y5zYgOd7cVtMr1DIvXa4I8PSIOC4Wnb/5A1S03dJ2e8GJ/qSbl5R2fsDr\nXhjIm/KeBPI9p2dVZM8fPoWppR3SgDaHY5qxAED111DnEZuTMl5BO87QZXurTSiF\nfbGsWaVqdVieRAQ3b5DEkC9TSwKBgQDFEFgui7iyPhQaQafsjnVbWyrWF821xjTG\nb6Bo4FO97c9pw/tbkpfM+dcOU4SsZL8HjwGBUhUsDsVOX7m/sWRjZqNM5t/VR+52\n9ygIPEjNyh0b3aARgn8AQ8n+RZvl1Z2A32KCO3MFzhpVKnv2sdSc1TNHQkuJH/rq\neUAm3El6lwKBgQCK8w+jIOAXRB2NAZ66PbaXRqD5rTg2cUguwmpRsNVDiqTw+DJI\nYO+4enoMhspDROeofWlHqGzD/j/8KwN59ys4ILV6YXCNoWltmd17HD/luHCDAyUU\n6VOrSqCEF7jnnXtktmvWy+kEUevPiW7kyspIQ8GjzDXmVZvpGZIwDyOGFQKBgGtS\nl3PiDFimjnQuRbIDc86pPA8VL6dLpvpbWNVFNtY9abSEU6RvldTATGs0+RCaXZ9U\nNtGjTnyMHtCsOZE4nx+zikQbiNOzNR/9QwQZMN1Csc+3R7HBjEEsqhmc92aYjArf\nndqnXeFPee/gD1svRkeTpTWt2U146UJBfrqrRilJAoGAQp7FtEtps5I9xK92AVpD\nHj2p1JNKzLCRtWQ8j4jthKqR0iTQ9SwQyjiAvcKc7HdMaG11gmr5XbmKAzelVC+f\no9kEwoumo8yHVn5Ztp4F2cxaD6+MzSJ/I6WesPyePUD7sPeorXByg1UNOXyzqDub\n/aU4/sNo2f8epM9l7QGiCtY=\n-----END PRIVATE KEY-----"}, "config_version": 2, "home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["oacnativeproduction"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["oci_compute"]}, "resource_collection_enabled": true, "user_ocid": "ocid1.user.test"}, "id": "ocid1.tenancy.dummy_value", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 201 Created

  @team:DataDog/emerging-cloud-integrations
  Scenario: Delete tenancy config returns "No Content" response
    Given there is a valid "oci_tenancy" resource in the system
    And new "DeleteTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "oci_tenancy.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/emerging-cloud-integrations
  Scenario: Delete tenancy config returns "Not Found" response
    Given new "DeleteTenancyConfig" request
    And request contains "tenancy_ocid" parameter with value "ocid1.tenancy.fake"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/emerging-cloud-integrations
  Scenario: Get tenancy config returns "Not Found" response
    Given new "GetTenancyConfig" request
    And request contains "tenancy_ocid" parameter with value "ocid1.tenancy.fake"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/emerging-cloud-integrations
  Scenario: Get tenancy config returns "OK" response
    Given there is a valid "oci_tenancy" resource in the system
    And new "GetTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "oci_tenancy.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{oci_tenancy.data.id}}"

  @team:DataDog/emerging-cloud-integrations
  Scenario: Get tenancy configs returns "OK" response
    Given there is a valid "oci_tenancy" resource in the system
    And new "GetTenancyConfigs" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].id" is equal to "{{oci_tenancy.data.id}}"

  @team:DataDog/emerging-cloud-integrations
  Scenario: Update tenancy config returns "Bad Request" response
    Given there is a valid "oci_tenancy" resource in the system
    And new "UpdateTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "oci_tenancy.data.id"
    And body with value {"data": {"attributes": {"home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["objectstorage"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["oci_compute"]}, "resource_collection_enabled": true, "user_ocid": "user.test"}, "id": "ocid1.tenancy.dummy_value", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/emerging-cloud-integrations
  Scenario: Update tenancy config returns "Not Found" response
    Given new "UpdateTenancyConfig" request
    And request contains "tenancy_ocid" parameter with value "ocid1.tenancy.fake"
    And body with value {"data": {"attributes": {"home_region": "us-ashburn-1", "logs_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "enabled_services": ["objectstorage"]}, "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": true, "excluded_services": ["oci_compute"]}, "resource_collection_enabled": true, "user_ocid": "ocid1.user.test"}, "id": "ocid1.tenancy.fake", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/emerging-cloud-integrations
  Scenario: Update tenancy config returns "OK" response
    Given there is a valid "oci_tenancy" resource in the system
    And new "UpdateTenancyConfig" request
    And request contains "tenancy_ocid" parameter from "oci_tenancy.data.id"
    And body with value {"data": {"attributes": {"home_region": "us-sanjose-1", "metrics_config": {"compartment_tag_filters": ["datadog:true", "env:prod"], "enabled": false, "excluded_services": []}, "resource_collection_enabled": false, "user_ocid": "ocid1.user.test_updated"}, "id": "{{oci_tenancy.data.id}}", "type": "oci_tenancy"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "{{oci_tenancy.data.id}}"
    And the response "data.attributes.user_ocid" is equal to "{{oci_tenancy.data.attributes.user_ocid}}_updated"
    And the response "data.attributes.home_region" is equal to "us-sanjose-1"
