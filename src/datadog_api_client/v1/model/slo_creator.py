# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOCreator(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "id": (int,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "id": "id",
        "name": "name",
    }

    def __init__(self_, *args, **kwargs):
        """
        The creator of the SLO

        :param email: Email of the creator.
        :type email: str, optional

        :param id: User ID of the creator.
        :type id: int, optional

        :param name: Name of the creator.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
