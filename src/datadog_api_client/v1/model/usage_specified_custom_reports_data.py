# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageSpecifiedCustomReportsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_specified_custom_reports_attributes import (
            UsageSpecifiedCustomReportsAttributes,
        )
        from datadog_api_client.v1.model.usage_reports_type import UsageReportsType

        return {
            "attributes": (UsageSpecifiedCustomReportsAttributes,),
            "id": (str,),
            "type": (UsageReportsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Response containing date and type for specified custom reports.

        :param attributes: The response containing attributes for specified custom reports.
        :type attributes: UsageSpecifiedCustomReportsAttributes, optional

        :param id: The date for specified custom reports.
        :type id: str, optional

        :param type: The type of reports.
        :type type: UsageReportsType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSpecifiedCustomReportsData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
