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


class IdpFormData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "idp_file": (file_type,),
        }

    attribute_map = {
        "idp_file": "idp_file",
    }

    read_only_vars = {}

    def __init__(self, idp_file, *args, **kwargs):
        """IdpFormData - a model defined in OpenAPI

        Args:
            idp_file (file_type): The path to the XML metadata file you wish to upload.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.idp_file = idp_file

    @classmethod
    def _from_openapi_data(cls, idp_file, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IdpFormData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.idp_file = idp_file
        return self
