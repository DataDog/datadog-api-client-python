@endpoint(hosts) @endpoint(hosts-v1)
Feature: Hosts
  Get information about your live hosts in Datadog.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Hosts" API

  @generated @skip @team:DataDog/core-index
  Scenario: Get all hosts for your organization returns "Invalid Parameter Error" response
    Given new "ListHosts" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @integration-only @team:DataDog/core-index
  Scenario: Get all hosts for your organization returns "OK" response
    Given new "ListHosts" request
    And request contains "filter" parameter with value "env:ci"
    When the request is sent
    Then the response status is 200 OK

  @replay-only @team:DataDog/core-index
  Scenario: Get all hosts with metadata deserializes successfully
    Given new "ListHosts" request
    And request contains "include_hosts_metadata" parameter with value true
    When the request is sent
    Then the response status is 200 OK
    And the response "total_returned" is equal to 1
    And the response "host_list[0].meta.platform" is equal to "linux"
    And the response "host_list[0].meta.nixV" is equal to ["ubuntu","18.04",""]
    And the response "host_list[0].meta.install_method.tool" is equal to "install_script"
    And the response "host_list[0].meta.agent_checks[0]" is equal to ["ntp","ntp","ntp:d884b5186b651429","OK","",""]
    And the response "host_list[0].meta.gohai" is equal to "{\"cpu\":{\"cache_size\":\"8192 KB\",\"cpu_cores\":\"1\",\"cpu_logical_processors\":\"1\",\"family\":\"6\",\"mhz\":\"2711.998\",\"model\":\"142\",\"model_name\":\"Intel(R) Core(TM) i7-8559U CPU @ 2.70GHz\",\"stepping\":\"10\",\"vendor_id\":\"GenuineIntel\"},\"filesystem\":[{\"kb_size\":\"3966892\",\"mounted_on\":\"/dev\",\"name\":\"udev\"},{\"kb_size\":\"797396\",\"mounted_on\":\"/run\",\"name\":\"tmpfs\"},{\"kb_size\":\"64800356\",\"mounted_on\":\"/\",\"name\":\"/dev/mapper/vagrant--vg-root\"},{\"kb_size\":\"3986968\",\"mounted_on\":\"/dev/shm\",\"name\":\"tmpfs\"},{\"kb_size\":\"5120\",\"mounted_on\":\"/run/lock\",\"name\":\"tmpfs\"},{\"kb_size\":\"3986968\",\"mounted_on\":\"/sys/fs/cgroup\",\"name\":\"tmpfs\"},{\"kb_size\":\"488245288\",\"mounted_on\":\"/vagrant\",\"name\":\"/vagrant\"},{\"kb_size\":\"797392\",\"mounted_on\":\"/run/user/1000\",\"name\":\"tmpfs\"}],\"memory\":{\"swap_total\":\"1003516kB\",\"total\":\"7973940kB\"},\"network\":{\"interfaces\":[{\"ipv4\":\"10.0.2.15\",\"ipv4-network\":\"10.0.2.0/24\",\"ipv6\":\"fe80::a00:27ff:fec2:be11\",\"ipv6-network\":\"fe80::/64\",\"macaddress\":\"08:00:27:c2:be:11\",\"name\":\"eth0\"},{\"ipv4\":\"192.168.122.1\",\"ipv4-network\":\"192.168.122.0/24\",\"macaddress\":\"52:54:00:6f:1c:bf\",\"name\":\"virbr0\"}],\"ipaddress\":\"10.0.2.15\",\"ipaddressv6\":\"fe80::a00:27ff:fec2:be11\",\"macaddress\":\"08:00:27:c2:be:11\"},\"platform\":{\"GOOARCH\":\"amd64\",\"GOOS\":\"linux\",\"goV\":\"1.16.7\",\"hardware_platform\":\"x86_64\",\"hostname\":\"vagrant\",\"kernel_name\":\"Linux\",\"kernel_release\":\"4.15.0-29-generic\",\"kernel_version\":\"#31-Ubuntu SMP Tue Jul 17 15:39:52 UTC 2018\",\"machine\":\"x86_64\",\"os\":\"GNU/Linux\",\"processor\":\"x86_64\",\"pythonV\":\"2.7.15rc1\"}}"

  @team:DataDog/core-index
  Scenario: Get all hosts with metadata for your organization returns "OK" response
    Given new "ListHosts" request
    And request contains "include_hosts_metadata" parameter with value true
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Get the total number of active hosts returns "Invalid Parameter Error" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Get the total number of active hosts returns "OK" response
    Given new "GetHostTotals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Mute a host returns "Invalid Parameter Error" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Mute a host returns "OK" response
    Given new "MuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    And body with value {"end": 1579098130, "message": "Muting this host for a test!", "override": false}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/core-index
  Scenario: Unmute a host returns "Invalid Parameter Error" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Invalid Parameter Error

  @generated @skip @team:DataDog/core-index
  Scenario: Unmute a host returns "OK" response
    Given new "UnmuteHost" request
    And request contains "host_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK
