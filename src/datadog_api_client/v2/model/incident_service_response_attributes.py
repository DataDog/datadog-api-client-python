# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class IncidentServiceResponseAttributes(ModelNormal):
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

    def __init__(self_, *args, **kwargs):
        """
        The incident service's attributes from a response.

        :param created: Timestamp of when the incident service was created.
        :type created: datetime, optional

        :param modified: Timestamp of when the incident service was modified.
        :type modified: datetime, optional

        :param name: Name of the incident service.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
