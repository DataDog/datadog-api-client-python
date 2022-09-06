# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageCustomReportsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_custom_reports_attributes import UsageCustomReportsAttributes
        from datadog_api_client.v1.model.usage_reports_type import UsageReportsType

        return {
            "attributes": (UsageCustomReportsAttributes,),
            "id": (str,),
            "type": (UsageReportsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, *args, **kwargs):
        """
        The response containing the date and type for custom reports.

        :param attributes: The response containing attributes for custom reports.
        :type attributes: UsageCustomReportsAttributes, optional

        :param id: The date for specified custom reports.
        :type id: str, optional

        :param type: The type of reports.
        :type type: UsageReportsType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
