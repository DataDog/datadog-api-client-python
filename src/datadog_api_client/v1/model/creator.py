# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class Creator(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "name": (str, none_type),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "name": "name",
    }

    def __init__(self, *args, **kwargs):
        """
        Object describing the creator of the shared element.

        :param email: Email of the creator.
        :type email: str, optional

        :param handle: Handle of the creator.
        :type handle: str, optional

        :param name: Name of the creator.
        :type name: str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Creator, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
