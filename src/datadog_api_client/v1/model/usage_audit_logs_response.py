# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_audit_logs_hour import UsageAuditLogsHour

    globals()["UsageAuditLogsHour"] = UsageAuditLogsHour


class UsageAuditLogsResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "usage": ([UsageAuditLogsHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Response containing the audit logs usage for each hour for a given organization.

        :param usage: Get hourly usage for audit logs.
        :type usage: [UsageAuditLogsHour], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageAuditLogsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
