# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SyntheticsPlayingTab(ModelSimple):
    """
    Navigate between different tabs for your browser test.

    :param value: Must be one of [-1, 0, 1, 2, 3].
    :type value: int
    """

    allowed_values = {
        "value": {
            "MAIN_TAB": -1,
            "NEW_TAB": 0,
            "TAB_1": 1,
            "TAB_2": 2,
            "TAB_3": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
