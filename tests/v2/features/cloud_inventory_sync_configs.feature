@endpoint(cloud-inventory-sync-configs) @endpoint(cloud-inventory-sync-configs-v2)
Feature: Cloud Inventory Sync Configs
  Enable Storage Management for S3 buckets, GCS buckets, and Azure
  containers. Each configuration registers the destination that holds
  inventory reports for the storage being monitored.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "CloudInventorySyncConfigs" API
    And operation "UpsertSyncConfig" enabled
    And new "UpsertSyncConfig" request
    And body with value {"data": {"attributes": {"aws": {"aws_account_id": "123456789012", "destination_bucket_name": "my-inventory-bucket", "destination_bucket_region": "us-east-1", "destination_prefix": "logs/"}, "azure": {"client_id": "11111111-1111-1111-1111-111111111111", "container": "inventory-container", "resource_group": "my-resource-group", "storage_account": "mystorageaccount", "subscription_id": "33333333-3333-3333-3333-333333333333", "tenant_id": "22222222-2222-2222-2222-222222222222"}, "gcp": {"destination_bucket_name": "my-inventory-reports", "project_id": "my-gcp-project", "service_account_email": "reader@my-gcp-project.iam.gserviceaccount.com", "source_bucket_name": "my-monitored-bucket"}}, "id": "aws", "type": "cloud_provider"}}

  @generated @skip @team:DataDog/storage-management
  Scenario: Enable Storage Management for a bucket returns "Bad Request" response
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/storage-management
  Scenario: Enable Storage Management for a bucket returns "OK" response
    When the request is sent
    Then the response status is 200 OK
