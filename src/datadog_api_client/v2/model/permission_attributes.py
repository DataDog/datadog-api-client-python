# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (  # noqa: F401
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


class PermissionAttributes(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "created": (datetime,),
            "description": (str,),
            "display_name": (str,),
            "display_type": (str,),
            "group_name": (str,),
            "name": (str,),
            "restricted": (bool,),
        }

    attribute_map = {
        "created": "created",
        "description": "description",
        "display_name": "display_name",
        "display_type": "display_type",
        "group_name": "group_name",
        "name": "name",
        "restricted": "restricted",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """PermissionAttributes - a model defined in OpenAPI

        Keyword Args:
            created (datetime): [optional] Creation time of the permission.
            description (str): [optional] Description of the permission.
            display_name (str): [optional] Displayed name for the permission.
            display_type (str): [optional] Display type.
            group_name (str): [optional] Name of the permission group.
            name (str): [optional] Name of the permission.
            restricted (bool): [optional] Whether or not the permission is restricted.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(PermissionAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
