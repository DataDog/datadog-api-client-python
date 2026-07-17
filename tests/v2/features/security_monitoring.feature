@endpoint(security-monitoring) @endpoint(security-monitoring-v2)
Feature: Security Monitoring
  Create and manage your security rules, signals, filters, and more. See the
  [Datadog Security page](https://docs.datadoghq.com/security/) for more
  information.

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "SecurityMonitoring" API

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Activate an entity context sync integration returns "Bad Request" response
    Given operation "ActivateIntegration" enabled
    And new "ActivateIntegration" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "default", "name": "My Entra ID Integration", "settings": {"setting1": "value1"}}, "type": "activate_entra_id_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Activate an entity context sync integration returns "Not Found" response
    Given operation "ActivateIntegration" enabled
    And new "ActivateIntegration" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "default", "name": "My Entra ID Integration", "settings": {"setting1": "value1"}}, "type": "activate_entra_id_request"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Activate an entity context sync integration returns "OK" response
    Given operation "ActivateIntegration" enabled
    And new "ActivateIntegration" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "default", "name": "My Entra ID Integration", "settings": {"setting1": "value1"}}, "type": "activate_entra_id_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Activate content pack returns "Accepted" response
    Given operation "ActivateContentPack" enabled
    And new "ActivateContentPack" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Activate content pack returns "Not Found" response
    Given operation "ActivateContentPack" enabled
    And new "ActivateContentPack" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Analyze code returns "Bad Request" response
    Given operation "CreateStaticAnalysisServerAnalysis" enabled
    And new "CreateStaticAnalysisServerAnalysis" request
    And body with value {"data": {"attributes": {"code": "aW1wb3J0IHN5cw==", "file_encoding": "utf-8", "filename": "test.py", "language": "python", "rules": [{"category": "BEST_PRACTICES", "checksum": "abc123def456", "code": "ZnVuY3Rpb24gdmlzaXQobm9kZSkge30=", "entity_checked": null, "id": "python-best-practices/no-exit", "language": "python", "regex": null, "severity": "WARNING", "tree_sitter_query": "KGNhbGwgbmFtZTogKGF0dHJpYnV0ZSkpQHZhbA==", "type": "TREE_SITTER_QUERY"}]}, "type": "analysis_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Analyze code returns "OK" response
    Given operation "CreateStaticAnalysisServerAnalysis" enabled
    And new "CreateStaticAnalysisServerAnalysis" request
    And body with value {"data": {"attributes": {"code": "aW1wb3J0IHN5cw==", "file_encoding": "utf-8", "filename": "test.py", "language": "python", "rules": [{"category": "BEST_PRACTICES", "checksum": "abc123def456", "code": "ZnVuY3Rpb24gdmlzaXQobm9kZSkge30=", "entity_checked": null, "id": "python-best-practices/no-exit", "language": "python", "regex": null, "severity": "WARNING", "tree_sitter_query": "KGNhbGwgbmFtZTogKGF0dHJpYnV0ZSkpQHZhbA==", "type": "TREE_SITTER_QUERY"}]}, "type": "analysis_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Assign or unassign security findings returns "Accepted" response
    Given operation "UpdateFindingsAssignee" enabled
    And new "UpdateFindingsAssignee" request
    And body with value {"data": {"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "assignee"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Assign or unassign security findings returns "Bad Request" response
    Given operation "UpdateFindingsAssignee" enabled
    And new "UpdateFindingsAssignee" request
    And body with value {"data": {"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "assignee"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Assign or unassign security findings returns "Not Found" response
    Given operation "UpdateFindingsAssignee" enabled
    And new "UpdateFindingsAssignee" request
    And body with value {"data": {"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0"}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "assignee"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-investigation
  Scenario: Attach security finding to a Jira issue returns "OK" response
    Given new "AttachJiraIssue" request
    And body with value {"data": {"attributes": {"jira_issue_url": "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"}, "relationships": {"findings": {"data": [{"id": "OTQ3NjJkMmYwMTIzMzMxNTc1Y2Q4MTA5NWU0NTBmMDl-ZjE3NjMxZWVkYzBjZGI1NDY2NWY2OGQxZDk4MDY4MmI=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.status_group" is equal to "SG_OPEN"
    And the response "data.attributes.insights" has item with field "resource_id" with value "OTQ3NjJkMmYwMTIzMzMxNTc1Y2Q4MTA5NWU0NTBmMDl-ZjE3NjMxZWVkYzBjZGI1NDY2NWY2OGQxZDk4MDY4MmI="
    And the response "data.attributes.jira_issue.result.issue_url" is equal to "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"

  @team:DataDog/k9-investigation
  Scenario: Attach security finding to a case returns "OK" response
    Given new "AttachCase" request
    And request contains "case_id" parameter with value "7d16945b-baf8-411e-ab2a-20fe43af1ea3"
    And body with value {"data": {"id": "7d16945b-baf8-411e-ab2a-20fe43af1ea3", "relationships": {"findings": {"data": [{"id": "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=", "type": "findings"}]}}, "type": "cases"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "7d16945b-baf8-411e-ab2a-20fe43af1ea3"
    And the response "data.attributes.status_group" is equal to "SG_OPEN"
    And the response "data.attributes.insights" has item with field "resource_id" with value "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y="

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Jira issue returns "Bad Request" response
    Given new "AttachJiraIssue" request
    And body with value {"data": {"attributes": {"jira_issue_url": "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"}, "relationships": {"findings": {"data": []}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Jira issue returns "Not Found" response
    Given new "AttachJiraIssue" request
    And body with value {"data": {"attributes": {"jira_issue_url": "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"}, "relationships": {"findings": {"data": [{"id": "wrong-finding-id", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Jira issue returns "OK" response
    Given new "AttachJiraIssue" request
    And body with value {"data": {"attributes": {"jira_issue_url": "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"}, "relationships": {"findings": {"data": [{"id": "OTQ3NjJkMmYwMTIzMzMxNTc1Y2Q4MTA5NWU0NTBmMDl-ZjE3NjMxZWVkYzBjZGI1NDY2NWY2OGQxZDk4MDY4MmI=", "type": "findings"}, {"id": "MTNjN2ZmYWMzMDIxYmU1ZDFiZDRjNWUwN2I1NzVmY2F-YTA3MzllMTUzNWM3NmEyZjdiNzEzOWM5YmViZTMzOGM=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.status_group" is equal to "SG_OPEN"
    And the response "data.attributes.insights" has item with field "resource_id" with value "OTQ3NjJkMmYwMTIzMzMxNTc1Y2Q4MTA5NWU0NTBmMDl-ZjE3NjMxZWVkYzBjZGI1NDY2NWY2OGQxZDk4MDY4MmI="
    And the response "data.attributes.insights" has item with field "resource_id" with value "MTNjN2ZmYWMzMDIxYmU1ZDFiZDRjNWUwN2I1NzVmY2F-YTA3MzllMTUzNWM3NmEyZjdiNzEzOWM5YmViZTMzOGM="
    And the response "data.attributes.jira_issue.result.issue_url" is equal to "https://datadoghq-sandbox-538.atlassian.net/browse/CSMSEC-105476"

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Linear issue returns "Bad Request" response
    Given operation "AttachLinearIssue" enabled
    And new "AttachLinearIssue" request
    And body with value {"data": {"attributes": {"linear_issue_url": "https://linear.app/your-workspace/issue/ENG-123"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Linear issue returns "Not Found" response
    Given operation "AttachLinearIssue" enabled
    And new "AttachLinearIssue" request
    And body with value {"data": {"attributes": {"linear_issue_url": "https://linear.app/your-workspace/issue/ENG-123"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a Linear issue returns "OK" response
    Given operation "AttachLinearIssue" enabled
    And new "AttachLinearIssue" request
    And body with value {"data": {"attributes": {"linear_issue_url": "https://linear.app/your-workspace/issue/ENG-123"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a ServiceNow ticket returns "Bad Request" response
    Given new "AttachServiceNowTicket" request
    And body with value {"data": {"attributes": {"servicenow_ticket_url": "https://example.service-now.com/now/nav/ui/classic/params/target/incident.do?sys_id=abcdef0123456789abcdef0123456789"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a ServiceNow ticket returns "Not Found" response
    Given new "AttachServiceNowTicket" request
    And body with value {"data": {"attributes": {"servicenow_ticket_url": "https://example.service-now.com/now/nav/ui/classic/params/target/incident.do?sys_id=abcdef0123456789abcdef0123456789"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Attach security findings to a ServiceNow ticket returns "OK" response
    Given new "AttachServiceNowTicket" request
    And body with value {"data": {"attributes": {"servicenow_ticket_url": "https://example.service-now.com/now/nav/ui/classic/params/target/incident.do?sys_id=abcdef0123456789abcdef0123456789"}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a case returns "Bad Request" response
    Given new "AttachCase" request
    And request contains "case_id" parameter with value "7d16945b-baf8-411e-ab2a-20fe43af1ea3"
    And body with value {"data": {"id": "7d16945b-baf8-411e-ab2a-20fe43af1ea3", "relationships": {"findings": {"data": []}}, "type": "cases"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a case returns "Not Found" response
    Given new "AttachCase" request
    And request contains "case_id" parameter with value "wrong-case-id"
    And body with value {"data": {"id": "wrong-case-id", "relationships": {"findings": {"data": [{"id": "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=", "type": "findings"}]}}, "type": "cases"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-investigation
  Scenario: Attach security findings to a case returns "OK" response
    Given new "AttachCase" request
    And request contains "case_id" parameter with value "7d16945b-baf8-411e-ab2a-20fe43af1ea3"
    And body with value {"data": {"id": "7d16945b-baf8-411e-ab2a-20fe43af1ea3", "relationships": {"findings": {"data": [{"id": "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=", "type": "findings"}, {"id": "MmUzMzZkODQ2YTI3NDU0OTk4NDk3NzhkOTY5YjU2Zjh-YWJjZGI1ODI4OTYzNWM3ZmUwZTBlOWRkYTRiMGUyOGQ=", "type": "findings"}]}}, "type": "cases"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" is equal to "7d16945b-baf8-411e-ab2a-20fe43af1ea3"
    And the response "data.attributes.status_group" is equal to "SG_OPEN"
    And the response "data.attributes.insights" has item with field "resource_id" with value "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y="
    And the response "data.attributes.insights" has item with field "resource_id" with value "MmUzMzZkODQ2YTI3NDU0OTk4NDk3NzhkOTY5YjU2Zjh-YWJjZGI1ODI4OTYzNWM3ZmUwZTBlOWRkYTRiMGUyOGQ="

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk convert rules to Terraform returns "Bad Request" response
    Given new "BulkConvertExistingSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["def-000-u7q", "def-000-7dd"]}, "id": "convert_bulk", "type": "security_monitoring_rules_convert_bulk"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk convert rules to Terraform returns "Not Found" response
    Given new "BulkConvertExistingSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["def-000-u7q", "def-000-7dd"]}, "id": "convert_bulk", "type": "security_monitoring_rules_convert_bulk"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk convert rules to Terraform returns "OK" response
    Given new "BulkConvertExistingSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["def-000-u7q", "def-000-7dd"]}, "id": "convert_bulk", "type": "security_monitoring_rules_convert_bulk"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk delete security monitoring rules returns "Bad Request" response
    Given new "BulkDeleteSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["abc-000-u7q", "abc-000-7dd"]}, "type": "bulk_delete_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk delete security monitoring rules returns "Not Found" response
    Given new "BulkDeleteSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["abc-000-u7q", "abc-000-7dd"]}, "type": "bulk_delete_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk delete security monitoring rules returns "OK" response
    Given new "BulkDeleteSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["abc-000-u7q", "abc-000-7dd"]}, "type": "bulk_delete_rules"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk export security monitoring rules returns "Bad Request" response
    Given new "BulkExportSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": []}, "type": "security_monitoring_rules_bulk_export"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk export security monitoring rules returns "Not Found" response
    Given new "BulkExportSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["non-existent-rule-id"]}, "type": "security_monitoring_rules_bulk_export"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Bulk export security monitoring rules returns "OK" response
    Given there is a valid "security_rule" in the system
    And new "BulkExportSecurityMonitoringRules" request
    And body with value {"data": {"attributes": {"ruleIds": ["{{ security_rule.id }}"]}, "type": "security_monitoring_rules_bulk_export"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk subscribe to sample log generation returns "Bad Request" response
    Given operation "BulkCreateSampleLogGenerationSubscriptions" enabled
    And new "BulkCreateSampleLogGenerationSubscriptions" request
    And body with value {"data": {"attributes": {"content_pack_ids": ["aws-cloudtrail"], "duration": "3d"}, "type": "bulk_subscription_requests"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk subscribe to sample log generation returns "OK" response
    Given operation "BulkCreateSampleLogGenerationSubscriptions" enabled
    And new "BulkCreateSampleLogGenerationSubscriptions" request
    And body with value {"data": {"attributes": {"content_pack_ids": ["aws-cloudtrail"], "duration": "3d"}, "type": "bulk_subscription_requests"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk update security signals returns "Bad Request" response
    Given new "BulkEditSecurityMonitoringSignals" request
    And body with value {"data": [{"attributes": {"archive_reason": "none", "assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "state": "open"}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk update security signals returns "OK" response
    Given new "BulkEditSecurityMonitoringSignals" request
    And body with value {"data": [{"attributes": {"archive_reason": "none", "assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "state": "open"}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk update triage assignee of security signals returns "Bad Request" response
    Given operation "BulkEditSecurityMonitoringSignalsAssignee" enabled
    And new "BulkEditSecurityMonitoringSignalsAssignee" request
    And body with value {"data": [{"attributes": {}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk update triage assignee of security signals returns "OK" response
    Given new "BulkEditSecurityMonitoringSignalsAssignee" request
    And body with value {"data": [{"attributes": {"assignee": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Bulk update triage state of security signals returns "Bad Request" response
    Given operation "BulkEditSecurityMonitoringSignalsState" enabled
    And new "BulkEditSecurityMonitoringSignalsState" request
    And body with value {"data": [{"attributes": {}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Bulk update triage state of security signals returns "OK" response
    Given new "BulkEditSecurityMonitoringSignalsState" request
    And body with value {"data": [{"attributes": {"archive_reason": "none", "state": "open"}, "id": "AAAAAWgN8Xwgr1vKDQAAAABBV2dOOFh3ZzZobm1mWXJFYTR0OA", "type": "signal"}]}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Cancel a historical job returns "Bad Request" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Cancel a historical job returns "Conflict" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/cloud-siem
  Scenario: Cancel a historical job returns "Not Found" response
    Given operation "CancelHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Cancel a historical job returns "OK" response
    Given operation "CancelHistoricalJob" enabled
    And operation "RunHistoricalJob" enabled
    And new "CancelHistoricalJob" request
    And there is a valid "historical_job" in the system
    And request contains "job_id" parameter from "historical_job.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Change the related incidents of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Change the related incidents of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Change the related incidents of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalIncidents" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"incident_ids": [2066]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Change the triage state of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Change the triage state of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Change the triage state of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalState" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"archive_reason": "none", "state": "open"}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Convert a job result to a signal returns "Bad Request" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Convert a job result to a signal returns "Not Found" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Convert a job result to a signal returns "OK" response
    Given operation "ConvertJobResultToSignal" enabled
    And new "ConvertJobResultToSignal" request
    And body with value {"data": {"attributes": {"jobResultIds": [""], "notifications": [""], "signalMessage": "A large number of failed login attempts.", "signalSeverity": "critical"}, "type": "historicalDetectionsJobResultSignalConversion"}}
    When the request is sent
    Then the response status is 204 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Convert a rule from JSON to Terraform returns "Bad Request" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Convert a rule from JSON to Terraform returns "Not Found" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Convert a rule from JSON to Terraform returns "OK" response
    Given new "ConvertSecurityMonitoringRuleFromJSONToTerraform" request
    And body with value {"name":"_{{ unique_hash }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection"}
    When the request is sent
    Then the response status is 200 OK
    And the response "terraformContent" is equal to "resource \"datadog_security_monitoring_rule\" \"_{{ unique_hash }}\" {\n\tname = \"_{{ unique_hash }}\"\n\tenabled = true\n\tquery {\n\t\tquery = \"@test:true\"\n\t\tgroup_by_fields = []\n\t\thas_optional_group_by_fields = false\n\t\tdistinct_fields = []\n\t\taggregation = \"count\"\n\t\tname = \"\"\n\t\tdata_source = \"logs\"\n\t}\n\toptions {\n\t\tkeep_alive = 3600\n\t\tmax_signal_duration = 86400\n\t\tdetection_method = \"threshold\"\n\t\tevaluation_window = 900\n\t}\n\tcase {\n\t\tname = \"\"\n\t\tstatus = \"info\"\n\t\tnotifications = []\n\t\tcondition = \"a > 0\"\n\t}\n\tmessage = \"Test rule\"\n\ttags = []\n\thas_extended_title = false\n\ttype = \"log_detection\"\n}\n"

  @skip @team:DataDog/cloud-siem
  Scenario: Convert an existing rule from JSON to Terraform returns "Bad Request" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Convert an existing rule from JSON to Terraform returns "Not Found" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Convert an existing rule from JSON to Terraform returns "OK" response
    Given new "ConvertExistingSecurityMonitoringRule" request
    And there is a valid "security_rule_hash" in the system
    And request contains "rule_id" parameter from "security_rule_hash.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "terraformContent" is equal to "resource \"datadog_security_monitoring_rule\" \"_{{ unique_hash }}\" {\n\tname = \"_{{ unique_hash }}\"\n\tenabled = true\n\tquery {\n\t\tquery = \"@test:true\"\n\t\tgroup_by_fields = []\n\t\thas_optional_group_by_fields = false\n\t\tdistinct_fields = []\n\t\taggregation = \"count\"\n\t\tname = \"\"\n\t\tdata_source = \"logs\"\n\t}\n\toptions {\n\t\tkeep_alive = 3600\n\t\tmax_signal_duration = 86400\n\t\tdetection_method = \"threshold\"\n\t\tevaluation_window = 900\n\t}\n\tcase {\n\t\tname = \"\"\n\t\tstatus = \"info\"\n\t\tnotifications = []\n\t\tcondition = \"a > 0\"\n\t}\n\tmessage = \"Test rule\"\n\ttags = []\n\thas_extended_title = false\n\ttype = \"log_detection\"\n}\n"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Convert security monitoring resource to Terraform returns "Bad Request" response
    Given operation "ConvertSecurityMonitoringTerraformResource" enabled
    And new "ConvertSecurityMonitoringTerraformResource" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_json": {"enabled": true, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "suppression_query": "env:staging status:low"}}, "id": "abc-123", "type": "convert_resource"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/cloud-siem
  Scenario: Convert security monitoring resource to Terraform returns "OK" response
    Given operation "ConvertSecurityMonitoringTerraformResource" enabled
    And new "ConvertSecurityMonitoringTerraformResource" request
    And request contains "resource_type" parameter with value "suppressions"
    And body with value {"data": {"type": "convert_resource", "id": "abc-123", "attributes": {"resource_json": {"enabled": true, "name": "Example-Security-Monitoring", "rule_query": "source:cloudtrail", "suppression_query": "env:test"}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.type_name" is equal to "datadog_security_monitoring_suppression"
    And the response "data.attributes.resource_id" is equal to "abc-123"

  @team:DataDog/k9-investigation
  Scenario: Create Jira issue for security finding returns "Created" response
    Given new "CreateJiraIssues" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "YmNlZmJhYTcyMDU5ZDk0ZDhiNjRmNGI0NDk4MDdiNzN-MDJlMjg0NzNmYzJiODY2MzJkNjU0OTI4NmVhZTUyY2U=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 1
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 1
    And the response "data[0].attributes.insights[0].resource_id" is equal to "YmNlZmJhYTcyMDU5ZDk0ZDhiNjRmNGI0NDk4MDdiNzN-MDJlMjg0NzNmYzJiODY2MzJkNjU0OTI4NmVhZTUyY2U="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"
    And the response "data[0].attributes.jira_issue.status" is equal to "COMPLETED"

  @team:DataDog/k9-investigation
  Scenario: Create Jira issue for security findings returns "Created" response
    Given new "CreateJiraIssues" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "a3ZoLXNjbS14eXV-aS0wNWY5MGYwMGE4NDg2ODdlOA==", "type": "findings"}, {"id": "eWswLWJsdC1hZm5-aS0wMjRlYTgwMzVkZTU1MGIwYQ==", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 1
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 2
    And the response "data[0].attributes.insights[1].resource_id" is equal to "eWswLWJsdC1hZm5-aS0wMjRlYTgwMzVkZTU1MGIwYQ=="
    And the response "data[0].attributes.insights[1].type" is equal to "SECURITY_FINDING"
    And the response "data[0].attributes.insights[0].resource_id" is equal to "a3ZoLXNjbS14eXV-aS0wNWY5MGYwMGE4NDg2ODdlOA=="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"
    And the response "data[0].attributes.jira_issue.status" is equal to "COMPLETED"

  @team:DataDog/k9-investigation
  Scenario: Create Jira issues for security findings returns "Bad Request" response
    Given new "CreateJiraIssues" request
    And body with value {"data": [{"attributes": {}, "relationships": {"findings": {"data": []}, "project": {"data": {"id": "7f198869-c7ef-4afc-97cf-da5cdc13b5c3", "type": "projects"}}}, "type": "jira_issues"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-investigation
  Scenario: Create Jira issues for security findings returns "Created" response
    Given new "CreateJiraIssues" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "eWswLWJsdC1hZm5-aS0wMjRlYTgwMzVkZTU1MGIwYQ==", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}, {"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "a3ZoLXNjbS14eXV-aS0wNWY5MGYwMGE4NDg2ODdlOA==", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "jira_issues"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 2
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 1
    And the response "data[0].attributes.insights[0].resource_id" is equal to "eWswLWJsdC1hZm5-aS0wMjRlYTgwMzVkZTU1MGIwYQ=="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"
    And the response "data[0].attributes.jira_issue.status" is equal to "COMPLETED"
    And the response "data[1]" has field "id"
    And the response "data[1].attributes.title" is equal to "A title"
    And the response "data[1].attributes.description" is equal to "A description"
    And the response "data[1].attributes.type" is equal to "SECURITY"
    And the response "data[1].attributes.insights" has length 1
    And the response "data[1].attributes.insights[0].resource_id" is equal to "a3ZoLXNjbS14eXV-aS0wNWY5MGYwMGE4NDg2ODdlOA=="
    And the response "data[1].attributes.insights[0].type" is equal to "SECURITY_FINDING"
    And the response "data[1].attributes.jira_issue.status" is equal to "COMPLETED"

  @team:DataDog/k9-investigation
  Scenario: Create Jira issues for security findings returns "Not Found" response
    Given new "CreateJiraIssues" request
    And body with value {"data": [{"attributes": {}, "relationships": {"findings": {"data": [{"id": "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=", "type": "findings"}]}, "project": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "projects"}}}, "type": "jira_issues"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create Linear issues for security findings returns "Bad Request" response
    Given operation "CreateLinearIssues" enabled
    And new "CreateLinearIssues" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the Linear issue.", "label_ids": ["a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d"], "linear_project_id": "d4c3b2a1-6f5e-8b7a-0d9c-2f1e4a3b6c5d", "priority": "NOT_DEFINED", "title": "A title for the Linear issue."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create Linear issues for security findings returns "Created" response
    Given operation "CreateLinearIssues" enabled
    And new "CreateLinearIssues" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the Linear issue.", "label_ids": ["a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d"], "linear_project_id": "d4c3b2a1-6f5e-8b7a-0d9c-2f1e4a3b6c5d", "priority": "NOT_DEFINED", "title": "A title for the Linear issue."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}]}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create Linear issues for security findings returns "Not Found" response
    Given operation "CreateLinearIssues" enabled
    And new "CreateLinearIssues" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the Linear issue.", "label_ids": ["a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d"], "linear_project_id": "d4c3b2a1-6f5e-8b7a-0d9c-2f1e4a3b6c5d", "priority": "NOT_DEFINED", "title": "A title for the Linear issue."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "linear_issues"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create ServiceNow tickets for security findings returns "Bad Request" response
    Given new "CreateServiceNowTickets" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the ServiceNow ticket.", "priority": "NOT_DEFINED", "title": "A title for the ServiceNow ticket."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create ServiceNow tickets for security findings returns "Created" response
    Given new "CreateServiceNowTickets" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the ServiceNow ticket.", "priority": "NOT_DEFINED", "title": "A title for the ServiceNow ticket."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}]}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Create ServiceNow tickets for security findings returns "Not Found" response
    Given new "CreateServiceNowTickets" request
    And body with value {"data": [{"attributes": {"assignee_id": "f315bdaf-9ee7-4808-a9c1-99c15bf0f4d0", "description": "A description of the ServiceNow ticket.", "priority": "NOT_DEFINED", "title": "A title for the ServiceNow ticket."}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}, "project": {"data": {"id": "aeadc05e-98a8-11ec-ac2c-da7ad0900001", "type": "projects"}}}, "type": "servicenow_tickets"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a cloud_configuration rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"type":"cloud_configuration","name":"{{ unique }}_cloud","isEnabled":false,"cases":[{"status":"info","notifications":["channel"]}],"options":{"complianceRuleOptions":{"resourceType":"gcp_compute_disk","complexRule": false,"regoRule":{"policy":"package datadog\n\nimport data.datadog.output as dd_output\n\nimport future.keywords.contains\nimport future.keywords.if\nimport future.keywords.in\n\nmilliseconds_in_a_day := ((1000 * 60) * 60) * 24\n\neval(iam_service_account_key) = \"skip\" if {\n\tiam_service_account_key.disabled\n} else = \"pass\" if {\n\t(iam_service_account_key.resource_seen_at / milliseconds_in_a_day) - (iam_service_account_key.valid_after_time / milliseconds_in_a_day) <= 90\n} else = \"fail\"\n\n# This part remains unchanged for all rules\nresults contains result if {\n\tsome resource in input.resources[input.main_resource_type]\n\tresult := dd_output.format(resource, eval(resource))\n}\n","resourceTypes":["gcp_compute_disk"]}}},"message":"ddd","tags":["my:tag"],"complianceSignalOptions":{"userActivationStatus":true,"userGroupByFields":["@account_id"]},"filters":[{"action":"require","query":"resource_id:helo*"},{"action":"suppress","query":"control:helo*"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud"
    And the response "type" is equal to "cloud_configuration"
    And the response "message" is equal to "ddd"
    And the response "options.complianceRuleOptions.resourceType" is equal to "gcp_compute_disk"

  @skip @team:DataDog/cloud-siem
  Scenario: Create a critical asset returns "Bad Request" response
    Given new "CreateSecurityMonitoringCriticalAsset" request
    And body with value {"data": {"type": "critical_assets", "attributes": {"query": "host:test"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a critical asset returns "Conflict" response
    Given new "CreateSecurityMonitoringCriticalAsset" request
    And body with value {"data": {"attributes": {"description": "Production database servers handling PII", "enabled": true, "query": "security:monitoring", "rule_query": "type:(log_detection OR signal_correlation OR workload_security OR application_security) source:cloudtrail", "severity": "increase", "tags": ["team:database", "source:cloudtrail"]}, "type": "critical_assets"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a critical asset returns "OK" response
    Given new "CreateSecurityMonitoringCriticalAsset" request
    And body with value {"data": {"type": "critical_assets", "attributes": {"query": "host:{{ unique_lower_alnum }}", "rule_query": "type:(log_detection OR signal_correlation OR workload_security OR application_security) source:cloudtrail", "severity": "decrease", "tags": ["team:security", "env:test"]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "critical_assets"
    And the response "data.attributes.severity" is equal to "decrease"

  @team:DataDog/cloud-siem
  Scenario: Create a custom framework returns "Bad Request" response
    Given new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Create a custom framework returns "Conflict" response
    Given there is a valid "custom_framework" in the system
    And new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 409 Conflict

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Create a custom framework returns "OK" response
    Given new "CreateCustomFramework" request
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a dataset returns "Bad Request" response
    Given operation "CreateSecurityMonitoringDataset" enabled
    And new "CreateSecurityMonitoringDataset" request
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetCreate"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a dataset returns "Conflict" response
    Given operation "CreateSecurityMonitoringDataset" enabled
    And new "CreateSecurityMonitoringDataset" request
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetCreate"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a dataset returns "Created" response
    Given operation "CreateSecurityMonitoringDataset" enabled
    And new "CreateSecurityMonitoringDataset" request
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetCreate"}}
    When the request is sent
    Then the response status is 201 Created

  @skip @team:DataDog/cloud-siem
  Scenario: Create a detection rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection", "referenceTables":[{"tableName": "synthetics_test_reference_table_dont_delete", "columnName": "value", "logFieldPath":"testtag", "checkPresence":true, "ruleQueryName":"a"}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "Test rule"
    And the response "referenceTables" is equal to [{"tableName": "synthetics_test_reference_table_dont_delete", "columnName": "value", "logFieldPath":"testtag", "checkPresence":true, "ruleQueryName":"a"}]

  @team:DataDog/cloud-siem
  Scenario: Create a detection rule with detection method 'anomaly_detection' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"queries":[{"aggregation":"count","dataSource":"logs","distinctFields":[],"groupByFields":["@usr.email","@network.client.ip"],"hasOptionalGroupByFields":false,"name":"","query":"service:app status:error"}],"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0.995"}],"message":"An anomaly detection rule","options":{"detectionMethod":"anomaly_detection","evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400,"anomalyDetectionOptions":{"bucketDuration":300,"learningDuration":24,"detectionTolerance":3,"learningPeriodBaseline":10}},"tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "anomaly_detection"
    And the response "options.anomalyDetectionOptions.bucketDuration" is equal to 300
    And the response "options.anomalyDetectionOptions.learningDuration" is equal to 24
    And the response "options.anomalyDetectionOptions.learningPeriodBaseline" is equal to 10
    And the response "options.anomalyDetectionOptions.detectionTolerance" is equal to 3

  @team:DataDog/cloud-siem
  Scenario: Create a detection rule with detection method 'anomaly_detection' with enabled feature 'instantaneousBaseline' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"queries":[{"aggregation":"count","dataSource":"logs","distinctFields":[],"groupByFields":["@usr.email","@network.client.ip"],"hasOptionalGroupByFields":false,"name":"","query":"service:app status:error"}],"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0.995"}],"message":"An anomaly detection rule","options":{"detectionMethod":"anomaly_detection","evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400,"anomalyDetectionOptions":{"bucketDuration":300,"learningDuration":24,"detectionTolerance":3,"instantaneousBaseline":true}},"tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "anomaly_detection"
    And the response "options.anomalyDetectionOptions.instantaneousBaseline" is equal to true

  @team:DataDog/cloud-siem
  Scenario: Create a detection rule with detection method 'sequence_detection' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"queries":[{"aggregation":"count","dataSource":"logs","distinctFields":[],"groupByFields":[],"hasOptionalGroupByFields":false,"name":"","query":"service:logs-rule-reducer source:paul test2"},{"aggregation":"count","dataSource":"logs","distinctFields":[],"groupByFields":[],"hasOptionalGroupByFields":false,"name":"","query":"service:logs-rule-reducer source:paul test1"}],"cases":[{"name":"","status":"info","notifications":[],"condition":"step_b > 0"}],"message":"Logs and signals asdf","options":{"detectionMethod":"sequence_detection","evaluationWindow":0,"keepAlive":300,"maxSignalDuration":600,"sequenceDetectionOptions":{"stepTransitions":[{"child":"step_b","evaluationWindow":900,"parent":"step_a"}],"steps":[{"condition":"a > 0","evaluationWindow":60,"name":"step_a"},{"condition":"b > 0","evaluationWindow":60,"name":"step_b"}]}},"tags":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "sequence_detection"

  @team:DataDog/cloud-siem
  Scenario: Create a detection rule with detection method 'third_party' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}","type":"log_detection","isEnabled":true,"thirdPartyCases":[{"query":"status:error","name":"high","status":"high"},{"query":"status:info","name":"low","status":"low"}],"queries":[],"cases":[],"message":"This is a third party rule","options":{"detectionMethod":"third_party","keepAlive":0,"maxSignalDuration":600,"thirdPartyRuleOptions":{"defaultStatus":"info","rootQueries":[{"query":"source:guardduty @details.alertType:*EC2*", "groupByFields":["instance-id"]},{"query":"source:guardduty", "groupByFields":[]}]}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "options.detectionMethod" is equal to "third_party"
    And the response "thirdPartyCases[0].query" is equal to "status:error"

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule with type 'application_security 'returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"type":"application_security","name":"{{unique}}_appsec_rule","queries":[{"query":"@appsec.security_activity:business_logic.users.login.failure","aggregation":"count","groupByFields":["service","@http.client_ip"],"distinctFields":[]}],"filters":[],"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 100000","actions":[{"type":"block_ip","options":{"duration":900}}, {"type":"user_behavior","options":{"userBehaviorName":"behavior"}}, {"type":"flag_ip","options":{"flaggedIPType":"FLAGGED"}}]}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900,"detectionMethod":"threshold"},"isEnabled":true,"message":"Test rule","tags":[],"groupSignalsBy":["service"]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_appsec_rule"
    And the response "type" is equal to "application_security"
    And the response "message" is equal to "Test rule"

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule with type 'impossible_travel' and baselineUserLocationsDuration returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"queries":[{"aggregation":"geo_data","groupByFields":["@usr.id"],"distinctFields":[],"metric":"@network.client.geoip","query":"*"}],"cases":[{"name":"","status":"info","notifications":[]}],"hasExtendedTitle":true,"message":"test","isEnabled":true,"options":{"maxSignalDuration":86400,"evaluationWindow":900,"keepAlive":3600,"detectionMethod":"impossible_travel","impossibleTravelOptions":{"baselineUserLocations":true,"baselineUserLocationsDuration":7}},"name":"{{ unique }}","type":"log_detection","tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "test"
    And the response "options.detectionMethod" is equal to "impossible_travel"
    And the response "options.impossibleTravelOptions.baselineUserLocations" is equal to true
    And the response "options.impossibleTravelOptions.baselineUserLocationsDuration" is equal to 7

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule with type 'impossible_travel' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"queries":[{"aggregation":"geo_data","groupByFields":["@usr.id"],"distinctFields":[],"metric":"@network.client.geoip","query":"*"}],"cases":[{"name":"","status":"info","notifications":[]}],"hasExtendedTitle":true,"message":"test","isEnabled":true,"options":{"maxSignalDuration":86400,"evaluationWindow":900,"keepAlive":3600,"detectionMethod":"impossible_travel","impossibleTravelOptions":{"baselineUserLocations":false}},"name":"{{ unique }}","type":"log_detection","tags":[],"filters":[]}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "test"
    And the response "options.detectionMethod" is equal to "impossible_travel"

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule with type 'signal_correlation' returns "OK" response
    Given there is a valid "security_rule" in the system
    And there is a valid "security_rule_bis" in the system
    And new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}_signal_rule", "queries":[{"ruleId":"{{ security_rule.id }}","aggregation":"event_count","correlatedByFields":["host"],"correlatedQueryIndex":1}, {"ruleId":"{{ security_rule_bis.id }}","aggregation":"event_count","correlatedByFields":["host"]}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0 && b > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test signal correlation rule","tags":[],"isEnabled":true, "type": "signal_correlation"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_signal_rule"
    And the response "type" is equal to "signal_correlation"
    And the response "message" is equal to "Test signal correlation rule"
    And the response "isEnabled" is equal to true

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a detection rule with type 'workload_security' returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"metric":""}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type": "workload_security"}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "workload_security"
    And the response "message" is equal to "Test rule"
    And the response "isEnabled" is equal to true

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a due date rule returns "Bad Request" response
    Given operation "CreateSecurityFindingsAutomationDueDateRule" enabled
    And new "CreateSecurityFindingsAutomationDueDateRule" request
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen", "reason_description": "Applied for production findings only"}, "enabled": true, "name": "Critical findings due in 7 days", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Create a due date rule returns "Successfully created the due date rule" response
    Given operation "CreateSecurityFindingsAutomationDueDateRule" enabled
    And new "CreateSecurityFindingsAutomationDueDateRule" request
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen"}, "enabled": true, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the due date rule
    And the response "data.type" is equal to "due_date_rules"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.enabled" is equal to true

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a due date rule returns "Unprocessable Entity" response
    Given operation "CreateSecurityFindingsAutomationDueDateRule" enabled
    And new "CreateSecurityFindingsAutomationDueDateRule" request
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen", "reason_description": "Applied for production findings only"}, "enabled": true, "name": "Critical findings due in 7 days", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a mute rule returns "Bad Request" response
    Given operation "CreateSecurityFindingsAutomationMuteRule" enabled
    And new "CreateSecurityFindingsAutomationMuteRule" request
    And body with value {"data": {"attributes": {"action": {"expire_at": 4070908800000, "reason": "risk_accepted", "reason_description": "Accepted for dev environments only"}, "enabled": true, "name": "Mute accepted risks in dev", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Create a mute rule returns "Successfully created the mute rule" response
    Given operation "CreateSecurityFindingsAutomationMuteRule" enabled
    And new "CreateSecurityFindingsAutomationMuteRule" request
    And body with value {"data": {"attributes": {"action": {"reason": "risk_accepted"}, "enabled": true, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the mute rule
    And the response "data.type" is equal to "mute_rules"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.enabled" is equal to true

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a mute rule returns "Unprocessable Entity" response
    Given operation "CreateSecurityFindingsAutomationMuteRule" enabled
    And new "CreateSecurityFindingsAutomationMuteRule" request
    And body with value {"data": {"attributes": {"action": {"expire_at": 4070908800000, "reason": "risk_accepted", "reason_description": "Accepted for dev environments only"}, "enabled": true, "name": "Mute accepted risks in dev", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Create a new signal-based notification rule returns "Bad Request" response
    Given new "CreateSignalNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "routing": {"mode": "manual"}, "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Create a new signal-based notification rule returns "Successfully created the notification rule." response
    Given new "CreateSignalNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the notification rule.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Create a new vulnerability-based notification rule returns "Bad Request" response
    Given new "CreateVulnerabilityNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "routing": {"mode": "manual"}, "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Create a new vulnerability-based notification rule returns "Successfully created the notification rule." response
    Given new "CreateVulnerabilityNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the notification rule.

  @team:DataDog/cloud-security-posture-management
  Scenario: Create a new vulnerability-based notification rule with sast and secret rule types returns "Successfully created the notification rule." response
    Given new "CreateVulnerabilityNotificationRule" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "{{ unique }}", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["sast_vulnerability", "secret_vulnerability"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the notification rule.

  @team:DataDog/cloud-siem
  Scenario: Create a scheduled detection rule returns "OK" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"indexes":["main"]}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection", "schedulingOptions": {"rrule": "FREQ=HOURLY;INTERVAL=2;", "start": "2025-06-18T12:00:00", "timezone": "Europe/Paris"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "type" is equal to "log_detection"
    And the response "message" is equal to "Test rule"
    And the response "schedulingOptions" is equal to {"rrule": "FREQ=HOURLY;INTERVAL=2;", "start": "2025-06-18T12:00:00", "timezone": "Europe/Paris"}

  @team:DataDog/cloud-siem
  Scenario: Create a scheduled rule without rrule returns "Bad Request" response
    Given new "CreateSecurityMonitoringRule" request
    And body with value {"name":"{{ unique }}", "queries":[{"query":"@test:true","aggregation":"count","groupByFields":[],"distinctFields":[],"indexes":["main"]}],"filters":[],"cases":[{"name":"","status":"info","condition":"a > 0","notifications":[]}],"options":{"evaluationWindow":900,"keepAlive":3600,"maxSignalDuration":86400},"message":"Test rule","tags":[],"isEnabled":true, "type":"log_detection", "schedulingOptions": {"start": "2025-06-18T12:00:00", "timezone": "Europe/Paris"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a security filter returns "Bad Request" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a security filter returns "Conflict" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/cloud-siem
  Scenario: Create a security filter returns "OK" response
    Given new "CreateSecurityFilter" request
    And body with value {"data": {"attributes": {"exclusion_filters": [{"name": "Exclude staging", "query": "source:staging"}], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}"}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.is_enabled" is equal to true
    And the response "data.attributes.exclusion_filters[0].name" is equal to "Exclude staging"
    And the response "data.attributes.exclusion_filters[0].query" is equal to "source:staging"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a suppression rule returns "Bad Request" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create a suppression rule returns "Conflict" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 409 Conflict

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a suppression rule returns "OK" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "start_date": {{ timestamp('now + 10d') }}000, "expiration_date": {{ timestamp('now + 21d') }}000, "name": "{{ unique }}", "rule_query": "type:log_detection source:cloudtrail", "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.rule_query" is equal to "type:log_detection source:cloudtrail"

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Create a suppression rule with an exclusion query returns "OK" response
    Given new "CreateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "start_date": {{ timestamp('now + 10d') }}000, "expiration_date": {{ timestamp('now + 21d') }}000, "name": "{{ unique }}", "rule_query": "type:log_detection source:cloudtrail", "data_exclusion_query": "account_id:12345"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.enabled" is equal to true
    And the response "data.attributes.rule_query" is equal to "type:log_detection source:cloudtrail"
    And the response "data.attributes.data_exclusion_query" is equal to "account_id:12345"

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a ticket creation rule returns "Bad Request" response
    Given operation "CreateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "CreateSecurityFindingsAutomationTicketCreationRule" request
    And body with value {"data": {"attributes": {"action": {"assignee_id": "22222222-2222-2222-2222-222222222222", "fields": {"labels": ["security"]}, "max_tickets_per_day": 100, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "Auto-create Jira tickets for critical findings", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Create a ticket creation rule returns "Successfully created the ticket creation rule" response
    Given operation "CreateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "CreateSecurityFindingsAutomationTicketCreationRule" request
    And body with value {"data": {"attributes": {"action": {"max_tickets_per_day": 10, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 201 Successfully created the ticket creation rule
    And the response "data.type" is equal to "ticket_creation_rules"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.enabled" is equal to true

  @generated @skip @team:DataDog/k9-automation
  Scenario: Create a ticket creation rule returns "Unprocessable Entity" response
    Given operation "CreateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "CreateSecurityFindingsAutomationTicketCreationRule" request
    And body with value {"data": {"attributes": {"action": {"assignee_id": "22222222-2222-2222-2222-222222222222", "fields": {"labels": ["security"]}, "max_tickets_per_day": 100, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "Auto-create Jira tickets for critical findings", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create an entity context sync configuration returns "Bad Request" response
    Given operation "CreateSecurityMonitoringIntegrationConfig" enabled
    And new "CreateSecurityMonitoringIntegrationConfig" request
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "integration_type": "GOOGLE_WORKSPACE", "name": "My GWS Integration", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}, "settings": {"setting1": "value1"}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Create an entity context sync configuration returns "OK" response
    Given operation "CreateSecurityMonitoringIntegrationConfig" enabled
    And new "CreateSecurityMonitoringIntegrationConfig" request
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "integration_type": "GOOGLE_WORKSPACE", "name": "My GWS Integration", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}, "settings": {"setting1": "value1"}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-investigation
  Scenario: Create case for security finding returns "Created" response
    Given new "CreateCases" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "YjdhNDM3N2QyNTFjYmUwYTY3NDdhMTg0YTk2Yjg5MDl-ZjNmMzAwOTFkZDNhNGQzYzI0MzgxNTk4MjRjZmE2NzE=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "cases"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 1
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 1
    And the response "data[0].attributes.insights[0].resource_id" is equal to "YjdhNDM3N2QyNTFjYmUwYTY3NDdhMTg0YTk2Yjg5MDl-ZjNmMzAwOTFkZDNhNGQzYzI0MzgxNTk4MjRjZmE2NzE="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"

  @team:DataDog/k9-investigation
  Scenario: Create case for security findings returns "Created" response
    Given new "CreateCases" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "ZTd5LWNuYi1seWV-aS0wMjI2NGZjZjRmZWQ5ODMyMg==", "type": "findings"}, {"id": "c2FuLXhyaS1kZnN-aS0wODM3MjVhMTM2MDExNzNkOQ==", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "cases"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 1
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 2
    And the response "data[0].attributes.insights[1].resource_id" is equal to "c2FuLXhyaS1kZnN-aS0wODM3MjVhMTM2MDExNzNkOQ=="
    And the response "data[0].attributes.insights[1].type" is equal to "SECURITY_FINDING"
    And the response "data[0].attributes.insights[0].resource_id" is equal to "ZTd5LWNuYi1seWV-aS0wMjI2NGZjZjRmZWQ5ODMyMg=="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"

  @team:DataDog/k9-investigation
  Scenario: Create cases for security findings returns "Bad Request" response
    Given new "CreateCases" request
    And body with value {"data": [{"attributes": {}, "relationships": {"findings": {"data": []}, "project": {"data": {"id": "7f198869-c7ef-4afc-97cf-da5cdc13b5c3", "type": "projects"}}}, "type": "cases"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-investigation
  Scenario: Create cases for security findings returns "Created" response
    Given new "CreateCases" request
    And body with value {"data": [{"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "YjdhNDM3N2QyNTFjYmUwYTY3NDdhMTg0YTk2Yjg5MDl-ZjNmMzAwOTFkZDNhNGQzYzI0MzgxNTk4MjRjZmE2NzE=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "cases"}, {"attributes": {"title": "A title", "description": "A description"}, "relationships": {"findings": {"data": [{"id": "OGRlMDIwYzk4MjFmZTZiNTQwMzk2ZjUxNzg0MDc0NjR-MTk3Yjk4MDI4ZDQ4YzI2ZGZiMWJmMTNhNDEwZGZkYWI=", "type": "findings"}]}, "project": {"data": {"id": "959a6f71-bac8-4027-b1d3-2264f569296f", "type": "projects"}}}, "type": "cases"}]}
    When the request is sent
    Then the response status is 201 Created
    And the response "data" has length 2
    And the response "data[0]" has field "id"
    And the response "data[0].attributes.title" is equal to "A title"
    And the response "data[0].attributes.description" is equal to "A description"
    And the response "data[0].attributes.type" is equal to "SECURITY"
    And the response "data[0].attributes.insights" has length 1
    And the response "data[0].attributes.insights[0].resource_id" is equal to "YjdhNDM3N2QyNTFjYmUwYTY3NDdhMTg0YTk2Yjg5MDl-ZjNmMzAwOTFkZDNhNGQzYzI0MzgxNTk4MjRjZmE2NzE="
    And the response "data[0].attributes.insights[0].type" is equal to "SECURITY_FINDING"
    And the response "data[1]" has field "id"
    And the response "data[1].attributes.title" is equal to "A title"
    And the response "data[1].attributes.description" is equal to "A description"
    And the response "data[1].attributes.type" is equal to "SECURITY"
    And the response "data[1].attributes.insights" has length 1
    And the response "data[1].attributes.insights[0].resource_id" is equal to "OGRlMDIwYzk4MjFmZTZiNTQwMzk2ZjUxNzg0MDc0NjR-MTk3Yjk4MDI4ZDQ4YzI2ZGZiMWJmMTNhNDEwZGZkYWI="
    And the response "data[1].attributes.insights[0].type" is equal to "SECURITY_FINDING"

  @team:DataDog/k9-investigation
  Scenario: Create cases for security findings returns "Not Found" response
    Given new "CreateCases" request
    And body with value {"data": [{"attributes": {}, "relationships": {"findings": {"data": [{"id": "ZGZhMDI3ZjdjMDM3YjJmNzcxNTlhZGMwMjdmZWNiNTZ-MTVlYTNmYWU3NjNlOTNlYTE2YjM4N2JmZmI4Yjk5N2Y=", "type": "findings"}]}, "project": {"data": {"id": "00000000-0000-0000-0000-000000000000", "type": "projects"}}}, "type": "cases"}]}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Create or update an indicator triage state returns "Bad Request" response
    Given operation "CreateIoCTriageState" enabled
    And new "CreateIoCTriageState" request
    And body with value {"data": {"attributes": {"indicator": "192.0.2.1", "triage_state": "invalid_state"}, "type": "ioc_triage_state"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Create or update an indicator triage state returns "Created" response
    Given operation "CreateIoCTriageState" enabled
    And new "CreateIoCTriageState" request
    And body with value {"data": {"attributes": {"indicator": "192.0.2.1", "triage_state": "reviewed"}, "type": "ioc_triage_state"}}
    When the request is sent
    Then the response status is 201 Created

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Deactivate an entity context sync integration returns "Not Found" response
    Given operation "DeactivateIntegration" enabled
    And new "DeactivateIntegration" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Deactivate an entity context sync integration returns "OK" response
    Given operation "DeactivateIntegration" enabled
    And new "DeactivateIntegration" request
    And request contains "integration_type" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Deactivate content pack returns "Accepted" response
    Given operation "DeactivateContentPack" enabled
    And new "DeactivateContentPack" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Deactivate content pack returns "Not Found" response
    Given operation "DeactivateContentPack" enabled
    And new "DeactivateContentPack" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Delete a critical asset returns "Not Found" response
    Given new "DeleteSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Delete a critical asset returns "OK" response
    Given there is a valid "critical_asset" in the system
    And new "DeleteSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter from "critical_asset.data.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-siem
  Scenario: Delete a custom framework returns "Bad Request" response
    Given new "DeleteCustomFramework" request
    And request contains "handle" parameter with value "handle-does-not-exist"
    And request contains "version" parameter with value "version-does-not-exist"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/cloud-siem
  Scenario: Delete a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "DeleteCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete a dataset returns "Bad Request" response
    Given operation "DeleteSecurityMonitoringDataset" enabled
    And new "DeleteSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete a dataset returns "No Content" response
    Given operation "DeleteSecurityMonitoringDataset" enabled
    And new "DeleteSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete a dataset returns "Not Found" response
    Given operation "DeleteSecurityMonitoringDataset" enabled
    And new "DeleteSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-automation
  Scenario: Delete a due date rule returns "Not Found" response
    Given operation "DeleteSecurityFindingsAutomationDueDateRule" enabled
    And new "DeleteSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Delete a due date rule returns "Rule successfully deleted." response
    Given operation "DeleteSecurityFindingsAutomationDueDateRule" enabled
    And there is a valid "valid_due_date_rule" in the system
    And new "DeleteSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "valid_due_date_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @generated @skip @team:DataDog/k9-automation
  Scenario: Delete a mute rule returns "Not Found" response
    Given operation "DeleteSecurityFindingsAutomationMuteRule" enabled
    And new "DeleteSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Delete a mute rule returns "Rule successfully deleted." response
    Given operation "DeleteSecurityFindingsAutomationMuteRule" enabled
    And there is a valid "valid_mute_rule" in the system
    And new "DeleteSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "valid_mute_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @skip @team:DataDog/cloud-siem
  Scenario: Delete a non existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "ThisRuleIdProbablyDoesntExist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Delete a security filter returns "No Content" response
    Given there is a valid "security_filter" in the system
    And new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete a security filter returns "Not Found" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete a security filter returns "OK" response
    Given new "DeleteSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a signal-based notification rule returns "Not Found" response
    Given new "DeleteSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a signal-based notification rule returns "Rule successfully deleted." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "DeleteSignalNotificationRule" request
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @skip @team:DataDog/cloud-siem
  Scenario: Delete a suppression rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter with value "does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Delete a suppression rule returns "OK" response
    Given there is a valid "suppression" in the system
    And new "DeleteSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/k9-automation
  Scenario: Delete a ticket creation rule returns "Not Found" response
    Given operation "DeleteSecurityFindingsAutomationTicketCreationRule" enabled
    And new "DeleteSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Delete a ticket creation rule returns "Rule successfully deleted." response
    Given operation "DeleteSecurityFindingsAutomationTicketCreationRule" enabled
    And there is a valid "valid_ticket_creation_rule" in the system
    And new "DeleteSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "valid_ticket_creation_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a vulnerability-based notification rule returns "Not Found" response
    Given new "DeleteVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Delete a vulnerability-based notification rule returns "Rule successfully deleted." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "DeleteVulnerabilityNotificationRule" request
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    When the request is sent
    Then the response status is 204 Rule successfully deleted.

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete an entity context sync configuration returns "Not Found" response
    Given operation "DeleteSecurityMonitoringIntegrationConfig" enabled
    And new "DeleteSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete an entity context sync configuration returns "OK" response
    Given operation "DeleteSecurityMonitoringIntegrationConfig" enabled
    And new "DeleteSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-siem
  Scenario: Delete an existing job returns "Bad Request" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete an existing job returns "Conflict" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/cloud-siem
  Scenario: Delete an existing job returns "Not Found" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete an existing job returns "OK" response
    Given operation "DeleteHistoricalJob" enabled
    And new "DeleteHistoricalJob" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Delete an existing rule returns "Not Found" response
    Given new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Delete an existing rule returns "OK" response
    Given there is a valid "security_rule" in the system
    And new "DeleteSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/k9-investigation
  Scenario: Detach security findings from their case returns "Bad Request" response
    Given new "DetachCase" request
    And body with value {"data": {"relationships": {"findings": {"data": []}}, "type": "cases"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-investigation
  Scenario: Detach security findings from their case returns "No Content" response
    Given new "DetachCase" request
    And body with value {"data": {"relationships": {"findings": {"data": [{"id": "YzM2MTFjYzcyNmY0Zjg4MTAxZmRlNjQ1MWU1ZGQwYzR-YzI5NzE5Y2Y4MzU4ZjliNzhkNjYxNTY0ODIzZDQ2YTM=", "type": "findings"}]}}, "type": "cases"}}
    When the request is sent
    Then the response status is 204 No Content

  @team:DataDog/k9-investigation
  Scenario: Detach security findings from their case returns "Not Found" response
    Given new "DetachCase" request
    And body with value {"data": {"relationships": {"findings": {"data": [{"id": "wrong-finding-id", "type": "findings"}]}}, "type": "cases"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Export security monitoring resource to Terraform returns "Not Found" response
    Given operation "ExportSecurityMonitoringTerraformResource" enabled
    And new "ExportSecurityMonitoringTerraformResource" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And request contains "resource_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Export security monitoring resource to Terraform returns "OK" response
    Given operation "ExportSecurityMonitoringTerraformResource" enabled
    And there is a valid "suppression" in the system
    And new "ExportSecurityMonitoringTerraformResource" request
    And request contains "resource_type" parameter with value "suppressions"
    And request contains "resource_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.type_name" is equal to "datadog_security_monitoring_suppression"
    And the response "data.attributes.resource_id" has the same value as "suppression.data.id"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Export security monitoring resources to Terraform returns "Bad Request" response
    Given operation "BulkExportSecurityMonitoringTerraformResources" enabled
    And new "BulkExportSecurityMonitoringTerraformResources" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_ids": [""]}, "type": "bulk_export_resources"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Export security monitoring resources to Terraform returns "Not Found" response
    Given operation "BulkExportSecurityMonitoringTerraformResources" enabled
    And new "BulkExportSecurityMonitoringTerraformResources" request
    And request contains "resource_type" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"resource_ids": [""]}, "type": "bulk_export_resources"}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Export security monitoring resources to Terraform returns "OK" response
    Given operation "BulkExportSecurityMonitoringTerraformResources" enabled
    And there is a valid "suppression" in the system
    And new "BulkExportSecurityMonitoringTerraformResources" request
    And request contains "resource_type" parameter with value "suppressions"
    And body with value {"data": {"attributes": {"resource_ids": ["{{ suppression.data.id }}"]}, "type": "bulk_export_resources"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get AST for source code returns "Bad Request" response
    Given operation "CreateStaticAnalysisAst" enabled
    And new "CreateStaticAnalysisAst" request
    And body with value {"data": {"attributes": {"code": "aW1wb3J0IHN5cw==", "file_encoding": "utf-8", "language": "python"}, "type": "get_ast_request"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get AST for source code returns "OK" response
    Given operation "CreateStaticAnalysisAst" enabled
    And new "CreateStaticAnalysisAst" request
    And body with value {"data": {"attributes": {"code": "aW1wb3J0IHN5cw==", "file_encoding": "utf-8", "language": "python"}, "type": "get_ast_request"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get Entra ID Azure App Registration prerequisites returns "OK" response
    Given operation "GetEntraIdAzureAppRegistrations" enabled
    And new "GetEntraIdAzureAppRegistrations" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: Get SBOM returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given new "GetSBOM" request
    And request contains "asset_type" parameter from "REPLACE.ME"
    And request contains "filter[asset_name]" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @team:DataDog/k9-cloud-vm
  Scenario: Get SBOM returns "Not found: asset not found" response
    Given new "GetSBOM" request
    And request contains "asset_type" parameter with value "Host"
    And request contains "filter[asset_name]" parameter with value "unknown-host"
    When the request is sent
    Then the response status is 404 Not found: asset not found

  @skip @team:DataDog/k9-cloud-vm
  Scenario: Get SBOM returns "OK" response
    Given new "GetSBOM" request
    And request contains "asset_type" parameter with value "Repository"
    And request contains "filter[asset_name]" parameter with value "github.com/datadog/datadog-agent"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get a SAST ruleset returns "Bad Request" response
    Given operation "GetStaticAnalysisRuleset" enabled
    And new "GetStaticAnalysisRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get a SAST ruleset returns "Not Found" response
    Given operation "GetStaticAnalysisRuleset" enabled
    And new "GetStaticAnalysisRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get a SAST ruleset returns "OK" response
    Given operation "GetStaticAnalysisRuleset" enabled
    And new "GetStaticAnalysisRuleset" request
    And request contains "ruleset_name" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Get a cloud configuration rule's details returns "OK" response
    Given there is a valid "cloud_configuration_rule" in the system
    And new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "cloud_configuration_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud"
    And the response "id" has the same value as "cloud_configuration_rule.id"

  @team:DataDog/cloud-siem
  Scenario: Get a critical asset returns "Not Found" response
    Given new "GetSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter with value "00000000-0000-0000-0000-000000000000"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Get a critical asset returns "OK" response
    Given new "GetSecurityMonitoringCriticalAsset" request
    And there is a valid "critical_asset" in the system
    And request contains "critical_asset_id" parameter from "critical_asset.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.rule_query" has the same value as "critical_asset.data.attributes.rule_query"
    And the response "data.attributes.severity" is equal to "medium"

  @team:DataDog/cloud-siem
  Scenario: Get a custom framework returns "Bad Request" response
    Given new "GetCustomFramework" request
    And request contains "handle" parameter with value "frame-does-not-exist"
    And request contains "version" parameter with value "frame-does-not-exist"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/cloud-siem
  Scenario: Get a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "GetCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset at a specific version returns "Bad Request" response
    Given operation "GetSecurityMonitoringDatasetByVersion" enabled
    And new "GetSecurityMonitoringDatasetByVersion" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset at a specific version returns "Not Found" response
    Given operation "GetSecurityMonitoringDatasetByVersion" enabled
    And new "GetSecurityMonitoringDatasetByVersion" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset at a specific version returns "OK" response
    Given operation "GetSecurityMonitoringDatasetByVersion" enabled
    And new "GetSecurityMonitoringDatasetByVersion" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset returns "Bad Request" response
    Given operation "GetSecurityMonitoringDataset" enabled
    And new "GetSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset returns "Not Found" response
    Given operation "GetSecurityMonitoringDataset" enabled
    And new "GetSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a dataset returns "OK" response
    Given operation "GetSecurityMonitoringDataset" enabled
    And new "GetSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-automation
  Scenario: Get a due date rule returns "Not Found" response
    Given operation "GetSecurityFindingsAutomationDueDateRule" enabled
    And new "GetSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Get a due date rule returns "Successfully retrieved the due date rule" response
    Given operation "GetSecurityFindingsAutomationDueDateRule" enabled
    And there is a valid "valid_due_date_rule" in the system
    And new "GetSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "valid_due_date_rule.data.id"
    When the request is sent
    Then the response status is 200 Successfully retrieved the due date rule
    And the response "data.id" is equal to "{{ valid_due_date_rule.data.id }}"
    And the response "data.type" is equal to "due_date_rules"

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "Bad Request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "Not Found: The requested finding cannot be found." response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found: The requested finding cannot be found.

  @replay-only @team:DataDog/cloud-security-posture-management
  Scenario: Get a finding returns "OK" response
    Given operation "GetFinding" enabled
    And new "GetFinding" request
    And request contains "finding_id" parameter with value "AgAAAYd59gjghzF52gAAAAAAAAAYAAAAAEFZZDU5Z2pnQUFCRTRvV1lFeEo4SlFBQQAAACQAAAAAMDE4NzdhMDEtMDRiYS00NTZlLWFmMzMtNTIxNmNkNjVlNDMz"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.evaluation" is equal to "pass"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a hist signal's details returns "Bad Request" response
    Given operation "GetSecurityMonitoringHistsignal" enabled
    And new "GetSecurityMonitoringHistsignal" request
    And request contains "histsignal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a hist signal's details returns "Not Found" response
    Given operation "GetSecurityMonitoringHistsignal" enabled
    And new "GetSecurityMonitoringHistsignal" request
    And request contains "histsignal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a hist signal's details returns "OK" response
    Given operation "GetSecurityMonitoringHistsignal" enabled
    And new "GetSecurityMonitoringHistsignal" request
    And request contains "histsignal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Get a job's details returns "Bad Request" response
    Given operation "GetHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And request contains "job_id" parameter with value "inva-lid"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Get a job's details returns "Not Found" response
    Given operation "GetHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And request contains "job_id" parameter with value "8e2a37fb-b0c8-4761-a7f0-0a8d6a98ba93"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Get a job's details returns "OK" response
    Given operation "GetHistoricalJob" enabled
    And operation "RunHistoricalJob" enabled
    And new "GetHistoricalJob" request
    And there is a valid "historical_job" in the system
    And request contains "job_id" parameter from "historical_job.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a job's hist signals returns "Bad Request" response
    Given operation "GetSecurityMonitoringHistsignalsByJobId" enabled
    And new "GetSecurityMonitoringHistsignalsByJobId" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a job's hist signals returns "Not Found" response
    Given operation "GetSecurityMonitoringHistsignalsByJobId" enabled
    And new "GetSecurityMonitoringHistsignalsByJobId" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a job's hist signals returns "OK" response
    Given operation "GetSecurityMonitoringHistsignalsByJobId" enabled
    And new "GetSecurityMonitoringHistsignalsByJobId" request
    And request contains "job_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a list of security signals returns "Bad Request" response
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a list of security signals returns "OK" response
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/cloud-siem @with-pagination
  Scenario: Get a list of security signals returns "OK" response with pagination
    Given new "SearchSecurityMonitoringSignals" request
    And body with value {"filter": {"from": "{{ timeISO("now-15m") }}", "query": "security:attack status:high", "to": "{{ timeISO("now") }}"}, "page": {"limit": 2}, "sort": "timestamp"}
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @generated @skip @team:DataDog/k9-automation
  Scenario: Get a mute rule returns "Not Found" response
    Given operation "GetSecurityFindingsAutomationMuteRule" enabled
    And new "GetSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Get a mute rule returns "Successfully retrieved the mute rule" response
    Given operation "GetSecurityFindingsAutomationMuteRule" enabled
    And there is a valid "valid_mute_rule" in the system
    And new "GetSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "valid_mute_rule.data.id"
    When the request is sent
    Then the response status is 200 Successfully retrieved the mute rule
    And the response "data.id" is equal to "{{ valid_mute_rule.data.id }}"
    And the response "data.type" is equal to "mute_rules"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a quick list of security signals returns "Bad Request" response
    Given new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a quick list of security signals returns "OK" response
    Given new "ListSecurityMonitoringSignals" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-validation @team:DataDog/cloud-siem @with-pagination
  Scenario: Get a quick list of security signals returns "OK" response with pagination
    Given new "ListSecurityMonitoringSignals" request
    And request contains "page[limit]" parameter with value 2
    When the request with pagination is sent
    Then the response status is 200 OK
    And the response has 3 items

  @team:DataDog/cloud-siem
  Scenario: Get a rule's details returns "Not Found" response
    Given new "GetSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "abcde-12345"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Get a rule's details returns "OK" response
    Given new "GetSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}"
    And the response "id" has the same value as "security_rule.id"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a rule's version history returns "Bad Request" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a rule's version history returns "Not Found" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a rule's version history returns "OK" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a security filter returns "Not Found" response
    Given new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Get a security filter returns "OK" response
    Given there is a valid "security_filter" in the system
    And new "GetSecurityFilter" request
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.name" is equal to "{{ unique }}"
    And the response "data.attributes.is_enabled" is equal to true
    And the response "data.attributes.exclusion_filters[0].name" is equal to "Exclude logs from staging"
    And the response "data.attributes.exclusion_filters[0].query" is equal to "source:staging"

  @replay-only @team:DataDog/cloud-siem
  Scenario: Get a signal's details returns "Not Found" response
    Given new "GetSecurityMonitoringSignal" request
    And request contains "signal_id" parameter with value "AQAAAYNqUBVU4-rffwAAAABBWU5xVUJWVUFBQjJBd3ptCL3QUEm3nt2"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Get a signal's details returns "OK" response
    Given new "GetSecurityMonitoringSignal" request
    And request contains "signal_id" parameter with value "AQAAAYNqUBVU4-rffwAAAABBWU5xVUJWVUFBQjJBd3ptMDdQUnF3QUE"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a single entity context returns "Bad Request" response
    Given operation "GetSingleEntityContext" enabled
    And new "GetSingleEntityContext" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a single entity context returns "Not Found" response
    Given operation "GetSingleEntityContext" enabled
    And new "GetSingleEntityContext" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get a single entity context returns "OK" response
    Given operation "GetSingleEntityContext" enabled
    And new "GetSingleEntityContext" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Get a suppression rule returns "Not Found" response
    Given new "GetSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter with value "this-does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Get a suppression rule returns "OK" response
    Given new "GetSecurityMonitoringSuppression" request
    And there is a valid "suppression" in the system
    And request contains "suppression_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.attributes.rule_query" has the same value as "suppression.data.attributes.rule_query"
    And the response "data.attributes.suppression_query" is equal to "env:test"

  @team:DataDog/cloud-siem
  Scenario: Get a suppression's version history returns "Not Found" response
    Given new "GetSuppressionVersionHistory" request
    And request contains "suppression_id" parameter with value "this-does-not-exist"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Get a suppression's version history returns "OK" response
    Given new "GetSuppressionVersionHistory" request
    And there is a valid "suppression" in the system
    And request contains "suppression_id" parameter from "suppression.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-automation
  Scenario: Get a ticket creation rule returns "Not Found" response
    Given operation "GetSecurityFindingsAutomationTicketCreationRule" enabled
    And new "GetSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Get a ticket creation rule returns "Successfully retrieved the ticket creation rule" response
    Given operation "GetSecurityFindingsAutomationTicketCreationRule" enabled
    And there is a valid "valid_ticket_creation_rule" in the system
    And new "GetSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "valid_ticket_creation_rule.data.id"
    When the request is sent
    Then the response status is 200 Successfully retrieved the ticket creation rule
    And the response "data.id" is equal to "{{ valid_ticket_creation_rule.data.id }}"
    And the response "data.type" is equal to "ticket_creation_rules"

  @team:DataDog/cloud-siem
  Scenario: Get all critical assets returns "OK" response
    Given new "ListSecurityMonitoringCriticalAssets" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-automation
  Scenario: Get all due date rules returns "Successfully retrieved the list of due date rules" response
    Given operation "ListSecurityFindingsAutomationDueDateRules" enabled
    And there is a valid "valid_due_date_rule" in the system
    And new "ListSecurityFindingsAutomationDueDateRules" request
    When the request is sent
    Then the response status is 200 Successfully retrieved the list of due date rules
    And the response "data" has item with field "id" with value "{{ valid_due_date_rule.data.id }}"

  @team:DataDog/k9-automation
  Scenario: Get all mute rules returns "Successfully retrieved the list of mute rules" response
    Given operation "ListSecurityFindingsAutomationMuteRules" enabled
    And there is a valid "valid_mute_rule" in the system
    And new "ListSecurityFindingsAutomationMuteRules" request
    When the request is sent
    Then the response status is 200 Successfully retrieved the list of mute rules
    And the response "data" has item with field "id" with value "{{ valid_mute_rule.data.id }}"

  @team:DataDog/cloud-siem
  Scenario: Get all security filters returns "OK" response
    Given new "ListSecurityFilters" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has item with field "attributes.filtered_data_type" with value "logs"
    And the response "data" has item with field "attributes.is_builtin" with value true

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get all suppression rules returns "OK" response
    Given new "ListSecurityMonitoringSuppressions" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Get all suppression rules returns "OK" response with pagination
    Given new "ListSecurityMonitoringSuppressions" request
    And there is a valid "suppression" in the system
    And there is a valid "suppression2" in the system
    And request contains "page[size]" parameter with value 1
    And request contains "page[number]" parameter with value 0
    And request contains "query" parameter with value "id:{{ suppression.data.id }} OR id:{{ suppression2.data.id }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1

  @team:DataDog/cloud-siem
  Scenario: Get all suppression rules returns "OK" response with sort ascending
    Given new "ListSecurityMonitoringSuppressions" request
    And there is a valid "suppression" in the system
    And there is a valid "suppression2" in the system
    And request contains "sort" parameter with value "name"
    And request contains "query" parameter with value "id:{{ suppression.data.id }} OR id:{{ suppression2.data.id }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "suppression {{ unique_hash }}"

  @team:DataDog/cloud-siem
  Scenario: Get all suppression rules returns "OK" response with sort descending
    Given new "ListSecurityMonitoringSuppressions" request
    And there is a valid "suppression" in the system
    And there is a valid "suppression2" in the system
    And request contains "sort" parameter with value "-name"
    And request contains "query" parameter with value "id:{{ suppression.data.id }} OR id:{{ suppression2.data.id }}"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].attributes.name" is equal to "suppression2 {{ unique_hash }}"

  @team:DataDog/k9-automation
  Scenario: Get all ticket creation rules returns "Successfully retrieved the list of ticket creation rules" response
    Given operation "ListSecurityFindingsAutomationTicketCreationRules" enabled
    And there is a valid "valid_ticket_creation_rule" in the system
    And new "ListSecurityFindingsAutomationTicketCreationRules" request
    When the request is sent
    Then the response status is 200 Successfully retrieved the list of ticket creation rules
    And the response "data" has item with field "id" with value "{{ valid_ticket_creation_rule.data.id }}"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get an entity context sync configuration returns "Not Found" response
    Given operation "GetSecurityMonitoringIntegrationConfig" enabled
    And new "GetSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get an entity context sync configuration returns "OK" response
    Given operation "GetSecurityMonitoringIntegrationConfig" enabled
    And new "GetSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get an indicator of compromise returns "Bad Request" response
    Given operation "GetIndicatorOfCompromise" enabled
    And new "GetIndicatorOfCompromise" request
    And request contains "indicator" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Get an indicator of compromise returns "Not Found" response
    Given operation "GetIndicatorOfCompromise" enabled
    And new "GetIndicatorOfCompromise" request
    And request contains "indicator" parameter with value "this-indicator-does-not-exist.invalid"
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: Get an indicator of compromise returns "OK" response
    Given operation "GetIndicatorOfCompromise" enabled
    And new "GetIndicatorOfCompromise" request
    And request contains "indicator" parameter with value "192.0.2.1"
    And request contains "include_triage_history" parameter with value true
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get content pack states returns "Not Found" response
    Given operation "GetContentPacksStates" enabled
    And new "GetContentPacksStates" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get content pack states returns "OK" response
    Given operation "GetContentPacksStates" enabled
    And new "GetContentPacksStates" request
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Get critical assets affecting a specific rule returns "Not Found" response
    Given new "GetCriticalAssetsAffectingRule" request
    And request contains "rule_id" parameter with value "aaa-bbb-ccc-ddd"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Get critical assets affecting a specific rule returns "OK" response
    Given new "GetCriticalAssetsAffectingRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get dataset dependencies returns "Bad Request" response
    Given operation "BatchGetSecurityMonitoringDatasetDependencies" enabled
    And new "BatchGetSecurityMonitoringDatasetDependencies" request
    And body with value {"data": {"attributes": {"datasetIds": ["123e4567-e89b-12d3-a456-426614174000"]}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get dataset dependencies returns "OK" response
    Given operation "BatchGetSecurityMonitoringDatasetDependencies" enabled
    And new "BatchGetSecurityMonitoringDatasetDependencies" request
    And body with value {"data": {"attributes": {"datasetIds": ["123e4567-e89b-12d3-a456-426614174000"]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get default rulesets for a language returns "Bad Request" response
    Given operation "GetStaticAnalysisDefaultRulesets" enabled
    And new "GetStaticAnalysisDefaultRulesets" request
    And request contains "language" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get default rulesets for a language returns "OK" response
    Given operation "GetStaticAnalysisDefaultRulesets" enabled
    And new "GetStaticAnalysisDefaultRulesets" request
    And request contains "language" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Bad Request" response
    Given new "GetSignalNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Not Found" response
    Given new "GetSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a signal-based notification rule returns "Notification rule details." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "GetSignalNotificationRule" request
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 Notification rule details.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Bad Request" response
    Given new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Not Found" response
    Given new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Get details of a vulnerability notification rule returns "Notification rule details." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "GetVulnerabilityNotificationRule" request
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    When the request is sent
    Then the response status is 200 Notification rule details.

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get entities related to a signal returns "Bad Request" response
    Given operation "GetSignalEntities" enabled
    And new "GetSignalEntities" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get entities related to a signal returns "Not Found" response
    Given operation "GetSignalEntities" enabled
    And new "GetSignalEntities" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get entities related to a signal returns "OK" response
    Given operation "GetSignalEntities" enabled
    And new "GetSignalEntities" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get entity context returns "Bad Request" response
    Given operation "GetEntityContext" enabled
    And new "GetEntityContext" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get entity context returns "OK" response
    Given operation "GetEntityContext" enabled
    And new "GetEntityContext" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get investigation queries for a signal returns "Not Found" response
    Given new "GetInvestigationLogQueriesMatchingSignal" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/cloud-siem
  Scenario: Get investigation queries for a signal returns "OK" response
    Given new "GetInvestigationLogQueriesMatchingSignal" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "investigation_log_queries"
    And the response "data[0]" has field "id"
    And the response "data[0].attributes" has field "name"
    And the response "data[0].attributes" has field "query_filter"
    And the response "data[0].attributes" has field "url"

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get node types for a language returns "Bad Request" response
    Given operation "GetStaticAnalysisNodeTypes" enabled
    And new "GetStaticAnalysisNodeTypes" request
    And request contains "language" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get node types for a language returns "OK" response
    Given operation "GetStaticAnalysisNodeTypes" enabled
    And new "GetStaticAnalysisNodeTypes" request
    And request contains "language" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-go @skip-java @skip-ruby @team:DataDog/cloud-siem
  Scenario: Get rule version history returns "OK" response
    Given operation "GetRuleVersionHistory" enabled
    And new "GetRuleVersionHistory" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK
    And the response "data.id" has the same value as "security_rule.id"
    And the response "data.type" is equal to "GetRuleVersionHistoryResponse"
    And the response "data.attributes.count" is equal to 1
    And the response "data.attributes.data[1].rule.name" has the same value as "security_rule.name"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get sample log generation subscriptions returns "Bad Request" response
    Given operation "ListSampleLogGenerationSubscriptions" enabled
    And new "ListSampleLogGenerationSubscriptions" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get sample log generation subscriptions returns "OK" response
    Given operation "ListSampleLogGenerationSubscriptions" enabled
    And new "ListSampleLogGenerationSubscriptions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get suggested actions for a signal returns "Not Found" response
    Given new "GetSuggestedActionsMatchingSignal" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/cloud-siem
  Scenario: Get suggested actions for a signal returns "OK" response
    Given new "GetSuggestedActionsMatchingSignal" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "investigation_log_queries"
    And the response "data[0]" has field "id"
    And the response "data[0].attributes" has field "name"
    And the response "data[0].attributes" has field "query_filter"
    And the response "data[0].attributes" has field "url"
    And the response "data[1].type" is equal to "recommended_blog_posts"
    And the response "data[1]" has field "id"
    And the response "data[1].attributes" has field "title"
    And the response "data[1].attributes" has field "url"

  @team:DataDog/cloud-siem
  Scenario: Get suppressions affecting a specific rule returns "Not Found" response
    Given new "GetSuppressionsAffectingRule" request
    And request contains "rule_id" parameter with value "aaa-bbb-ccc-ddd"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Get suppressions affecting a specific rule returns "OK" response
    Given new "GetSuppressionsAffectingRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Get suppressions affecting future rule returns "Bad Request" response
    Given new "GetSuppressionsAffectingFutureRule" request
    And body with value {"invalid_key":"invalid_value"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Get suppressions affecting future rule returns "OK" response
    Given new "GetSuppressionsAffectingFutureRule" request
    And body from file "security_monitoring_future_rule_suppression_payload.json"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-security-posture-management
  Scenario: Get the list of signal-based notification rules returns "The list of notification rules." response
    Given there is a valid "valid_signal_notification_rule" in the system
    And new "GetSignalNotificationRules" request
    When the request is sent
    Then the response status is 200 The list of notification rules.

  @team:DataDog/cloud-security-posture-management
  Scenario: Get the list of vulnerability notification rules returns "The list of notification rules." response
    Given there is a valid "valid_vulnerability_notification_rule" in the system
    And new "GetVulnerabilityNotificationRules" request
    When the request is sent
    Then the response status is 200 The list of notification rules.

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get the version history of a dataset returns "Bad Request" response
    Given operation "GetSecurityMonitoringDatasetVersionHistory" enabled
    And new "GetSecurityMonitoringDatasetVersionHistory" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get the version history of a dataset returns "Not Found" response
    Given operation "GetSecurityMonitoringDatasetVersionHistory" enabled
    And new "GetSecurityMonitoringDatasetVersionHistory" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get the version history of a dataset returns "OK" response
    Given operation "GetSecurityMonitoringDatasetVersionHistory" enabled
    And new "GetSecurityMonitoringDatasetVersionHistory" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Get the version history of security filters returns "OK" response
    Given new "ListSecurityFilterVersions" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get tree-sitter WASM file returns "BLOB with the content of the WASM file" response
    Given operation "GetStaticAnalysisTreeSitterWasm" enabled
    And new "GetStaticAnalysisTreeSitterWasm" request
    And request contains "file" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 BLOB with the content of the WASM file

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Get tree-sitter WASM file returns "Bad Request" response
    Given operation "GetStaticAnalysisTreeSitterWasm" enabled
    And new "GetStaticAnalysisTreeSitterWasm" request
    And request contains "file" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: Import security vulnerabilities returns "Bad Request" response
    Given operation "ImportSecurityVulnerabilities" enabled
    And new "ImportSecurityVulnerabilities" request
    And body with value {"bomFormat": "CycloneDX", "components": [{"bom-ref": "a3390fca-c315-41ae-ae05-af5e7859cdee", "name": "lodash", "purl": "pkg:npm/lodash@4.17.21", "type": "library", "version": "4.17.21"}], "metadata": {"component": {"bom-ref": "host-ref-abc123", "name": "i-12345", "type": "operating-system"}, "tools": {"components": [{"name": "my-scanner", "type": "application"}]}}, "specVersion": "1.5", "version": 1, "vulnerabilities": [{"advisories": [{"url": "https://example.com/advisory/CVE-2021-1234"}], "affects": [{"ref": "a3390fca-c315-41ae-ae05-af5e7859cdee"}], "analysis": {"state": "resolved"}, "cwes": [123, 345], "description": "Sample vulnerability detected in the application.", "detail": "Details about the vulnerability.", "id": "CVE-2021-1234", "ratings": [{"score": 9.0, "severity": "high", "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N"}], "references": [{"id": "GHSA-35m5-8cvj-8783", "source": {"url": "https://example.com"}}]}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: Import security vulnerabilities returns "Vulnerabilities accepted successfully." response
    Given operation "ImportSecurityVulnerabilities" enabled
    And new "ImportSecurityVulnerabilities" request
    And body with value {"bomFormat": "CycloneDX", "components": [{"bom-ref": "a3390fca-c315-41ae-ae05-af5e7859cdee", "name": "lodash", "purl": "pkg:npm/lodash@4.17.21", "type": "library", "version": "4.17.21"}], "metadata": {"component": {"bom-ref": "host-ref-abc123", "name": "i-12345", "type": "operating-system"}, "tools": {"components": [{"name": "my-scanner", "type": "application"}]}}, "specVersion": "1.5", "version": 1, "vulnerabilities": [{"advisories": [{"url": "https://example.com/advisory/CVE-2021-1234"}], "affects": [{"ref": "a3390fca-c315-41ae-ae05-af5e7859cdee"}], "analysis": {"state": "resolved"}, "cwes": [123, 345], "description": "Sample vulnerability detected in the application.", "detail": "Details about the vulnerability.", "id": "CVE-2021-1234", "ratings": [{"score": 9.0, "severity": "high", "vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N"}], "references": [{"id": "GHSA-35m5-8cvj-8783", "source": {"url": "https://example.com"}}]}]}
    When the request is sent
    Then the response status is 200 Vulnerabilities accepted successfully.

  @team:DataDog/k9-cloud-vm
  Scenario: List assets SBOMs returns "Bad request: Invalid pagination token." response
    Given new "ListAssetsSBOMs" request
    And request contains "page[token]" parameter with value "SERVICE:unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 400 Bad request: Invalid pagination token.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List assets SBOMs returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given new "ListAssetsSBOMs" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List assets SBOMs returns "Not found: asset not found" response
    Given new "ListAssetsSBOMs" request
    When the request is sent
    Then the response status is 404 Not found: asset not found

  @team:DataDog/k9-cloud-vm
  Scenario: List assets SBOMs returns "OK" response
    Given new "ListAssetsSBOMs" request
    And request contains "filter[package_name]" parameter with value "pandas"
    And request contains "filter[asset_type]" parameter with value "Service"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List codegen rulesets returns "Bad Request" response
    Given operation "ListStaticAnalysisCodegenRulesets" enabled
    And new "ListStaticAnalysisCodegenRulesets" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: List codegen rulesets returns "OK" response
    Given operation "ListStaticAnalysisCodegenRulesets" enabled
    And new "ListStaticAnalysisCodegenRulesets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List datasets returns "Bad Request" response
    Given operation "ListSecurityMonitoringDatasets" enabled
    And new "ListSecurityMonitoringDatasets" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List datasets returns "OK" response
    Given operation "ListSecurityMonitoringDatasets" enabled
    And new "ListSecurityMonitoringDatasets" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List entity context sync configurations returns "OK" response
    Given operation "ListSecurityMonitoringIntegrationConfigs" enabled
    And new "ListSecurityMonitoringIntegrationConfigs" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "Bad Request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 400 Bad Request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "Not Found: The requested finding cannot be found." response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 404 Not Found: The requested finding cannot be found.

  @replay-only @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "OK" response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request is sent
    Then the response status is 200 OK
    And the response "data[0].type" is equal to "finding"

  @team:DataDog/cloud-security-posture-management
  Scenario: List findings returns "OK" response with details
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    And request contains "detailed_findings" parameter with value true
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-security-posture-management @with-pagination
  Scenario: List findings returns "OK" response with pagination
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    When the request with pagination is sent
    Then the response status is 200 OK

  @skip-terraform-config @team:DataDog/cloud-security-posture-management
  Scenario: List findings with detection_type query param returns "OK" response
    Given operation "ListFindings" enabled
    And new "ListFindings" request
    And request contains "filter[vulnerability_type]" parameter with value ["misconfiguration", "attack_path"]
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List hist signals returns "Bad Request" response
    Given operation "ListSecurityMonitoringHistsignals" enabled
    And new "ListSecurityMonitoringHistsignals" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List hist signals returns "Not Found" response
    Given operation "ListSecurityMonitoringHistsignals" enabled
    And new "ListSecurityMonitoringHistsignals" request
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List hist signals returns "OK" response
    Given operation "ListSecurityMonitoringHistsignals" enabled
    And new "ListSecurityMonitoringHistsignals" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List historical jobs returns "Bad Request" response
    Given operation "ListHistoricalJobs" enabled
    And new "ListHistoricalJobs" request
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List historical jobs returns "OK" response
    Given operation "ListHistoricalJobs" enabled
    And new "ListHistoricalJobs" request
    When the request is sent
    Then the response status is 200 OK

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: List indicators of compromise returns "Bad Request" response
    Given operation "ListIndicatorsOfCompromise" enabled
    And new "ListIndicatorsOfCompromise" request
    And request contains "query" parameter with value "invalid:::query"
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @skip-terraform-config @team:DataDog/cloud-siem
  Scenario: List indicators of compromise returns "OK" response
    Given operation "ListIndicatorsOfCompromise" enabled
    And new "ListIndicatorsOfCompromise" request
    And request contains "limit" parameter with value 1
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: List resource filters returns "Bad Request" response
    Given new "GetResourceEvaluationFilters" request
    And request contains "account_id" parameter with value "123456789"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: List resource filters returns "OK" response
    Given new "GetResourceEvaluationFilters" request
    And request contains "cloud_provider" parameter with value "aws"
    And request contains "account_id" parameter with value "123456789"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: List rules returns "Bad Request" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 400 Bad Request

  @skip-validation @team:DataDog/cloud-siem
  Scenario: List rules returns "OK" response
    Given new "ListSecurityMonitoringRules" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-vm
  Scenario: List scanned assets metadata returns "Bad request: Invalid Pagination Token" response
    Given operation "ListScannedAssetsMetadata" enabled
    And new "ListScannedAssetsMetadata" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 400 Bad request: Invalid pagination token.

  @skip @team:DataDog/k9-cloud-vm
  Scenario: List scanned assets metadata returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListScannedAssetsMetadata" enabled
    And new "ListScannedAssetsMetadata" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List scanned assets metadata returns "Not found: asset not found" response
    Given operation "ListScannedAssetsMetadata" enabled
    And new "ListScannedAssetsMetadata" request
    When the request is sent
    Then the response status is 404 Not found: asset not found

  @team:DataDog/k9-cloud-vm
  Scenario: List scanned assets metadata returns "OK" response
    Given operation "ListScannedAssetsMetadata" enabled
    And new "ListScannedAssetsMetadata" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform
  Scenario: List security findings returns "Bad Request" response
    Given new "ListSecurityFindings" request
    And request contains "page[cursor]" parameter with value "invalid_cursor"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform
  Scenario: List security findings returns "OK" response
    Given new "ListSecurityFindings" request
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform
  Scenario: List security findings returns "OK" response with pagination
    Given new "ListSecurityFindings" request
    And request contains "page[limit]" parameter with value 5
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 5
    And the response "meta.page" has field "after"
    And the response "links" has field "next"

  @team:DataDog/k9-cloud-vm
  Scenario: List vulnerabilities returns "Bad request: Invalid pagination token." response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 400 Bad request: Invalid pagination token.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List vulnerabilities returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List vulnerabilities returns "Not found: There is no request associated with the provided token." response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    When the request is sent
    Then the response status is 404 Not found: There is no request associated with the provided token.

  @team:DataDog/k9-cloud-vm
  Scenario: List vulnerabilities returns "OK" response
    Given operation "ListVulnerabilities" enabled
    And new "ListVulnerabilities" request
    And request contains "filter[cvss.base.severity]" parameter with value "High"
    And request contains "filter[asset.type]" parameter with value "Service"
    And request contains "filter[tool]" parameter with value "Infra"
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-cloud-vm
  Scenario: List vulnerable assets returns "Bad request: Invalid Pagination Token" response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    And request contains "page[token]" parameter with value "unknown"
    And request contains "page[number]" parameter with value 1
    When the request is sent
    Then the response status is 400 Bad request: Invalid pagination token.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List vulnerable assets returns "Bad request: The server cannot process the request due to invalid syntax in the request." response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    When the request is sent
    Then the response status is 400 Bad request: The server cannot process the request due to invalid syntax in the request.

  @generated @skip @team:DataDog/k9-cloud-vm
  Scenario: List vulnerable assets returns "Not found: There is no request associated with the provided token." response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    When the request is sent
    Then the response status is 404 Not found: There is no request associated with the provided token.

  @team:DataDog/k9-cloud-vm
  Scenario: List vulnerable assets returns "OK" response
    Given operation "ListVulnerableAssets" enabled
    And new "ListVulnerableAssets" request
    And request contains "filter[type]" parameter with value "Host"
    And request contains "filter[repository_url]" parameter with value "github.com/datadog/dd-go"
    And request contains "filter[risks.in_production]" parameter with value true
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Modify the triage assignee of a security signal returns "Bad Request" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"name": null, "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Modify the triage assignee of a security signal returns "Not Found" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"assignee": {"name": null, "uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @replay-only @team:DataDog/cloud-siem
  Scenario: Modify the triage assignee of a security signal returns "OK" response
    Given new "EditSecurityMonitoringSignalAssignee" request
    And request contains "signal_id" parameter with value "AQAAAYG1bl5K4HuUewAAAABBWUcxYmw1S0FBQmt2RmhRN0V4ZUVnQUE"
    And body with value {"data": {"attributes": {"assignee": {"uuid": ""}}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Mute or unmute security findings returns "Accepted" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "PENDING_FIX"}}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 202 Accepted

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Mute or unmute security findings returns "Bad Request" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "PENDING_FIX"}}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Mute or unmute security findings returns "Not Found" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "PENDING_FIX"}}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-investigation
  Scenario: Mute or unmute security findings returns "Unprocessable Entity" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "PENDING_FIX"}}, "id": "00000000-0000-0000-0000-000000000001", "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/k9-investigation
  Scenario: Mute security findings returns "Accepted" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "RISK_ACCEPTED"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwMC0wYmd-MDE4NjcyMDJkMzE4MDE5ODY5MGE4ZmQ2MmFlMjg0Y2M=", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 202 Accepted

  @team:DataDog/k9-investigation
  Scenario: Mute security findings returns "Not Found" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1778721573794, "is_muted": true, "reason": "RISK_ACCEPTED"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-investigation
  Scenario: Mute security findings returns "Unprocessable Entity" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "To be resolved later.", "expire_at": 1, "is_muted": true, "reason": "RISK_ACCEPTED"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Bad Request" response
    Given new "PatchSignalNotificationRule" request
    And there is a valid "valid_signal_notification_rule" in the system
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Not Found" response
    Given new "PatchSignalNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "Notification rule successfully patched." response
    Given new "PatchSignalNotificationRule" request
    And there is a valid "valid_signal_notification_rule" in the system
    And request contains "id" parameter from "valid_signal_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 200 Notification rule successfully patched.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Patch a signal-based notification rule returns "The server cannot process the request because it contains invalid data." response
    Given new "PatchSignalNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "routing": {"mode": "manual"}, "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Bad Request" response
    Given new "PatchVulnerabilityNotificationRule" request
    And there is a valid "valid_vulnerability_notification_rule" in the system
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Not Found" response
    Given new "PatchVulnerabilityNotificationRule" request
    And request contains "id" parameter with value "000-000-000"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "Notification rule successfully patched." response
    Given new "PatchVulnerabilityNotificationRule" request
    And there is a valid "valid_vulnerability_notification_rule" in the system
    And request contains "id" parameter from "valid_vulnerability_notification_rule.data.id"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 200 Notification rule successfully patched.

  @generated @skip @team:DataDog/cloud-security-posture-management
  Scenario: Patch a vulnerability-based notification rule returns "The server cannot process the request because it contains invalid data." response
    Given new "PatchVulnerabilityNotificationRule" request
    And request contains "id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "routing": {"mode": "manual"}, "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400, "version": 1}, "id": "aaa-bbb-ccc", "type": "notification_rules"}}
    When the request is sent
    Then the response status is 422 The server cannot process the request because it contains invalid data.

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder due date rules returns "Bad Request" response
    Given operation "ReorderSecurityFindingsAutomationDueDateRules" enabled
    And new "ReorderSecurityFindingsAutomationDueDateRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "due_date_rules"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Reorder due date rules returns "Successfully reordered the due date rules" response
    Given operation "ReorderSecurityFindingsAutomationDueDateRules" enabled
    And there is a valid "valid_due_date_rule" in the system
    And new "ReorderSecurityFindingsAutomationDueDateRules" request
    And body with value {"data": [{"id": "{{ valid_due_date_rule.data.id }}", "type": "due_date_rules"}]}
    When the request is sent
    Then the response status is 200 Successfully reordered the due date rules

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder due date rules returns "Unprocessable Entity" response
    Given operation "ReorderSecurityFindingsAutomationDueDateRules" enabled
    And new "ReorderSecurityFindingsAutomationDueDateRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "due_date_rules"}]}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder mute rules returns "Bad Request" response
    Given operation "ReorderSecurityFindingsAutomationMuteRules" enabled
    And new "ReorderSecurityFindingsAutomationMuteRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "mute_rules"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Reorder mute rules returns "Successfully reordered the mute rules" response
    Given operation "ReorderSecurityFindingsAutomationMuteRules" enabled
    And there is a valid "valid_mute_rule" in the system
    And new "ReorderSecurityFindingsAutomationMuteRules" request
    And body with value {"data": [{"id": "{{ valid_mute_rule.data.id }}", "type": "mute_rules"}]}
    When the request is sent
    Then the response status is 200 Successfully reordered the mute rules

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder mute rules returns "Unprocessable Entity" response
    Given operation "ReorderSecurityFindingsAutomationMuteRules" enabled
    And new "ReorderSecurityFindingsAutomationMuteRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "mute_rules"}]}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder ticket creation rules returns "Bad Request" response
    Given operation "ReorderSecurityFindingsAutomationTicketCreationRules" enabled
    And new "ReorderSecurityFindingsAutomationTicketCreationRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "ticket_creation_rules"}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/k9-automation
  Scenario: Reorder ticket creation rules returns "Successfully reordered the ticket creation rules" response
    Given operation "ReorderSecurityFindingsAutomationTicketCreationRules" enabled
    And there is a valid "valid_ticket_creation_rule" in the system
    And new "ReorderSecurityFindingsAutomationTicketCreationRules" request
    And body with value {"data": [{"id": "{{ valid_ticket_creation_rule.data.id }}", "type": "ticket_creation_rules"}]}
    When the request is sent
    Then the response status is 200 Successfully reordered the ticket creation rules

  @generated @skip @team:DataDog/k9-automation
  Scenario: Reorder ticket creation rules returns "Unprocessable Entity" response
    Given operation "ReorderSecurityFindingsAutomationTicketCreationRules" enabled
    And new "ReorderSecurityFindingsAutomationTicketCreationRules" request
    And body with value {"data": [{"id": "00000000-0000-0000-0000-000000000000", "type": "ticket_creation_rules"}]}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Restore a rule to a historical version returns "Bad Request" response
    Given operation "RestoreSecurityMonitoringRule" enabled
    And new "RestoreSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And request contains "version" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Restore a rule to a historical version returns "Conflict" response
    Given operation "RestoreSecurityMonitoringRule" enabled
    And there is a valid "security_rule" in the system
    And there is a valid "security_rule_updated" in the system
    And new "RestoreSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    And request contains "version" parameter with value 2
    When the request is sent
    Then the response status is 409 Conflict

  @team:DataDog/cloud-siem
  Scenario: Restore a rule to a historical version returns "Not Found" response
    Given operation "RestoreSecurityMonitoringRule" enabled
    And there is a valid "security_rule" in the system
    And new "RestoreSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    And request contains "version" parameter with value 9999
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Restore a rule to a historical version returns "OK" response
    Given operation "RestoreSecurityMonitoringRule" enabled
    And there is a valid "security_rule" in the system
    And there is a valid "security_rule_updated" in the system
    And new "RestoreSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "security_rule.id"
    And request contains "version" parameter with value 1
    When the request is sent
    Then the response status is 200 OK
    And the response "id" has the same value as "security_rule.id"

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Returns a list of Secrets rules returns "OK" response
    Given operation "GetSecretsRules" enabled
    And new "GetSecretsRules" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/k9-vm-ast
  Scenario: Ruleset get multiple returns "OK" response
    Given operation "ListMultipleRulesets" enabled
    And new "ListMultipleRulesets" request
    And body with value {"data": {"attributes": {"rulesets": []}, "type": "get_multiple_rulesets_request"}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-siem
  Scenario: Run a historical job returns "Bad Request" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data":{"type":"historicalDetectionsJobCreate","attributes":{"jobDefinition":{"type":"log_detection","name":"Excessive number of failed attempts.","queries":[{"query":"source:non_existing_src_weekend","aggregation":"count","groupByFields":[],"distinctFields":[]}],"cases":[{"name":"Condition 1","status":"info","notifications":[],"condition":"a > 1"}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900},"message":"A large number of failed login attempts.","tags":[],"from":1730387522611,"to":1730391122611,"index":"non_existing_index"}}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Run a historical job returns "Not Found" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data": { "type": "historicalDetectionsJobCreate", "attributes": {"fromRule": {"from": 1730201035064, "id": "non-existng", "index": "main", "notifications": [], "to": 1730204635115}}}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Run a historical job returns "Status created" response
    Given operation "RunHistoricalJob" enabled
    And new "RunHistoricalJob" request
    And body with value {"data":{"type":"historicalDetectionsJobCreate","attributes":{"jobDefinition":{"type":"log_detection","name":"Excessive number of failed attempts.","queries":[{"query":"source:non_existing_src_weekend","aggregation":"count","groupByFields":[],"distinctFields":[]}],"cases":[{"name":"Condition 1","status":"info","notifications":[],"condition":"a > 1"}],"options":{"keepAlive":3600,"maxSignalDuration":86400,"evaluationWindow":900},"message":"A large number of failed login attempts.","tags":[],"from":1730387522611,"to":1730387532611,"index":"main"}}}}
    When the request is sent
    Then the response status is 201 Status created

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Search hist signals returns "Bad Request" response
    Given operation "SearchSecurityMonitoringHistsignals" enabled
    And new "SearchSecurityMonitoringHistsignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Search hist signals returns "Not Found" response
    Given operation "SearchSecurityMonitoringHistsignals" enabled
    And new "SearchSecurityMonitoringHistsignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Search hist signals returns "OK" response
    Given operation "SearchSecurityMonitoringHistsignals" enabled
    And new "SearchSecurityMonitoringHistsignals" request
    And body with value {"filter": {"from": "2019-01-02T09:42:36.320Z", "query": "security:attack status:high", "to": "2019-01-03T09:42:36.320Z"}, "page": {"cursor": "eyJzdGFydEF0IjoiQVFBQUFYS2tMS3pPbm40NGV3QUFBQUJCV0V0clRFdDZVbG8zY3pCRmNsbHJiVmxDWlEifQ==", "limit": 25}, "sort": "timestamp"}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform
  Scenario: Search security findings returns "Bad Request" response
    Given new "SearchSecurityFindings" request
    And body with value {"page": {"cursor": "invalid_cursor"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform
  Scenario: Search security findings returns "OK" response
    Given new "SearchSecurityFindings" request
    And body with value {"data": {"attributes": {"filter": "@severity:(critical OR high)"}}}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/cloud-security-posture-management @team:DataDog/k9-findings-platform @with-pagination
  Scenario: Search security findings returns "OK" response with pagination
    Given new "SearchSecurityFindings" request
    And body with value {"data": {"attributes": {"filter": "@severity:(critical OR high)", "page": {"limit": 1}}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data" has length 1
    And the response "meta.page" has field "after"
    And the response "links" has field "next"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Subscribe to sample log generation returns "Bad Request" response
    Given operation "CreateSampleLogGenerationSubscription" enabled
    And new "CreateSampleLogGenerationSubscription" request
    And body with value {"data": {"attributes": {"content_pack_id": "aws-cloudtrail", "duration": "3d"}, "type": "subscription_requests"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Subscribe to sample log generation returns "OK" response
    Given operation "CreateSampleLogGenerationSubscription" enabled
    And new "CreateSampleLogGenerationSubscription" request
    And body with value {"data": {"attributes": {"content_pack_id": "aws-cloudtrail", "duration": "3d"}, "type": "subscription_requests"}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Test a notification rule returns "Bad Request" response
    Given new "SendSecurityMonitoringNotificationPreview" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "routing": {"mode": "manual"}, "selectors": {"query": "(source:production_service OR env:prod)", "rule_types": ["misconfiguration", "attack_path"], "severities": ["critical"], "trigger_source": "security_findings"}, "targets": ["@john.doe@email.com"], "time_aggregation": 86400}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Test a notification rule returns "OK" response
    Given new "SendSecurityMonitoringNotificationPreview" request
    And body with value {"data": {"attributes": {"enabled": true, "name": "Rule 1", "selectors": {"query": "env:prod", "rule_types": ["log_detection"], "severities": ["critical"], "trigger_source": "security_signals"}, "targets": ["@john.doe@email.com"]}, "type": "notification_rules"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Test a rule returns "Bad Request" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [], "filters": [{"action": "require"}], "hasExtendedTitle": true, "isEnabled": true, "message": "", "name": "My security monitoring rule.", "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}, "thirdPartyRuleOptions": {"defaultNotifications": [], "defaultStatus": "critical", "rootQueries": [{"groupByFields": [], "query": "source:cloudtrail"}]}}, "queries": [], "tags": ["env:prod", "team:security"], "thirdPartyCases": [], "type": "application_security"}, "ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Test a rule returns "Not Found" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [], "filters": [{"action": "require"}], "hasExtendedTitle": true, "isEnabled": true, "message": "", "name": "My security monitoring rule.", "options": {"decreaseCriticalityBasedOnEnv": false, "detectionMethod": "threshold", "evaluationWindow": 0, "hardcodedEvaluatorType": "log4shell", "impossibleTravelOptions": {"baselineUserLocations": true}, "keepAlive": 0, "maxSignalDuration": 0, "newValueOptions": {"forgetAfter": 1, "learningDuration": 0, "learningMethod": "duration", "learningThreshold": 0}, "thirdPartyRuleOptions": {"defaultNotifications": [], "defaultStatus": "critical", "rootQueries": [{"groupByFields": [], "query": "source:cloudtrail"}]}}, "queries": [], "tags": ["env:prod", "team:security"], "thirdPartyCases": [], "type": "application_security"}, "ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-go @skip-java @skip-ruby @skip-typescript @team:DataDog/cloud-siem
  Scenario: Test a rule returns "OK" response
    Given new "TestSecurityMonitoringRule" request
    And body with value {"rule": {"cases": [{"name": "","status": "info","notifications": [],"condition": "a > 0"}],"hasExtendedTitle": true,"isEnabled": true,"message": "My security monitoring rule message.","name": "My security monitoring rule.","options": {"decreaseCriticalityBasedOnEnv": false,"detectionMethod": "threshold","evaluationWindow": 0,"keepAlive": 0,"maxSignalDuration": 0},"queries": [{"query": "source:source_here","groupByFields": ["@userIdentity.assumed_role"],"distinctFields": [],"aggregation": "count","name": ""}],"tags": ["env:prod", "team:security"],"type": "log_detection"}, "ruleQueryPayloads": [{"expectedResult": true,"index": 0,"payload": {"ddsource": "source_here","ddtags": "env:staging,version:5.1","hostname": "i-012345678","message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World","service": "payment","userIdentity": {"assumed_role" : "fake assumed_role"}}}]}
    When the request is sent
    Then the response status is 200 OK
    And the response "results[0]" is equal to true

  @skip @team:DataDog/cloud-siem
  Scenario: Test an existing rule returns "Bad Request" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Test an existing rule returns "Not Found" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/cloud-siem
  Scenario: Test an existing rule returns "OK" response
    Given new "TestExistingSecurityMonitoringRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"ruleQueryPayloads": [{"expectedResult": true, "index": 0, "payload": {"ddsource": "nginx", "ddtags": "env:staging,version:5.1", "hostname": "i-012345678", "message": "2019-11-19T14:37:58,995 INFO [process.name][20081] Hello World", "service": "payment"}}]}
    When the request is sent
    Then the response status is 200 OK

  @team:DataDog/k9-investigation
  Scenario: Unmute security findings returns "Accepted" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "Resolved.", "is_muted": false, "reason": "NO_PENDING_FIX"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwMC0wYmd-MDE4NjcyMDJkMzE4MDE5ODY5MGE4ZmQ2MmFlMjg0Y2M=", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 202 Accepted

  @team:DataDog/k9-investigation
  Scenario: Unmute security findings returns "Not Found" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "Resolved.", "is_muted": false, "reason": "NO_PENDING_FIX"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-investigation
  Scenario: Unmute security findings returns "Unprocessable Entity" response
    Given new "MuteSecurityFindings" request
    And body with value {"data": {"attributes": {"mute": {"description": "Resolved.", "is_muted": false, "reason": "RISK_ACCEPTED"}}, "relationships": {"findings": {"data": [{"id": "ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==", "type": "findings"}]}}, "type": "mute"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Unsubscribe from sample log generation returns "Bad Request" response
    Given operation "DeleteSampleLogGenerationSubscription" enabled
    And new "DeleteSampleLogGenerationSubscription" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Unsubscribe from sample log generation returns "OK" response
    Given operation "DeleteSampleLogGenerationSubscription" enabled
    And new "DeleteSampleLogGenerationSubscription" request
    And request contains "content_pack_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Update a cloud configuration rule's details returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "cloud_configuration_rule" in the system
    And request contains "rule_id" parameter from "cloud_configuration_rule.id"
    And body with value {"name":"{{ unique }}_cloud_updated","isEnabled":false,"cases":[{"status":"info","notifications":[]}],"options":{"complianceRuleOptions":{"resourceType":"gcp_compute_disk", "regoRule":{"policy":"package datadog\n\nimport data.datadog.output as dd_output\n\nimport future.keywords.contains\nimport future.keywords.if\nimport future.keywords.in\n\nmilliseconds_in_a_day := ((1000 * 60) * 60) * 24\n\neval(iam_service_account_key) = \"skip\" if {\n\tiam_service_account_key.disabled\n} else = \"pass\" if {\n\t(iam_service_account_key.resource_seen_at / milliseconds_in_a_day) - (iam_service_account_key.valid_after_time / milliseconds_in_a_day) <= 90\n} else = \"fail\"\n\n# This part remains unchanged for all rules\nresults contains result if {\n\tsome resource in input.resources[input.main_resource_type]\n\tresult := dd_output.format(resource, eval(resource))\n}\n","resourceTypes":["gcp_compute_disk"]}}},"message":"ddd","tags":[],"complianceSignalOptions":{"userActivationStatus":false,"userGroupByFields":[]}}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}_cloud_updated"
    And the response "id" has the same value as "cloud_configuration_rule.id"

  @skip @team:DataDog/cloud-siem
  Scenario: Update a critical asset returns "Bad Request" response
    Given new "UpdateSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter with value "00000000-0000-0000-0000-000000000000"
    And body with value {"data": {"type": "critical_assets", "attributes": {"severity": "invalid_severity"}}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a critical asset returns "Concurrent Modification" response
    Given new "UpdateSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"description": "Production database servers handling PII", "enabled": true, "query": "security:monitoring", "rule_query": "type:log_detection source:cloudtrail", "severity": "increase", "tags": ["technique:T1110-brute-force", "source:cloudtrail"], "version": 1}, "type": "critical_assets"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @team:DataDog/cloud-siem
  Scenario: Update a critical asset returns "Not Found" response
    Given new "UpdateSecurityMonitoringCriticalAsset" request
    And request contains "critical_asset_id" parameter with value "00000000-0000-0000-0000-000000000001"
    And body with value {"data": {"type": "critical_assets", "attributes": {"severity": "high"}}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Update a critical asset returns "OK" response
    Given new "UpdateSecurityMonitoringCriticalAsset" request
    And there is a valid "critical_asset" in the system
    And request contains "critical_asset_id" parameter from "critical_asset.data.id"
    And body with value {"data": {"type": "critical_assets", "attributes": {"enabled": false, "query": "no:alert", "rule_query": "type:(log_detection OR signal_correlation OR workload_security OR application_security) ruleId:djg-ktx-ipq", "severity": "decrease", "tags": ["env:production"], "version": 1}}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "critical_assets"
    And the response "data.attributes.severity" is equal to "decrease"
    And the response "data.attributes.enabled" is equal to false
    And the response "data.attributes.version" is equal to 2

  @team:DataDog/cloud-siem
  Scenario: Update a custom framework returns "Bad Request" response
    Given new "UpdateCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    And body with value {"data": {"attributes": {"handle": "", "name": "", "requirements": [{"controls": [{"name": "", "rules_id": [""]}], "name": ""}], "version": ""}, "type": "custom_framework"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @replay-only @team:DataDog/cloud-siem
  Scenario: Update a custom framework returns "OK" response
    Given there is a valid "custom_framework" in the system
    And new "UpdateCustomFramework" request
    And request contains "handle" parameter with value "create-framework-new"
    And request contains "version" parameter with value "10"
    And body with value {"data":{"type":"custom_framework","attributes":{"name":"name","handle":"create-framework-new","version":"10","icon_url":"test-url","requirements":[{"name":"requirement","controls":[{"name":"control","rules_id":["def-000-be9"]}]}]}}}
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a dataset returns "Bad Request" response
    Given operation "UpdateSecurityMonitoringDataset" enabled
    And new "UpdateSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetUpdate"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a dataset returns "Conflict" response
    Given operation "UpdateSecurityMonitoringDataset" enabled
    And new "UpdateSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetUpdate"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a dataset returns "No Content" response
    Given operation "UpdateSecurityMonitoringDataset" enabled
    And new "UpdateSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetUpdate"}}
    When the request is sent
    Then the response status is 204 No Content

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a dataset returns "Not Found" response
    Given operation "UpdateSecurityMonitoringDataset" enabled
    And new "UpdateSecurityMonitoringDataset" request
    And request contains "dataset_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"definition": {"columns": [{"column": "message", "type": "string"}], "data_source": "logs", "indexes": [], "name": "sample_dataset", "query_filter": "status = 'active'", "search": {"query": "*"}, "storage": "hot", "table_name": "my_reference_table", "time_window": {"from": 1700000000000, "to": 1700003600000}}, "description": "A sample dataset used for detection rules.", "version": 1}, "type": "datasetUpdate"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a due date rule returns "Bad Request" response
    Given operation "UpdateSecurityFindingsAutomationDueDateRule" enabled
    And new "UpdateSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen", "reason_description": "Applied for production findings only"}, "enabled": true, "name": "Critical findings due in 7 days", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a due date rule returns "Not Found" response
    Given operation "UpdateSecurityFindingsAutomationDueDateRule" enabled
    And new "UpdateSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen", "reason_description": "Applied for production findings only"}, "enabled": true, "name": "Critical findings due in 7 days", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Update a due date rule returns "Successfully updated the due date rule" response
    Given operation "UpdateSecurityFindingsAutomationDueDateRule" enabled
    And there is a valid "valid_due_date_rule" in the system
    And new "UpdateSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "valid_due_date_rule.data.id"
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 14, "severity": "critical"}], "due_from": "first_seen"}, "enabled": false, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 200 Successfully updated the due date rule
    And the response "data.id" is equal to "{{ valid_due_date_rule.data.id }}"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a due date rule returns "Unprocessable Entity" response
    Given operation "UpdateSecurityFindingsAutomationDueDateRule" enabled
    And new "UpdateSecurityFindingsAutomationDueDateRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"due_days_per_severity": [{"due_in_days": 7, "severity": "critical"}], "due_from": "first_seen", "reason_description": "Applied for production findings only"}, "enabled": true, "name": "Critical findings due in 7 days", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "due_date_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a mute rule returns "Bad Request" response
    Given operation "UpdateSecurityFindingsAutomationMuteRule" enabled
    And new "UpdateSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"expire_at": 4070908800000, "reason": "risk_accepted", "reason_description": "Accepted for dev environments only"}, "enabled": true, "name": "Mute accepted risks in dev", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a mute rule returns "Not Found" response
    Given operation "UpdateSecurityFindingsAutomationMuteRule" enabled
    And new "UpdateSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"expire_at": 4070908800000, "reason": "risk_accepted", "reason_description": "Accepted for dev environments only"}, "enabled": true, "name": "Mute accepted risks in dev", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Update a mute rule returns "Successfully updated the mute rule" response
    Given operation "UpdateSecurityFindingsAutomationMuteRule" enabled
    And there is a valid "valid_mute_rule" in the system
    And new "UpdateSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "valid_mute_rule.data.id"
    And body with value {"data": {"attributes": {"action": {"reason": "false_positive"}, "enabled": false, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 200 Successfully updated the mute rule
    And the response "data.id" is equal to "{{ valid_mute_rule.data.id }}"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a mute rule returns "Unprocessable Entity" response
    Given operation "UpdateSecurityFindingsAutomationMuteRule" enabled
    And new "UpdateSecurityFindingsAutomationMuteRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"expire_at": 4070908800000, "reason": "risk_accepted", "reason_description": "Accepted for dev environments only"}, "enabled": true, "name": "Mute accepted risks in dev", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "mute_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a security filter returns "Bad Request" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a security filter returns "Concurrent Modification" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a security filter returns "Not Found" response
    Given new "UpdateSecurityFilter" request
    And request contains "security_filter_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "Custom security filter", "query": "service:api", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/cloud-siem
  Scenario: Update a security filter returns "OK" response
    Given new "UpdateSecurityFilter" request
    And there is a valid "security_filter" in the system
    And request contains "security_filter_id" parameter from "security_filter.data.id"
    And body with value {"data": {"attributes": {"exclusion_filters": [], "filtered_data_type": "logs", "is_enabled": true, "name": "{{ unique }}", "query": "service:{{ unique_alnum }}", "version": 1}, "type": "security_filters"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "security_filters"
    And the response "data.attributes.filtered_data_type" is equal to "logs"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a suppression rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a suppression rule returns "Concurrent Modification" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 409 Concurrent Modification

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update a suppression rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And request contains "suppression_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "expiration_date": 1703187336000, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail", "start_date": 1703187336000, "suppression_query": "env:staging status:low", "tags": ["technique:T1110-brute-force", "source:cloudtrail"]}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Update a suppression rule returns "OK" response
    Given new "UpdateSecurityMonitoringSuppression" request
    And there is a valid "suppression" in the system
    And request contains "suppression_id" parameter from "suppression.data.id"
    And body with value {"data": {"attributes": {"suppression_query": "env:staging status:low"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 200 OK
    And the response "data.type" is equal to "suppressions"
    And the response "data.attributes.suppression_query" is equal to "env:staging status:low"
    And the response "data.attributes.version" is equal to 2

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a ticket creation rule returns "Bad Request" response
    Given operation "UpdateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "UpdateSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"assignee_id": "22222222-2222-2222-2222-222222222222", "fields": {"labels": ["security"]}, "max_tickets_per_day": 100, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "Auto-create Jira tickets for critical findings", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a ticket creation rule returns "Not Found" response
    Given operation "UpdateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "UpdateSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"assignee_id": "22222222-2222-2222-2222-222222222222", "fields": {"labels": ["security"]}, "max_tickets_per_day": 100, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "Auto-create Jira tickets for critical findings", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/k9-automation
  Scenario: Update a ticket creation rule returns "Successfully updated the ticket creation rule" response
    Given operation "UpdateSecurityFindingsAutomationTicketCreationRule" enabled
    And there is a valid "valid_ticket_creation_rule" in the system
    And new "UpdateSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "valid_ticket_creation_rule.data.id"
    And body with value {"data": {"attributes": {"action": {"max_tickets_per_day": 5, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": false, "name": "{{ unique }}", "rule": {"finding_types": ["misconfiguration"], "query": "env:staging"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 200 Successfully updated the ticket creation rule
    And the response "data.id" is equal to "{{ valid_ticket_creation_rule.data.id }}"
    And the response "data.attributes.name" is equal to "{{ unique }}"

  @generated @skip @team:DataDog/k9-automation
  Scenario: Update a ticket creation rule returns "Unprocessable Entity" response
    Given operation "UpdateSecurityFindingsAutomationTicketCreationRule" enabled
    And new "UpdateSecurityFindingsAutomationTicketCreationRule" request
    And request contains "rule_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"action": {"assignee_id": "22222222-2222-2222-2222-222222222222", "fields": {"labels": ["security"]}, "max_tickets_per_day": 100, "project_id": "11111111-1111-1111-1111-111111111111", "target": "jira"}, "enabled": true, "name": "Auto-create Jira tickets for critical findings", "rule": {"finding_types": ["misconfiguration"], "query": "env:prod team:platform"}}, "type": "ticket_creation_rules"}}
    When the request is sent
    Then the response status is 422 Unprocessable Entity

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update an entity context sync configuration returns "Bad Request" response
    Given operation "UpdateSecurityMonitoringIntegrationConfig" enabled
    And new "UpdateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "enabled": true, "integration_type": "GOOGLE_WORKSPACE", "name": "My GWS Integration (renamed)", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}, "settings": {"setting1": "value1"}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update an entity context sync configuration returns "Not Found" response
    Given operation "UpdateSecurityMonitoringIntegrationConfig" enabled
    And new "UpdateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "enabled": true, "integration_type": "GOOGLE_WORKSPACE", "name": "My GWS Integration (renamed)", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}, "settings": {"setting1": "value1"}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Update an entity context sync configuration returns "OK" response
    Given operation "UpdateSecurityMonitoringIntegrationConfig" enabled
    And new "UpdateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "enabled": true, "integration_type": "GOOGLE_WORKSPACE", "name": "My GWS Integration (renamed)", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}, "settings": {"setting1": "value1"}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Update an existing rule returns "Bad Request" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    And body with value {"name":"{{ unique }}", "queries":[{"query":""}],"cases":[{"status":"info"}],"options":{},"message":"Test rule Bad","tags":[],"isEnabled":true}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Update an existing rule returns "Not Found" response
    Given new "UpdateSecurityMonitoringRule" request
    And request contains "rule_id" parameter with value "abcde-12345"
    And body with value {"name": "{{ unique }}-NotFound","queries": [{"query": "@test:true","aggregation": "count","groupByFields": [],"distinctFields": [],"metrics": []}],"filters": [],"cases": [{"name": "", "status": "info", "condition": "a > 0", "notifications": []}], "options": {"evaluationWindow": 900, "keepAlive": 3600, "maxSignalDuration": 86400}, "message": "Test rule", "tags": [], "isEnabled": true}
    When the request is sent
    Then the response status is 404 Not Found

  @skip-validation @team:DataDog/cloud-siem
  Scenario: Update an existing rule returns "OK" response
    Given new "UpdateSecurityMonitoringRule" request
    And there is a valid "security_rule" in the system
    And request contains "rule_id" parameter from "security_rule.id"
    And body with value {"name": "{{ unique }}-Updated","queries": [{"query": "@test:true","aggregation": "count","groupByFields": [],"distinctFields": [],"metrics": []}],"filters": [],"cases": [{"name": "", "status": "info", "condition": "a > 0", "notifications": []}], "options": {"evaluationWindow": 900, "keepAlive": 3600, "maxSignalDuration": 86400}, "message": "Test rule", "tags": [], "isEnabled": true}
    When the request is sent
    Then the response status is 200 OK
    And the response "name" is equal to "{{ unique }}-Updated"
    And the response "id" has the same value as "security_rule.id"

  @team:DataDog/cloud-siem
  Scenario: Update resource filters returns "Bad Request" response
    Given new "UpdateResourceEvaluationFilters" request
    And body with value {"data": {"attributes": {"cloud_provider": {"invalid": {"aws_account_id": ["tag1:v1"]}}}, "id": "csm_resource_filter", "type": "csm_resource_filter"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Update resource filters returns "OK" response
    Given new "UpdateResourceEvaluationFilters" request
    And body with value {"data": {"attributes": {"cloud_provider": {"aws": {"aws_account_id": ["tag1:v1"]}}}, "id": "csm_resource_filter", "type": "csm_resource_filter"}}
    When the request is sent
    Then the response status is 201 OK

  @skip @team:DataDog/cloud-siem
  Scenario: Update security signal triage state or assignee returns "Bad Request" response
    Given new "EditSecurityMonitoringSignal" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @skip @team:DataDog/cloud-siem
  Scenario: Update security signal triage state or assignee returns "Not Found" response
    Given new "EditSecurityMonitoringSignal" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 404 Not Found

  @skip @team:DataDog/cloud-siem
  Scenario: Update security signal triage state or assignee returns "OK" response
    Given new "EditSecurityMonitoringSignal" request
    And request contains "signal_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"archive_reason": "none", "assignee": {"uuid": "773b045d-ccf8-4808-bd3b-955ef6a8c940"}, "state": "open"}, "type": "signal_metadata"}}
    When the request is sent
    Then the response status is 200 OK

  @skip-go @skip-java @skip-python @skip-ruby @skip-rust @skip-typescript @skip-validation @team:DataDog/cloud-siem
  Scenario: Validate a detection rule returns "Bad Request" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0"}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":1800,"keepAlive":999999,"maxSignalDuration":1800,"detectionMethod":"threshold"},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"aggregation":"count","name":""}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Validate a detection rule returns "OK" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[],"condition":"a > 0"}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":1800,"keepAlive":1800,"maxSignalDuration":1800,"detectionMethod":"threshold"},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"aggregation":"count","name":""}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-siem
  Scenario: Validate a detection rule with detection method 'new_value' with enabled feature 'instantaneousBaseline' returns "OK" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[]}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":0,"keepAlive":300,"maxSignalDuration":600,"detectionMethod":"new_value","newValueOptions":{"forgetAfter":7,"instantaneousBaseline":true,"learningDuration":1,"learningThreshold":0,"learningMethod":"duration"}},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"metric":"name","metrics":["name"],"aggregation":"new_value","name":"","dataSource":"logs"}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-siem
  Scenario: Validate a detection rule with detection method 'sequence_detection' returns "OK" response
    Given new "ValidateSecurityMonitoringRule" request
    And body with value {"cases":[{"name":"","status":"info","notifications":[],"condition":"step_b > 0"}],"hasExtendedTitle":true,"isEnabled":true,"message":"My security monitoring rule","name":"My security monitoring rule","options":{"evaluationWindow":0,"keepAlive":300,"maxSignalDuration":600,"detectionMethod":"sequence_detection","sequenceDetectionOptions":{"stepTransitions":[{"child":"step_b","evaluationWindow":900,"parent":"step_a"}],"steps":[{"condition":"a > 0","evaluationWindow":60,"name":"step_a"},{"condition":"b > 0","evaluationWindow":60,"name":"step_b"}]}},"queries":[{"query":"source:source_here","groupByFields":["@userIdentity.assumed_role"],"distinctFields":[],"aggregation":"count","name":""},{"query":"source:source_here2","groupByFields":[],"distinctFields":[],"aggregation":"count","name":""}],"tags":["env:prod","team:security"],"type":"log_detection"}
    When the request is sent
    Then the response status is 204 OK

  @team:DataDog/cloud-siem
  Scenario: Validate a suppression rule returns "Bad Request" response
    Given new "ValidateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"name" : "cold_harbour", "enabled": false, "rule_query":"rule:[A-Invalid", "data_exclusion_query": "not enough attributes"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/cloud-siem
  Scenario: Validate a suppression rule returns "OK" response
    Given new "ValidateSecurityMonitoringSuppression" request
    And body with value {"data": {"attributes": {"data_exclusion_query": "source:cloudtrail account_id:12345", "description": "This rule suppresses low-severity signals in staging environments.", "enabled": true, "name": "Custom suppression", "rule_query": "type:log_detection source:cloudtrail"}, "type": "suppressions"}}
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Validate an entity context sync configuration returns "Bad Request" response
    Given operation "ValidateSecurityMonitoringIntegrationConfig" enabled
    And new "ValidateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Validate an entity context sync configuration returns "Not Found" response
    Given operation "ValidateSecurityMonitoringIntegrationConfig" enabled
    And new "ValidateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Validate an entity context sync configuration returns "OK" response
    Given operation "ValidateSecurityMonitoringIntegrationConfig" enabled
    And new "ValidateSecurityMonitoringIntegrationConfig" request
    And request contains "integration_config_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Validate entity context sync credentials returns "Bad Request" response
    Given operation "ValidateSecurityMonitoringIntegrationCredentials" enabled
    And new "ValidateSecurityMonitoringIntegrationCredentials" request
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "integration_type": "GOOGLE_WORKSPACE", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/cloud-siem
  Scenario: Validate entity context sync credentials returns "OK" response
    Given operation "ValidateSecurityMonitoringIntegrationCredentials" enabled
    And new "ValidateSecurityMonitoringIntegrationCredentials" request
    And body with value {"data": {"attributes": {"domain": "siem-test.com", "integration_type": "GOOGLE_WORKSPACE", "secrets": {"admin_email": "admin@example.com", "service_account_json": {"client_email": "svc@my-project.iam.gserviceaccount.com", "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----", "project_id": "my-project", "type": "service_account"}}}, "type": "integration_config"}}
    When the request is sent
    Then the response status is 200 OK
