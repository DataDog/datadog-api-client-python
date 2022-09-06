# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageAuditLogsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_audit_logs_hour import UsageAuditLogsHour

        return {
            "usage": ([UsageAuditLogsHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    def __init__(self_, *args, **kwargs):
        """
        Response containing the audit logs usage for each hour for a given organization.

        :param usage: Get hourly usage for audit logs.
        :type usage: [UsageAuditLogsHour], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
