# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOCorrectionResponseAttributesModifier(ModelNormal):

    validations = {}
    _nullable = True

    @cached_property
    def openapi_types():
        return {
            "email": (str,),
            "handle": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "name": "name",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Modifier of the object.

        :param email: Email of the Modifier.
        :type email: str, optional

        :param handle: Handle of the Modifier.
        :type handle: str, optional

        :param name: Name of the Modifier.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOCorrectionResponseAttributesModifier, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
