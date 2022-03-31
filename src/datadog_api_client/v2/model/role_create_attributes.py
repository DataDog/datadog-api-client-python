# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class RoleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
    }
    read_only_vars = {
        "created_at",
        "modified_at",
    }

    def __init__(self, name, *args, **kwargs):
        """
        Attributes of the created role.

        :param created_at: Creation time of the role.
        :type created_at: datetime, optional

        :param modified_at: Time of last role modification.
        :type modified_at: datetime, optional

        :param name: Name of the role.
        :type name: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name

    @classmethod
    def _from_openapi_data(cls, name, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RoleCreateAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        return self
