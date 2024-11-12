@endpoint(aws-logs-integration) @endpoint(aws-logs-integration-v2)
Feature: AWS Logs Integration
  Configure your Datadog-AWS-Logs integration directly through Datadog API.
  For more information, see the [AWS integration
  page](https://docs.datadoghq.com/integrations/amazon_web_services/#log-
  collection).

  @team:DataDog/aws-integrations
  Scenario: Get list of AWS log ready services returns "AWS Logs Services List object" response
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "AWSLogsIntegration" API
    And operation "ListAWSLogsServices" enabled
    And new "ListAWSLogsServices" request
    When the request is sent
    Then the response status is 200 AWS Logs Services List object
