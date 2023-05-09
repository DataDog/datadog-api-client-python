# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class NotifyEndTypes(ModelSimple):
    """
    If set, notifies if a monitor is in an alert-worthy state ( ``ALERT`` , ``WARNING`` , or ``NO DATA`` )
        when this downtime expires or is canceled. Applied to monitors that change states during
        the downtime (such as from ``OK`` to ``ALERT`` , ``WARNING`` , or ``NO DATA`` ), and to monitors that
        already have an alert-worthy state when downtime begins.


    :param value: If omitted defaults to "['expired']".
    :type value: [NotifyEndType]
    """

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notify_end_type import NotifyEndType

        return {
            "value": ([NotifyEndType],),
        }
