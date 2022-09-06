# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorState(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_state_group import MonitorStateGroup

        return {
            "groups": ({str: (MonitorStateGroup,)},),
        }

    attribute_map = {
        "groups": "groups",
    }

    def __init__(self_, *args, **kwargs):
        """
        Wrapper object with the different monitor states.

        :param groups: Dictionary where the keys are groups (comma separated lists of tags) and the values are
            the list of groups your monitor is broken down on.
        :type groups: {str: (MonitorStateGroup,)}, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
