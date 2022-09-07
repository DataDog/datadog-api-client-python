# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOHistoryResponseError(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "error": (str,),
        }

    attribute_map = {
        "error": "error",
    }

    def __init__(self_, *args, **kwargs):
        """
        A list of errors while querying the history data for the service level objective.

        :param error: Human readable error.
        :type error: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
