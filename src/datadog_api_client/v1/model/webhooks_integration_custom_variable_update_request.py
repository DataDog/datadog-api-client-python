# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


class WebhooksIntegrationCustomVariableUpdateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "is_secret": (bool,),
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "is_secret": "is_secret",
        "name": "name",
        "value": "value",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """WebhooksIntegrationCustomVariableUpdateRequest - a model defined in OpenAPI

        Keyword Args:
            is_secret (bool): [optional] Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
            name (str): [optional] The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`. It must only contains upper-case characters, integers or underscores.
            value (str): [optional] Value of the custom variable.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WebhooksIntegrationCustomVariableUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
