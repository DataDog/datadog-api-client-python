# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentTeamResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created": (datetime,),
            "modified": (datetime,),
            "name": (str,),
        }

    attribute_map = {
        "created": "created",
        "modified": "modified",
        "name": "name",
    }
    read_only_vars = {
        "created",
        "modified",
    }

    def __init__(self, *args, **kwargs):
        """
        The incident team's attributes from a response.

        :param created: Timestamp of when the incident team was created.
        :type created: datetime, optional

        :param modified: Timestamp of when the incident team was modified.
        :type modified: datetime, optional

        :param name: Name of the incident team.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentTeamResponseAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
