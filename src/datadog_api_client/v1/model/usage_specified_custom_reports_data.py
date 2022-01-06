# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_reports_type import UsageReportsType
    from datadog_api_client.v1.model.usage_specified_custom_reports_attributes import (
        UsageSpecifiedCustomReportsAttributes,
    )

    globals()["UsageReportsType"] = UsageReportsType
    globals()["UsageSpecifiedCustomReportsAttributes"] = UsageSpecifiedCustomReportsAttributes


class UsageSpecifiedCustomReportsData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageSpecifiedCustomReportsData - a model defined in OpenAPI

        Keyword Args:
            attributes (UsageSpecifiedCustomReportsAttributes): [optional]
            id (str): [optional] The date for specified custom reports.
            type (UsageReportsType): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSpecifiedCustomReportsData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
