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


def lazy_import():
    from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID

    globals()["SyntheticsDeviceID"] = SyntheticsDeviceID


class SyntheticsDevice(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "height": (int,),
            "id": (SyntheticsDeviceID,),
            "is_mobile": (bool,),
            "name": (str,),
            "width": (int,),
        }

    attribute_map = {
        "height": "height",
        "id": "id",
        "name": "name",
        "width": "width",
        "is_mobile": "isMobile",
    }

    read_only_vars = {}

    def __init__(self, height, id, name, width, *args, **kwargs):
        """SyntheticsDevice - a model defined in OpenAPI

        Args:
            height (int): Screen height of the device.
            id (SyntheticsDeviceID):
            name (str): The device name.
            width (int): Screen width of the device.

        Keyword Args:
            is_mobile (bool): [optional] Whether or not the device is a mobile.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.height = height
        self.id = id
        self.name = name
        self.width = width

    @classmethod
    def _from_openapi_data(cls, height, id, name, width, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsDevice, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.height = height
        self.id = id
        self.name = name
        self.width = width
        return self
