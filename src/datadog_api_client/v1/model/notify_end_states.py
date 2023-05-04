# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class NotifyEndStates(ModelSimple):
    """
    States for which ``notify_end_types`` sends out notifications for.


    :param value: If omitted defaults to "['alert', 'no data', 'warn']".
    :type value: [NotifyEndState]
    """

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notify_end_state import NotifyEndState

        return {
            "value": ([NotifyEndState],),
        }
