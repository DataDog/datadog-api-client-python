# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_by_retention_org_usage import LogsByRetentionOrgUsage

    globals()["LogsByRetentionOrgUsage"] = LogsByRetentionOrgUsage


class LogsByRetentionOrgs(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "usage": ([LogsByRetentionOrgUsage],),
        }

    attribute_map = {
        "usage": "usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Indexed logs usage summary for each organization for each retention period with usage.

        :param usage: Indexed logs usage summary for each organization.
        :type usage: [LogsByRetentionOrgUsage], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsByRetentionOrgs, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
