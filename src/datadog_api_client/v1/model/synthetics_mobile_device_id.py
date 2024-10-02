# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsMobileDeviceID(ModelSimple):
    """
    The device ID.

    :param value: Must be one of ["apple ipad (2022),16.4", "apple ipad (2022),17.3.1", "apple ipad 7th gen (2019),13.3", "apple ipad 9th gen (2021),15.0.2", "apple ipad 9th gen (2021),16.1", "apple ipad air (2022),15.4.1", "apple ipad mini (5th gen),14.6", "apple ipad mini (6th gen),15.1", "apple ipad pro 11 (2022),16.3", "apple ipad pro 12.9 (2020),14.8", "apple ipad pro 12.9 (2021),15.6.1", "apple ipad pro 12.9 (2022),16.5", "apple iphone 11 pro max,13.1.3", "apple iphone 11 pro,13.6", "apple iphone 11 pro,15.5", "apple iphone 11,13.3.1", "apple iphone 11,14.0", "apple iphone 11,16.3", "apple iphone 12 mini,14.2", "apple iphone 12 mini,16.5", "apple iphone 12 pro max,14.5.1", "apple iphone 12 pro,14.5.1", "apple iphone 12 pro,14.8", "apple iphone 12 pro,15.0.2", "apple iphone 12 pro,16.2", "apple iphone 12,14.2", "apple iphone 12,14.6", "apple iphone 12,14.8", "apple iphone 12,15.6.1", "apple iphone 12,16.6.1", "apple iphone 13 mini,15.0.2", "apple iphone 13 mini,16.6", "apple iphone 13 pro max,15.1", "apple iphone 13 pro max,17.3", "apple iphone 13 pro,15.0.2", "apple iphone 13 pro,15.2", "apple iphone 14 plus,16.1", "apple iphone 14 pro max,16.2", "apple iphone 14 pro,16.1", "apple iphone 14 pro,17.3.1", "apple iphone 14,16.1", "apple iphone 15 pro max,17.3.1", "apple iphone 15 pro,17.3.1", "apple iphone 15,17.2.1", "apple iphone se (2022),15.4.1", "galaxy a40,9", "galaxy a5,8.0.0", "galaxy note 10,9", "galaxy note5 (at&t),7.0", "galaxy s10,9", "galaxy s6 edge sm-g925f,7.0", "galaxy s8 (t-mobile),8.0.0", "galaxy s8 unlocked,8.0.0", "galaxy s9 (unlocked),9", "galaxy s9+ (unlocked),8.0.0", "galaxy s9+ (unlocked),9", "google pixel 2,8.0.0", "google pixel 2,9", "google pixel 3 xl,10", "google pixel 3 xl,9", "google pixel 3,10", "google pixel 3,9", "google pixel 3a xl,11", "google pixel 3a xl,12", "google pixel 3a,10", "google pixel 4 (unlocked),10", "google pixel 4 (unlocked),11", "google pixel 4 xl (unlocked),10", "google pixel 4a,11", "google pixel 4a,12", "google pixel 5a 5g,12", "google pixel 6 pro,12", "google pixel 6,12", "google pixel 6a,13", "google pixel 7 pro,13", "google pixel 7,13", "google pixel 7,14", "google pixel 8 pro,14", "google pixel 8,14", "ipad 8th gen (2020),14.8", "ipad air 2,13.6", "ipad air 4th gen (2020),14.8", "iphone 13,15.0.2", "iphone 13,16.0.2", "iphone 6,12.5.4", "iphone 6s,14.4.2", "iphone 7,14.8", "iphone 8,13.5.1", "iphone 8,14.4.2", "iphone se (2020),13.6", "iphone se (2020),14.6", "iphone se (2020),15.0.2", "iphone x,14.6", "iphone xr,12.0", "iphone xr,14.0", "iphone xs max,12.1", "iphone xs,13.6", "lg stylo 5,9", "lg stylo 6,10", "moto g 4,7.0", "moto g7 play,9", "nexus 7 - 2nd gen (wifi),6.0", "oneplus 8t,11", "pixel 2 xl,8.1.0", "pixel 2 xl,9", "pixel 5,11", "pixel 5,12", "pixel xl,8.0.0", "pixel,7.1.2", "samsung a51,10", "samsung galaxy a10s,10", "samsung galaxy a13 5g,11", "samsung galaxy a53 5g,12", "samsung galaxy a7,8.0.0", "samsung galaxy a71,11", "samsung galaxy a73 5g,12", "samsung galaxy j7 (2018),8.0.0", "samsung galaxy note20,11", "samsung galaxy s20 (unlocked),10", "samsung galaxy s20+ (unlocked),10", "samsung galaxy s21 ultra,11", "samsung galaxy s21 ultra,12", "samsung galaxy s21+,11", "samsung galaxy s21,11", "samsung galaxy s21,12", "samsung galaxy s22 5g,12", "samsung galaxy s22 5g,13", "samsung galaxy s22 ultra 5g,12", "samsung galaxy s22+ 5g,12", "samsung galaxy s23 ultra,13", "samsung galaxy s23+,13", "samsung galaxy s23,13", "samsung galaxy s23,14", "samsung galaxy tab a 10.1,10", "samsung galaxy tab a 10.1,7.0", "samsung galaxy tab a8 (2021),11", "samsung galaxy tab s4,8.1.0", "samsung galaxy tab s6,9", "samsung galaxy tab s7,11", "samsung galaxy tab s8,12", "samsung s20 ultra,10", "sony xperia xz3,9", "xiaomi redmi note 10 5g,11", "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16", "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_17", "synthetics:mobile:device:apple_ipad_9th_gen_2021_ios_15", "synthetics:mobile:device:apple_ipad_air_2022_ios_15", "synthetics:mobile:device:apple_ipad_mini_5th_gen_ios_14", "synthetics:mobile:device:apple_ipad_mini_6th_gen_ios_15", "synthetics:mobile:device:apple_ipad_pro_11_2022_ios_16", "synthetics:mobile:device:apple_ipad_pro_12_9_2020_ios_14", "synthetics:mobile:device:apple_ipad_pro_12_9_2021_ios_15", "synthetics:mobile:device:apple_ipad_pro_12_9_2022_ios_16", "synthetics:mobile:device:apple_iphone_11_ios_14", "synthetics:mobile:device:apple_iphone_11_ios_16", "synthetics:mobile:device:apple_iphone_11_pro_ios_15", "synthetics:mobile:device:apple_iphone_12_ios_14", "synthetics:mobile:device:apple_iphone_12_ios_15", "synthetics:mobile:device:apple_iphone_12_ios_16", "synthetics:mobile:device:apple_iphone_12_mini_ios_14", "synthetics:mobile:device:apple_iphone_12_mini_ios_16", "synthetics:mobile:device:apple_iphone_12_pro_ios_14", "synthetics:mobile:device:apple_iphone_12_pro_max_ios_14", "synthetics:mobile:device:apple_iphone_13_mini_ios_15", "synthetics:mobile:device:apple_iphone_13_mini_ios_16", "synthetics:mobile:device:apple_iphone_13_pro_ios_15", "synthetics:mobile:device:apple_iphone_13_pro_max_ios_15", "synthetics:mobile:device:apple_iphone_13_pro_max_ios_17", "synthetics:mobile:device:apple_iphone_14_ios_16", "synthetics:mobile:device:apple_iphone_14_plus_ios_16", "synthetics:mobile:device:apple_iphone_14_pro_ios_16", "synthetics:mobile:device:apple_iphone_14_pro_ios_17", "synthetics:mobile:device:apple_iphone_14_pro_max_ios_16", "synthetics:mobile:device:apple_iphone_6_ios_12", "synthetics:mobile:device:apple_iphone_8_ios_13", "synthetics:mobile:device:apple_iphone_8_ios_14", "synthetics:mobile:device:apple_iphone_se_2022_ios_15", "synthetics:mobile:device:apple_iphone_se_2022_ios_16", "synthetics:mobile:device:galaxy_a5_android_8", "synthetics:mobile:device:galaxy_note5_android_7", "synthetics:mobile:device:google_pixel_3a_xl_android_11", "synthetics:mobile:device:google_pixel_4_unlocked_android_11", "synthetics:mobile:device:google_pixel_4_xl_unlocked_android_10", "synthetics:mobile:device:google_pixel_4a_android_11", "synthetics:mobile:device:google_pixel_6_android_12", "synthetics:mobile:device:google_pixel_6_pro_android_12", "synthetics:mobile:device:google_pixel_6a_android_13", "synthetics:mobile:device:google_pixel_7_android_13", "synthetics:mobile:device:google_pixel_7_android_14", "synthetics:mobile:device:google_pixel_7_pro_android_13", "synthetics:mobile:device:google_pixel_8_android_14", "synthetics:mobile:device:google_pixel_8_pro_android_14", "synthetics:mobile:device:ipad_air_2_ios_13", "synthetics:mobile:device:ipad_air_4th_gen_2020_ios_14", "synthetics:mobile:device:iphone_13_ios_15", "synthetics:mobile:device:iphone_13_ios_16", "synthetics:mobile:device:iphone_15_ios_17", "synthetics:mobile:device:iphone_15_pro_ios_17", "synthetics:mobile:device:iphone_15_pro_max_ios_17", "synthetics:mobile:device:iphone_se_2020_ios_13", "synthetics:mobile:device:iphone_se_2020_ios_14", "synthetics:mobile:device:iphone_x_ios_14", "synthetics:mobile:device:iphone_xr_ios_14", "synthetics:mobile:device:iphone_xs_ios_13", "synthetics:mobile:device:lg_stylo_6_android_10", "synthetics:mobile:device:pixel_5_android_12", "synthetics:mobile:device:samsung_a51_android_10", "synthetics:mobile:device:samsung_galaxy_a71_android_11", "synthetics:mobile:device:samsung_galaxy_note20_android_11", "synthetics:mobile:device:samsung_galaxy_s21_android_11", "synthetics:mobile:device:samsung_galaxy_s21_android_12", "synthetics:mobile:device:samsung_galaxy_s21_plus_android_11", "synthetics:mobile:device:samsung_galaxy_s21_ultra_android_11", "synthetics:mobile:device:samsung_galaxy_s22_5g_android_12", "synthetics:mobile:device:samsung_galaxy_s22_5g_android_13", "synthetics:mobile:device:samsung_galaxy_s22_plus_5g_android_12", "synthetics:mobile:device:samsung_galaxy_s22_ultra_5g_android_12", "synthetics:mobile:device:samsung_galaxy_s23_android_13", "synthetics:mobile:device:samsung_galaxy_s23_android_14", "synthetics:mobile:device:samsung_galaxy_s23_plus_android_13", "synthetics:mobile:device:samsung_galaxy_s23_plus_android_14", "synthetics:mobile:device:samsung_galaxy_s23_ultra_android_13", "synthetics:mobile:device:samsung_galaxy_tab_a_10_1_android_7", "synthetics:mobile:device:samsung_galaxy_tab_s7_android_11", "synthetics:mobile:device:samsung_galaxy_tab_s8_android_12", "synthetics:mobile:device:xiaomi_redmi_note_10_5g_android_11"].
    :type value: str
    """

    allowed_values = {
        "apple ipad (2022),16.4",
        "apple ipad (2022),17.3.1",
        "apple ipad 7th gen (2019),13.3",
        "apple ipad 9th gen (2021),15.0.2",
        "apple ipad 9th gen (2021),16.1",
        "apple ipad air (2022),15.4.1",
        "apple ipad mini (5th gen),14.6",
        "apple ipad mini (6th gen),15.1",
        "apple ipad pro 11 (2022),16.3",
        "apple ipad pro 12.9 (2020),14.8",
        "apple ipad pro 12.9 (2021),15.6.1",
        "apple ipad pro 12.9 (2022),16.5",
        "apple iphone 11 pro max,13.1.3",
        "apple iphone 11 pro,13.6",
        "apple iphone 11 pro,15.5",
        "apple iphone 11,13.3.1",
        "apple iphone 11,14.0",
        "apple iphone 11,16.3",
        "apple iphone 12 mini,14.2",
        "apple iphone 12 mini,16.5",
        "apple iphone 12 pro max,14.5.1",
        "apple iphone 12 pro,14.5.1",
        "apple iphone 12 pro,14.8",
        "apple iphone 12 pro,15.0.2",
        "apple iphone 12 pro,16.2",
        "apple iphone 12,14.2",
        "apple iphone 12,14.6",
        "apple iphone 12,14.8",
        "apple iphone 12,15.6.1",
        "apple iphone 12,16.6.1",
        "apple iphone 13 mini,15.0.2",
        "apple iphone 13 mini,16.6",
        "apple iphone 13 pro max,15.1",
        "apple iphone 13 pro max,17.3",
        "apple iphone 13 pro,15.0.2",
        "apple iphone 13 pro,15.2",
        "apple iphone 14 plus,16.1",
        "apple iphone 14 pro max,16.2",
        "apple iphone 14 pro,16.1",
        "apple iphone 14 pro,17.3.1",
        "apple iphone 14,16.1",
        "apple iphone 15 pro max,17.3.1",
        "apple iphone 15 pro,17.3.1",
        "apple iphone 15,17.2.1",
        "apple iphone se (2022),15.4.1",
        "galaxy a40,9",
        "galaxy a5,8.0.0",
        "galaxy note 10,9",
        "galaxy note5 (at&t),7.0",
        "galaxy s10,9",
        "galaxy s6 edge sm-g925f,7.0",
        "galaxy s8 (t-mobile),8.0.0",
        "galaxy s8 unlocked,8.0.0",
        "galaxy s9 (unlocked),9",
        "galaxy s9+ (unlocked),8.0.0",
        "galaxy s9+ (unlocked),9",
        "google pixel 2,8.0.0",
        "google pixel 2,9",
        "google pixel 3 xl,10",
        "google pixel 3 xl,9",
        "google pixel 3,10",
        "google pixel 3,9",
        "google pixel 3a xl,11",
        "google pixel 3a xl,12",
        "google pixel 3a,10",
        "google pixel 4 (unlocked),10",
        "google pixel 4 (unlocked),11",
        "google pixel 4 xl (unlocked),10",
        "google pixel 4a,11",
        "google pixel 4a,12",
        "google pixel 5a 5g,12",
        "google pixel 6 pro,12",
        "google pixel 6,12",
        "google pixel 6a,13",
        "google pixel 7 pro,13",
        "google pixel 7,13",
        "google pixel 7,14",
        "google pixel 8 pro,14",
        "google pixel 8,14",
        "ipad 8th gen (2020),14.8",
        "ipad air 2,13.6",
        "ipad air 4th gen (2020),14.8",
        "iphone 13,15.0.2",
        "iphone 13,16.0.2",
        "iphone 6,12.5.4",
        "iphone 6s,14.4.2",
        "iphone 7,14.8",
        "iphone 8,13.5.1",
        "iphone 8,14.4.2",
        "iphone se (2020),13.6",
        "iphone se (2020),14.6",
        "iphone se (2020),15.0.2",
        "iphone x,14.6",
        "iphone xr,12.0",
        "iphone xr,14.0",
        "iphone xs max,12.1",
        "iphone xs,13.6",
        "lg stylo 5,9",
        "lg stylo 6,10",
        "moto g 4,7.0",
        "moto g7 play,9",
        "nexus 7 - 2nd gen (wifi),6.0",
        "oneplus 8t,11",
        "pixel 2 xl,8.1.0",
        "pixel 2 xl,9",
        "pixel 5,11",
        "pixel 5,12",
        "pixel xl,8.0.0",
        "pixel,7.1.2",
        "samsung a51,10",
        "samsung galaxy a10s,10",
        "samsung galaxy a13 5g,11",
        "samsung galaxy a53 5g,12",
        "samsung galaxy a7,8.0.0",
        "samsung galaxy a71,11",
        "samsung galaxy a73 5g,12",
        "samsung galaxy j7 (2018),8.0.0",
        "samsung galaxy note20,11",
        "samsung galaxy s20 (unlocked),10",
        "samsung galaxy s20+ (unlocked),10",
        "samsung galaxy s21 ultra,11",
        "samsung galaxy s21 ultra,12",
        "samsung galaxy s21+,11",
        "samsung galaxy s21,11",
        "samsung galaxy s21,12",
        "samsung galaxy s22 5g,12",
        "samsung galaxy s22 5g,13",
        "samsung galaxy s22 ultra 5g,12",
        "samsung galaxy s22+ 5g,12",
        "samsung galaxy s23 ultra,13",
        "samsung galaxy s23+,13",
        "samsung galaxy s23,13",
        "samsung galaxy s23,14",
        "samsung galaxy tab a 10.1,10",
        "samsung galaxy tab a 10.1,7.0",
        "samsung galaxy tab a8 (2021),11",
        "samsung galaxy tab s4,8.1.0",
        "samsung galaxy tab s6,9",
        "samsung galaxy tab s7,11",
        "samsung galaxy tab s8,12",
        "samsung s20 ultra,10",
        "sony xperia xz3,9",
        "xiaomi redmi note 10 5g,11",
        "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16",
        "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_17",
        "synthetics:mobile:device:apple_ipad_9th_gen_2021_ios_15",
        "synthetics:mobile:device:apple_ipad_air_2022_ios_15",
        "synthetics:mobile:device:apple_ipad_mini_5th_gen_ios_14",
        "synthetics:mobile:device:apple_ipad_mini_6th_gen_ios_15",
        "synthetics:mobile:device:apple_ipad_pro_11_2022_ios_16",
        "synthetics:mobile:device:apple_ipad_pro_12_9_2020_ios_14",
        "synthetics:mobile:device:apple_ipad_pro_12_9_2021_ios_15",
        "synthetics:mobile:device:apple_ipad_pro_12_9_2022_ios_16",
        "synthetics:mobile:device:apple_iphone_11_ios_14",
        "synthetics:mobile:device:apple_iphone_11_ios_16",
        "synthetics:mobile:device:apple_iphone_11_pro_ios_15",
        "synthetics:mobile:device:apple_iphone_12_ios_14",
        "synthetics:mobile:device:apple_iphone_12_ios_15",
        "synthetics:mobile:device:apple_iphone_12_ios_16",
        "synthetics:mobile:device:apple_iphone_12_mini_ios_14",
        "synthetics:mobile:device:apple_iphone_12_mini_ios_16",
        "synthetics:mobile:device:apple_iphone_12_pro_ios_14",
        "synthetics:mobile:device:apple_iphone_12_pro_max_ios_14",
        "synthetics:mobile:device:apple_iphone_13_mini_ios_15",
        "synthetics:mobile:device:apple_iphone_13_mini_ios_16",
        "synthetics:mobile:device:apple_iphone_13_pro_ios_15",
        "synthetics:mobile:device:apple_iphone_13_pro_max_ios_15",
        "synthetics:mobile:device:apple_iphone_13_pro_max_ios_17",
        "synthetics:mobile:device:apple_iphone_14_ios_16",
        "synthetics:mobile:device:apple_iphone_14_plus_ios_16",
        "synthetics:mobile:device:apple_iphone_14_pro_ios_16",
        "synthetics:mobile:device:apple_iphone_14_pro_ios_17",
        "synthetics:mobile:device:apple_iphone_14_pro_max_ios_16",
        "synthetics:mobile:device:apple_iphone_6_ios_12",
        "synthetics:mobile:device:apple_iphone_8_ios_13",
        "synthetics:mobile:device:apple_iphone_8_ios_14",
        "synthetics:mobile:device:apple_iphone_se_2022_ios_15",
        "synthetics:mobile:device:apple_iphone_se_2022_ios_16",
        "synthetics:mobile:device:galaxy_a5_android_8",
        "synthetics:mobile:device:galaxy_note5_android_7",
        "synthetics:mobile:device:google_pixel_3a_xl_android_11",
        "synthetics:mobile:device:google_pixel_4_unlocked_android_11",
        "synthetics:mobile:device:google_pixel_4_xl_unlocked_android_10",
        "synthetics:mobile:device:google_pixel_4a_android_11",
        "synthetics:mobile:device:google_pixel_6_android_12",
        "synthetics:mobile:device:google_pixel_6_pro_android_12",
        "synthetics:mobile:device:google_pixel_6a_android_13",
        "synthetics:mobile:device:google_pixel_7_android_13",
        "synthetics:mobile:device:google_pixel_7_android_14",
        "synthetics:mobile:device:google_pixel_7_pro_android_13",
        "synthetics:mobile:device:google_pixel_8_android_14",
        "synthetics:mobile:device:google_pixel_8_pro_android_14",
        "synthetics:mobile:device:ipad_air_2_ios_13",
        "synthetics:mobile:device:ipad_air_4th_gen_2020_ios_14",
        "synthetics:mobile:device:iphone_13_ios_15",
        "synthetics:mobile:device:iphone_13_ios_16",
        "synthetics:mobile:device:iphone_15_ios_17",
        "synthetics:mobile:device:iphone_15_pro_ios_17",
        "synthetics:mobile:device:iphone_15_pro_max_ios_17",
        "synthetics:mobile:device:iphone_se_2020_ios_13",
        "synthetics:mobile:device:iphone_se_2020_ios_14",
        "synthetics:mobile:device:iphone_x_ios_14",
        "synthetics:mobile:device:iphone_xr_ios_14",
        "synthetics:mobile:device:iphone_xs_ios_13",
        "synthetics:mobile:device:lg_stylo_6_android_10",
        "synthetics:mobile:device:pixel_5_android_12",
        "synthetics:mobile:device:samsung_a51_android_10",
        "synthetics:mobile:device:samsung_galaxy_a71_android_11",
        "synthetics:mobile:device:samsung_galaxy_note20_android_11",
        "synthetics:mobile:device:samsung_galaxy_s21_android_11",
        "synthetics:mobile:device:samsung_galaxy_s21_android_12",
        "synthetics:mobile:device:samsung_galaxy_s21_plus_android_11",
        "synthetics:mobile:device:samsung_galaxy_s21_ultra_android_11",
        "synthetics:mobile:device:samsung_galaxy_s22_5g_android_12",
        "synthetics:mobile:device:samsung_galaxy_s22_5g_android_13",
        "synthetics:mobile:device:samsung_galaxy_s22_plus_5g_android_12",
        "synthetics:mobile:device:samsung_galaxy_s22_ultra_5g_android_12",
        "synthetics:mobile:device:samsung_galaxy_s23_android_13",
        "synthetics:mobile:device:samsung_galaxy_s23_android_14",
        "synthetics:mobile:device:samsung_galaxy_s23_plus_android_13",
        "synthetics:mobile:device:samsung_galaxy_s23_plus_android_14",
        "synthetics:mobile:device:samsung_galaxy_s23_ultra_android_13",
        "synthetics:mobile:device:samsung_galaxy_tab_a_10_1_android_7",
        "synthetics:mobile:device:samsung_galaxy_tab_s7_android_11",
        "synthetics:mobile:device:samsung_galaxy_tab_s8_android_12",
        "synthetics:mobile:device:xiaomi_redmi_note_10_5g_android_11",
    }
    APPLE_IPAD__2022__16_4: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD__2022__17_3_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_7TH_GEN__2019__13_3: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_9TH_GEN__2021__15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_9TH_GEN__2021__16_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_AIR__2022__15_4_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_MINI__5TH_GEN__14_6: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_MINI__6TH_GEN__15_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_PRO_11__2022__16_3: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_PRO_12_9__2020__14_8: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_PRO_12_9__2021__15_6_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPAD_PRO_12_9__2022__16_5: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_PRO_MAX_13_1_3: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_PRO_13_6: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_PRO_15_5: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_13_3_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_14_0: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_11_16_3: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_MINI_14_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_MINI_16_5: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_PRO_MAX_14_5_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_PRO_14_5_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_PRO_14_8: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_PRO_15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_PRO_16_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_14_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_14_6: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_14_8: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_15_6_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_12_16_6_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_MINI_15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_MINI_16_6: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_PRO_MAX_15_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_PRO_MAX_17_3: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_PRO_15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_13_PRO_15_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_14_PLUS_16_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_14_PRO_MAX_16_2: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_14_PRO_16_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_14_PRO_17_3_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_14_16_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_15_PRO_MAX_17_3_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_15_PRO_17_3_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_15_17_2_1: ClassVar["SyntheticsMobileDeviceID"]
    APPLE_IPHONE_SE__2022__15_4_1: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_A40_9: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_A5_8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_NOTE_10_9: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_NOTE5__AT_T__7_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S10_9: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S6_EDGE_SMNOT_G925F_7_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S8__TNOT_MOBILE__8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S8_UNLOCKED_8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S9__UNLOCKED__9: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S9___UNLOCKED__8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    GALAXY_S9___UNLOCKED__9: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_2_8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_2_9: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3_XL_10: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3_XL_9: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3_10: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3_9: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3A_XL_11: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3A_XL_12: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_3A_10: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_4__UNLOCKED__10: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_4__UNLOCKED__11: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_4_XL__UNLOCKED__10: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_4A_11: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_4A_12: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_5A_5G_12: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_6_PRO_12: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_6_12: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_6A_13: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_7_PRO_13: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_7_13: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_7_14: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_8_PRO_14: ClassVar["SyntheticsMobileDeviceID"]
    GOOGLE_PIXEL_8_14: ClassVar["SyntheticsMobileDeviceID"]
    IPAD_8TH_GEN__2020__14_8: ClassVar["SyntheticsMobileDeviceID"]
    IPAD_AIR_2_13_6: ClassVar["SyntheticsMobileDeviceID"]
    IPAD_AIR_4TH_GEN__2020__14_8: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_13_15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_13_16_0_2: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_6_12_5_4: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_6S_14_4_2: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_7_14_8: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_8_13_5_1: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_8_14_4_2: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_SE__2020__13_6: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_SE__2020__14_6: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_SE__2020__15_0_2: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_X_14_6: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_XR_12_0: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_XR_14_0: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_XS_MAX_12_1: ClassVar["SyntheticsMobileDeviceID"]
    IPHONE_XS_13_6: ClassVar["SyntheticsMobileDeviceID"]
    LG_STYLO_5_9: ClassVar["SyntheticsMobileDeviceID"]
    LG_STYLO_6_10: ClassVar["SyntheticsMobileDeviceID"]
    MOTO_G_4_7_0: ClassVar["SyntheticsMobileDeviceID"]
    MOTO_G7_PLAY_9: ClassVar["SyntheticsMobileDeviceID"]
    NEXUS_7_NOT__2ND_GEN__WIFI__6_0: ClassVar["SyntheticsMobileDeviceID"]
    ONEPLUS_8T_11: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_2_XL_8_1_0: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_2_XL_9: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_5_11: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_5_12: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_XL_8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    PIXEL_7_1_2: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_A51_10: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A10S_10: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A13_5G_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A53_5G_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A7_8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A71_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_A73_5G_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_J7__2018__8_0_0: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_NOTE20_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S20__UNLOCKED__10: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S20___UNLOCKED__10: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S21_ULTRA_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S21_ULTRA_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S21__11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S21_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S21_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S22_5G_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S22_5G_13: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S22_ULTRA_5G_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S22__5G_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S23_ULTRA_13: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S23__13: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S23_13: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_S23_14: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_A_10_1_10: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_A_10_1_7_0: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_A8__2021__11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_S4_8_1_0: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_S6_9: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_S7_11: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_GALAXY_TAB_S8_12: ClassVar["SyntheticsMobileDeviceID"]
    SAMSUNG_S20_ULTRA_10: ClassVar["SyntheticsMobileDeviceID"]
    SONY_XPERIA_XZ3_9: ClassVar["SyntheticsMobileDeviceID"]
    XIAOMI_REDMI_NOTE_10_5G_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_10TH_GEN_2022_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_10TH_GEN_2022_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_9TH_GEN_2021_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_AIR_2022_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_MINI_5TH_GEN_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_MINI_6TH_GEN_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_11_2022_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2020_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2021_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2022_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_PRO_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_MINI_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_MINI_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_PRO_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_PRO_MAX_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_MINI_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_MINI_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_MAX_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_MAX_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PLUS_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_MAX_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_6_IOS_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_8_IOS_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_8_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_SE_2022_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_SE_2022_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GALAXY_A5_ANDROID_8: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GALAXY_NOTE5_ANDROID_7: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_3A_XL_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4_UNLOCKED_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4_XL_UNLOCKED_ANDROID_10: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4A_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6_PRO_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6A_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_ANDROID_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_PRO_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_8_ANDROID_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_8_PRO_ANDROID_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPAD_AIR_2_IOS_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPAD_AIR_4TH_GEN_2020_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_13_IOS_15: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_13_IOS_16: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_15_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_15_PRO_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_15_PRO_MAX_IOS_17: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_SE_2020_IOS_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_SE_2020_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_X_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_XR_IOS_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_IPHONE_XS_IOS_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_LG_STYLO_6_ANDROID_10: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_PIXEL_5_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_A51_ANDROID_10: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_A71_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_NOTE20_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_PLUS_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ULTRA_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_5G_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_5G_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_PLUS_5G_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_ULTRA_5G_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ANDROID_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_PLUS_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_PLUS_ANDROID_14: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ULTRA_ANDROID_13: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_A_10_1_ANDROID_7: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_S7_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_S8_ANDROID_12: ClassVar["SyntheticsMobileDeviceID"]
    SYNTHETICS_MOBILE_DEVICE_XIAOMI_REDMI_NOTE_10_5G_ANDROID_11: ClassVar["SyntheticsMobileDeviceID"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsMobileDeviceID.APPLE_IPAD__2022__16_4 = SyntheticsMobileDeviceID("apple ipad (2022),16.4")
SyntheticsMobileDeviceID.APPLE_IPAD__2022__17_3_1 = SyntheticsMobileDeviceID("apple ipad (2022),17.3.1")
SyntheticsMobileDeviceID.APPLE_IPAD_7TH_GEN__2019__13_3 = SyntheticsMobileDeviceID("apple ipad 7th gen (2019),13.3")
SyntheticsMobileDeviceID.APPLE_IPAD_9TH_GEN__2021__15_0_2 = SyntheticsMobileDeviceID("apple ipad 9th gen (2021),15.0.2")
SyntheticsMobileDeviceID.APPLE_IPAD_9TH_GEN__2021__16_1 = SyntheticsMobileDeviceID("apple ipad 9th gen (2021),16.1")
SyntheticsMobileDeviceID.APPLE_IPAD_AIR__2022__15_4_1 = SyntheticsMobileDeviceID("apple ipad air (2022),15.4.1")
SyntheticsMobileDeviceID.APPLE_IPAD_MINI__5TH_GEN__14_6 = SyntheticsMobileDeviceID("apple ipad mini (5th gen),14.6")
SyntheticsMobileDeviceID.APPLE_IPAD_MINI__6TH_GEN__15_1 = SyntheticsMobileDeviceID("apple ipad mini (6th gen),15.1")
SyntheticsMobileDeviceID.APPLE_IPAD_PRO_11__2022__16_3 = SyntheticsMobileDeviceID("apple ipad pro 11 (2022),16.3")
SyntheticsMobileDeviceID.APPLE_IPAD_PRO_12_9__2020__14_8 = SyntheticsMobileDeviceID("apple ipad pro 12.9 (2020),14.8")
SyntheticsMobileDeviceID.APPLE_IPAD_PRO_12_9__2021__15_6_1 = SyntheticsMobileDeviceID(
    "apple ipad pro 12.9 (2021),15.6.1"
)
SyntheticsMobileDeviceID.APPLE_IPAD_PRO_12_9__2022__16_5 = SyntheticsMobileDeviceID("apple ipad pro 12.9 (2022),16.5")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_PRO_MAX_13_1_3 = SyntheticsMobileDeviceID("apple iphone 11 pro max,13.1.3")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_PRO_13_6 = SyntheticsMobileDeviceID("apple iphone 11 pro,13.6")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_PRO_15_5 = SyntheticsMobileDeviceID("apple iphone 11 pro,15.5")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_13_3_1 = SyntheticsMobileDeviceID("apple iphone 11,13.3.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_14_0 = SyntheticsMobileDeviceID("apple iphone 11,14.0")
SyntheticsMobileDeviceID.APPLE_IPHONE_11_16_3 = SyntheticsMobileDeviceID("apple iphone 11,16.3")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_MINI_14_2 = SyntheticsMobileDeviceID("apple iphone 12 mini,14.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_MINI_16_5 = SyntheticsMobileDeviceID("apple iphone 12 mini,16.5")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_PRO_MAX_14_5_1 = SyntheticsMobileDeviceID("apple iphone 12 pro max,14.5.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_PRO_14_5_1 = SyntheticsMobileDeviceID("apple iphone 12 pro,14.5.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_PRO_14_8 = SyntheticsMobileDeviceID("apple iphone 12 pro,14.8")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_PRO_15_0_2 = SyntheticsMobileDeviceID("apple iphone 12 pro,15.0.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_PRO_16_2 = SyntheticsMobileDeviceID("apple iphone 12 pro,16.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_14_2 = SyntheticsMobileDeviceID("apple iphone 12,14.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_14_6 = SyntheticsMobileDeviceID("apple iphone 12,14.6")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_14_8 = SyntheticsMobileDeviceID("apple iphone 12,14.8")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_15_6_1 = SyntheticsMobileDeviceID("apple iphone 12,15.6.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_12_16_6_1 = SyntheticsMobileDeviceID("apple iphone 12,16.6.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_MINI_15_0_2 = SyntheticsMobileDeviceID("apple iphone 13 mini,15.0.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_MINI_16_6 = SyntheticsMobileDeviceID("apple iphone 13 mini,16.6")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_PRO_MAX_15_1 = SyntheticsMobileDeviceID("apple iphone 13 pro max,15.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_PRO_MAX_17_3 = SyntheticsMobileDeviceID("apple iphone 13 pro max,17.3")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_PRO_15_0_2 = SyntheticsMobileDeviceID("apple iphone 13 pro,15.0.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_13_PRO_15_2 = SyntheticsMobileDeviceID("apple iphone 13 pro,15.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_14_PLUS_16_1 = SyntheticsMobileDeviceID("apple iphone 14 plus,16.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_14_PRO_MAX_16_2 = SyntheticsMobileDeviceID("apple iphone 14 pro max,16.2")
SyntheticsMobileDeviceID.APPLE_IPHONE_14_PRO_16_1 = SyntheticsMobileDeviceID("apple iphone 14 pro,16.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_14_PRO_17_3_1 = SyntheticsMobileDeviceID("apple iphone 14 pro,17.3.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_14_16_1 = SyntheticsMobileDeviceID("apple iphone 14,16.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_15_PRO_MAX_17_3_1 = SyntheticsMobileDeviceID("apple iphone 15 pro max,17.3.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_15_PRO_17_3_1 = SyntheticsMobileDeviceID("apple iphone 15 pro,17.3.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_15_17_2_1 = SyntheticsMobileDeviceID("apple iphone 15,17.2.1")
SyntheticsMobileDeviceID.APPLE_IPHONE_SE__2022__15_4_1 = SyntheticsMobileDeviceID("apple iphone se (2022),15.4.1")
SyntheticsMobileDeviceID.GALAXY_A40_9 = SyntheticsMobileDeviceID("galaxy a40,9")
SyntheticsMobileDeviceID.GALAXY_A5_8_0_0 = SyntheticsMobileDeviceID("galaxy a5,8.0.0")
SyntheticsMobileDeviceID.GALAXY_NOTE_10_9 = SyntheticsMobileDeviceID("galaxy note 10,9")
SyntheticsMobileDeviceID.GALAXY_NOTE5__AT_T__7_0 = SyntheticsMobileDeviceID("galaxy note5 (at&t),7.0")
SyntheticsMobileDeviceID.GALAXY_S10_9 = SyntheticsMobileDeviceID("galaxy s10,9")
SyntheticsMobileDeviceID.GALAXY_S6_EDGE_SMNOT_G925F_7_0 = SyntheticsMobileDeviceID("galaxy s6 edge sm-g925f,7.0")
SyntheticsMobileDeviceID.GALAXY_S8__TNOT_MOBILE__8_0_0 = SyntheticsMobileDeviceID("galaxy s8 (t-mobile),8.0.0")
SyntheticsMobileDeviceID.GALAXY_S8_UNLOCKED_8_0_0 = SyntheticsMobileDeviceID("galaxy s8 unlocked,8.0.0")
SyntheticsMobileDeviceID.GALAXY_S9__UNLOCKED__9 = SyntheticsMobileDeviceID("galaxy s9 (unlocked),9")
SyntheticsMobileDeviceID.GALAXY_S9___UNLOCKED__8_0_0 = SyntheticsMobileDeviceID("galaxy s9+ (unlocked),8.0.0")
SyntheticsMobileDeviceID.GALAXY_S9___UNLOCKED__9 = SyntheticsMobileDeviceID("galaxy s9+ (unlocked),9")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_2_8_0_0 = SyntheticsMobileDeviceID("google pixel 2,8.0.0")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_2_9 = SyntheticsMobileDeviceID("google pixel 2,9")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3_XL_10 = SyntheticsMobileDeviceID("google pixel 3 xl,10")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3_XL_9 = SyntheticsMobileDeviceID("google pixel 3 xl,9")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3_10 = SyntheticsMobileDeviceID("google pixel 3,10")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3_9 = SyntheticsMobileDeviceID("google pixel 3,9")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3A_XL_11 = SyntheticsMobileDeviceID("google pixel 3a xl,11")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3A_XL_12 = SyntheticsMobileDeviceID("google pixel 3a xl,12")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_3A_10 = SyntheticsMobileDeviceID("google pixel 3a,10")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_4__UNLOCKED__10 = SyntheticsMobileDeviceID("google pixel 4 (unlocked),10")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_4__UNLOCKED__11 = SyntheticsMobileDeviceID("google pixel 4 (unlocked),11")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_4_XL__UNLOCKED__10 = SyntheticsMobileDeviceID("google pixel 4 xl (unlocked),10")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_4A_11 = SyntheticsMobileDeviceID("google pixel 4a,11")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_4A_12 = SyntheticsMobileDeviceID("google pixel 4a,12")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_5A_5G_12 = SyntheticsMobileDeviceID("google pixel 5a 5g,12")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_6_PRO_12 = SyntheticsMobileDeviceID("google pixel 6 pro,12")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_6_12 = SyntheticsMobileDeviceID("google pixel 6,12")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_6A_13 = SyntheticsMobileDeviceID("google pixel 6a,13")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_7_PRO_13 = SyntheticsMobileDeviceID("google pixel 7 pro,13")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_7_13 = SyntheticsMobileDeviceID("google pixel 7,13")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_7_14 = SyntheticsMobileDeviceID("google pixel 7,14")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_8_PRO_14 = SyntheticsMobileDeviceID("google pixel 8 pro,14")
SyntheticsMobileDeviceID.GOOGLE_PIXEL_8_14 = SyntheticsMobileDeviceID("google pixel 8,14")
SyntheticsMobileDeviceID.IPAD_8TH_GEN__2020__14_8 = SyntheticsMobileDeviceID("ipad 8th gen (2020),14.8")
SyntheticsMobileDeviceID.IPAD_AIR_2_13_6 = SyntheticsMobileDeviceID("ipad air 2,13.6")
SyntheticsMobileDeviceID.IPAD_AIR_4TH_GEN__2020__14_8 = SyntheticsMobileDeviceID("ipad air 4th gen (2020),14.8")
SyntheticsMobileDeviceID.IPHONE_13_15_0_2 = SyntheticsMobileDeviceID("iphone 13,15.0.2")
SyntheticsMobileDeviceID.IPHONE_13_16_0_2 = SyntheticsMobileDeviceID("iphone 13,16.0.2")
SyntheticsMobileDeviceID.IPHONE_6_12_5_4 = SyntheticsMobileDeviceID("iphone 6,12.5.4")
SyntheticsMobileDeviceID.IPHONE_6S_14_4_2 = SyntheticsMobileDeviceID("iphone 6s,14.4.2")
SyntheticsMobileDeviceID.IPHONE_7_14_8 = SyntheticsMobileDeviceID("iphone 7,14.8")
SyntheticsMobileDeviceID.IPHONE_8_13_5_1 = SyntheticsMobileDeviceID("iphone 8,13.5.1")
SyntheticsMobileDeviceID.IPHONE_8_14_4_2 = SyntheticsMobileDeviceID("iphone 8,14.4.2")
SyntheticsMobileDeviceID.IPHONE_SE__2020__13_6 = SyntheticsMobileDeviceID("iphone se (2020),13.6")
SyntheticsMobileDeviceID.IPHONE_SE__2020__14_6 = SyntheticsMobileDeviceID("iphone se (2020),14.6")
SyntheticsMobileDeviceID.IPHONE_SE__2020__15_0_2 = SyntheticsMobileDeviceID("iphone se (2020),15.0.2")
SyntheticsMobileDeviceID.IPHONE_X_14_6 = SyntheticsMobileDeviceID("iphone x,14.6")
SyntheticsMobileDeviceID.IPHONE_XR_12_0 = SyntheticsMobileDeviceID("iphone xr,12.0")
SyntheticsMobileDeviceID.IPHONE_XR_14_0 = SyntheticsMobileDeviceID("iphone xr,14.0")
SyntheticsMobileDeviceID.IPHONE_XS_MAX_12_1 = SyntheticsMobileDeviceID("iphone xs max,12.1")
SyntheticsMobileDeviceID.IPHONE_XS_13_6 = SyntheticsMobileDeviceID("iphone xs,13.6")
SyntheticsMobileDeviceID.LG_STYLO_5_9 = SyntheticsMobileDeviceID("lg stylo 5,9")
SyntheticsMobileDeviceID.LG_STYLO_6_10 = SyntheticsMobileDeviceID("lg stylo 6,10")
SyntheticsMobileDeviceID.MOTO_G_4_7_0 = SyntheticsMobileDeviceID("moto g 4,7.0")
SyntheticsMobileDeviceID.MOTO_G7_PLAY_9 = SyntheticsMobileDeviceID("moto g7 play,9")
SyntheticsMobileDeviceID.NEXUS_7_NOT__2ND_GEN__WIFI__6_0 = SyntheticsMobileDeviceID("nexus 7 - 2nd gen (wifi),6.0")
SyntheticsMobileDeviceID.ONEPLUS_8T_11 = SyntheticsMobileDeviceID("oneplus 8t,11")
SyntheticsMobileDeviceID.PIXEL_2_XL_8_1_0 = SyntheticsMobileDeviceID("pixel 2 xl,8.1.0")
SyntheticsMobileDeviceID.PIXEL_2_XL_9 = SyntheticsMobileDeviceID("pixel 2 xl,9")
SyntheticsMobileDeviceID.PIXEL_5_11 = SyntheticsMobileDeviceID("pixel 5,11")
SyntheticsMobileDeviceID.PIXEL_5_12 = SyntheticsMobileDeviceID("pixel 5,12")
SyntheticsMobileDeviceID.PIXEL_XL_8_0_0 = SyntheticsMobileDeviceID("pixel xl,8.0.0")
SyntheticsMobileDeviceID.PIXEL_7_1_2 = SyntheticsMobileDeviceID("pixel,7.1.2")
SyntheticsMobileDeviceID.SAMSUNG_A51_10 = SyntheticsMobileDeviceID("samsung a51,10")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A10S_10 = SyntheticsMobileDeviceID("samsung galaxy a10s,10")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A13_5G_11 = SyntheticsMobileDeviceID("samsung galaxy a13 5g,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A53_5G_12 = SyntheticsMobileDeviceID("samsung galaxy a53 5g,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A7_8_0_0 = SyntheticsMobileDeviceID("samsung galaxy a7,8.0.0")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A71_11 = SyntheticsMobileDeviceID("samsung galaxy a71,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_A73_5G_12 = SyntheticsMobileDeviceID("samsung galaxy a73 5g,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_J7__2018__8_0_0 = SyntheticsMobileDeviceID("samsung galaxy j7 (2018),8.0.0")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_NOTE20_11 = SyntheticsMobileDeviceID("samsung galaxy note20,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S20__UNLOCKED__10 = SyntheticsMobileDeviceID("samsung galaxy s20 (unlocked),10")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S20___UNLOCKED__10 = SyntheticsMobileDeviceID(
    "samsung galaxy s20+ (unlocked),10"
)
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S21_ULTRA_11 = SyntheticsMobileDeviceID("samsung galaxy s21 ultra,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S21_ULTRA_12 = SyntheticsMobileDeviceID("samsung galaxy s21 ultra,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S21__11 = SyntheticsMobileDeviceID("samsung galaxy s21+,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S21_11 = SyntheticsMobileDeviceID("samsung galaxy s21,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S21_12 = SyntheticsMobileDeviceID("samsung galaxy s21,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S22_5G_12 = SyntheticsMobileDeviceID("samsung galaxy s22 5g,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S22_5G_13 = SyntheticsMobileDeviceID("samsung galaxy s22 5g,13")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S22_ULTRA_5G_12 = SyntheticsMobileDeviceID("samsung galaxy s22 ultra 5g,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S22__5G_12 = SyntheticsMobileDeviceID("samsung galaxy s22+ 5g,12")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S23_ULTRA_13 = SyntheticsMobileDeviceID("samsung galaxy s23 ultra,13")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S23__13 = SyntheticsMobileDeviceID("samsung galaxy s23+,13")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S23_13 = SyntheticsMobileDeviceID("samsung galaxy s23,13")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_S23_14 = SyntheticsMobileDeviceID("samsung galaxy s23,14")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_A_10_1_10 = SyntheticsMobileDeviceID("samsung galaxy tab a 10.1,10")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_A_10_1_7_0 = SyntheticsMobileDeviceID("samsung galaxy tab a 10.1,7.0")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_A8__2021__11 = SyntheticsMobileDeviceID("samsung galaxy tab a8 (2021),11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_S4_8_1_0 = SyntheticsMobileDeviceID("samsung galaxy tab s4,8.1.0")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_S6_9 = SyntheticsMobileDeviceID("samsung galaxy tab s6,9")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_S7_11 = SyntheticsMobileDeviceID("samsung galaxy tab s7,11")
SyntheticsMobileDeviceID.SAMSUNG_GALAXY_TAB_S8_12 = SyntheticsMobileDeviceID("samsung galaxy tab s8,12")
SyntheticsMobileDeviceID.SAMSUNG_S20_ULTRA_10 = SyntheticsMobileDeviceID("samsung s20 ultra,10")
SyntheticsMobileDeviceID.SONY_XPERIA_XZ3_9 = SyntheticsMobileDeviceID("sony xperia xz3,9")
SyntheticsMobileDeviceID.XIAOMI_REDMI_NOTE_10_5G_11 = SyntheticsMobileDeviceID("xiaomi redmi note 10 5g,11")
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_10TH_GEN_2022_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_10TH_GEN_2022_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_9TH_GEN_2021_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_9th_gen_2021_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_AIR_2022_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_air_2022_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_MINI_5TH_GEN_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_mini_5th_gen_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_MINI_6TH_GEN_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_mini_6th_gen_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_11_2022_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_pro_11_2022_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2020_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_pro_12_9_2020_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2021_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_pro_12_9_2021_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPAD_PRO_12_9_2022_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_ipad_pro_12_9_2022_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_11_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_11_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_11_PRO_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_11_pro_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_MINI_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_mini_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_MINI_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_mini_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_PRO_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_pro_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_12_PRO_MAX_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_12_pro_max_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_MINI_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_13_mini_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_MINI_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_13_mini_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_13_pro_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_MAX_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_13_pro_max_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_13_PRO_MAX_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_13_pro_max_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_14_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PLUS_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_14_plus_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_14_pro_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_14_pro_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_14_PRO_MAX_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_14_pro_max_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_6_IOS_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_6_ios_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_8_IOS_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_8_ios_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_8_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_8_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_SE_2022_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_se_2022_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_APPLE_IPHONE_SE_2022_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:apple_iphone_se_2022_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GALAXY_A5_ANDROID_8 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:galaxy_a5_android_8"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GALAXY_NOTE5_ANDROID_7 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:galaxy_note5_android_7"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_3A_XL_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_3a_xl_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4_UNLOCKED_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_4_unlocked_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4_XL_UNLOCKED_ANDROID_10 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_4_xl_unlocked_android_10"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_4A_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_4a_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_6_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6_PRO_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_6_pro_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_6A_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_6a_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_7_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_ANDROID_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_7_android_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_7_PRO_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_7_pro_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_8_ANDROID_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_8_android_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_GOOGLE_PIXEL_8_PRO_ANDROID_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:google_pixel_8_pro_android_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPAD_AIR_2_IOS_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:ipad_air_2_ios_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPAD_AIR_4TH_GEN_2020_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:ipad_air_4th_gen_2020_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_13_IOS_15 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_13_ios_15"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_13_IOS_16 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_13_ios_16"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_15_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_15_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_15_PRO_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_15_pro_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_15_PRO_MAX_IOS_17 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_15_pro_max_ios_17"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_SE_2020_IOS_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_se_2020_ios_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_SE_2020_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_se_2020_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_X_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_x_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_XR_IOS_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_xr_ios_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_IPHONE_XS_IOS_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:iphone_xs_ios_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_LG_STYLO_6_ANDROID_10 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:lg_stylo_6_android_10"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_PIXEL_5_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:pixel_5_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_A51_ANDROID_10 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_a51_android_10"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_A71_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_a71_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_NOTE20_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_note20_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s21_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s21_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_PLUS_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s21_plus_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S21_ULTRA_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s21_ultra_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_5G_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s22_5g_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_5G_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s22_5g_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_PLUS_5G_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s22_plus_5g_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S22_ULTRA_5G_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s22_ultra_5g_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s23_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ANDROID_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s23_android_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_PLUS_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s23_plus_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_PLUS_ANDROID_14 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s23_plus_android_14"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_S23_ULTRA_ANDROID_13 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_s23_ultra_android_13"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_A_10_1_ANDROID_7 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_tab_a_10_1_android_7"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_S7_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_tab_s7_android_11"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_SAMSUNG_GALAXY_TAB_S8_ANDROID_12 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:samsung_galaxy_tab_s8_android_12"
)
SyntheticsMobileDeviceID.SYNTHETICS_MOBILE_DEVICE_XIAOMI_REDMI_NOTE_10_5G_ANDROID_11 = SyntheticsMobileDeviceID(
    "synthetics:mobile:device:xiaomi_redmi_note_10_5g_android_11"
)
