# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CheckCanDeleteSLOResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ok": ([str],),
        }

    attribute_map = {
        "ok": "ok",
    }

    def __init__(self_, *args, **kwargs):
        """
        An array of service level objective objects.

        :param ok: An array of of SLO IDs that can be safely deleted.
        :type ok: [str], optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
