# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SecurityMonitoringContentPackStateDetails(ModelComposed):
    def __init__(self, **kwargs):
        """
        Type-specific details for a content pack state. The set of fields present depends
        on the content pack's ``type``. When Cloud SIEM is inactive for the requesting organization, ``onboarding`` is returned instead of the content pack's usual type, such as ``logs`` or ``vulnerability``.`

        :param cp_activation: The activation status of a content pack.
        :type cp_activation: SecurityMonitoringContentPackActivation

        :param data_last_seen: Timestamp bucket indicating when logs were last collected.
        :type data_last_seen: SecurityMonitoringContentPackTimestampBucket

        :param filters_configured: Whether filters (Security Filters or Index Query depending on the pricing model) are
            present and correctly configured to route logs into Cloud SIEM.
        :type filters_configured: bool

        :param integration_installed_status: The installation status of the related integration.
        :type integration_installed_status: SecurityMonitoringContentPackIntegrationStatus

        :param logs_seen_from_any_index: Whether logs for this content pack have been seen in any Datadog index in the last 72 hours.
        :type logs_seen_from_any_index: bool

        :param siem_index_incorrect: Whether the Cloud SIEM index configuration is incorrect (only applies to certain pricing models).
        :type siem_index_incorrect: bool

        :param type: The filtered data type.
        :type type: SecurityFilterFilteredDataType
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.security_monitoring_content_pack_logs_details import (
            SecurityMonitoringContentPackLogsDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_threat_intel_details import (
            SecurityMonitoringContentPackThreatIntelDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_entity_details import (
            SecurityMonitoringContentPackEntityDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_audit_details import (
            SecurityMonitoringContentPackAuditDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_app_sec_details import (
            SecurityMonitoringContentPackAppSecDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_vulnerability_details import (
            SecurityMonitoringContentPackVulnerabilityDetails,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_onboarding_details import (
            SecurityMonitoringContentPackOnboardingDetails,
        )

        return {
            "oneOf": [
                SecurityMonitoringContentPackLogsDetails,
                SecurityMonitoringContentPackThreatIntelDetails,
                SecurityMonitoringContentPackEntityDetails,
                SecurityMonitoringContentPackAuditDetails,
                SecurityMonitoringContentPackAppSecDetails,
                SecurityMonitoringContentPackVulnerabilityDetails,
                SecurityMonitoringContentPackOnboardingDetails,
            ],
        }
