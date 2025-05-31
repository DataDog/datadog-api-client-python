# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ObservabilityPipelineEnrichmentTableGeoIp(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key_field": (str,),
            "locale": (str,),
            "path": (str,),
        }

    attribute_map = {
        "key_field": "key_field",
        "locale": "locale",
        "path": "path",
    }

    def __init__(self_, key_field: str, locale: str, path: str, **kwargs):
        """
        Uses a GeoIP database to enrich logs based on an IP field.

        :param key_field: Path to the IP field in the log.
        :type key_field: str

        :param locale: Locale used to resolve geographical names.
        :type locale: str

        :param path: Path to the GeoIP database file.
        :type path: str
        """
        super().__init__(kwargs)

        self_.key_field = key_field
        self_.locale = locale
        self_.path = path
